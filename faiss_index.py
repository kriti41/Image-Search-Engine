import faiss
import numpy as np
import os
from embedding import extract_embedding

IMAGE_DIR = "images"

embeddings = []
image_paths = []

for img in os.listdir(IMAGE_DIR):
    path = os.path.join(IMAGE_DIR, img)
    emb = extract_embedding(path)
    embeddings.append(emb)
    image_paths.append(path)

embeddings = np.array(embeddings).astype("float32")

dimension = embeddings.shape[1]  # 2048
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

print("Total images indexed:", index.ntotal)
