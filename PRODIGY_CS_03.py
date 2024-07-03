# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 18:00:05 2024

@author: Hxtreme
"""

import re

def password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None

    # Strength levels
    strength = {
        'length': length_criteria,
        'lowercase': lowercase_criteria,
        'uppercase': uppercase_criteria,
        'digit': digit_criteria,
        'special_char': special_char_criteria
    }

    score = sum(strength.values())

    # Feedback based on the score
    if score == 5:
        feedback = "Very Strong"
    elif score == 4:
        feedback = "Strong"
    elif score == 3:
        feedback = "Moderate"
    elif score == 2:
        feedback = "Weak"
    else:
        feedback = "Very Weak"

    return feedback, strength

def main():
    password = input("Enter a password to check its strength: ")
    feedback, criteria = password_strength(password)
    
    print(f"Password Strength: {feedback}")
    print("Criteria Met:")
    print(f" - Length >= 8 characters: {'Yes' if criteria['length'] else 'No'}")
    print(f" - Contains lowercase letters: {'Yes' if criteria['lowercase'] else 'No'}")
    print(f" - Contains uppercase letters: {'Yes' if criteria['uppercase'] else 'No'}")
    print(f" - Contains digits: {'Yes' if criteria['digit'] else 'No'}")
    print(f" - Contains special characters: {'Yes' if criteria['special_char'] else 'No'}")

if __name__ == "__main__":
    main()
