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

    # Divide a lista de valores ASCII em grupos de 3 caracteres
    ascii_groups = [ascii_list[i:i+3] for i in range(0, len(ascii_list), 3)]

    # Calculates the number of pixel rows needed
    num_lines = len(ascii_groups) // MAX_WIDTH + 1

    # Creates an empty image with the appropriate dimensions
    img = Image.new('RGB', (MAX_WIDTH, num_lines), color = 'white')

    # Split the list of ASCII values into groups of 3 characters.

    pixels = img.load()
    for i in range(len(ascii_groups)):
        x = i % MAX_WIDTH
        y = i // MAX_WIDTH
        r = ascii_groups[i][0] << 16
        g = ascii_groups[i][1] << 8
        b = ascii_groups[i][2]
        pixels[x, y] = (r + g + b,)

    
    # Saves the image as a PNG file
    filename='text_image.png'
    img.save(filename, 'PNG')
    return img