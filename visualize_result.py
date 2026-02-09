import matplotlib.pyplot as plt
from PIL import Image
from search_similar_file import search_similar_images

def visualize(query_image_path, k=3):
    results = search_similar_images(query_image_path, k)

    images = [query_image_path] + results
    titles = ["Query Image"] + [f"Result {i+1}" for i in range(len(results))]

    plt.figure(figsize=(15, 5))

    for i, (img_path, title) in enumerate(zip(images, titles)):
        img = Image.open(img_path).convert("RGB")
        plt.subplot(1, len(images), i + 1)
        plt.imshow(img)
        plt.title(title)
        plt.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    visualize("images/parrot.jpg", k=3)
