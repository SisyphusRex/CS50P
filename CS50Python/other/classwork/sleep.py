def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(m):
    for i in range(m):
        #returns one line at a time
        yield "🐑" * i



if __name__ == "__main__":
    main()
