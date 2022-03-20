# Function which encoding Caesar Cipher with any key or decoding Caesar Cipher with any key
# For example encoding word "Hello" with key 4 gives to us "Lipps"
# Or decoding word "Ykixkz&]uxj" with key 6 gives to us "Secret Word"
def caesar(word, coding: str, key: int) -> str:
    output = ""
    if coding == "encode":
        for char in word:
            output += chr(ord(char) + key)
        return (output + "\n")
    elif coding == "decode":
        for char in word:
            output += chr(ord(char) - key)
        return (output + "\n")


# Function which bruting Caesar Cipher with keys from 1 to 35
def brute_caesar(word: str) -> str:
    output = ""
    for key in range(1, 36):
        for char in word:
            output += chr(ord(char) - key)
        print(f"Key #{key}: {output[(len(word) * key - 5):]}")


# Testsing Functions
def main():
    print(caesar("Hello", "encode", 4))  # "Hello -> Lipps"
    print(caesar("Lipps", "decode", 4))  # "Lipps -> Hello"
    print(brute_caesar("Lipps"))  # Bruting with all keys in range(1, 36)


if __name__ == '__main__':
    main()