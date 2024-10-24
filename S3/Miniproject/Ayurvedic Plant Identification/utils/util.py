import os

def list_folders(directory):
    # Check if the provided path is valid
    if not os.path.exists(directory):
        print(f"Error: The directory {directory} does not exist.")
        return
    
    # List only folders in the directory
    folders = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    
    if folders:
        print(f"Folders in {directory}:")
        for folder in folders:
            print(folder)
    else:
        print(f"No folders found in {directory}")

if __name__ == "__main__":
    # Take directory input from user
    user_path = "D:\\mca project\\dataset\\test"
    list_folders(user_path)
