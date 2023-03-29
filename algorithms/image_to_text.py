from PIL import Image


def image_to_text(image_path):
    """
    Converts the image in a text string.

   
    Args:
        image_path: A string containing the name of image to be a text.

    Returns:
        A text string extracted from image.
        
    """
def image_to_text(image_path):
    # Open the image
    img = Image.open(image_path)

    # Extract the pixels from the image
    pixels = img.load()

    # Convert the colors of the pixels into ASCII values
    ascii_list = []
    ignore_next_blue = False #fix blue
    ignore_gb = False 
    for y in range(img.height):
        for x in range(img.width):
            b, g, r = pixels[x, y]
            if ignore_gb and g == 255 and b == 255: # Check if G and B should be ignored
                continue
            if (ignore_next_blue and b == 255): #fix blue
                ignore_next_blue = False #fix blue
                continue #fix blue
            if (r, g, b) == (255, 255, 255) and (x == img.width - 1): # Stop when finding the validating pixel
                return ''.join(map(chr, (ascii_list)))
            ascii_list.extend([r, g, b])
            
            ignore_next_blue = (x == img.width - 2) and (b == 255) #fix blue
            ignore_gb = (x == img.width - 2) and (g == 255 and b == 255) # Determine if G and B should be ignored
            
    # Convert the list of ASCII values into a string
    ascii_str = ''.join(map(chr, (ascii_list)))
    
    # Replace the '\n' sequence with a line break
    text = ascii_str.replace('\\n', '\n')
    
    return text
    

    return