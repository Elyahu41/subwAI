import os

from config import PATH_TO_IMAGES2

"""
Script for quickly sorting training images and restoring order in case the original order is not kept anymore.
E.g. after changing labels of certain images in image_check.py.
"""

images = []
labels = []
done = False


def sort():
    for folder in os.listdir(PATH_TO_IMAGES2):
        folder_path = os.path.join(PATH_TO_IMAGES2, str(folder))
        image_list = []
        for image in os.listdir(folder_path):
            if image.endswith('.png') and image[:-4].isdigit():
                image_list.append(int(image[:-4]))
        image_list.sort()
        for i, number in enumerate(image_list):
            if number-1 != i:
                os.rename(os.path.join(folder_path, str(image_list[-1])+'.png'),
                          os.path.join(folder_path, str(number-1)+'.png'))
                print(f'{number} saved in {folder_path}')
                print('restart sorting')
                return False
    print('all done')
    return True


while done is False:
    done = sort()
