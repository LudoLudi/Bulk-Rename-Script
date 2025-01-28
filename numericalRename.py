import os

def rename_files_in_numerical_order(folder_path):
    try:
        # Get a sorted list of all files in the folder
        files = sorted(os.listdir(folder_path))
        # Filter out directories and focus only on files
        files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

        # Rename each file
        for idx, file_name in enumerate(files, start=1):
            # Get the file extension
            file_ext = os.path.splitext(file_name)[1]
            # Construct the new file name with zero-padding
            new_name = f"{idx:02}{file_ext}"
            # Get the full paths for the old and new file names
            old_file_path = os.path.join(folder_path, file_name)
            new_file_path = os.path.join(folder_path, new_name)
            # Rename the file
            os.rename(old_file_path, new_file_path)

        print(f"Renamed {len(files)} files in '{folder_path}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace with the path to the folder containing your files
folder_path = input("Enter the path to the folder: ").strip()
rename_files_in_numerical_order(folder_path)
