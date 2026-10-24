
import os
import glob
import sys

directory = input("Enter directory path: ").strip()

if not directory:
    print("No directory provided. Exiting program.")
    sys.exit(0)

if not os.path.isdir(directory):
    print(f"Directory does not exist: {directory}")
    sys.exit(1)

extension = input("Enter file extension (e.g. .raw, .csv): ").strip()

if not extension:
    print("No extension provided. Exiting program.")
    sys.exit(0)


if not extension.startswith("."):
    extension = "." + extension

del_files = glob.glob(os.path.join(directory, f"*{extension}"))

if not del_files:
    print(f"No {extension} files found in {directory}.")
    sys.exit(0)

print(f"Found {len(del_files)} file(s).")

for file_path in del_files:
    try:
        os.remove(file_path)
        print(f"Deleted successfully: {file_path}")
    except OSError as e:
        print(f"Error deleting {file_path}: {e}")

print("Cleanup finished!")
