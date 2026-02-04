import json
import os

from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip



# ------------------------------
# Config
# ------------------------------
VIDEO_NAME = "video_3"      # change for video_2, video_3
STORY_ID = "story_3"

# ------------------------------
# Paths
# ------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_VIDEO_PATH = os.path.join(BASE_DIR, "input_videos", f"{VIDEO_NAME}.mp4")
OUTPUT_DIR = os.path.join(BASE_DIR, "output_videos")
OUTPUT_VIDEO_PATH = os.path.join(OUTPUT_DIR, f"{VIDEO_NAME}_final.mp4")
SCENE_JSON_PATH = os.path.join(BASE_DIR, "fixed_scene_data.json")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ------------------------------
# Load video and JSON data
# ------------------------------
if not os.path.exists(INPUT_VIDEO_PATH):
    raise FileNotFoundError(f"Video not found at: {INPUT_VIDEO_PATH}")

if not os.path.exists(SCENE_JSON_PATH):
    raise FileNotFoundError(f"Scene JSON not found at: {SCENE_JSON_PATH}")

video = VideoFileClip(INPUT_VIDEO_PATH)

with open(SCENE_JSON_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

scenes = data["stories"][STORY_ID]["scenes"]

clips = []

# ------------------------------
# Title screen
# ------------------------------
title = TextClip(
    text=data["stories"][STORY_ID]["title"],
    font_size=50,
    color="white",
    bg_color="black",
    size=video.size,
    method="caption"
).with_duration(3)

clips.append(title)

# ------------------------------
# Subtitles for each scene
# ------------------------------
start_time = 0

for scene in scenes:
    subtitle = TextClip(
        text=scene["narration_text"],
        font_size=36,
        color="white",
        stroke_color="black",
        stroke_width=2,
        method="caption",
        size=(1100, None)
    ).with_position(("center", "bottom")) \
     .with_start(start_time) \
     .with_duration(scene["duration_seconds"])

    clips.append(subtitle)
    start_time += scene["duration_seconds"]

# ------------------------------
# End credits
# ------------------------------
credits_text = (
    "Thanks for Watching\n\n"
    "Project Team:\n"
    "Afia Noor\n"
    "Fiza Aslam\n"
    "Hafsa Javed\n"
    "Abdul Jabbar\n"
    "Faraz Khan\n"
    "Eman Afzal\n"
    "Ghazal Hafeez\n"
    "Eman Zahra Awan\n"
    "M Zaheer\n"
)

credits = TextClip(
    text=credits_text,
    font_size=32,
    color="white",
    bg_color="black",
    size=video.size,
    method="caption"
).with_start(video.duration) \
 .with_duration(4)


# ------------------------------
# Compose final video
# ------------------------------
final = CompositeVideoClip([video] + clips + [credits])

# ------------------------------
# Write output
# ------------------------------
final.write_videofile(
    OUTPUT_VIDEO_PATH,
    fps=video.fps,
    codec="libx264",
    audio_codec="aac"
)

print("✅ Video successfully created at:")
print(OUTPUT_VIDEO_PATH)
