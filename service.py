from pathlib import Path
import hashlib
import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st
import tempfile
load_dotenv()

genai.configure(api_key= os.getenv("API_KEY"))

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
      genai.upload_file(tmp_file_name),
      ]

      response = model.generate_content(prompt_parts)
    
    return response