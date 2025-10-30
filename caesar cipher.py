alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
              'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z']
print(alphabets)
def encrypt(alphabets,text,shift):
    encrypted=" "
    for char in text:
        new=alphabets.index(char)+shift
        new=new%len(alphabets)
        encrypted+=alphabets[new]
    print(encrypted)

def decrypt(alphabets,text,shift):
    decrypted=" "
    for char in text:
        new=alphabets.index(char)-shift
        decrypted+=alphabets[new]
    print(decrypted)

choice=input("enter if u want to encode or decode: ")
if choice=="encode":
    text=input("enter text: ")
    shift=int(input("enter shift number: "))
    encrypt(alphabets,text,shift)
else:
    text = input("enter text: ")
    shift = int(input("enter shift number: "))
    decrypt(alphabets,text,shift)

