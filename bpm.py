import essentia.standard as es
import essentia
import numpy as np

# Load audio
audio = es.MonoLoader(filename='Karaoke.mp3', sampleRate=44100)()

# Ensure audio is valid
if audio is None or len(audio) == 0:
    raise ValueError("Audio file could not be loaded properly.")

# Extract rhythm
rhythm_extractor = es.RhythmExtractor2013(method='multifeature')
bpm, beats_times, confidence, _, _ = rhythm_extractor(audio)

# Validate beats_times before using
if beats_times is None or len(beats_times) == 0:
    raise ValueError("No beats detected. Check audio quality or method used.")

# Add beep markers
marker = es.AudioOnsetsMarker(onsets=beats_times, type='beep')
audio_with_beats = marker(audio)

# Save output
es.MonoWriter(filename='audio_with_beats.mp3')(audio_with_beats)

print(f"BPM: {bpm}")
print(f"Beat times: {beats_times}")
