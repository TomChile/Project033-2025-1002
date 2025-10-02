# Emoji Generator
# This script generates random emojis or combinations of emojis


import random

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
print("--- Emoji Generator ---")

# Generate and display a random emoji concept
emoji_concept, description = generate_random_emoji()

print(f"\nGenerated Concept: {emoji_concept}")
print(f"Description: {description}")

print("\nTry running the script again for a different result!")