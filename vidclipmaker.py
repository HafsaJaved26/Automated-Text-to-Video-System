import os
import zipfile
import shutil
from moviepy.editor import ImageClip, CompositeVideoClip

INPUT_ZIP = "/content/pixel_perfect_images.zip"
EXTRACT_DIR = "/content/temp_extracted_images"
VIDEO_OUTPUT_DIR = "/content/pixel_perfect_videos"
FINAL_VIDEO_ZIP = "/content/pixel_perfect_videos.zip"

def create_ken_burns_clip(image_path, output_name):
    try:
        W, H = 1280, 720
        clip = ImageClip(image_path).set_duration(6)

        if clip.w / clip.h < W / H:
            clip = clip.resize(width=W)
        else:
            clip = clip.resize(height=H)

        clip = clip.resize(lambda t: 1 + 0.02 * t)

        clip = clip.set_position(('center', 'center'))

        final_clip = CompositeVideoClip([clip], size=(W, H))

        final_clip = final_clip.fadein(0.5).fadeout(0.5)

        final_clip.write_videofile(
            output_name,
            fps=24,
            codec='libx264',
            preset='fast',
            logger=None
        )
        print(f"   [OK] Generated: {os.path.basename(output_name)}")
        return True
    except Exception as e:
        print(f"   [ERR] Failed on {os.path.basename(image_path)}: {e}")
        return False

def main():
    if os.path.exists(EXTRACT_DIR): shutil.rmtree(EXTRACT_DIR)
    if os.path.exists(VIDEO_OUTPUT_DIR): shutil.rmtree(VIDEO_OUTPUT_DIR)
    os.makedirs(EXTRACT_DIR, exist_ok=True)
    os.makedirs(VIDEO_OUTPUT_DIR, exist_ok=True)

    print(f"📂 Unzipping {INPUT_ZIP}...")
    if not os.path.exists(INPUT_ZIP):
        print("❌ Error: Input zip file not found! Run images.py first.")
        return

    with zipfile.ZipFile(INPUT_ZIP, 'r') as zip_ref:
        zip_ref.extractall(EXTRACT_DIR)

    print("🎬 Starting Video Conversion...")
    video_count = 0

    for root, dirs, files in os.walk(EXTRACT_DIR):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(root, file)

                rel_path = os.path.relpath(root, EXTRACT_DIR)

                clean_rel_path = rel_path.replace("pixel_perfect_images/", "").replace("pixel_perfect_images", "")
                video_folder = os.path.join(VIDEO_OUTPUT_DIR, clean_rel_path)
                os.makedirs(video_folder, exist_ok=True)

                video_filename = os.path.splitext(file)[0] + ".mp4"
                video_path = os.path.join(video_folder, video_filename)

                if create_ken_burns_clip(img_path, video_path):
                    video_count += 1

    print(f"\n📦 Zipping {video_count} videos...")
    shutil.make_archive(FINAL_VIDEO_ZIP.replace('.zip', ''), 'zip', VIDEO_OUTPUT_DIR)

    print("🧹 Cleaning up temporary files...")
    shutil.rmtree(EXTRACT_DIR)

    print("="*60)
    print(f"✅ DONE! Video Zip created at: {FINAL_VIDEO_ZIP}")
    print("="*60)

if __name__ == "__main__":
    main()
    main()
