import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def scaleData(df):

    scaler = pickle.load(open("src\dumpFiles\scaler.pkl", "rb"))
    df_scaled = scaler.transform(df)
    df_scaled = pd.DataFrame(df_scaled, columns=df.columns)

    return df_scaled


def create_windows(df_scaled):
    # Create a sliding window of 10 seconds for the data
    window_size = 128
    stride = 64

    # Generate sequences using sliding windows
    sequences = []
    labels = []
    for i in range(len(df_scaled) - window_size):
        window = df_scaled[i:i+window_size]
        sequences.append(window)

    X_sliding = np.array(sequences)

    return X_sliding
