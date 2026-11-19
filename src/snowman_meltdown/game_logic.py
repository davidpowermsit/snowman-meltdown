import random


def get_random_word(secret_words: list[str]) -> str:
    """Selects a random word from the list."""
    return secret_words[random.randint(0, len(secret_words) - 1)]


def display_game_state(display_stages: list[str], mistakes: set[str]) -> None:
    print(display_stages[len(mistakes)])


def play_game(game_stages: list[str], secret_words: list[str]) -> None:
    guessed_letters: set[str] = set()
    mistaken_letters: set[str] = set()
    secret_word: str = get_random_word(secret_words)
    print("Welcome to Snowman Meltdown!")
    lost: bool = False

    while not lost:
        guess = input("Guess a letter: ").lower()
        guessed_letters.add(guess)
        print(f"You guessed: {guess}")

        mistaken_letters = guessed_letters - set(secret_word)
        display_game_state(game_stages, mistaken_letters)

        lost = len(mistaken_letters) >= len(game_stages) - 1

    print("You lost. Please try again.")
