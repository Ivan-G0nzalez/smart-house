import os

def create_folder_if_not_exists(path):
    try:
        if path is None or path == "":
            raise Exception("Invalid path")
        if not os.path.exists(path):
            os.makedirs(path)
        return True
    except Exception as e:
        raise
