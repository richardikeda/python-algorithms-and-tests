import unittest
from PIL import Image
from unittest import TestCase

from algorithms.text_to_image import text_to_image
from algorithms.image_to_text import image_to_text

class TextToImageTestCase(TestCase):

    def test_text_to_image(self):
        # Tests if the text_to_image function correctly generates an image with one row of length 4
        text = "Eu Te Amo"

        actual_filename =  text_to_image(text)

        expected_filename = "tests/img/expected.png"
        expected_img = Image.new('RGB', (4, 1), color = 'white')

        expected_pixels = expected_img.load()
        expected_pixels[0, 0] = (69, 117,32) #"Eu "
        expected_pixels[1, 0] = (84, 101, 32) #"Te "
        expected_pixels[2, 0] = (65, 109, 111) #"Amo"
        expected_pixels[3, 0] = (255, 255, 255) #white space test
        
        expected_img.save(expected_filename, 'PNG')
        
        with open(expected_filename, 'rb') as expected_file:
            expected_bytes = expected_file.read()
        with open(actual_filename, 'rb') as actual_file:
            actual_bytes = actual_file.read()
        self.assertEqual(expected_bytes, actual_bytes)

class TextToImageFromTxtTestCase(TestCase):
    def test_text_to_image_from_txt(self):
        # read file
        with open("tests/txt/test1.txt", "r") as f:
            text = f.read()

        actual_filename = text_to_image(text)

        # verify that the image can be read back to the original text
        read_text = image_to_text(actual_filename)

        self.assertEqual(text, read_text)

    def test_non_multiple_of_3(self):
        # Ensures that text length not multiple of 3 doesn't crash and is padded properly
        actual_filename = text_to_image("Hello") # 5 characters
        img = Image.open(actual_filename)
        pixels = img.load()
        # "Hel" -> (72, 101, 108)
        self.assertEqual(pixels[0, 0], (72, 101, 108))
        # "lo" -> (108, 111, 255) padding with 255
        self.assertEqual(pixels[1, 0], (108, 111, 255))
        # End of message -> (255, 255, 255)
        self.assertEqual(pixels[2, 0], (255, 255, 255))


if __name__ == '__main__':
    unittest.main()
