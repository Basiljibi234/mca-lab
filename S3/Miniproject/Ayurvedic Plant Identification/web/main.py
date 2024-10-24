import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Plant classification index
index_to_class = {0: 'Aloevera', 1: 'Amla', 2: 'Arive-Dantu', 3: 'Basale', 4: 'Betel',
                  5: 'Bhrami', 6: 'Coriender', 7: 'Crape_jasmine', 8: 'Curry', 9: 'Drumstick',
                  10: 'Fenugreek', 11: 'Guava', 12: 'Henna', 13: 'Hibiscus', 14: 'Honge', 15: 'Indian_Beech',
                  16: 'Indian_Mustard', 17: 'Insulin', 18: 'Jackfruit', 19: 'Jamaica_Cherry-Gasagase',
                  20: 'Jamun', 21: 'Jasmin', 22: 'Karanda', 23: 'Lemon', 24: 'Mango', 25: 'Marigold',
                  26: 'Mexican_Mint', 27: 'Mint', 28: 'Neem', 29: 'Oleander', 30: 'Palak(Spinach)',
                  31: 'Papaya', 32: 'Parijata', 33: 'Peepal', 34: 'Pomegranate', 35: 'Rasna', 36: 'Rose',
                  37: 'Rose_apple', 38: 'Roxburgh_fig', 39: 'Sandalwood', 40: 'Seethapala', 41: 'tamarind',
                  42: 'Tulsi', 43: 'Turmeric', 44: 'ashoka'}

# TensorFlow Model Prediction
def predict_plant_disease(img_path, confidence_threshold=0.5):
    model = load_model('best_model.h5')
    img = image.load_img(img_path, target_size=(150, 150))  # Load the image with target size
    img_array = image.img_to_array(img)  # Convert the image to a numpy array
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension (1, height, width, 3)
    img_array /= 255.0  # Rescale the image (same as done during training)

    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction, axis=1)[0]
    predicted_class_name = index_to_class[predicted_class]
    confidence = np.max(prediction)

    if confidence < confidence_threshold:
        return f"Error: The input image is likely not there. Confidence: {confidence:.2f}"
    else:
        return f"Predicted plant: {predicted_class_name} with confidence {confidence:.2f}"

# Streamlit Application
# Add custom CSS for background color
st.markdown(
    """
    <style>
    .main {
        background-color: #d4edda;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header("Ayurvedic Plant Identifier")
test_image = st.file_uploader("Choose an Image:")

# Show uploaded image automatically
if test_image is not None:
    st.image(test_image, width=400, use_column_width=True)
    
    # Button to trigger prediction
    if st.button("Predict"):
        # Validate if the image is uploaded
        if test_image is not None:
            # Predict the plant disease
            result = predict_plant_disease(test_image)
            
            # Display the prediction result
            st.success(result)
        else:
            st.error("Please upload an image before predicting.")
