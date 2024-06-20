#
# # Calculate the total size of files in a directory in bytes
# Pratyakcha Upadhyay

import os

def get_directory_size(directory_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size

# Specify the directory path
directory_path = "C:\Prats Python Files"

# Calculate the total size of files in the directory
total_size_bytes = get_directory_size(directory_path)

# Print the result
print(f"Total size of files in {directory_path}: {total_size_bytes} bytes")

