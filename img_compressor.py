import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def resizer():
    # Select the image file
    image_file = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.jpeg;*.jpg;*.png")]
    )

    if not image_file:
        return  # Exit if no file is selected

    filepath = os.path.abspath(image_file)
    filename, filextension = os.path.splitext(filepath)
    img = Image.open(filepath)

    # If JPEG/JPG, ask for quality input
    if filextension.lower() in [".jpeg", ".jpg"]:
        qual = quality_slider.get()
        img.save(
            filename + "_compressed" + ".jpeg",
            "JPEG",
            optimize=True,
            quality=qual
        )
        messagebox.showinfo("Success", "Your compressed image has been saved.")

    # If PNG, convert and compress
    elif filextension.lower() == ".png":
        img = img.convert("P", palette=Image.ADAPTIVE, colors=256)
        img.save(filename + "_compressed" + ".png", optimize=True, quality=10)
        messagebox.showinfo("Note", "PNG may not compress much. The image has been saved.")

    else:
        messagebox.showerror("Error", "Invalid file type. Please select a JPEG or PNG file.")

def create_gui():
    # Create the main window
    window = tk.Tk()
    window.title("Image Resizer")
    window.geometry("400x300")
    window.config(bg="#2c3e50")

    # Add title label
    title_label = tk.Label(window, text="Image Compressor", font=("Arial", 20), fg="#ecf0f1", bg="#2c3e50")
    title_label.pack(pady=20)

    # Add quality slider for JPEG
    global quality_slider
    quality_label = tk.Label(window, text="JPEG Quality", font=("Arial", 14), fg="#ecf0f1", bg="#2c3e50")
    quality_label.pack(pady=10)
    quality_slider = tk.Scale(window, from_=10, to_=100, orient="horizontal", length=300, bg="#34495e", fg="#ecf0f1")
    quality_slider.set(50)
    quality_slider.pack(pady=10)

    # Add resize button
    resize_button = tk.Button(window, text="Select and Compress Image", font=("Arial", 14), bg="#3498db", fg="#ecf0f1", command=resizer)
    resize_button.pack(pady=20)

    # Run the main loop
    window.mainloop()

create_gui()
