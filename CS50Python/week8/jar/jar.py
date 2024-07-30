class Jar:
#initialize the capacity to 12 and size (or number of 🍪) to 0
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0
#had to put quotes around 🍪 to prevent invalid character (math: cannot multiply)
    def __str__(self):
        return (f"{self.size * "🍪"}")

    def deposit(self, n):
        self.size = self.size + int(n)

    def withdraw(self, n):
        self.size = self.size - int(n)

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) < 0:
            raise ValueError("negative capacity not allowed")
        self._capacity = int(capacity)
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        if int(size) > self.capacity:
            raise ValueError("not enough capacity")
        if int(size) < 0:
            raise ValueError("not enough cookies")
        self._size = size

def main():
    my_jar = Jar(input("What is your jar's capacity? "))
    my_jar.deposit(input("How many cookies to add? "))
    my_jar.withdraw(input("How many cookies to withdraw? "))
    print(my_jar)

if __name__ == "__main__":
    main()

