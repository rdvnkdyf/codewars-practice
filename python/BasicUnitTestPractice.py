"""
Solution 
from unittest import TestCase
from unittest.mock import patch
from collections import UserDict


class TestPhoneBook(TestCase):
    
    def setUp(self):
        # This method is run before each test method.
        # It ensures a fresh PhoneBook instance for every test.
        self.phone_book = PhoneBook()
        self.phone_book.create("Alice", "1234567890")

    def test_create_method(self):
        # Tests Statement 1: Ensures the create method adds a new entry correctly.
        self.phone_book.create("Bob", "0987654321")
        self.assertEqual(self.phone_book["Bob"], "0987654321")

    def test_retrieve_method_when_the_name_does_not_exist(self):
        # Tests Statement 3: Ensures a KeyError is raised when a name is not found.
        with self.assertRaisesRegex(KeyError, "Name not found!"):
            self.phone_book.retrieve("Charlie")

    def test_retrieve_method_when_the_name_exists(self):
        # Tests Statement 2: Ensures the correct phone number is returned for an existing name.
        self.assertEqual(self.phone_book.retrieve("Alice"), "1234567890")

    def test_update_method_when_the_name_exists(self):
        # Tests Statement 4: Ensures an existing phone number is updated correctly.
        self.phone_book.update("Alice", "9999999999")
        self.assertEqual(self.phone_book.retrieve("Alice"), "9999999999")
        self.assertEqual(len(self.phone_book), 1) # Ensure no new entry was created

    def test_delete_method_when_the_name_exists(self):
        # Tests Statement 5: Ensures an existing entry is deleted correctly.
        self.phone_book.delete("Alice")
        self.assertNotIn("Alice", self.phone_book)
        self.assertEqual(len(self.phone_book), 0)
"""
"""
Test kodu 
class PhoneBook(UserDict):
    def create(self, name: str, phone_number: str) -> None:
        self[name] = phone_number              # Statement 1

    def retrieve(self, name: str) -> str:
        if name not in self:
            raise KeyError('Name not found!')  # Statement 3
        return self[name]                      # Statement 2

    def update(self, name: str, phone_number: str) -> None:
        if name not in self:
            raise KeyError('Name not found!')
        self[name] = phone_number              # Statement 4

    def delete(self, name: str) -> None:
        if name not in self:
            raise KeyError('Name not found!')
        del self[name]                         # Statement 5





















import codewars_test as test

@test.describe('This kata does not have Sample Tests.')
def _():
    @test.it('Use the ATTEMPT button directly instead.')
    def _():
        test.expect(True)
"""