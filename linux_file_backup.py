import shutil
import os

'''
Note! This is a .py script dedicated for Linux FS.
Enjoy (: DanCohVax
'''

def backup_files(source_dirs, backup_dir):
    try:
        # Create the backup directory if it doesn't exist
        os.makedirs(backup_dir, exist_ok=True)
        
        # Iterate through each source directory provided by the user
        for source_dir in source_dirs:
            # Recursively walk through the directory tree
            for root, dirs, files in os.walk(source_dir):
                # Iterate through files in the current directory
                for file in files:
                    # Construct source and destination paths for each file
                    source_path = os.path.join(root, file)
                    dest_path = os.path.join(backup_dir, os.path.relpath(source_path, source_dir))
                    # Ensure destination directory exists
                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                    # Copy the file to the backup location
                    shutil.copy2(source_path, dest_path)
        
        print("Backup completed successfully!")
    except Exception as e:
        print(f"An error occurred during backup: {e}")

# Example usage:
source_dirs = ["/path/to/source/dir1", "/path/to/source/dir2"]
backup_dir = "/path/to/backup"
backup_files(source_dirs, backup_dir)
