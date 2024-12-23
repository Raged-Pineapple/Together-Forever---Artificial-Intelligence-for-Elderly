import torchaudio
from transformers import Wav2Vec2Processor, Wav2Vec2ForSequenceClassification
import torch

# Load Wav2Vec2 processor and model
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForSequenceClassification.from_pretrained("path_to_your_model_directory")

# Set the model to evaluation mode
model.eval()

def preprocess_audio(file_path):
    """
    Preprocess audio to ensure compatibility with the Wav2Vec2 model.
    - Resamples to 16 kHz
    - Converts to mono if stereo
    """
    # Load audio file
    waveform, sample_rate = torchaudio.load(file_path)

    # Resample to 16 kHz
    if sample_rate != 16000:
        resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
        waveform = resampler(waveform)

    # Convert to mono if the audio is stereo
    if waveform.shape[0] > 1:
        waveform = waveform.mean(dim=0)

    return waveform

def predict_emotion(file_path, model, processor):
    """
    Predict emotion from the given audio file.
    """
    # Preprocess the audio
    audio = preprocess_audio(file_path)

    # Prepare the input for the model
    inputs = processor(audio, sampling_rate=16000, return_tensors="pt", padding=True)

    # Extract input values
    input_tensor = inputs.input_values

    # Predict emotion
    with torch.no_grad():
        logits = model(input_tensor).logits

    # Get the predicted emotion label
    predicted_class_id = torch.argmax(logits, dim=-1).item()
    return predicted_class_id

# Example usage
if __name__ == "__main__":
    # Path to your audio file
    audio_file_path = "03-01-05-01-01-01-03.wav"

    # Predict emotion
    emotion_label = predict_emotion(audio_file_path, model, processor)

    # Print the result
    print(f"Predicted Emotion Label: {emotion_label}")
