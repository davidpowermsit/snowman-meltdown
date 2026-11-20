import pytest

from snowman_meltdown.ascii_art import STAGES
from snowman_meltdown.game_logic import get_random_word, play_game, prompt_letter, prompt_play_again
from snowman_meltdown.secret_words import SECRET_WORDS

WORD_TO_GUESS = "git"


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


class TestPromptPlayAgain:
    @pytest.mark.parametrize(("answer", "expected"), [("y", True), ("n", False), (" Y ", True)])
    def test_valid_answers(self, monkeypatch: pytest.MonkeyPatch, answer: str, expected: bool) -> None:
        monkeypatch.setattr("builtins.input", lambda _: answer)
        assert prompt_play_again() is expected

    def test_invalid_answer_asks_again(self, monkeypatch: pytest.MonkeyPatch) -> None:
        answers = iter(["maybe", "y"])
        monkeypatch.setattr("builtins.input", lambda _: next(answers))
        assert prompt_play_again() is True


class TestPlayGame:
    def test_player_wins(self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
        monkeypatch.setattr("snowman_meltdown.game_logic.get_random_word", lambda _: WORD_TO_GUESS)
        answers = iter([*WORD_TO_GUESS, "n"])
        monkeypatch.setattr("builtins.input", lambda _: next(answers))

        play_game(STAGES, [WORD_TO_GUESS])

        assert "Congratulations" in capsys.readouterr().out

    def test_player_loses(self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
        monkeypatch.setattr("snowman_meltdown.game_logic.get_random_word", lambda _: WORD_TO_GUESS)
        wrong_letters = "xyzqwvu"[: len(STAGES) - 1]  # one wrong guess per allowed mistake
        answers = iter([*wrong_letters, "n"])
        monkeypatch.setattr("builtins.input", lambda _: next(answers))

        play_game(STAGES, [WORD_TO_GUESS])

        assert "The snowman died" in capsys.readouterr().out

    def test_play_again_starts_a_second_game(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        monkeypatch.setattr("snowman_meltdown.game_logic.get_random_word", lambda _: WORD_TO_GUESS)
        answers = iter([*WORD_TO_GUESS, "y", *WORD_TO_GUESS, "n"])  # win. Then replay, win again, and quit
        monkeypatch.setattr("builtins.input", lambda _: next(answers))

        play_game(STAGES, [WORD_TO_GUESS])

        assert capsys.readouterr().out.count("Congratulations") == 2
