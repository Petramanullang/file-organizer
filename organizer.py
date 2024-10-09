import os
import shutil

# Buat nyari item di dalam path / membaca folder
folder_path = input("masukkan pathname:")

custom_folder = {
    'TXT': ['txt'],
    'PDF': ['pdf'],
    'WORD': ['doc', 'docx'],
    'EXCEL': ['xls', 'xlsx'],
    'PPT': ['pptx', 'ppt'],
    'Picture': ['jpg', 'jpeg', 'png', 'gif'],
    'Video': ['mp4', 'mkv', 'avi'],
    'Audio': ['mp3', 'wav'],
    'Zip' : ['zip', 'rar'],
    'SVG': ['svg'],
    'ETC': [] 
}

# Mengambil Daftar item di dalam folder
items = os.listdir(folder_path)


# Memeriksa Apakah dia Item / Folder
for item in items:
    item_path = os.path.join(folder_path, item)

    if item.startswith('.'):
        continue

    if os.path.isfile(item_path):
        file_extension = item_path.split(".")[-1].lower()
        folder_name = 'Lainnya'

        for key, value in custom_folder.items():
            if file_extension in value:
                folder_name = key
                break

        extension_folder = os.path.join(folder_path, folder_name)

        if not os.path.exists(extension_folder):
            os.makedirs(extension_folder)
            print(f"{file_extension} sudah dibuat.")

        shutil.move(item_path, os.path.join(extension_folder, item))

    elif os.path.isdir(item_path):
        print(f"{item} adalah folder dan tidak dipindahkan.")
        