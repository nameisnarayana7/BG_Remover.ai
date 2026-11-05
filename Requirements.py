
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from rembg import remove
import io

def choose_image():
    global original_image

    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[
            ("Image Files", "*.jpg *.jpeg *.png")
        ]
    )

    if file_path:
        try:
            original_image = Image.open(file_path).convert("RGBA")
            preview_image(original_image)
        except Exception as e:
            messagebox.showerror("Error", str(e))

def remove_background():
    global result_image

    if original_image is None:
        messagebox.showwarning("Warning", "Please select an image first!")
        return

    try:
        result = remove(original_image)
        result_image = result

        # Display result with white background
        white_bg = Image.new("RGBA", result.size, "white")
        white_bg.alpha_composite(result)

        preview_image(white_bg)

        messagebox.showinfo("Success", "Background removed!")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def preview_image(image):
    image.thumbnail((350, 350))
    photo = ImageTk.PhotoImage(image)

    preview_label.config(image=photo)
    preview_label.image = photo

def save_image():
    if result_image is None:
        messagebox.showwarning("Warning", "Remove background first!")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg")]
    )

    if file_path:
        if file_path.lower().endswith(".jpg"):
            white_bg = Image.new("RGBA", result_image.size, "white")
            white_bg.alpha_composite(result_image)
            white_bg.convert("RGB").save(file_path, quality=95)
        else:
            result_image.save(file_path)

        messagebox.showinfo("Success", "Image saved successfully!")

# Application window
root = tk.Tk()
root.title("Background Remover")
root.geometry("500x550")

original_image = None
result_image = None

tk.Label(
    root,
    text="AI Background Remover",
    font=("Arial", 20, "bold")
).pack(pady=15)

preview_label = tk.Label(root, text="Image Preview")
preview_label.pack(pady=15)

tk.Button(
    root, text="Choose Image",
    command=choose_image,
    width=25
).pack(pady=8)

tk.Button(
    root, text="Remove Background",
    command=remove_background,
    width=25
).pack(pady=8)

tk.Button(
    root, text="Save Image",
    command=save_image,
    width=25
).pack(pady=8)

root.mainloop()
