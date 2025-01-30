from rembg import remove
from PIL import Image

img_path = "/Users/lxiaodoh/PycharmProjects/tufting/dog.jpeg"
output_path = "/Users/lxiaodoh/PycharmProjects/tufting/dog_removeBackground.png"

def remove_background(input_path, output_path):
    # Open the input image
    input_image = Image.open(input_path)

    # Perform background removal
    output_image = remove(input_image)

    # Save the output image
    output_image.save(output_path)


if __name__ == "__main__":
    remove_background(img_path, output_path)
    print("Background removal completed!")