import os
import shutil

# Path to the folder containing your audio dataset
dataset_path = r'D:\archive\ASVP-ESD-Update\Audio'

# Path to the folder where filtered audio will be moved
output_folder = r'D:\filtered_audio'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Create Non-Panic folder if it doesn't exist
non_panic_folder = os.path.join(output_folder, 'non_panic')
os.makedirs(non_panic_folder, exist_ok=True)

# Function to check if the file matches the required criteria for Panic
def is_relevant_file_for_panic(filename):
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
    if emotion in ['16', '36', '15', '11']:
        return True

    return False


# Loop through all files in the dataset directory to identify Non-Panic files.
for root, dirs, files in os.walk(dataset_path):
    for file in files:
        if file.endswith('.wav'):  # Only process .wav files
            # Check if the file is already in the panic folder
            panic_file_path = os.path.join(output_folder, 'panic', file)
            if os.path.exists(panic_file_path):
                continue  # Skip the file if it has already been moved to the panic folder

            # If not in panic folder, classify as Non-Panic
            # Check if the file meets Panic criteria
            if is_relevant_file_for_panic(file):
                continue  # Skip files that are relevant to Panic (already moved)

            # Get the full path of the current audio file
            source_file_path = os.path.join(root, file)

            # Get the destination path in the Non-Panic folder
            destination_file_path = os.path.join(non_panic_folder, file)

            # Move the file to the Non-Panic folder
            shutil.move(source_file_path, destination_file_path)
            print(f"Moved to Non-Panic: {file}")

print("Processing complete. Panic and Non-Panic audio files have been organized.")
