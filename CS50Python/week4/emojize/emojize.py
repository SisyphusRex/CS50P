import emoji

def main():
    my_string = input()
    #print(my_string)
    print(emoji.emojize(my_string, language = 'alias'))

if __name__ == "__main__":
    main()
