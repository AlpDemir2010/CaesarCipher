gr = int(input("Do you want to encrypt or decrypt? 0 for encrypt, 1 for decrypt: "))

if gr == 0:
    x = (input("Insert text to be encrypted: "))
    l = int(input("By how many characters should the Caesar Cipher encrypt? "))
    x = x.lower()
    z = 0
    m = ''
    encrypted = ""

    for char in x:
        if char.isalpha():
            print(char)
            z = (ord(char) + l - ord('a')) % 26
            m = chr(ord('a') + z)
            encrypted += m
        elif char.isspace():
            encrypted += char
        else:
            print("Unexpected char encounter! Make sure to only use letters and spaces")
            break

    print("See encrypted text: " + encrypted)

elif gr == 1:
    x = (input("Insert text to be decrypted: "))
    l = int(input("how many characters was the cipher encrypted by? "))
    x = x.lower()
    z = 0
    m = ''
    decrypted = ""

    for char in x:
        if char.isalpha():
            print(char)
            z = (ord(char) - l - ord('a')) % 26
            m = chr(ord('a') + z)
            decrypted += m
        elif char.isspace():
            decrypted += char
        else:
            print("Unexpected char encounter! Make sure to only use letters and spaces")
            break

    print("See decrypted text: " + decrypted)

else:
    print("You inputted something that was unexpected")
