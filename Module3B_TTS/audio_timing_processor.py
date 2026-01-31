import os
from pydub import AudioSegment, effects

INPUT_FOLDER = "tts_audio"
OUTPUT_FOLDER = "processed_audio"
TARGET_MS = 6000

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

scene_number = 1

for file in sorted(os.listdir(INPUT_FOLDER)):
    if file.endswith(".mp3") or file.endswith(".wav"):

        path = os.path.join(INPUT_FOLDER, file)

        if file.endswith(".mp3"):
            audio = AudioSegment.from_mp3(path)
        else:
            audio = AudioSegment.from_wav(path)

        # Normalize volume
        audio = effects.normalize(audio)

        # Fix duration
        if len(audio) < TARGET_MS:
            pad = AudioSegment.silent(TARGET_MS - len(audio))
            audio = audio + pad
        else:
            audio = audio[:TARGET_MS]

        output_name = f"scene_{scene_number}.wav"
        audio.export(os.path.join(OUTPUT_FOLDER, output_name), format="wav")

        scene_number += 1

print("All audio processed successfully.")
