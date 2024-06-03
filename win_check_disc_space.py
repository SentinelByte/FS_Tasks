import psutil

def check_disk_space():
    # Ask for free disk space threshold
    threshold_GB = float(input("Enter the threshold for free disk space (in GB): "))
    
    # Get disk partitions info
    partitions = psutil.disk_partitions()
    # Flag to track
    low_disk_space = False
    # Iterate each partition
    for partition in partitions:
        # Disk statistics for the partition
        partition_usage = psutil.disk_usage(partition.mountpoint)
        # Calculate free space (GB)
        free_space_GB = partition_usage.free / (2**30) # Convert bytes to gigabytes
        # Check if free space is below threshold
        if free_space_GB < threshold_GB:
            # Print 
            print(f"[L] Low disk space alert for {partition.mountpoint}: {free_space_GB:.2f} GB free")
            low_disk_space = True
    
    # True if the partitions have sufficient disk space, otherwise False
    return not low_disk_space

# Check disk space and print status message based on return value
if check_disk_space():
    print("[+] Disk space check completed. Partitions have sufficient free space.")
else:
    print("[!] Error. Some partitions have low disk space.")
