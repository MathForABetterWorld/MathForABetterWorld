import streamlit as st
from PIL import Image
import os
import time 

# Get the directory of the current script
script_path = os.path.dirname(__file__)
assets_path = os.path.join(script_path, '..', 'assets')
image_path = os.path.join(assets_path, 'bmore_food_logo_dark_theme.png')

# Set page configuration with the image
st.set_page_config(layout="centered", page_icon=image_path, page_title="Bmore Food")  
# Open the image using Pillow
image = Image.open(image_path)


### Header ###
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.image(image)
with col3:
    st.write(' ')




st.write("This dashboard was made in Spring 2023 by students of the class Math for a Better World in the Johns Hopkins University department of Applied Mathematics & Statistics.")
st.write()
st.write("Students: Chris Anto, Tim Chau, Jillayne Clarke, Matt Kleiman, Nolan Lombardo, Sofia LoVuolo, Gavin McElhennon, Nader Najjar, Joy Neuberger, Emi Ochoa, Krutal Patel, Kiana Soleiman, Jamie Stelnik, Sophia Stone, Kenny Testa, Isabel Thomas, Rishika Vadlamudi, Chris Wilhelm.")
st.write()
st.write("Taught by JC Faulk and Fadil Santosa, with teaching assistant Kaleigh Rudge.")


# Start the image slideshow automatically
# Define the path to the folder containing your images
image_folder_path = os.path.join(assets_path, 'credits_pictures')
# Get a list of image files in the specified folder
image_files = [f for f in os.listdir(image_folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
# Set the delay (in seconds) between images
delay_between_images = 6  # Adjust as needed

# Initialize the index to track the current image
current_image_index = 0
# Run the slideshow
while True:
    image_file = image_files[current_image_index]
    image_path = os.path.join(image_folder_path, image_file)
    image = Image.open(image_path)
    placeholder = st.image(image, use_column_width=True)
    # Add a delay between images
    time.sleep(delay_between_images)
    # Clear the previous image
    placeholder.empty()
    # Increment the current image index and loop back to the first image if necessary
    current_image_index = (current_image_index + 1) % len(image_files)

