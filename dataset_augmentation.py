from PIL import Image
import os

from config import PATH_TO_IMAGES2

"""
Script for flipping all training images horizontally in order to double the size of the training set.
Changes labels accordingly if necessary (left flipped -> right).
"""

images = []
labels = []

total = 0
for folder in os.listdir(PATH_TO_IMAGES2):
    folder_path = os.path.join(PATH_TO_IMAGES2, str(folder))
    total += len(os.listdir(folder_path))

counter = 0
for folder in os.listdir(PATH_TO_IMAGES2):
    # Use / operator for Path objects
    folder_path = PATH_TO_IMAGES2 / folder

    # Skip any flipped folders that already exist to avoid an infinite loop
    if folder.endswith('_flipped'):
        continue

    if not os.path.isdir(folder_path):
        continue

    for image in os.listdir(folder_path):
        counter += 1
        progress = counter / total * 100

        print(
            f"[{int(round(progress) / 10 + 1) * '='}>{int(10 - round(progress) / 10 + 1) * '.'}] {round(progress, 2)}% done "
            f"({counter}/{total} images flipped!)")

        # Open the image using the Path object
        img_path = folder_path / image
        original_img = Image.open(img_path)

        # Define the output directory
        output_folder = PATH_TO_IMAGES2 / f"{folder}_flipped"
        output_folder.mkdir(parents=True, exist_ok=True)

        # Flip and Save using Pathlib logic
        horz_img = original_img.transpose(method=Image.FLIP_LEFT_RIGHT)

        # This converts the Path object to a string just for the .save() method
        save_path = output_folder / image
        horz_img.save(str(save_path))

        original_img.close()
        horz_img.close()
