# 🚀 Deep Learning Training & DeepVision AI Studio

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/deploy?repository=yogenjangle-ai/DL_Training_Project2&branch=main&mainModule=app.py)

A unified Deep Learning repository combining **DeepVision AI (CNN & Explainable AI Studio)** with **Interactive Streamlit and RAG / NLP Notebooks**.

---

## 🌟 Modules Included

### 1. 🧠 DeepVision AI: CNN Image Classifier & Explainable AI Studio (`app2.py` / `cnn_model.py`)
- **Modular PyTorch CNN Architecture**:
  - `Conv2D (32)` $\to$ `BatchNorm` $\to$ `ReLU` $\to$ `MaxPool`
  - `Conv2D (64)` $\to$ `BatchNorm` $\to$ `ReLU` $\to$ `MaxPool`
  - `Adaptive Pooling` $\to$ `Flatten` $\to$ `Linear(128)` $\to$ `Dropout(0.3)` $\to$ `Output`
- **Dual Dataset Pipelines**:
  - Built-in **CIFAR-10** (10 classes: Airplane, Automobile, Bird, Cat, Deer, Dog, Frog, Horse, Ship, Truck)
  - Custom ZIP dataset upload with automatic folder parsing (includes `sample_cats_vs_dogs.zip`)
- **Pretrained Weights**: Pre-loaded PyTorch models in `models/` (`cats_dogs_cnn.pth` and `cifar10_cnn.pth`).
- **Explainable AI (XAI)**:
  - **Grad-CAM (Gradient-weighted Class Activation Mapping)** heatmaps.
  - **Intermediate Feature Map Visualizer** (inspect all 16/32 convolution filters).
- **Interactive Data Augmentation**: Real-time sliders for rotation, flipping, brightness jitter, and zoom.
- **Academic Evaluation**: Confusion matrix heatmap, Precision/Recall/F1 metrics, and viva exam cheat sheet.

### 2. 📊 Streamlit & RAG / NLP Interactive Demos (`streamlittut.py`, Notebooks)
- **Interactive UI Components**: Streamlit widgets, charts, form handlers, media embedding, and file uploaders.
- **Jupyter Notebooks**: Exploratory experiments for RAG (`ragblog.ipynb`, `cppRag.ipynb`, `cppchat.ipynb`).

---

## 🚀 Quick Start (Local)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Launch the Unified Studio (Recommended)
```bash
streamlit run app.py
```
*(On Windows, you can simply double-click **`run_app.bat`**)*

### 3. Or Launch Individual Apps Directly
- **DeepVision AI Studio**:
  ```bash
  streamlit run app2.py
  ```
- **Streamlit Demo**:
  ```bash
  streamlit run streamlittut.py
  ```

---

## ☁️ 1-Click Cloud Deployment (Streamlit Community Cloud)

You can launch this entire unified suite online for free:

👉 **[Deploy `yogenjangle-ai/DL_Training_Project2` on Streamlit Cloud](https://share.streamlit.io/deploy?repository=yogenjangle-ai/DL_Training_Project2&branch=main&mainModule=app.py)**
