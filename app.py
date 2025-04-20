import json
from essentia.standard import MonoLoader, TensorflowPredictEffnetDiscogs, TensorflowPredict2D

def main():
    audio = MonoLoader(filename="jrock.mp3", sampleRate=44100, resampleQuality=4)()
    embedding_model = TensorflowPredictEffnetDiscogs(graphFilename="discogs-effnet-bs64-1.pb", output="PartitionedCall:1")
    embeddings = embedding_model(audio)

    model = TensorflowPredict2D(graphFilename="genre_discogs400-discogs-effnet-1.pb", input="serving_default_model_Placeholder", output="PartitionedCall:0")
    predictions = model(embeddings)
    predictions = predictions[0] 
    # Load genre labels from JSON
    with open("genre_discogs400-discogs-effnet-1.json") as f:
        model_info = json.load(f)
        labels = model_info["classes"]

    # Pair labels with predictions and sort by score
    top_n = 10
    genre_scores = list(zip(labels, predictions))
    genre_scores.sort(key=lambda x: x[1], reverse=True)

    # Print top genres
    print(f"Top {top_n} predicted genres:")
    for genre, score in genre_scores[:top_n]:
        print(f"{genre}: {score:.4f}")

if __name__ == "__main__":
    main()

# from essentia.standard import MonoLoader, TensorflowPredictMusiCNN, TensorflowPredictVGGish
# import numpy as np
# import matplotlib.pyplot as plt