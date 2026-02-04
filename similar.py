import numpy as np
from essentia.standard import MusicExtractor
from scipy.spatial.distance import cosine

def extract_features(audio_path):
    print(f"Processing: {audio_path}")

    features, _ = MusicExtractor(lowlevelStats=['mean', 'stdev'],
                                 rhythmStats=['mean', 'stdev'],
                                 tonalStats=['mean', 'stdev'])(audio_path)

    keys_to_include = [
        'lowlevel.mfcc.mean', 'lowlevel.mfcc.stdev',
        'lowlevel.spectral_centroid.mean',
        'lowlevel.spectral_complexity.mean',
        'rhythm.bpm',
        'tonal.key_strength', 'tonal.tuning_frequency'
    ]

    feature_vector = []
    for key in keys_to_include:
        value = features[key]
        if isinstance(value, (list, np.ndarray)):
            feature_vector.extend(value)
        else:
            feature_vector.append(value)

    return np.array(feature_vector)

def compute_similarity(vec1, vec2):
    vec1_norm = vec1 / np.linalg.norm(vec1)
    vec2_norm = vec2 / np.linalg.norm(vec2)
    return 1 - cosine(vec1_norm, vec2_norm)

if __name__ == '__main__':
    song1 = "Karaoke.wav"
    song2 = "audio_with_beats.wav"

    vec1 = extract_features(song1)
    vec2 = extract_features(song2)

    print(f"Feature vector 1 length: {len(vec1)}")
    print(f"Feature vector 2 length: {len(vec2)}")

    sim = compute_similarity(vec1, vec2)
    print(f"Cosine similarity: {sim:.4f}")
