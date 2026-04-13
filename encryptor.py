def encrypt(text, shift):
    result = ""
    for char in text:
        result += chr((ord(char) + shift) % 256)
    return result

def decrypt(text, shift):
    result = ""
    for char in text:
        result += chr((ord(char) - shift) % 256)
    return result

choice = input("1. Encrypt\n2. Decrypt\nChoose: ")
filename = input("Enter file name: ")
shift = int(input("Enter key (number): "))

try:
    with open(filename, "r") as file:
        content = file.read()

    if choice == "1":
        result = encrypt(content, shift)
        output_file = "encrypted.txt"
    elif choice == "2":
        result = decrypt(content, shift)
        output_file = "decrypted.txt"
    else:
        print("Invalid choice")
        exit()

    with open(output_file, "w") as file:
        file.write(result)

    print(f"Output saved in {output_file}")

except FileNotFoundError:
    print("File not found.")
