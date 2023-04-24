import unittest
from tkinter import Tk , Entry , Button , Label
from tkinter import END
from tkinter import messagebox
from unittest.mock import patch

from convertorGUI import ConvertorGui as cg


class TestConvertorMorseGUI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.root = Tk()
        cls.gui = cg(cls.root)

    @classmethod
    def tearDownClass(cls):
        cls.root.destroy()

    def test_convert(self):
        self.gui.entry.insert(END, "hello")
        self.gui.convert()
        self.assertEqual(self.gui.output_label.cget("text"), ".... . .-.. .-.. ---")

    def test_invalid_input(self):
        with patch.object(messagebox, "showerror") as mock_method:
            self.gui.entry.delete(0, END)
            self.gui.convert()
            mock_method.assert_called_with("Error", "Please enter your message")