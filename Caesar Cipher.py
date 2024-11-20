alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:").lower()
text = input("Type your message:").lower()
shift = int(input("Type the shift number:"))

def ceasar_cipher(original_text, shifted_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == 'decode':
        shifted_amount = -shifted_amount

    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shifted_amount) % len(alphabet)
            output_text += alphabet[shifted_position]

        else:
            output_text += letter

    return output_text

result = ceasar_cipher(text,shift,direction)
print(f"Your {direction}d result is: {result}")
