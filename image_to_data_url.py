import base64
from PIL import Image

# Prompt the user for the image file path
image_path = input("Enter the path to the image file: ")

try:
    # Open the image file
    with open(image_path, 'rb') as image_file:
        # Determine the image format using Pillow
        image = Image.open(image_file)
        image_format = image.format.lower()

        if image_format in ["jpeg", "jpg", "png", "gif", "webp", "bmp", "svg", "ico", "tiff"]:
            # Read the image data and encode it as a Data URL
            data_url = f'data:image/{image_format};base64,' + base64.b64encode(image_file.read()).decode()

            # Extract the image file name from the path
            image_name = image_path.split('\\')[-1]

            # Create a text file with the same name as the image and save the Data URL
            with open(image_name + '.txt', 'w') as text_file:
                text_file.write(data_url)

            print(f"Data URL saved to {image_name}.txt")
        else:
            print("Unsupported image format. Please provide an image in a supported format (e.g., JPEG, PNG, GIF).")
except FileNotFoundError:
    print("File not found. Please check the path to the image.")
except Exception as e:
    print(f"An error occurred: {str(e)}")