import unittest
from tests.test_text_to_image import TextToImageTestCase
from tests.test_image_to_text import ImageToTextTestCase

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TextToImageTestCase)
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ImageToTextTestCase))
    unittest.TextTestRunner(verbosity=2).run(suite)