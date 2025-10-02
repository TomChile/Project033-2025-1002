import random

def generate_random_greeting():
    """
    Generates a personalized greeting by randomly combining
    a salutation, a name, and a closing phrase.
    """

    # --- 1. Lists of Greeting Components ---

    # Ways to start the greeting
    salutations = [
        "Hello",
        "Hi there",
        "Greetings",
        "Hey",
        "Howdy",
        "What's up",
        "Good day"
    ]

    # Names or titles to address (can be expanded)
    names = [
        "User",
        "Friend",
        "Code Enthusiast",
        "Programmer",
        "Explorer",
        "Developer"
    ]

    # Friendly closing phrases (ensure some include punctuation)
    closures = [
        "Hope you're having a great time!",
        "Let's get some work done.",
        "Ready to start coding?",
        "How can I help you today?",
        "Have a productive day!",
        "It's good to see you.",
        "Welcome back!"
    ]

    # --- 2. Random Selection ---

    # Select one item from each list
    salutation = random.choice(salutations)
    name = random.choice(names)
    closure = random.choice(closures)

    # --- 3. Combination and Formatting ---

    # Join the selected parts into a single string
    # Using an f-string for clear formatting
    greeting = f"{salutation}, {name}! {closure}"

    return greeting

# --- Main Program Execution ---
print("--- Randomized Greeting Generator ---")

# Generate and display a few random greetings
for i in range(3):
    greeting_message = generate_random_greeting()
    print(f"\nGreeting {i+1}: {greeting_message}")

print("\nRun the script again for more variety!")