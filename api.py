from fastapi import FastAPI, UploadFile, File
import shutil
import os

from search_similar_file import search_similar_images

app = FastAPI(title="Image Search Engine API")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/search")
def search_image(file: UploadFile = File(...), k: int = 3):
    # Save uploaded image
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Search similar images
    results = search_similar_images(file_path, k)

    return {
        "query_image": file.filename,
        "similar_images": results
    }
