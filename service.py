from pathlib import Path
import hashlib
import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st
import tempfile



genai.configure(api_key= st.secrets["API_KEY"])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


      
    

def send_message(image):
    """
    Sends a message using the generative model.

    Returns:
        str: The generated response from the model.
    """
    
    if image is not None:
    # To read file as bytes:
      with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        # Write the image data to the temporary file
        tmp.write(image.getvalue())
        tmp_file_name = tmp.name
      
      prompt_parts = [
      "Do you know what plant this is? How do I best take care of it?\n\n",
      'export in json data',
      'like this: \'name\': "plant_name", \'scientific_name\': "plant scientificname", \'care\': "care_instructions"\n\n',
      '''answer the follwoing factors like Light: Spider plants prefer bright, indirect light. They can tolerate some shade, but they will grow best in a spot that receives at least 4 hours of indirect light per day.
      Water: Water your spider plant when the top inch of soil is dry. Avoid overwatering, as this can lead to root rot.
      Soil: Use a well-draining potting mix for your spider plant.
      Temperature: Spider plants prefer temperatures between 65 and 80 degrees Fahrenheit. They can tolerate cooler temperatures, but they may stop growing.
      Humidity: Spider plants prefer moderate humidity, but they can tolerate dry air. If your home is very dry, you can mist your plant occasionally.
      Fertilizer: Fertilize your spider plant once a month during the growing season (spring and summer).
      Propagation: Spider plants are easy to propagate. You can simply take a cutting from a plantlet (baby spider plant) and pot it in a small pot of well-draining potting mix.''',
      'add good spacing between the factors\n\n',
      genai.upload_file(tmp_file_name),
      ]

      response = model.generate_content(prompt_parts)
    
    return response
