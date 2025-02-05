print("Welcome to the Word Counter Program!")
print("Type 'exit' anytime to quit.\n")

while True:
    # Prompt the user for input
    user_input = input("Enter a sentence or paragraph: ").strip()
    
    # Handle empty input
    if not user_input:
        print("Input cannot be empty. Please try again.")
        continue

    # Allow the user to exit
    if user_input.lower() == 'exit':
        print("Exiting the program. Thank you for using it!")
        break

    # Remove extra spaces between words and at the ends
    cleaned_input = ' '.join(user_input.split())
    
    # Count the words by splitting based on spaces
    word_count = len(cleaned_input.split())
    
    # Display the result
    print(f"Your input contains {word_count} word(s).\n")
