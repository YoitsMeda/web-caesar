def alphabet_postion(char):
    import string
    if char in string.ascii_lowercase:
        return(string.ascii_lowercase.index(char))
    if char in string.ascii_uppercase:
        return(string.ascii_uppercase.index(char))
    return("error")

def rotate_character(char, rot ):
    import string
    if char in string.ascii_lowercase:
        return( string.ascii_lowercase[((alphabet_postion(char)+rot)%26)] )
    if char in string.ascii_uppercase:
        return( string.ascii_uppercase[((alphabet_postion(char)+rot)%26)] )
    else:
        return(char)



def main():

    print(rotate_character())



if __name__ == "__main__":
    main()
