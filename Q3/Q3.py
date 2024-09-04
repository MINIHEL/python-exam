numbers = []

numberEnter = False

while True:
    inputNumber = int()input()
    if inputNumber == "stop":
        break
    else:
        numbers.append(int(inputNumber))
        numberEnter = True

if numberEnter:
    smallest = min(numbers)
    largest = max(numbers)
    print(f"smallest number:{smallest}")
    print(f"largest number:{largest}")
else:
    print("No numbers were entered.")
