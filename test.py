import os

current_file_path = os.path.abspath(__file__)
current_folder_path = os.path.dirname(current_file_path)
print(current_folder_path)