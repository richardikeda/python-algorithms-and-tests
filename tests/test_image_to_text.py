from algorithms.image_to_text import image_to_text

# This test is for the image_to_text function in algorithms/image_to_text.py.
# The function takes an image file path and converts the text in the image to a string.
# In this test, an image file containing the text is passed to the function, and the resulting string is printed.
image_file_path = "test_image.png"
resulting_text = image_to_text(image_file_path)
print(resulting_text)