print("Mohd Jawwad Ali Farooqui,USN:1AY24AI070,SEC:O")
def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result
try:
    number = int(input("Enter number: "))
    while number != 1:
        number = collatz(number)
    print(1)
except ValueError:
    print("Please enter a valid integer.")
