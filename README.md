Image-Search-Engine
Build a content-based image search engine that allows users to upload an image and retrieve visually similar images using deep learning–based embeddings and a vector database

About the project:

I built an end-to-end Image Search Engine that allows users to upload an image and retrieve visually similar images using computer vision and vector similarity search. The system extracts deep visual features from images, indexes them using FAISS, and exposes the functionality through both a FastAPI backend and an interactive Streamlit UI.This project demonstrates how unstructured image data can be converted into meaningful vector representations and searched efficiently at scale.

Key Features of my project:

Deep feature extraction using a pretrained ResNet-50 CNN

High-dimensional vector similarity search using FAISS

FastAPI-based backend for image upload and search

Interactive Streamlit UI for visual search

Real-time inference and similarity matching

Works entirely on local machine (no paid services)

 The System Architecture of the project:

Images are first converted into embeddings using a CNN-based feature extractor

All image embeddings are than indexed using FAISS

A query image is embedded using the same model

FAISS retrieves the top-K most similar images

Results are displayed visually in the Streamlit UI or returned via API

 Tech Stack implemented:

Programming Language: Python

Computer Vision: PyTorch, Torchvision, ResNet-50

Vector Search: FAISS

Backend API: FastAPI

Frontend/UI: Streamlit

Image Processing: Pillow

Numerical Computing: NumPy
