import pytest

from app.wordapp import WordApp


@pytest.fixture(autouse=True)
def wordapp():
    wordapp = WordApp()
    wordapp.sentence = ""
    return wordapp


def test_can_accept_sentence(wordapp):
    wordapp.accept_sentence("My simple sentence.")
    assert "my" in wordapp.sentence
    assert "simple" in wordapp.sentence
    assert "sentence" in wordapp.sentence
    assert len(wordapp.sentence) == 3


def test_returns_error_message_if_no_entry_longest(wordapp):
    assert wordapp.accept_sentence() == "Empty words"
    assert wordapp.get_longest_word() == "No word"


def test_returns_error_message_if_no_entry_shortest(wordapp):
    assert wordapp.accept_sentence() == "Empty words"
    assert wordapp.get_shortest_word() == "No word"


def test_return_only_word_if_only_one_word(wordapp):
    wordapp.accept_sentence("The")
    words, word_length = wordapp.get_longest_word()
    assert "the" in words
    assert word_length == 3


def test_return_longest_word_list_with_length(wordapp):
    line = "The cow jumped over the rock beside the moon."
    wordapp.accept_sentence(line)
    words, word_length = wordapp.get_longest_word()
    assert "jumped" in words
    assert "beside" in words
    assert word_length == 6


def test_return_shortest_word_list_with_length(wordapp):
    line = "The cow jumped over the rock beside the moon."
    wordapp.accept_sentence(line)
    words, word_length = wordapp.get_shortest_word()
    assert "cow" in words
    assert "the" in words
    assert word_length == 3


def test_return_longest_words_from_sentence_with_integers(wordapp):
    line = "Please do not count 123456789 in the poem."
    wordapp.accept_sentence(line)
    words, word_length = wordapp.get_longest_word()
    assert "please" in words
    assert "123456789" not in words
    assert word_length == 6


def test_can_return_valid_error_if_sentence_is_none(wordapp):
    line = None
    wordapp.accept_sentence(line)
    valid_error_msg = wordapp.get_longest_word()
    assert valid_error_msg == "No word"


def test_can_return_valid_error_if_sentence_set_to_none(wordapp):
    line = None
    wordapp.accept_sentence(line)
    wordapp.sentence = None
    valid_error_msg_longest = wordapp.get_longest_word()
    assert valid_error_msg_longest == "No word"

    valid_error_msg_shortest = wordapp.get_shortest_word()
    assert valid_error_msg_shortest == "No word"
