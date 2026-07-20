def is_palindrome(text):
    # Convert to lowercase and remove spaces for accurate checking
    cleaned_text = "".join(text.lower().split())
    
    # Compare the string with its reverse
    return cleaned_text == cleaned_text[::-1]

# Example usage:
word = "RACEcar"
print(f"Is '{word}' a palindrome? {is_palindrome(word)}") # Returns True
