import os
import shutil

# Path to the folder containing your audio dataset
dataset_path = '/path/to/dataset/Audio'

# Path to the new folder where filtered audio will be moved
output_folder = '/path/to/output_folder'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Function to check if the file matches the required criteria
def is_relevant_file(filename):
    # Extract parts of the filename based on the naming convention
    parts = filename.split('-')
    
    # Check if the filename has the expected structure (e.g., '03-01-06-01-02-12-02-01-01-16.wav')
    if len(parts) < 10:
        return False
    
    # Age check (Age > 65 corresponds to '01' in filename)
    age = parts[7]
    if age != '01':
        return False
    
    # Emotion check (scream = '16', panic = '36', angry = '15', pain = '11')
    emotion = parts[2]
    if emotion not in ['16', '36', '15', '11']:
        return False
    
    return True

# Loop through all files in the dataset directory
for root, dirs, files in os.walk(dataset_path):
    for file in files:
        if file.endswith('.wav'):  # Only process .wav files
            if is_relevant_file(file):
                # Get the full path of the current audio file
                source_file_path = os.path.join(root, file)
                
                # Get the destination path in the output folder
                destination_file_path = os.path.join(output_folder, file)
                
                # Move the file to the new folder
                shutil.move(source_file_path, destination_file_path)
                print(f"Moved: {file}")

print("Processing complete. All relevant audio files are moved to the output folder.")
