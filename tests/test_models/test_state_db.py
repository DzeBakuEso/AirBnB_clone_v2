import unittest
import MySQLdb
from models.state import State
from models import storage


class TestStateDb(unittest.TestCase):
    """Test MySQL database operations for the State model"""

    @classmethod
    def setUpClass(cls):
        """Setup before tests run"""
        cls.db = MySQLdb.connect(
            host="localhost",
            user="hbnb_test",
            passwd="hbnb_test_pwd",
            db="hbnb_test_db"
        )
        cls.cursor = cls.db.cursor()

    @classmethod
    def tearDownClass(cls):
        """Cleanup after all tests run"""
        cls.cursor.close()
        cls.db.close()

    def test_create_state_in_db(self):
        """Test if creating a state adds it to the database"""
        # Get the current number of records in the `states` table
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        # Create a new state using the console (or directly in the model)
        new_state = State(name="California")
        new_state.save()

        # Get the updated count of records
        self.cursor.execute("SELECT COUNT(*) FROM states")
        updated_count = self.cursor.fetchone()[0]

        # Assert that the count has increased by 1
        self.assertEqual(updated_count, initial_count + 1)

    def test_create_state_with_invalid_name(self):
        """Test that creating a state with an invalid name fails"""
        # Try creating a state with an invalid name (e.g., empty name)
        new_state = State(name="")
        with self.assertRaises(ValueError):
            new_state.save()
