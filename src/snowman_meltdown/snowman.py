from snowman_meltdown.ascii_art import STAGES
from snowman_meltdown.game_logic import play_game
from snowman_meltdown.secret_words import SECRET_WORDS


def main() -> None:
    play_game(STAGES, SECRET_WORDS)


if __name__ == "__main__":
    main()
