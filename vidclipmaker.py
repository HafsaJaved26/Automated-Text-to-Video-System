import os
from moviepy.editor import ImageClip, CompositeVideoClip

def create_ken_burns_clip(image_path, output_name):
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
    final_clip.write_videofile(output_name, fps=24, codec='libx264')
    print(f"✅ Generated: {output_name}")
