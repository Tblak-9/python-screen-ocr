# 🖥️ Python Screen OCR

> A lightweight Python tool for selecting any area of your screen, extracting text using OCR, and automatically copying the result to your clipboard.

---

## ✨ Features

- 🖱️ Select any area of the screen with your mouse
- 📸 Capture the selected area as an image
- 🔍 Extract text using Tesseract OCR
- 🌐 Supports English and Persian text
- 📋 Automatically copy extracted text to the clipboard
- ⌨️ Press `ESC` to cancel the selection
- 🐍 Built entirely with Python
- ⚡ Lightweight and simple architecture

---

## 🧠 How It Works

```text
🖥️ Screen
   │
   ▼
🖱️ Select Area
   │
   ▼
📸 Capture Screenshot
   │
   ▼
🖼️ Process Image
   │
   ▼
🔍 Tesseract OCR
   │
   ├── 🇬🇧 English
   └── 🇮🇷 Persian
   │
   ▼
📝 Extracted Text
   │
   ▼
📋 Clipboard
```

---

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| 🐍 Python | Core programming language |
| 🪟 Tkinter | GUI and screen selection |
| 📸 MSS | Screen capture |
| 🖼️ Pillow | Image processing |
| 🔍 Tesseract OCR | Text recognition |
| 🔗 Pytesseract | Python interface for Tesseract |
| 📋 Pyperclip | Clipboard management |

---

## 📋 Requirements

- Python 3.x
- Tesseract OCR
- pip

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/python-screen-ocr.git
```

```bash
cd python-screen-ocr
```

### 2. Install Python dependencies

```bash
pip install mss pillow pytesseract pyperclip
```

---

## 🔍 Tesseract OCR

This project uses **Tesseract OCR** as its text recognition engine.

The default Tesseract path is:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

The path is configured in `main.py`:

```python
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)
```

If Tesseract is installed in another location, update the path accordingly.

---

## 🌐 Language Support

The current configuration supports:

- 🇮🇷 Persian
- 🇬🇧 English

```python
lang="fas+eng"
```

| Code | Language |
|---|---|
| `fas` | Persian |
| `eng` | English |

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

Then:

1. Select an area of your screen.
2. Drag the mouse over the desired text.
3. Release the mouse button.
4. The selected area will be captured.
5. Tesseract will extract the text.
6. The result will be displayed in the terminal.
7. The extracted text will automatically be copied to the clipboard.

Paste the result anywhere using:

```text
Ctrl + V
```

Press:

```text
ESC
```

to cancel the selection.

---

## 📁 Project Structure

```text
python-screen-ocr/
│
├── main.py
├── README.md
└── .gitignore
```

The application may generate:

```text
selected_area.png
```

This file contains the captured screen area.

---

## 🎯 Example

Select an area containing:

```text
Windows Learn

Python Screen OCR

Hello World
```

The OCR process:

```text
Screenshot
     ↓
Tesseract OCR
     ↓
Windows Learn

Python Screen OCR

Hello World
     ↓
Clipboard
```

---

## 🔮 Future Improvements

- ⌨️ Global keyboard shortcuts
- 🖥️ Multi-monitor support
- 🎨 Improved selection interface
- 📋 Dedicated OCR result window
- 🔊 Text-to-Speech
- 🌍 Automatic language detection
- 📄 Export extracted text to `.txt`
- 📑 Export OCR results to PDF
- ⚡ Faster OCR processing
- 🪟 Standalone Windows `.exe`
- ⚙️ Configurable OCR languages

---

## 🧪 Status

> 🟢 **Working**

The current version supports screen-area selection, screenshot capture, Persian/English OCR, terminal output, and automatic clipboard copying.

---

## 🤝 Contributing

Contributions, improvements, and suggestions are welcome.

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Open a Pull Request

---

## 📜 License

This project is open-source and available under the MIT License.

---

<div align="center">

### 🖥️ Python Screen OCR

**Select → Capture → Recognize → Copy**

Made with 🐍 Python and ❤️

</div>
