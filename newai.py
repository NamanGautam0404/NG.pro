import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np

# Load a pre-trained MobileNetV2 model
model = tf.keras.applications.MobileNetV2(weights="imagenet")

# Function to open an image file dialog
def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        display_image(file_path)
        analyze_image(file_path)

# Function to display the selected image
def display_image(image_path):
    image = Image.open(image_path)
    image = image.resize((300, 300))
    photo = ImageTk.PhotoImage(image)
    
    # Update the label widget to display the new image
    image_label.config(image=photo)
    image_label.image = photo

# Function to analyze the image using AI
def analyze_image(image_path):
    image = Image.open(image_path)
    image = image.resize((224, 224))  # Resize image to match MobileNetV2 input size
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    image = np.expand_dims(image, axis=0)

    # Predict the image class
    predictions = model.predict(image)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)[0]
    top_prediction = decoded_predictions[0]

    # Display the AI analysis result
    result_label.config(text=f"AI Analysis: {top_prediction[1]} ({top_prediction[2]:.2%})")

# Function to save patient information to a text file
def save_patient_info():
    patient_id = patient_id_entry.get()
    patient_name = patient_name_entry.get()
    age = age_entry.get()
    sex = sex_entry.get()
    mobile_no = mobile_no_entry.get()
    image_type = image_type_var.get()

    patient_info = f"Patient ID: {patient_id}\nPatient Name: {patient_name}\nAge: {age}\nSex: {sex}\nMobile No: {mobile_no}\nImage Type: {image_type}"
    
    # Save patient info to a text file
    with open(f"patient_{patient_id}.txt", "w") as file:
        file.write(patient_info)
    
    # Display a confirmation message
    confirmation_label.config(text=f"Patient information saved as patient_{patient_id}.txt")

# Create the main application window
root = tk.Tk()
root.title("AI-Based Diagnostic Assistance")

# Create and configure patient information entry fields
patient_id_label = tk.Label(root, text="Patient ID:")
patient_id_entry = tk.Entry(root)
patient_name_label = tk.Label(root, text="Patient Name:")
patient_name_entry = tk.Entry(root)
age_label = tk.Label(root, text="Age:")
age_entry = tk.Entry(root)
sex_label = tk.Label(root, text="Sex:")
sex_entry = tk.Entry(root)
mobile_no_label = tk.Label(root, text="Mobile No:")
mobile_no_entry = tk.Entry(root)

# Create a dropdown menu for image types
image_types = ["USG", "PET SCAN", "XRAY", "MRI", "CTSCAN"]
image_type_var = tk.StringVar()
image_type_var.set(image_types[0])
image_type_menu = tk.OptionMenu(root, image_type_var, *image_types)

# Create buttons to open images and analyze
open_button = tk.Button(root, text="Open Image", command=open_image)
analyze_button = tk.Button(root, text="Analyze Image", command=analyze_image)

# Create a label to display the selected image
image_label = tk.Label(root)

# Create a label to display AI analysis results
result_label = tk.Label(root, text="", wraplength=300)

# Create a button to save patient information
save_button = tk.Button(root, text="Save Patient Info", command=save_patient_info)

# Create a label for confirmation message
confirmation_label = tk.Label(root, text="")

# Layout the widgets using grid
patient_id_label.grid(row=0, column=0)
patient_id_entry.grid(row=0, column=1)
patient_name_label.grid(row=1, column=0)
patient_name_entry.grid(row=1, column=1)
age_label.grid(row=2, column=0)
age_entry.grid(row=2, column=1)
sex_label.grid(row=3, column=0)
sex_entry.grid(row=3, column=1)
mobile_no_label.grid(row=4, column=0)
mobile_no_entry.grid(row=4, column=1)
image_type_menu.grid(row=5, column=0)
open_button.grid(row=5, column=1)
analyze_button.grid(row=5, column=2)
image_label.grid(row=6, column=0, columnspan=3)
result_label.grid(row=7, column=0, columnspan=3)
save_button.grid(row=8, column=0, columnspan=3)
confirmation_label.grid(row=9, column=0, columnspan=3)

# Start the main GUI loop
root.mainloop()
