import unittest
import sys
sys.path.insert(1, './final_project')
import machinetranslation

class TestTranslation(unittest.TestCase):

    def test_frenchToEnglish_null(self):
        self.assertEqual(machinetranslation.frenchToEnglish(None), None)
        

    def test_englishTofrench_null(self):
        self.assertEqual(machinetranslation.englishTofrench(None), None)
        

    def test_frenchToEnglish_Equal(self):
        self.assertEqual(machinetranslation.frenchToEnglish("Bonjour"), "Hello")

    def test_englishTofrench_Equal(self):
        self.assertEqual(machinetranslation.englishTofrench("Hello"), "Bonjour")


if __name__ == '__main__':
    unittest.main()