
# Warmup: camelCase
# M. Surber, wo1624bu


def main():
    print("Please enter a word or phrase to be camelCased.")
    # Assertion user input is string was unnecessary, but helped to write it
    userInput = str(input())
    # Can't camelCase nothing, just let them try again
    if userInput == "":
        print("Nothing entered.")
        main()
    # Strip away all casing, we are using our own
    phrase = userInput.lower()
    # String split by space character to get all the words
    words = phrase.split(" ")
    # Camel case just uses lower case for the first word
    # So a phrase of one word is just lower case
    if len(words) == 1:
        print(phrase)
    else:
        # Start with the first word lower case
        outString = words[0]
        # All other words are Capitalized
        for word in words[1:]:
            outString += word.capitalize()
        print(outString)
    # Go again.
    main()

# Run the program
main()
