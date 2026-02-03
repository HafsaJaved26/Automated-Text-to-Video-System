TEXT-TO-SPEECH (TTS) AUDIO GENERATION MODULE

OVERVIEW
This module generates natural-sounding speech audio from structured narration text
stored in a JSON file. It converts scene-level narration into high-quality audio
files that can be synchronized with generated visuals and videos.

The module is designed as part of an automated text-to-video pipeline, enabling
clear and consistent voice narration for each scene.


PURPOSE
- Convert narration text into spoken audio
- Generate scene-wise audio files
- Maintain consistent voice style and pronunciation
- Prepare narration assets for video assembly


MODEL & VOICE USED

TEXT-TO-SPEECH ENGINE
- Engine          : Microsoft Edge Text-to-Speech
- Library         : edge-tts
- Voice           : en-US-AriaNeural
- Voice Type      : Neural (Natural human-like speech)
- Language        : English (US)

Reason for Selection:
- Natural pronunciation and intonation
- Clear female voice suitable for storytelling
- Stable performance and fast generation


TOOLS & TECHNOLOGIES USED
- edge-tts
  - Neural text-to-speech synthesis
  - Audio file generation

- Python (AsyncIO)
  - Asynchronous processing
  - Efficient handling of multiple scenes

- JSON
  - Structured narration input


INPUT DESCRIPTION
- JSON file containing:
  - Stories
  - Scene numbers
  - Scene-wise narration text

Each scene is processed sequentially to generate a corresponding audio file.


OUTPUT DESCRIPTION
- Format        : MP3
- Naming        : scene_1.mp3, scene_2.mp3, ...
- Organization  : Stored in a dedicated tts_audio folder

Each audio file corresponds to one scene narration.


PERFORMANCE CHARACTERISTICS
- Generation Speed : ~1–2 seconds per scene
- Processing Mode  : Sequential (asynchronous execution)
- Hardware         : CPU-based (no GPU required)

Performance may vary based on:
- Length of narration text
- Internet connectivity
- System load


AUDIO QUALITY
- Natural-sounding neural voice
- Clear pronunciation
- Consistent volume and tone
- Suitable for narration and storytelling



LIMITATIONS
- Requires active internet connection
- Fixed voice unless manually changed
- Sequential generation (not parallelized)

