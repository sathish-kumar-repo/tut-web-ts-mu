import os


def rename_files_in_folder(folder_path, prefix=""):
    files = os.listdir(folder_path)
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

    for index, filename in enumerate(files, start=1):
        name, ext = os.path.splitext(filename)
        new_name = f"{prefix}{index}{ext}"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")


# 📂 Replace this with your folder path
folder_path = r"D:\course\Web Development\tut-web-react-js-mu\temp\TEMP"
rename_files_in_folder(folder_path)

# files = [f for f in files if f.endswith(".jpg")]
