import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import cv2 as cv
import torch

st.set_page_config(page_title="Digit Sketch Predictor App")

# Load model
model = torch.load("model_091021_v2.pth", map_location=torch.device("cpu"))
model.eval()

# Sidebar
st.sidebar.title("About This Project")
st.sidebar.write("This project was built as a showcase of an end-to-end machine learning project from training a ResNet18 based classifier using PyTorch all the way to containerizing and deploying using Docker.")
st.sidebar.write(
    "The current model used here was trained on 60000 images and has an accuracy of 99% on a test set.")
st.sidebar.write(
    "Visit the repository for this app [here!](https://github.com/tengznaim/digit-sketch-predictor)")
st.sidebar.write("Built with ♥ by Tengku Naim")

# Main App
st.title("Digit Sketch Predictor")
st.write("Draw a digit between 0-9 and see if an AI can guess your drawing!")

canvas_col, result_col = st.columns((2, 1))

with canvas_col:
    canvas = st_canvas(
        stroke_width=25,
        stroke_color="#FFFFFF",
        background_color="#000000",
        background_image=None,
        update_streamlit=True,
        height=400,
        width=400,
        drawing_mode="freedraw",
        key="canvas",
    )

    submit = st.button("Submit")

with result_col:
    if submit:
        if len(canvas.json_data["objects"]) > 0:
            image = cv.resize(canvas.image_data.astype('uint8'), (28, 28))
            colour_converted = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            colour_converted = np.expand_dims(colour_converted, 0)

            input_image = torch.from_numpy(
                colour_converted).unsqueeze(0).float()
            input_image.div_(255)

            with torch.no_grad():
                predictions = model(input_image).numpy()
                label = np.argmax(predictions, axis=1)[0]

            st.markdown(
                f"<h1 style='text-align: center;'>Predicted Digit:</h1>", unsafe_allow_html=True)
            st.markdown(
                f"<h1 style='text-align: center;'>{label}</h1>", unsafe_allow_html=True)

        else:
            st.error("Make sure you've drawn something!")
