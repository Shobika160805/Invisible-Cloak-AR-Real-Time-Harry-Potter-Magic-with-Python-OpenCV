# 🪄 Harry Potter Invisible Cloak — Real-Time Computer Vision with Python & OpenCV

Make your own “invisible cloak” just like in Harry Potter! This project uses Python, OpenCV, and NumPy to detect a light blue cloth in your webcam feed and replace it with the background, creating a magical disappearing effect in real-time.


## 🚀 Features

- Real-time "invisibility" using color detection
- Easy to tune for different cloak colors (currently set to light blue)
- Simple Python code, perfect for beginners in OpenCV and computer vision
- Morphological filters for improved masking
- Works on Windows, macOS, and Linux (with a webcam)

---

## 🏗️ How It Works

1. Captures the static background (without anyone in frame)
2. Detects the light blue cloak in each frame using HSV color thresholds
3. Replaces the cloak region with the saved background for invisibility
4. Displays the magical result—“You disappear” on camera!

---

## 🛠️ Installation

1. **Clone this repository:**
    ```
    git clone https://github.com/your-username/HarryPotterCloak.git
    cd HarryPotterCloak
    ```

2. **Set up a Python virtual environment (optional but recommended):**
    ```
    python -m venv venv
    # Activate venv (Windows)
    venv\Scripts\activate
    # Activate venv (macOS/Linux)
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```
    pip install opencv-python numpy
    ```

---

## 👨‍💻 Usage

1. Make sure your webcam is connected.
2. Run the code:
    ```
    python main.py
    ```
3. When prompted, stay out of the frame to capture the background.
4. Hold or wear your light blue cloak, then move into view. Watch yourself vanish!
5. Press `q` in the display window to exit.

---

## 🎨 Change Cloak Color

To use a different colored cloak, adjust the HSV range in `main.py`, e.g. for red, green, black etc.  
See [this color range reference](https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html) for guidance.

---

## 🧠 What You’ll Learn

- Basics of computer vision and image processing
- Working with real-time video streams
- Masking, dilation, and morphological operations
- HSV color space for robust color detection

---

## 📚 Resources

- [OpenCV Python Tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- [NumPy Documentation](https://numpy.org/doc/stable/)
- [HSV color ranges explained](https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html)

---

## ✨ Credits

Inspired by the Harry Potter franchise and popular Computer Vision tutorials.

---

## 💡 License

MIT License


