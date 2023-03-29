import unittest
from PIL import Image
from unittest import TestCase

from algorithms.text_to_image import text_to_image

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

if __name__ == '__main__':
    unittest.main()
