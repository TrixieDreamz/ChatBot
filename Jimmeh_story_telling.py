import random

# Define story elements
settings = ["forest", "castle", "city", "mountain", "underwater kingdom"]
characters = ["wizard", "princess", "knight", "dragon", "pirate"]
destinations = ["find the treasure", "rescue the princess", "defeat the evil sorcerer", "discover a hidden secret"]
obstacles = ["a fierce storm", "a labyrinth", "a curse", "a rival"]
locations = ["mysterious cave", "enchanted castle", "forgotten temple", "secret island"]
emotions = ["excited", "nervous", "curious", "determined"]
goals = ["explore new lands", "solve a mystery", "help others", "prove themselves"]
characters_2 = ["friendly elf", "wise old sage", "brave adventurer", "mischievous gnome"]
challenges = ["overcome their fear", "learn a valuable lesson", "face their past", "make a difficult choice"]
landmarks = ["ancient ruins", "magic garden", "crystal cavern", "floating island"]
traits = ["bravery", "kindness", "wisdom", "strength"]
mysterious_objects = ["magical amulet", "enchanted map", "mysterious potion", "ancient artifact"]
magical_creatures = ["unicorn", "phoenix", "mermaid", "griffin"]
wishes = ["become the greatest hero", "bring peace to the world", "find true love", "restore balance"]
kingdoms = ["Fantasia", "Eldoria", "Grimdor", "Mystara"]
actions = ["save the kingdom", "defeat the villain", "rescue a friend", "uncover a secret"]

# Story templates with placeholders
story_templates = [
    "Once upon a time, in a {setting}, there lived a {character}. One day, {character} went on a journey to {destination}. On the way, they encountered {obstacle} and had to overcome it.",
    "{character} woke up in a {location} feeling {emotion}. They decided to embark on an adventure to {goal}. Along the way, they met {character_2} who helped them overcome {challenge}.",
    "In the land of {landmark}, there was a {character} known for their {trait}. One day, {character} discovered a {mysterious_object} that led them on a quest to {destination}.",
    "Long ago, in the kingdom of {kingdom}, there lived a {character} with a secret power. When {character} was called upon to {action}, they knew it was their destiny to fulfill the prophecy.",
    "In the enchanted forest, {character} stumbled upon a {magical_creature} who granted them three wishes. {character} used their wishes to {wish_1}, {wish_2}, and {wish_3}."
]

def generate_story():
    # Randomly select a story template
    story_template = random.choice(story_templates)

    # Fill in placeholders with randomly selected story elements
    story = story_template.format(
        setting=random.choice(settings),
        character=random.choice(characters),
        destination=random.choice(destinations),
        obstacle=random.choice(obstacles),
        location=random.choice(locations),
        emotion=random.choice(emotions),
        goal=random.choice(goals),
        character_2=random.choice(characters_2),
        challenge=random.choice(challenges),
        landmark=random.choice(landmarks),
        trait=random.choice(traits),
        mysterious_object=random.choice(mysterious_objects),
        magical_creature=random.choice(magical_creatures),
        wish_1=random.choice(wishes),
        wish_2=random.choice(wishes),
        wish_3=random.choice(wishes),
        kingdom=random.choice(kingdoms),
        action=random.choice(actions)  # Include the action variable here
    )

    return story
