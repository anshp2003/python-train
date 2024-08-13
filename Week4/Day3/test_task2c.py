import pytest
from Task2 import StringManipulator

def test_reverse():
    string_manipulator = StringManipulator()
    assert string_manipulator.reverse("hello") == "olleh"
    assert string_manipulator.reverse("world") == "dlrow"
    assert string_manipulator.reverse("") == ""
    assert string_manipulator.reverse("a") == "a"

def test_to_uppercase():
    string_manipulator = StringManipulator()
    assert string_manipulator.to_uppercase("hello") == "HELLO"
    assert string_manipulator.to_uppercase("world") == "WORLD"
    assert string_manipulator.to_uppercase("") == ""
    assert string_manipulator.to_uppercase("Hello World") == "HELLO WORLD"

def test_is_palindrome():
    string_manipulator = StringManipulator()
    assert string_manipulator.is_palindrome("madonna") == False
    assert string_manipulator.is_palindrome("madam") == True
    assert string_manipulator.is_palindrome("racecar") == True
    assert string_manipulator.is_palindrome("") == True
    assert string_manipulator.is_palindrome("a") == True
