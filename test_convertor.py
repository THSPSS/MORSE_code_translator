import unittest
from converter_MORSE import ConverterMorse as cm

class TestConvertorMorse(unittest.TestCase):

    def test_convertor(self):
        self.assertEqual(cm.makingList("A"),'.-')

    def test_convertor_string(self):
        self.assertEqual(cm.makingList("A/B/C/D"),'.- -... -.-. -..')

    def test_convertor_not_existing_char(self):
        self.assertEqual(cm.makingList("ABCD#%"),'Invalid input')

    def test_convertor_put_morse_code(self):
        self.assertEqual(cm.makingList(".-"),'A')


if __name__ == '__main__':
    unittest.main()