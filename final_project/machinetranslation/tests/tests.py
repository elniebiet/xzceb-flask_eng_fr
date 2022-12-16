import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello, how are you?"), "\"Bonjour, comment es-tu?\"")


class TestFrenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertEqual(frenchToEnglish("Bonjour, comment es-tu?"), "\"Hello, how are you?\"")

class TestForNullEnglishToFrench(unittest.TestCase):
    def test3(self):
        self.assertEqual(englishToFrench(""), "")

class TestForNullFrenchToEnglish(unittest.TestCase):
    def test4(self):
        self.assertEqual(frenchToEnglish(""), "")

class TestForHelloEnglishToFrench(unittest.TestCase):
    def test5(self):
        self.assertEqual(englishToFrench("Hello"), "\"Bonjour\"")
    
class TestForBonjourFrenchToEnglish(unittest.TestCase):
    def test6(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "\"Hello\"")


unittest.main()
