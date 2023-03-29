from algorithms.text_to_image import text_to_image

# This test is for the text_to_image function in algorithms/text_to_image.py.
# The function takes a text string and converts it into an image with the specified width and height. 
# In this test, the text "Eu Te Amo" is passed to the function, and the resulting image has a width of 4 pixels and a height of 1 pixel. 
# The last pixel of the image is set to the color white (RGB(255,255,255)).
text = "Eu Te Amo"
text_to_image(text)