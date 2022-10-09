"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        numbers.sort()
        middleLocation = (len(numbers) //2)
        if (len(numbers) % 2 == 0):
            print((numbers[middleLocation] + numbers[middleLocation - 1]) / 2)
        else:
            print(numbers[middleLocation])
        break

    


#print(numbers)
