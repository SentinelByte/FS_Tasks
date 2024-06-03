import os

def set_permissions():
    # Introduction
    print("=== File Permissions Setter ===")
    # User inputs directory path, user ID, group ID, and permissions
    directory = input("Enter directory path: ")
    user = int(input("Enter user ID: "))
    group = int(input("Enter group ID: "))
    permissions = int(input("Enter permissions in octal form (e.g., 755): "), 8)

    try:
        # Recursively set permissions and ownership for all files and directories within the specified directory
        for root, dirs, files in os.walk(directory):
            for d in dirs:
                os.chown(os.path.join(root, d), user, group)  # Set ownership
                os.chmod(os.path.join(root, d), permissions)  # Set permissions
            for f in files:
                os.chown(os.path.join(root, f), user, group)  # Set ownership
                os.chmod(os.path.join(root, f), permissions)  # Set permissions
        print("File permissions and ownership set successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

set_permissions()
