import tkinter as tk
import mss
from PIL import Image
import pytesseract
import pyperclip

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)
class ScreenSelector:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-alpha", 0.25)

        self.root.configure(bg="black")

        self.canvas = tk.Canvas(
            self.root,
            bg="black",
            cursor="crosshair",
            highlightthickness=0
        )

        self.canvas.pack(
            fill="both",
            expand=True
        )

        self.start_x = 0
        self.start_y = 0
        self.rectangle = None

        self.canvas.bind(
            "<ButtonPress-1>",
            self.start_selection
        )

        self.canvas.bind(
            "<B1-Motion>",
            self.update_selection
        )

        self.canvas.bind(
            "<ButtonRelease-1>",
            self.finish_selection
        )

        self.root.bind(
            "<Escape>",
            self.cancel
        )

        self.root.mainloop()


    def start_selection(self, event):
        self.start_x = event.x
        self.start_y = event.y
        if self.rectangle:
            self.canvas.delete(self.rectangle)
        self.rectangle = self.canvas.create_rectangle(
            self.start_x,
            self.start_y,
            self.start_x,
            self.start_y,
            outline="red",
            width=3
        )
    def update_selection(self, event):
        if self.rectangle:
            self.canvas.coords(
                self.rectangle,
                self.start_x,
                self.start_y,
                event.x,
                event.y
            )


    def finish_selection(self, event):

        x1 = min(self.start_x, event.x)
        y1 = min(self.start_y, event.y)
        x2 = max(self.start_x, event.x)
        y2 = max(self.start_y, event.y)
        print()
        print("========== SELECTED AREA ==========")
        print(f"X1: {x1}")
        print(f"Y1: {y1}")
        print(f"X2: {x2}")
        print(f"Y2: {y2}")
        print("===================================")
        self.root.destroy()
        self.take_screenshot(
            x1,
            y1,
            x2,
            y2
        )
    def take_screenshot(self, x1, y1, x2, y2):
        width = x2 - x1
        height = y2 - y1
        print()
        print("Taking screenshot...")
        with mss.mss() as screenshot:
            monitor = {
                "left": x1,
                "top": y1,
                "width": width,
                "height": height
            }
            image = screenshot.grab(monitor)
            img = Image.frombytes(
                "RGB",
                image.size,
                image.rgb
            )
            img.save("selected_area.png")
        print("Screenshot saved successfully!")
        print()
        print("Reading text...")

        text = pytesseract.image_to_string(
            img,
            lang="fas+eng"
        )
        print()
        print("========== OCR RESULT ==========")
        print(text)
        print("================================")
        pyperclip.copy(text)
        print()
        print("Text copied to clipboard!")
    def cancel(self, event=None):
        print("Selection cancelled.")
        self.root.destroy()


if __name__ == "__main__":
    ScreenSelector()