def get_input():
    input1 = input("What is your file name? ")
    return input1
def format_input(my_string):
    my_string = my_string.lower()
    my_string = my_string.replace(" ", "")
    my_string = my_string[::-1]
    x = my_string.find(".")
    #checks for extension, breaks if none
    if x == -1:
        print("application/octet-stream")
        exit()
    else:
        my_string = my_string[:x]
        my_string = my_string[::-1]
        return my_string
def check_file(my_string):
    match my_string:
        case "gif":
            return "image/gif"
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            print("application/octet-stream")
            exit()
def main():
    my_string = check_file(format_input(get_input()))
    print(my_string)
    exit()

main()





