import os
import glob

directory = "/home/wayne/Documents/LTspice"

del_files = glob.glob(os.path.join(directory, "*.raw"))

for file_path in del_files:
    try:
        os.remove(file_path)
        print("Deleted Successfull")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")
        

