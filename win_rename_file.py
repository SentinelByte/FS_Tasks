import os

def batch_rename_files():
    # Prompt the user to input directory path, pattern, and replacement pattern
    directory = input("Enter directory path: ")
    pattern = input("Enter pattern to search for in filenames: ")
    replacement = input("Enter replacement pattern: ")
    
    # Counter to track the number of files renamed
    renamed_count = 0
    
    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        # Check if the pattern exists in the filename
        if pattern in filename:
            # Construct the new filename by replacing the pattern with the replacement
            new_filename = filename.replace(pattern, replacement)
            # Rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            # Increment the renamed_count
            renamed_count += 1
    
    # Print appropriate message based on the number of files renamed
    if renamed_count == 0:
        print("No files matching the specified pattern found.")
    else:
        print(f"{renamed_count} file(s) renamed successfully!")

batch_rename_files()
