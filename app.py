import streamlit as st
from PIL import Image
import os

from search_similar_file import search_similar_images

st.set_page_config(page_title="Image Search Engine", layout="wide")

st.title("Image Search Engine (CV + FAISS)")
st.write("Upload an image to find visually similar images.")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    # Save uploaded image
    query_path = f"temp_{uploaded_file.name}"
    with open(query_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.subheader("Query Image")
    st.image(Image.open(query_path), width=300)

    # Search
    with st.spinner("Searching similar images..."):
        results = search_similar_images(query_path, k=5)

    st.subheader("Similar Images")
    cols = st.columns(len(results))

    for col, img_path in zip(cols, results):
        with col:
            st.image(Image.open(img_path), use_container_width=True)

    # Cleanup
    os.remove(query_path)
