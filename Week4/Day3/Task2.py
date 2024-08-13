class StringManipulator:
    def reverse(self, s):
        return s[::-1]

    def to_uppercase(self, s):
        return s.upper()

    def is_palindrome(self, s):
        return s == s[::-1]
