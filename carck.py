import random
import time
import nltk
from nltk.corpus import words
from colorama import Fore, Style, init

nltk.download('words')  # Download word dataset
word_list = words.words()  # Load word list

init(autoreset=True)  # Initialize colorama

# Predefined categories
categories = {
    "fruits": ["apple", "banana", "cherry", "date", "fig", "grape", "mango"],
    "books": ["harrypotter", "hobbit", "iliad", "odyssey", "gatsby"],
    "countries": ["india", "canada", "brazil", "germany", "japan", "france"],
    "colors": ["red", "blue", "green", "yellow", "purple", "orange"],
    "animals": ["lion", "tiger", "elephant", "giraffe", "zebra", "kangaroo"],
    "water bodies": ["ocean", "river", "lake", "pond", "stream", "sea"],
    "plants": ["rose", "tulip", "bamboo", "cactus", "fern", "maple"]
}

# Score tracking
score = 0


def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shift = shift if encrypt else -shift
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result


def vigenere_cipher(text, key, encrypt=True):
    key = key.lower()
    key_length = len(key)
    result = ""
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('a')
            if not encrypt:
                shift = -shift
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result


def challenge_mode():
    global score
    category = input(Fore.CYAN + "Choose a category (or type 'random' for any word): ").lower()

    if category in categories:
        word = random.choice(categories[category]).upper()
        hint = f"Category: {category.capitalize()}"
    else:
        word = random.choice(word_list).upper()
        hint = f"Hint: The word belongs to an unknown category."

    shift = random.randint(1, 25)
    encrypted = caesar_cipher(word, shift)
    print(Fore.YELLOW + f"Crack this code: {encrypted}")
    print(Fore.MAGENTA + hint)

    guess = input(Fore.CYAN + "Your answer: ").upper()
    if guess == word:
        print(Fore.GREEN + "Correct! You cracked the code!")
        score += 1
    else:
        print(Fore.RED + f"Wrong! The correct answer was {word}.")
        score -= 1

    print(Fore.BLUE + f"Your current score: {score}")


def typewriter_effect(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def main():
    while True:
        print(Fore.MAGENTA + "\n========================")
        typewriter_effect(Fore.CYAN + "Welcome to Cipher Master!")
        print(Fore.MAGENTA + "========================")
        print(Fore.BLUE + "1. Encrypt with Caesar Cipher")
        print(Fore.BLUE + "2. Decrypt with Caesar Cipher")
        print(Fore.BLUE + "3. Encrypt with Vigenère Cipher")
        print(Fore.BLUE + "4. Decrypt with Vigenère Cipher")
        print(Fore.YELLOW + "5. Challenge Mode")
        print(Fore.RED + "6. Exit")
        choice = input(Fore.CYAN + "Enter choice: ")

        if choice == "1":
            text = input(Fore.CYAN + "Enter text: ")
            shift = int(input(Fore.CYAN + "Enter shift value: "))
            print(Fore.GREEN + "Encrypted text:", caesar_cipher(text, shift))
        elif choice == "2":
            text = input(Fore.CYAN + "Enter text: ")
            shift = int(input(Fore.CYAN + "Enter shift value: "))
            print(Fore.GREEN + "Decrypted text:", caesar_cipher(text, shift, encrypt=False))
        elif choice == "3":
            text = input(Fore.CYAN + "Enter text: ")
            key = input(Fore.CYAN + "Enter keyword: ")
            print(Fore.GREEN + "Encrypted text:", vigenere_cipher(text, key))
        elif choice == "4":
            text = input(Fore.CYAN + "Enter text: ")
            key = input(Fore.CYAN + "Enter keyword: ")
            print(Fore.GREEN + "Decrypted text:", vigenere_cipher(text, key, encrypt=False))
        elif choice == "5":
            challenge_mode()
        elif choice == "6":
            print(Fore.RED + "Exiting Cipher Master... Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice! Try again.")


if __name__ == "__main__":
    main()
