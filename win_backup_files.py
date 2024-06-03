import shutil
import os

## Note! this script is adjust for Windows File System.
## If U want to use it on a Linux FS, U must modify the path separators and directory structures.
## Enjoy (: DanCohVax.

def backup_files():
    # Ask for source & backup dirs
    source_dirs = input("Enter source dir separated by comma: ").split(",")
    backup_dir = input("Enter backup directory: ")
    
    success = True  # Flag to track if all files were successfully backed up
    
    # Iterate each src dir
    for source_dir in source_dirs:
        # Recursively walk through dir tree
        for root, dirs, files in os.walk(source_dir.strip()):
            # Iterate through files
            for file in files:
                # Construct src & dest paths for each file
                source_path = os.path.join(root, file)
                dest_path = os.path.join(backup_dir, os.path.relpath(source_path, source_dir.strip()))
                # Ensure dest dirs exists
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                try:
                    # Copy file to backup location
                    shutil.copy2(source_path, dest_path)
                    # Print "successful copy"
                    print(f"[V] Copied {source_path} to {dest_path}")
                except Exception as e:
                    # If an error occurs during copying, set success flag to False
                    success = False
                    # Print an error message
                    print(f"[X] Failed to copy {source_path}: {e}")
    
    # Print final status
    if success:
        print("[+] Backup completed successfully!")
    else:
        print("[!] Backup completed with errors. Some files may not have been copied.")

backup_files()
