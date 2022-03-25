alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from cipher_art import logo

print(logo)

        

def caesar (entered_text,shift_amount,direction):
    if direction == "decode":
        shift_amount *= -1
    shift_amount %= 26 
    
    ans = ""
 
    for letter in entered_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            ans += alphabet[new_position]
        else:
            ans += letter
    print(f"{direction}d message : {ans}")
redo = True
while redo:
    todo = input("CHOOSE : encode or decode ")
    text = input("enter text : ")
    shift = int(input("enter shift amount : "))
    caesar(text,shift,todo)
    rd = input("do you want to do again ? ")
    if rd == "no":
        redo = False
        print("GoodBye")


        
        
