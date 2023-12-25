class MyString:
    def __init__(self, value):
        self.value = str(value)

    def get_length(self):
        return len(self.value)

    def reverse(self):
        return self.value[::-1]

    def count_words(self):
        words = self.value.split()
        return len(words)

    def replace_word(self, old_word, new_word):
        self.value = self.value.replace(old_word, new_word)

    def is_palindrome(self):
        cleaned_str = ''.join(c.lower() for c in self.value if c.isalnum())
        return cleaned_str == cleaned_str[::-1]


my_string = MyString("Hello, World!")
print("Original String:", my_string.value)
print("Length:", my_string.get_length())
print("Reversed:", my_string.reverse())
print("Is palindrome:", my_string.is_palindrome())
print("Word Count:", my_string.count_words())

my_string.replace_word("Hello","HI")
print("After replacement words:", my_string.value)
