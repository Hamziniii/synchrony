import essentia
import essentia.standard as es
import numpy as np

def main():
    # Example: Load an audio file and compute its duration
    audio_loader = es.MonoLoader(filename='song.mp3', sampleRate=44100)
    audio = audio_loader()
    
    duration = es.Duration()(audio)
    print(f"Audio duration: {duration} seconds")

if __name__ == "__main__":
    main()