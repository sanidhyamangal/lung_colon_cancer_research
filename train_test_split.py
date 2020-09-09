#!/usr/bin/python3
"""
author = Ravinder Singh
revision = 07-19-2020
"""
from pathlib import Path
import random
import os

def move_to_test_set(test_path,iterable):
    if not os.path.exists(test_path):
        os.mkdir(test_path)

    for image in iterable:
        if not os.path.exists(os.path.join(test_path, image.parent.name)):
            os.mkdir(os.path.join(test_path, image.parent.name))
        
        NEW_NAME = os.path.join(test_path, image.parent.name, image.name)
        print(f"Moving {str(image)} ===> {NEW_NAME}")
        os.rename(image, NEW_NAME)


def split_train_test(namespace):

    path_to_images = Path(f"{namespace}_image_sets")

    _images_root = [path for path in path_to_images.glob("*")]

    TRAIN_PATH = f"{namespace}_train"
    TEST_PATH = f"{namespace}_test"

    if not os.path.exists(TRAIN_PATH):
        os.mkdir(TRAIN_PATH)
    
    for image in _images_root:
        if not os.path.exists(os.path.join(TRAIN_PATH, image.name)):
            os.rename(str(image), os.path.join(TRAIN_PATH, image.name))

    path_to_train_images = Path(TRAIN_PATH)
    _images = [image for image in path_to_train_images.glob("*")]

    test_images = [random.sample([_test_images for _test_images in image.glob("*")], 500) for image in _images]

    for _test_set in test_images:
        move_to_test_set(TEST_PATH,_test_set)


if __name__ == "__main__":
    for _namescope in ["colon", "lung"]:
        split_train_test(_namescope)
