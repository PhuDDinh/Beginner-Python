def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result

    else:
        result = 3 * number + 1
        print(result)
        return result

try:
    n = input("Please enter a number: ")
    while n != 1:
        n = collatz(int(n))
except ValueError:
    print("Please enter a number.")
    
