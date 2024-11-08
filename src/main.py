import numpy as np
import librosa
from keras.models import load_model
import os
import sys

# Set the encoding for console output
os.environ["PYTHONIOENCODING"] = "utf-8"

# Load the model
model_path = r'C:\Users\Dell\Desktop\emotion_detection\model\TOGETHER-FORVER-VOICE ANALYSIS MODEL.h5'

try:
    model = load_model(model_path)
    print("Model loaded successfully.")
except FileNotFoundError:
    print(f"Error: The model file was not found at the path: {model_path}")
    exit(1)
except Exception as e:
    print(f"An error occurred while loading the model: {e}")
    exit(1)


# Function to load audio from file
def load_audio_file(file_path, fs=22050):
    try:
        audio_data, _ = librosa.load(file_path, sr=fs)
        print("Audio file loaded successfully.")
        return audio_data
    except FileNotFoundError:
        print(f"Error: The audio file was not found at the path: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while loading the audio file: {e}")
        return None


# Function to extract MFCCs
def extract_mfcc(audio_data, fs=22050):
    mfccs = librosa.feature.mfcc(y=audio_data, sr=fs, n_mfcc=40)
    mfccs = np.mean(mfccs.T, axis=0)
    return mfccs.reshape(1, -1)  # Reshape for prediction


# Function to predict emotion
def predict_emotion(audio_data):
    try:
        mfccs = extract_mfcc(audio_data)
        print(f"MFCCs Shape: {mfccs.shape}")
        prediction = model.predict(mfccs)
        print(f"Predictions Shape: {prediction.shape}")
        return prediction
    except Exception as e:
        print(f"An error occurred during prediction: {e}")
        return None


# Main execution flow
if __name__ == "__main__":
    # Replace 'your_audio_file_path.wav' with the path to your audio file
    audio_file_path = r'C:\Users\Dell\Downloads\OAF_bar_ps.wav'
    audio_data = load_audio_file(audio_file_path)

    if audio_data is not None:
        predictions = predict_emotion(audio_data)
        if predictions is not None:
            predicted_index = np.argmax(predictions)
            # Assuming you have a predefined list of emotion labels
            emotion_labels = ['Anger', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']  # Update as needed
            predicted_emotion = emotion_labels[predicted_index]

            # Use sys.stdout to print the predicted emotion with proper encoding
            sys.stdout.buffer.write(f'Predicted Emotion: {predicted_emotion}\n'.encode('utf-8'))
