def is_palindrome(word):
    if word < 2:
        return True
    elif word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

def is_palindrome_slice(word):
    if word == word[::-1]:
        return True
    return False

