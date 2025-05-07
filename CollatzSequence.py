print("Mohd Jawwad Ali Farooqui,USN:1AY24AI070,SEC:O")
def collatz(number):
    if number % 2 == 0:
        result = number 
    else:
        result = 3 * number + 1
    print(result)
    return result
try:
    user_input = int(input("Enter an integer: "))
    while user_input != 1:
        user_input = collatz(user_input)
except ValueError:
    print("Please enter a valid integer.")
