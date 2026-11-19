import random

# Snowman ASCII Art stages
STAGES = [
    # Stage 0: Full snowman
    """
      ___
     /___\\
     (o o)
     ( : )
     ( : )
     """,
    # Stage 1: Bottom part starts melting
    """
      ___
     /___\\
     (o o)
     ( : )
     """,
    # Stage 2: Only the head remains
    """
      ___
     /___\\
     (o o)
     """,
    # Stage 3: Snowman completely melted
    """
      ___
     /___\\
     """,
]


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word() -> str:
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(display_stages: list[str], mistakes: set[str]) -> None:
    print(display_stages[len(mistakes)])


def play_game(game_stages: list[str]) -> None:
    guessed_letters: set[str] = set()
    mistaken_letters: set[str] = set()
    secret_word: str = get_random_word()
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


def main() -> None:
    play_game(STAGES)


if __name__ == "__main__":
    main()
