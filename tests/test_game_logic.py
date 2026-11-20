import pytest

from snowman_meltdown.ascii_art import STAGES
from snowman_meltdown.game_logic import get_random_word, play_game, prompt_letter
from snowman_meltdown.secret_words import SECRET_WORDS


class TestGetRandomWord:
    def test_word_comes_from_list(self) -> None:
        assert get_random_word(SECRET_WORDS) in SECRET_WORDS


class TestPromptLetter:
    def test_valid_letter_is_returned(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr("builtins.input", lambda _: "a")
        assert prompt_letter(set()) == "a"

    def test_letter_is_lowercased(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr("builtins.input", lambda _: "A")
        assert prompt_letter(set()) == "a"

    def test_invalid_input_asks_again(self, monkeypatch: pytest.MonkeyPatch) -> None:
        answers = iter(["12", "b"])
        monkeypatch.setattr("builtins.input", lambda _: next(answers))
        assert prompt_letter(set()) == "b"

    def test_already_guessed_letter_asks_again(self, monkeypatch: pytest.MonkeyPatch) -> None:
        answers = iter(["a", "b"])
        monkeypatch.setattr("builtins.input", lambda _: next(answers))
        assert prompt_letter({"a"}) == "b"


class TestPlayGame:
    guess_word: str = "git"

    def test_player_wins(self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
        monkeypatch.setattr("snowman_meltdown.game_logic.get_random_word", lambda _: self.guess_word)
        answers = iter(["g", "i", "t", "n"])
        monkeypatch.setattr("builtins.input", lambda _: next(answers))

        play_game(STAGES, [self.guess_word])

        assert "Congratulations" in capsys.readouterr().out

    def test_player_loses(self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
        monkeypatch.setattr("snowman_meltdown.game_logic.get_random_word", lambda _: self.guess_word)
        wrong_letters = "xyzqwvu"[: len(STAGES) - 1]  # one wrong guess per allowed mistake
        answers = iter([*wrong_letters, "n"])
        monkeypatch.setattr("builtins.input", lambda _: next(answers))

        play_game(STAGES, [self.guess_word])

        assert "The snowman died" in capsys.readouterr().out
