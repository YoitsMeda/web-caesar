def encrypt(text, rot ):
    from helpers import alphabet_postion, rotate_character
    secret = ""
    for char in text:
        secret += rotate_character(char, rot)


    return(secret)
def main():
    text = input("What text is a secret today? ")
    print(encrypt(text))

if __name__ =="__main__":
    main()
