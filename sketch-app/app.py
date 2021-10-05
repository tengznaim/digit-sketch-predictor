import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import time

# Sidebar for defining sketch configurations
st.sidebar.title("Sketch Configurations")
stroke_width = st.sidebar.slider("Stroke Width:", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke Colour:")

# Main App
st.title("Digit Sketch Predictor")
st.write("Draw a digit between 0-9 and see if an AI can guess your drawing!")

canvas_col, result_col = st.columns((2, 1))

with canvas_col:
    canvas = st_canvas(
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color="#eee",
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
            image = np.array(canvas.image_data)
            gray = image[:, :, 0]
            print(gray)
            with st.spinner("Making a prediction..."):
                time.sleep(5)
            st.image(gray)
        else:
            st.error("Make sure you've drawn something!")
