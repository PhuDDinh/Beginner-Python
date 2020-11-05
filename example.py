def collatz(number):
    collatz = 0
    if number % 2 == 0:
        collatz = number // 2
        print(collatz)
        return collatz
    else:
        collatz = 3 * number + 1
        print(collatz)
        return collatz
number = input("Enter a number: ")
while number != 1:
    number = collatz(int(number))
