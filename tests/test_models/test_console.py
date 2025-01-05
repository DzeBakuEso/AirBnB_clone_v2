import unittest
from io import StringIO
import sys
from unittest.mock import patch
from console import HBNBCommand  # Assuming your class is named HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the do_create method in console.py"""

    @patch("sys.stdout", new_callable=StringIO)
    def test_create_state(self, mock_stdout):
        """Test creating a state"""
        command = "create State name=\"California\""
        # Simulate running the command
        HBNBCommand().onecmd(command)
        output = mock_stdout.getvalue().strip()
        self.assertEqual(len(output), 36)  # Check for the UUID length
        self.assertIn("California", output)  # Ensure the name is included in the output

    @patch("sys.stdout", new_callable=StringIO)
    def test_create_place(self, mock_stdout):
        """Test creating a place"""
        command = 'create Place city_id="0001" user_id="0001" name="My_little_house" ' \
                  'number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 ' \
                  'latitude=37.773972 longitude=-122.431297'
        HBNBCommand().onecmd(command)
        output = mock_stdout.getvalue().strip()
        self.assertEqual(len(output), 36)  # Check for the UUID length
        self.assertIn("My little house", output)  # Ensure the name is included in the output
        self.assertIn("0001", output)  # Ensure city_id is included

    @patch("sys.stdout", new_callable=StringIO)
    def test_invalid_create(self, mock_stdout):
        """Test invalid create command"""
        command = 'create Place city_id="0001" user_id="0001" name=My_little_house ' \
                  'number_rooms="four" number_bathrooms=two'
        HBNBCommand().onecmd(command)
        output = mock_stdout.getvalue().strip()
        self.assertNotIn("four", output)  # Check that invalid values are not included
        self.assertNotIn("two", output)   # Check that invalid values are not included

    @patch("sys.stdout", new_callable=StringIO)
    def test_create_with_missing_attribute(self, mock_stdout):
        """Test creating a place with missing attributes"""
        command = 'create Place name="My House" price_by_night=100'
        HBNBCommand().onecmd(command)
        output = mock_stdout.getvalue().strip()
        self.assertIn("My House", output)
        self.assertIn("100", output)
        self.assertNotIn("city_id", output)  # Ensure missing attributes are not part of the output


if __name__ == "__main__":
    unittest.main()
