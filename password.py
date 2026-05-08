"""
Enhancement: Added a visual feedback bar (ASCII) to represent the strength 
score from 0 to 5 for better user experience.
"""

LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\", "`", "~"]

def word_in_file(word, filename, case_sensitive=False):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                clean_word = line.strip()
                if case_sensitive:
                    if word == clean_word:
                        return True
                else:
                    if word.lower() == clean_word.lower():
                        return True
        return False
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return False

def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word):
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

def password_strength(password, min_length=10, strong_length=16):
    if word_in_file(password, "wordlist.txt", False):
        print("Password is a dictionary word and is not secure.")
        return 0
    if word_in_file(password, "toppasswords.txt", True):
        print("Password is a commonly used password and is not secure.")
        return 0
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    complexity_score = word_complexity(password)
    strength = 1 + complexity_score
    return strength

def main():
    print("--- Password Strength Checker ---")
    while True:
        user_input = input("\nEnter a password to test (or 'q' to quit): ")
        
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
        
        strength_result = password_strength(user_input)
        
        print(f"Password Strength Score: {strength_result}/5")
        visual_bar = "█" * strength_result + "░" * (5 - strength_result)
        print(f"Visual Rating: [{visual_bar}]")

if __name__ == "__main__":
    main()