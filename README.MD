# Plant Detector App

This repository contains a simple Streamlit application for detecting plants from uploaded images. The app utilizes a generative AI model to identify the plant and provide care instructions.

 ### [Streamlit App](https://foodmaker-3am7qzesdgisqqxzzep3if.streamlit.app/)

## Overview

The application allows users to upload an image of a plant and then detects the plant using a generative AI model. It displays the plant's name, scientific name, and care instructions. The app consists of two main components:
- `app.py`: The Streamlit app that handles the user interface and image upload.
- `service.py`: The service module that interacts with the AI model to process the image and generate the response.

# Usage
When you run the app, you will see a sidebar with the title "Plant Detector". Here, you can upload an image of a plant in png, jpg, or jpeg format. After uploading the image, click the "Detect plant" button to start the detection process. The app will display the detected plant's name, scientific name, and care instructions.

## Files Description

### `app.py`

The main Streamlit app file. It provides the user interface for uploading an image and displays the detection results. The main function initializes the app, handles the image upload, and calls the `send_message` function from the `service` module to get the plant details.

### `service.py`

This module contains the logic for interacting with the generative AI model. It configures the model with specific generation and safety settings, and the `send_message` function sends the uploaded image to the model for processing. The response from the model is expected to be in JSON format, which is parsed and returned to the app for display.