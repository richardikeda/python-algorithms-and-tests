from PIL import Image

def text_to_image(text):
    """
        Converts a text string to an image where each character of the text is represented as a 
        portion of a pixel color. The resulting image has the specified width and height.

        Args:
            text: A string containing the text to be converted to an image.

        Returns:
            Image filename representing the resulting image.

    """

    #Sets the maximum width of the image
    MAX_WIDTH = 500

    # Converts the text into a list of ASCII values
    ascii_list = [ord(c) for c in text]

    # Calculates the number of pixel rows needed
    num_lines = len(ascii_list) // MAX_WIDTH + 1

    # Creates an empty image with the appropriate dimensions
    img = Image.new('RGB', (MAX_WIDTH, num_lines), color = 'white')

    # Fills the pixels with colors corresponding to the ASCII values
    pixels = img.load()
    for i in range(len(ascii_list)):
        x = i % MAX_WIDTH
        y = i // MAX_WIDTH
        r = ascii_list[i]
        #fix the ideia is made division for g and b
        g = 0 
        b = 0
        pixels[x, y] = (r, g, b)

    
    # Saves the image as a PNG file
    filename='text_image.png'
    img.save(filename, 'PNG')
    return 