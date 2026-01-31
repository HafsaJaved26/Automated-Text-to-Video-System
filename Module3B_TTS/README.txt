Module 3B – Audio Timing Analysis (Faraz Khan)

This module processes Text-to-Speech audio files and prepares them for video synchronization.

Input:
Folder: tts_audio
Contains MP3 or WAV narration files.

Processing Steps:
- Normalizes audio volume
- Converts files to WAV format
- Forces each audio file to exactly 6 seconds duration
- Renames output sequentially (scene_1.wav, scene_2.wav, ...)

Output:
Folder: processed_audio

Run Command:
py -3.10 audio_timing_processor.py

The output audio files are ready for final video assembly.
