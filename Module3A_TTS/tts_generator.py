import edge_tts
import asyncio
import json
import os

INPUT_JSON = "fixed_scene_data.json"
OUTPUT_FOLDER = "../tts_audio"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

async def main():
    with open(INPUT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    scene_no = 1

    # Loop through each story
    for story in data["stories"].values():
        for scene in story["scenes"]:
            text = scene["narration_text"]

            output_file = f"{OUTPUT_FOLDER}/scene_{scene_no}.mp3"

            voice = edge_tts.Communicate(text, voice="en-US-AriaNeural")
            await voice.save(output_file)

            print("Generated:", output_file)
            scene_no += 1

asyncio.run(main())