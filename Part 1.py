import random

# Warmup: Guess the Number
# M. Surber, wo1624bu

def main():
    # Informational flavor text
    print("I'm thinking of a number between 0 and 100...")
    # Bot comes up with a number
    botNum = random.randint(0,100)
    # Setting up initial variables
    victory = False
    guesses = 0
    # While loop provides endless truns until a player wins or gives up.
    while not victory:
        # Turn counter
        guesses += 1
        # Input parsing method allows for cleaner main method
        guessNum = parseInput()
        difference = botNum - guessNum
        # Compare the difference and give one of five results:
        # more than 25 away, "Much too low/high"
        # 25 or less away, "Too low/high"
        # 0 away is victory, since that's the number guessed
        if difference > 25:
            print("Much too low.")
        elif difference > 0:
            print("Too low.")
        elif difference < -25:
            print("Much too high.")
        elif difference < 0:
            print("Too high.")
        elif difference == 0:
            victory = True
    # Flavor text and pluralization
    if guesses > 1:
        attempts = " tries."
    else:
        attempts = " try!"
    # Score printout
    print("That's the one!  You did it in only " + str(guesses) + attempts)
    # Computer judges your performance
    if guesses == 1:
        print("...How did you do that?")
    elif guesses <= 5:
        print("Amazing!")
    elif guesses <= 10:
        print("Pretty good!")
    elif guesses <= 15:
        print("Not bad!")
    elif guesses <= 25:
        print("Keep trying!")
    else:
        print("Wow, uh...  Practice makes perfect, right?")
    # Go again
    main()

# Input parsiing method
def parseInput():
    # Input comes in as a string, we want to catch anyone writing nonsense
    guessStr = input("Your guess: ")
    try:
        return int(guessStr)
    except ValueError:
        # User has typed something that we don't think is an integer
        # Let them know, and let them try again
        print("Please enter a number, written as a digit with no decimal places (e.g. 6)")
        return parseInput()

# Run the program
main()
