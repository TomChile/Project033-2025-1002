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

##### fix the range to 1 so it doesn't flood the output from 3. If you want more greetings, just run again or change 1 to higher number. #####

for i in range(1):
    greeting_message = generate_random_greeting()
    print(f"\n{greeting_message}\n")








#### Combining Scripts together to make a new Program ####

# Emoji Generator Part
# This script generates random emojis or combinations of emojis


def generate_random_emoji():
    """Generates a random emoji or a random combination of emojis."""

    # --- 1. Lists of Emoji Categories ---
    faces = ["😀", "😂", "😍", "🤩", "🤔", "🥳", "🥺", "😇", "😎"]
    objects = ["🌟", "💡", "🧠", "🍕", "💻", "💾", "🎨", "🎤", "🦄"]
    actions = ["🏃", "💃", "🕺", "🤸", "🧘", "👋", "✍️", "💪", "🙌"]

    # --- 2. Random Selection Modes ---
    # Choose a mode for generating the "emoji"
    modes = [
        "single_face",
        "face_with_object",
        "action_with_object",
        "feeling_and_action"
    ]
    chosen_mode = random.choice(modes)

    # --- 3. Generation Logic ---
    if chosen_mode == "single_face":
        result = random.choice(faces)
        description = f"A simple random face: {result}"

    elif chosen_mode == "face_with_object":
        face = random.choice(faces)
        obj = random.choice(objects)
        result = f"{face}{obj}"
        description = f"A face reacting to an object: {result}"

    elif chosen_mode == "action_with_object":
        action = random.choice(actions)
        obj = random.choice(objects)
        result = f"{action}{obj}"
        description = f"An action involving an object: {result}"

    elif chosen_mode == "feeling_and_action":
        face = random.choice(faces)
        action = random.choice(actions)
        result = f"{face}{action}"
        description = f"A feeling expressed through an action: {result}"

    # --- 4. Return the Result ---
    return result, description

# --- Main Program Execution ---
print("--- Emoji Generator What will you get today??? ---")

# Generate and display a random emoji concept
emoji_concept, description = generate_random_emoji()

print(f"\nGenerated Emoji: {emoji_concept}")

print("\nTry running the script again for a different result!\n")