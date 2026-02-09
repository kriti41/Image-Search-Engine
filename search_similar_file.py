import numpy as np
from load import extract_embedding
from faiss_index import index, image_paths

def search_similar_images(query_image_path, k=5):
    query_vector = extract_embedding(query_image_path)
    query_vector = np.expand_dims(query_vector, axis=0)

    k = min(k, len(image_paths))
    D, I = index.search(query_vector, k)

    results = [image_paths[i] for i in I[0]]
    return results


if __name__ == "__main__":
    results = search_similar_images("images/parrot.jpg")

    print("Similar images:")
    for r in results:
        print(r)


