import streamlit as st
from service import send_message
import time

def main():
    """
    A simple Streamlit app that sends a message and displays the response.

    This app displays a title and a button. When the button is clicked, it sends a message
    using the `send_message` function from the `service` module. The response from the
    function is then displayed on the app.

    """
    image = None
    with st.sidebar:
        st.title('Plant Detector')
        st.write('Upload an image of a plant')
        image = st.file_uploader('Upload image', type=['png', 'jpg', 'jpeg']) 
        if image is not None:
            if 'response' in st.session_state:
                del st.session_state['response']
            st.image(image, caption='Uploaded image', use_column_width=True)
            if st.button('Detect plant'):
                with st.empty():
                    st.write('Detecting plant...')
                    st.session_state['response'] = send_message(image)
                    if 'response' in st.session_state:
                        st.write('Plant detected!')
                    
    
    if 'response' in st.session_state:
        st.write('Plant detected!')
        col1, col2 = st.columns(2)
        col1.image(image, caption='Uploaded image', use_column_width=True)
        col2.write(st.session_state.response.text)   
        


if __name__ == '__main__':
    main()
    

