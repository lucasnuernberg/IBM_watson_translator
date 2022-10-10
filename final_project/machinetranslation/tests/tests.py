import unittest
from final_project.machinetranslation import translator
import machinetranslation.translator


class TestTranslation(unittest.TestCase):

    def test_frenchToEnglish_null(self):
        self.assertEqual(translator.frenchToEnglish(None), None)
        

    def test_englishTofrench_null(self):
        self.assertEqual(translator.englishTofrench(None), None)
        

    def test_frenchToEnglish_Equal(self):
        self.assertEqual(translator.englishTofrench("Bonjour"), "Hello")

    def test_englishTofrench_Equal(self):
        self.assertEqual(translator.englishTofrench("Bonjour"), "Hello")


if __name__ == '__main__':
    unittest.main()