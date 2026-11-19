from snowman_meltdown.snowman import WORDS, get_random_word


def test_random_word_returned_form_pool() -> None:
    assert get_random_word() in WORDS
