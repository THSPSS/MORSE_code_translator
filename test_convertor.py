import unittest
from converter_MORSE import ConvertorMorse as cm

class TestConvertorMorse(unittest.TestCase):

    def test_get_null_input(self):
        self.assertEqual(cm.getInput("") , "Please enter your message")

    def test_get_string_input(self):
        self.assertEqual(cm.getInput("D123"), "D123")

    def test_convertor(self):
        self.assertEqual(cm.convertor("A"),'.-')

    def test_convertor_string(self):
        self.assertEqual(cm.convertor("ABCD"),'.--...-.-.-..')

    def test_convertor_not_existing_char(self):
        self.assertEqual(cm.convertor("ABCD#%"),'.--...-.-.-..nn')



if __name__ == '__main__':
    unittest.main()