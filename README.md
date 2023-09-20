# Image to Data URL Converter

This simple Python script allows you to convert an image file into a Data URL and save it to a text file. You can use this script to easily embed images in your web applications or HTML documents.

## Usage

1. Clone or download this repository to your local machine.

2. Make sure you have Python installed on your system.

3. Run the script by executing the following command in your terminal:

   ```
   python image_to_data_url.py
   ```

4. You will be prompted to enter the path to the image file you want to convert. Please provide the full path to the image file, including the file extension (e.g., **C:\path\to\image.jpg** or **/path/to/image.png**).

5. The script will then convert the image into a Data URL and save it to a text file with the same name as the image, but with a **.txt** extension.

6. The Data URL will be saved as follows:

   ```
   data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/...
   ```

7. The Data URL text file will be saved in the same directory where the script is located.

8. You can use the Data URL in your web development projects as needed.

# Error Handling

* If the provided image file path is incorrect or the file does not exist, you will receive a "File not found" error message.

* If any other error occurs during the conversion process, you will receive an error message indicating the issue.

# Note

* Ensure that the Python script and the image file you want to convert are in the same directory or provide the full path to the image file.

* This script currently supports JPEG, JPG, PNG, GIF, WebP, BMP, SVG, ICO, and TIFF images, but you can modify it to support other image formats by changing the data:image/jpeg part of the Data URL to the appropriate MIME type for the image format you want to use.