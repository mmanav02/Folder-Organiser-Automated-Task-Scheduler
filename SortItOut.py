import os
import shutil
import time

# Define file types
IMAGE_EXTENSIONS = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff']
VIDEO_EXTENSIONS = ['.mp4', '.mov', '.wmv', '.avi', '.mkv']
DOCUMENT_EXTENSIONS = ['.pdf', '.docx', '.xlsx', '.pptx', '.txt', '.csv']
ZIP_EXTENSIONS = ['.zip', '.rar', '.7z', '.tar', '.gz']
# Miscellaneous is anything not matching the above types

# Folder categories
FOLDERS = {
    'Images': IMAGE_EXTENSIONS,
    'Videos': VIDEO_EXTENSIONS,
    'Documents': DOCUMENT_EXTENSIONS,
    'Zip Files': ZIP_EXTENSIONS,
    'Miscellaneous': []
}

def organize_folder(folder_path):
    """Organizes files in the folder by file types and moves subfolders."""
    
    # Handle subfolders
    for item_name in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item_name)
        
        if os.path.isdir(item_path):
            # Skip if it's one of the existing sorting folders
            if item_name not in FOLDERS.keys() and item_name != 'Subfolders':
                subfolder_target = os.path.join(folder_path, 'Subfolders')
                if not os.path.exists(subfolder_target):
                    os.makedirs(subfolder_target)
                
                # Move subfolder to the 'Subfolders' directory
                shutil.move(item_path, os.path.join(subfolder_target, item_name))
    
    # Organize files by extensions
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file_name)[1].lower()
            moved = False

            # Move files to corresponding folders based on extension
            for folder_name, extensions in FOLDERS.items():
                if file_ext in extensions:
                    target_folder = os.path.join(folder_path, folder_name)
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)
                    shutil.move(file_path, os.path.join(target_folder, file_name))
                    moved = True
                    break

            # If no matching extension, move to Miscellaneous
            if not moved:
                target_folder = os.path.join(folder_path, 'Miscellaneous')
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                shutil.move(file_path, os.path.join(target_folder, file_name))

def main(folder_path):
    """Continuously organizes the folder every 10 seconds."""
    while True:
        organize_folder(folder_path)
        break
        # time.sleep(10)  # Sleep for 10 seconds before next check

if __name__ == "__main__":
    user_profile = os.environ.get('USERPROFILE', '')
    folder_to_organize = os.path.join(user_profile, 'Downloads')
    print(f"Started organizing {folder_to_organize}.")
    
    main(folder_to_organize)
