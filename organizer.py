import os
import shutil


def organize_directory(directory_path):
    """
    This function organizes files in a specified directory by their extensions.  
    It creates subfolders for different categories and moves files accordingly.  
    """

    # Mapping of categories to their associated file extensions
    extension_mapping = {
        'Images': ['.jpg', '.jpeg', '.png'],
        'Documents': ['.pdf', '.docx', '.doc'],
        'Software': ['.exe', '.msi'],
        'Archives': ['.zip']
    }

    # Counter for the number of files moved
    moved_files_count = 0

    # Iterate through all entries in the directory
    for entry_name in os.listdir(directory_path):
        entry_path = os.path.join(directory_path, entry_name)

        # Process only if the entry is a file
        if os.path.isfile(entry_path):
            # Extract the file extension and convert to lowercase
            _, extension = os.path.splitext(entry_name)
            extension = extension.lower()

            # Determine the target folder based on the extension
            target_folder = None
            for folder_name, extensions in extension_mapping.items():
                if extension in extensions:
                    target_folder = folder_name
                    break

            # If a target folder is found, proceed to move the file
            if target_folder:
                target_directory = os.path.join(directory_path, target_folder)
                os.makedirs(target_directory, exist_ok=True)

                # Prepare destination path and handle name collisions
                destination_path = os.path.join(target_directory, entry_name)
                base_name, ext = os.path.splitext(entry_name)
                suffix = 1
                while os.path.exists(destination_path):
                    new_name = f"{base_name}_{suffix}{ext}"
                    destination_path = os.path.join(target_directory, new_name)
                    suffix += 1

                # Move the file and update the counter
                shutil.move(entry_path, destination_path)
                moved_files_count += 1

    # Print summary of moved files
    print(f"Moved {moved_files_count} files.")


if __name__ == "__main__":
    # Specify the path to the directory you want to organize
    path = "/path/to/Downloads"  # Replace this with the actual path
    organize_directory(path)
