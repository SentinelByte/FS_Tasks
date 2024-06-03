import os

def analyze_disk_usage():
    # Introduction
    print("=== Disk Usage Analyzer ===")
    # User inputs directory path
    directory = input("Enter directory path: ")

    try:
        disk_usage = {}
        # Recursively calculate disk usage for each directory and file within the specified directory
        for root, dirs, files in os.walk(directory):
            total_size = sum(os.path.getsize(os.path.join(root, name)) for name in files)
            disk_usage[root] = total_size

        # Sort and print the summary of disk usage
        sorted_disk_usage = sorted(disk_usage.items(), key=lambda x: x[1], reverse=True)
        print("Summary of disk usage:")
        for directory, size in sorted_disk_usage:
            print(f"{directory}: {size / (1024*1024)} MB")
    except Exception as e:
        print(f"An error occurred: {e}")

analyze_disk_usage()
