import os
import shutil

def copy_files_to_new_folder(source_folders, destination_folder):
    """
    Copy all files from multiple source folders into a single destination folder.
    
    Parameters:
        source_folders (list): List of paths to source folders.
        destination_folder (str): Path to the destination folder.
    """
    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Iterate over each source folder
    for folder in source_folders:
        # List all files in the source folder
        for root, _, files in os.walk(folder):
            for file in files:
                source_file = os.path.join(root, file)
                destination_file = os.path.join(destination_folder, file)

                # Copy the file to the destination folder
                shutil.copy2(source_file, destination_file)
                print(f"Copied: {source_file} -> {destination_file}")

# Example usage
source_folders = [
    "/mnt/aix23606/jiyoung/ADD/DS_E01_Encodec/ASVspoof2019_LA_dev_Spoof/E01_02_wav/flac",
    "/mnt/aix23606/jiyoung/ADD/DS_E01_Encodec/ASVspoof2019_LA_eval_Spoof/E01_02_wav/flac",
    "/mnt/aix23606/jiyoung/ADD/DS_E01_Encodec/ASVspoof2019_LA_train_Spoof/E01_02_wav/flac",
    "/mnt/aix23606/jiyoung/ADD/DS_E01_Encodec/inthewild_Spoof/E01_02_flac/flac"
]
destination_folder = "/mnt/aix23606/jiyoung/ADD/DS_E01_Encodec/E01_02/flac"

copy_files_to_new_folder(source_folders, destination_folder)