import os
import zipfile
import shutil

from unrar import rarfile


def un_zip(file_name):
    f = zipfile.ZipFile(file_name, 'r')
    path = file_name + "_files/"
    for fn in f.namelist():
        f.extract(fn, path)
    for temp_name in os.listdir(path):
        new_name = temp_name.encode('cp437')
        new_name = new_name.decode("gbk")
        os.rename(path + temp_name, path + new_name)
    os.remove(file_name)


def un_rar(file_name):
    rar = rarfile.RarFile(file_name)
    rar.extractall(file_name + '_files/')
    os.remove(file_name)


def copy_ppt(src_path, target_path):
    count = 1
    for dir_path, dir_names, file_names in os.walk(src_path):
        if len(file_names) != 0:
            for file_name in file_names:
                if '.ppt' in file_name or '.pptx' in file_name:
                    file_path = os.path.join(dir_path, file_name)
                    if os.path.exists(target_path.format(file_name)):
                        shutil.copyfile(file_path, target_path.format(str(count) + file_name))
                        count += 1
                    else:
                        shutil.copyfile(file_path, target_path.format(file_name))


if __name__ == '__main__':
    copy_ppt(src, target)
