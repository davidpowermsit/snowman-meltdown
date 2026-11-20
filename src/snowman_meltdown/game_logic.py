import random


def prompt_play_again() -> bool:
    """Ask until the user enters y or n."""
    while True:
        value = input("Would you like to play again? (y/n) ").strip().lower()
        if value in {"y", "n"}:
            return value == "y"
        print("Please enter 'y' or 'n' only.")


def prompt_letter(guessed_letters: set[str]) -> str:
    """Ask until the user enters a new single letter."""
    while True:
        value = input("Guess a letter: ").strip().lower()
        if len(value) != 1 or not value.isalpha():
            print("Enter a single letter.")
        elif value in guessed_letters:
            print("You already guessed that. Try another letter.")
        else:
            return value


def get_random_word(secret_words: list[str]) -> str:
    """Selects a random word from the list."""
    return secret_words[random.randint(0, len(secret_words) - 1)]


def display_game_state(display_stages: list[str], mistakes: set[str]) -> None:
    print(display_stages[len(mistakes)])


def play_game(game_stages: list[str], secret_words: list[str]) -> None:
    retry: bool = True
    while retry:
        guessed_letters: set[str] = set()
        mistaken_letters: set[str] = set()
        secret_word: str = get_random_word(secret_words)
        lost: bool = False
        won: bool = False

        print("Welcome to Snowman Meltdown!")

        while not (won or lost):
            display_game_state(game_stages, mistaken_letters)

            guess = prompt_letter(guessed_letters)
            guessed_letters.add(guess)

            mistaken_letters = guessed_letters - set(secret_word)
            won = set(secret_word) <= guessed_letters
            lost = len(mistaken_letters) >= len(game_stages) - 1

        print("Congratulations! You saved the snowman." if won else f"The snowman died. The word was {secret_word!r}.")
        retry = prompt_play_again()
