import streamlit as st
import pickle
import numpy as np
from collections import Counter
from src.components.data_preprocess import preprocess
from src.components.data_transformation import scaleData, create_windows


model = pickle.load(open('.\src\dumpFiles\CNN_model.pkl', 'rb'))
label_encoder = pickle.load(open('.\src\dumpFiles\label_encoder.pkl', 'rb'))

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:

    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    # To convert to a string based IO:
    data = bytes_data.decode("utf-8")

    print(data)
    processed_data = preprocess(data)
    scaled_data = scaleData(processed_data)
    sliced_data = create_windows(scaled_data)

    # # Predict the class using the model
    predictions = model.predict(sliced_data)

    # Get the class with maximum probability
    predicted_classes = np.argmax(predictions, axis=1)
    y_pred_list = label_encoder.inverse_transform(predicted_classes)

    counter = Counter(y_pred_list)

    most_occurred_pred = counter.most_common(1)[0][0]

    # Print out prediction results
    st.write(
        f"Let me analyse the data. I think your Dog is {most_occurred_pred}")
