import unittest
from PIL import Image
from algorithms.image_to_text import image_to_text

class ImageToTextTestCase(unittest.TestCase):

    def test_image_to_text(self):
        # Load an image containing text
        image_path = "text_image.png"

        # Convert the image to text using image_to_text function
        expected_text = "Eu Te Amo"

        actual_text = image_to_text(image_path)

        # Assert that the converted text is the same as the expected text
        self.assertEqual(expected_text, actual_text)

if __name__ == '__main__':
    unittest.main()