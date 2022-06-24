text = input()

encrypted_text = ""

for ch in text:
    encrypted_text += chr(ord(ch) + 3)

print(encrypted_text)

# Mario
# def caesar_cipher(text):
#     result = [chr(ord(ch) + 3) for ch in text]
#     print(''.join(result))
#
#
# text = input()
# caesar_cipher(text)
