import sys, shutil, re

from pathlib import Path

dic = {'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v',
       'Г': 'H', 'г': 'h', 'Ґ': 'G', 'ґ': 'g', 'Д': 'D', 'д': 'd', 'Е': 'E', 'Є': 'e', 'е': 'e', 'є': 'e', 'Ж': 'Zh',
       'ж': 'zh',
       'З': 'Z', 'з': 'z', 'И': 'Y', 'и': 'y', 'Й': 'Y', 'й': 'y', 'К': 'K', 'к': 'k', 'Л': 'L', 'л': 'l',
       'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r',
       'С': 'S', 'с': 's', 'Т': 'T', 'т': 't', 'У': 'U', 'у': 'u', 'Ф': 'F', 'ф': 'f', 'Х': 'Kh', 'х': 'kh',
       'Ц': 'Tc', 'ц': 'tc', 'Ч': 'Ch', 'ч': 'ch', 'Ш': 'Sh', 'ш': 'sh', 'Щ': 'Shch', 'щ': 'shch', 'Ю': 'Iu', 'ю': 'iu',
       'Я': 'Ia', 'я': 'ia', 'Ь': '', 'ь': '', }

ext_dict = {'images': ['JPEG', 'PNG', 'JPG', 'SVG', 'GIF'],
            'video': ['AVI', 'MP4', 'MOV', 'MKV'],
            'documents': ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX', 'XLS'],
            'audio': ['MP3', 'OGG', 'WAV', 'AMR'],
            'archives': ['ZIP', 'GZ', 'TAR', 'RAR']}

list_ext = []
list_unknown_ext = []
files_list = []

#path = Path(sys.argv[1])
path = Path(input('Input path to folder: '))

# path = Path('D:\Розбрати')

fix_path = path


def normalize(name_):
    result = str()
    file_name = name_.stem
    ext = name_.suffix
    for i in range(0, len(file_name)):
        if file_name[i] in dic:
            simb = dic[file_name[i]]
        else:
            simb = file_name[i]
        result = result + simb
    new_file_name = (''.join(re.findall(r"\w+", result))) + ext
    return new_file_name


def move_and_rename(file_old_name, file_new_name, path, new_path):
    path_file: str = f"{path}\{file_old_name}"
    path_file_new: str = f"{new_path}\{file_new_name}"
    shutil.move(path_file, path_file_new)


def create_folders_sort_extensions(folder):
    path_folder = path / folder
    if not path_folder.is_dir():
        path_folder.mkdir()


def parse_folder_recursion(path):
    for element in path.iterdir():
        if element.is_dir():
            parse_folder_recursion(element)
        else:
            extension_file = element.suffix.upper()
            if element.suffix.upper() not in list_ext:
                list_ext.append(element.suffix.upper())
            i = 0
            for key, value in ext_dict.items():

                if extension_file.removeprefix('.') in value:
                    i += 1
                    create_folders_sort_extensions(key)
                    path_folder = fix_path / key
                    file_new_name = normalize(element)
                    move_and_rename(element.name, file_new_name, path, path_folder)

            if i == 0:
                if element.suffix.upper() not in list_unknown_ext:
                    list_unknown_ext.append(element.suffix.upper())
                key = 'unknown_extensions'
                create_folders_sort_extensions(key)
                path_folder = fix_path / key
                move_and_rename(element.name, element.name, path, path_folder)

    return list_ext, list_unknown_ext


def delete_empty_folders(path):
    for element in path.iterdir():
        if element.is_dir():
            try:
                delete_empty_folders(element)
                path_empty_folder = path / element.name
                path_empty_folder.rmdir()

            # except OSError as e:
            # print("Folder: %s : %s" % (path/element.name, e.strerror))
            except:
                pass


def list_files_category(path):
    lst = []
    for element in path.iterdir():

        for file in element.iterdir():
            lst.append(file.name)
        print(f'Category {element.name}: {lst}')
        lst = []


def unpack_archive(path):
    if path.is_dir():
        # if Path(path).exists():
        for archive in path.iterdir():
            archive_name = path / archive.name
            folder_name = path / archive.stem
            try:
                shutil.unpack_archive(archive_name, folder_name)
                if archive.is_dir() == False:
                    archive.unlink()
            except:
                pass
            # except OSError as e:
            #     print("Ошибка: %s : %s" % (archive_name, e.strerror))


def cleanfunction(path):
    parse_folder_recursion(path)
    print(f'Перелік всіх розширень: {list_ext}')
    print(f'Перелік невідомих розширень: {list_unknown_ext}')
    path_archive_folder = path / 'archives'
    unpack_archive(path_archive_folder)
    delete_empty_folders(path)
    list_files_category(path)


if __name__ == "__main__":
    cleanfunction(path)
   
   