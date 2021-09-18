import unittest
import sys

from pathlib import Path
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

from translator import frenchtoenglish, englishtofrench

class TestTranslator(unittest.TestCase):
    
    def test_frenchToEnglish(self):
        self.assertEqual(frenchtoenglish('Lundi'), 'Monday')
        self.assertNotEqual(frenchtoenglish('Dimanche'), 'Monday')
        self.assertEqual(frenchtoenglish(), 'No text was provided')
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello')

    def test_englishtofrench(self):
        self.assertEqual(englishtofrench('Monday'), 'Lundi')
        self.assertNotEqual(englishtofrench('Sunday'), 'Lundi')
        self.assertEqual(englishtofrench(), 'No text was provided')
        self.assertEqual(englishtofrench('Hello'), 'Bonjour')
      

if __name__=='__main__':
    unittest.main()
