alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]
online = True
while online:
    action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type the message:\n").lower()
    complexity = int(input("Enter the shift number:\n")) % 25


    def caesar(message, direction, shift):
        final_text = ""
        if direction == "decode":
            shift *= -1
        for char in message:
            if char in alphabet:
                before_index = alphabet.index(char)
                after_index = before_index + shift
                final_text += alphabet[after_index]
            else:
                final_text += char
        print(f"The {direction}d message is {final_text}.")


    caesar(message=text, direction=action, shift=complexity)
    game_status = input("Type 'yes' to go again or 'no' to stop:\n").lower()
    if game_status == "no":
        online = False
        print("Goodbye!")
