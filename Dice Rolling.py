import random

def roll_dice(sides, rolls):
    results = [random.randint(1, sides) for _ in range(rolls)]
    return results

def main():
    while True:
        try:
            sides = int(input("Enter the number of sides on the dice: "))
            rolls = int(input("Enter the number of rolls: "))
            if sides <= 0 or rolls <= 0:
                print("Please enter positive numbers for sides and rolls.")
            else:
                break
        except ValueError:
            print("Please enter valid integers for sides and rolls.")
    
    # Roll the dice and get results
    results = roll_dice(sides, rolls)
    
    # Display the results
    print(f"Rolling a {sides}-sided dice {rolls} times:")
    for i, result in enumerate(results, 1):
        print(f"Roll {i}: {result}")

if __name__ == "__main__":
    main()
