import os
import os.path
import random
import shutil


def prepare_files_for_dataset():
    files = os.listdir('data/training/picture_raw/sprout')
    random.shuffle(files)
    sample = files[:899]
    src = 'data/training/picture_raw/sprout'
    dest = 'data/training/picture/sprout'

    for file_name in sample:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)


def count_files():
    print("Seed pictures raw", sum(len(files) for _, _, files in os.walk('data/training/picture_raw/seed')))
    print("Seed pictures", sum(len(files) for _, _, files in os.walk('data/training/picture/seed')))
    print("Sprout pictures raw", sum(len(files) for _, _, files in os.walk('data/training/picture_raw/sprout')))
    print("Sprout pictures", sum(len(files) for _, _, files in os.walk('data/training/picture/sprout')))


if __name__ == '__main__':
    prepare_files_for_dataset()
    count_files()
