import unittest
from tests.test_text_to_image import TextToImageTestCase
from tests.test_text_to_image import TextToImageFromTxtTestCase
from tests.test_image_to_text import ImageToTextTestCase

if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(TextToImageTestCase))
    suite.addTest(unittest.makeSuite(ImageToTextTestCase))
    suite.addTest(unittest.makeSuite(TextToImageFromTxtTestCase))

    unittest.TextTestRunner(verbosity=2).run(suite)
