from PIL import Image
import os

def crop_black_bars(image_path, output_dir):
    # Open the image using PIL
    image = Image.open(image_path)
    width, height = image.size

    # Get the RGB color values for black
    black_color = (0, 0, 0)

    # Scan for horizontal black bars
    top_crop = 0
    bottom_crop = height - 1
    for y in range(height):
        if all(image.getpixel((x, y)) == black_color for x in range(width)):
            top_crop = y + 1
        else:
            break

    for y in range(height - 1, -1, -1):
        if all(image.getpixel((x, y)) == black_color for x in range(width)):
            bottom_crop = y
        else:
            break

    # Scan for vertical black bars
    left_crop = 0
    right_crop = width - 1
    for x in range(width):
        if all(image.getpixel((x, y)) == black_color for y in range(height)):
            left_crop = x + 1
        else:
            break

    for x in range(width - 1, -1, -1):
        if all(image.getpixel((x, y)) == black_color for y in range(height)):
            right_crop = x
        else:
            break

    # Check if the cropping coordinates are valid
    if left_crop >= right_crop or top_crop >= bottom_crop:
        print(f"No black bars found in the image: {image_path}")
        output_filename = os.path.basename(image_path)
        output_path = os.path.join(output_dir + "/uncropped/", output_filename)
        cropped_image.save(output_path)
        return

    # Crop the image
    cropped_image = image.crop((left_crop, top_crop, right_crop + 1, bottom_crop + 1))

    # Save the cropped image to the output directory
    output_filename = os.path.basename(image_path)
    output_path = os.path.join(output_dir, output_filename)
    cropped_image.save(output_path)

    print(f"Cropped image saved: {output_path}")

# Prompt the user to enter the input directory path
input_dir = input("Enter the path to the input directory: ")

# Prompt the user to enter the output directory path
output_dir = input("Enter the path to the output directory: ")

# Iterate over each file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        image_path = os.path.join(input_dir, filename)
        crop_black_bars(image_path, output_dir)
