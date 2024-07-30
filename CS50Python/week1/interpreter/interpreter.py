def convert(token):
    x, y, z = token.split(" ")
    x = float(x)
    z = float(z)
    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "/":
            return x / z
        case "*":
            return x * z
def main():
    token = input("Give me your math: ")
    token = convert(token)
    print("{:.1f}".format(token))
if __name__ == "__main__":
    main()

