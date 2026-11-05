<div align="center">

# ✨ AI Background Remover

### Remove image backgrounds in seconds — right from your desktop.

A simple, AI-powered desktop application built with **Python, Tkinter, rembg and Pillow**.  
Choose an image, remove its background, preview the result, and save it in your preferred format.

<br/>

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-64748B?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Open%20Source-8B5CF6?style=for-the-badge)

<br/>

<!-- Replace this URL with your own banner image or GIF after uploading it to your repository. -->
<img src="assets/demo.gif" alt="AI Background Remover demo" width="85%" />

**[Features](#-features) · [Demo](#-demo) · [Installation](#-installation) · [Usage](#-how-to-use) · [Contributing](#-contributing)**

</div>

---

## 🌈 What is this?

**AI Background Remover** makes background removal easy for everyone. Select a photo using your computer's file manager and let the AI-powered `rembg` library isolate the foreground subject.

No complicated editing tools. No manual selection. Just choose, remove, preview, and save.

## 🚀 Features

| Feature | Description |
|---|---|
| 🖼️ Image picker | Browse your computer and select JPG, JPEG or PNG images |
| 🤖 AI background removal | Remove image backgrounds using `rembg` |
| 👀 Live preview | Preview the selected image and processed result |
| ⚪ White background | Composite the subject onto a clean white background |
| 💾 Save your image | Export the result as PNG or JPG |
| 🖥️ Desktop interface | Lightweight interface built with Tkinter |

## 🎬 Demo

> Add your own screenshots or screen recording to the `assets/` folder and update the paths below.

<div align="center">

| 1. Choose an image | 2. Remove the background |
|:---:|:---:|
| <img src="assets/step-1.png" alt="Choose image screen" width="95%"> | <img src="assets/step-2.png" alt="Background removal preview" width="95%"> |
| 3. Preview the result | 4. Save your image |
| <img src="assets/step-3.png" alt="Preview result" width="95%"> | <img src="assets/step-4.png" alt="Save image" width="95%"> |

</div>

## 🧰 Tech stack

- **Python** — application logic
- **Tkinter** — desktop graphical user interface
- **rembg** — AI-powered background removal
- **Pillow (PIL)** — image loading, processing and exporting

## 📁 Project structure

```text
AI-Background-Remover/
│
├── background_remover.py
├── README.md
├── requirements.txt
│
└── assets/
    ├── demo.gif
    ├── step-1.png
    ├── step-2.png
    ├── step-3.png
    └── step-4.png
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Background-Remover.git
cd AI-Background-Remover
```

### 2. Create a virtual environment (recommended)

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install "rembg[cpu]" pillow
```

### 4. Run the application

```bash
python background_remover.py
```

> **First run:** `rembg` may download its AI model. An internet connection may be required for the initial model download. Processing time depends on your computer and image size.

## 🧑‍💻 How to use

1. Launch the application.
2. Click **Choose Image**.
3. Select a JPG, JPEG or PNG file from your computer.
4. Click **Remove Background**.
5. Wait for the processed image to appear in the preview.
6. Click **Save Image** and choose PNG or JPG.

That's it! 🎉

## 📦 Dependencies

You can create a `requirements.txt` file with:

```text
rembg[cpu]
Pillow
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## 🛣️ Roadmap

Ideas for future improvements:

- [ ] Modern, responsive-looking desktop interface
- [ ] Transparent, white and custom-color backgrounds
- [ ] Before-and-after comparison slider
- [ ] Drag-and-drop image upload
- [ ] Batch background removal
- [ ] Image resizing and cropping
- [ ] Download/export quality settings
- [ ] Progress indicator for large images

## 🤝 Contributing

Contributions, ideas and bug reports are welcome!

1. Fork this repository.
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push your branch: `git push origin feature/your-feature`
5. Open a Pull Request.

## 🐛 Issues & feedback

Found a bug or have an idea? Open an issue in the repository and include steps to reproduce the problem, your operating system, and any relevant error messages.

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

<div align="center">

### 💜 Built with Python. Powered by AI. Made for everyone.

If this project helped you, consider giving the repository a ⭐

**Happy coding! 🚀**

</div>
