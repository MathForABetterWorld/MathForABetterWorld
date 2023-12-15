import streamlit as st
import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import PhotoImage

def image_slideshow(image_folder_path, delay=1000):
    # Create a Tkinter window for the slideshow
    root = tk.Tk()
    root.withdraw()  # Hide the window

    # Get a list of image files in the specified folder
    image_files = [f for f in os.listdir(image_folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    # Load the images
    images = [Image.open(os.path.join(image_folder_path, image_file)) for image_file in image_files]
    image_index = 0

    # Create a label to display the images
    image_label = tk.Label(root)
    image_label.pack()

    def update_image():
        nonlocal image_index
        image = ImageTk.PhotoImage(images[image_index])
        image_label.config(image=image)
        image_label.image = image
        image_index = (image_index + 1) % len(images)
        root.after(delay, update_image)

    update_image()
    root.after(delay, update_image)
    root.mainloop()
