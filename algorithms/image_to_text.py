from PIL import Image

def image_to_text(image_path):
    """
    Converts the image in a text string.

   
    Args:
        image_path: A string containing the name of image to be a text.

    Returns:
        A text string extracted from image.
        
    """
    # Open the image
    img = Image.open(image_path)

    # Extract the pixels from the image
    pixels = img.load()

    # Convert the colors of the pixels into ASCII values
    ascii_list = []

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            if (r, g, b) == (255, 255, 255):
                # Stop when finding the validating pixel (end of message)
                # Remove padding 255s that were added to complete a pixel
                while ascii_list and ascii_list[-1] == 255:
                    ascii_list.pop()
                ascii_str = ''.join(map(chr, ascii_list))
                return ascii_str.replace('\\n', '\n')
            ascii_list.extend([r, g, b])
            
    # Fallback in case there is no end pixel but loop finishes
    while ascii_list and ascii_list[-1] == 255:
        ascii_list.pop()
    ascii_str = ''.join(map(chr, ascii_list))
    
    # Replace the '\n' sequence with a line break
    text = ascii_str.replace('\\n', '\n')
    
    return text
