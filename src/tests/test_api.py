from starlette.testclient import TestClient

from app.wordapp import app

client = TestClient(app)

# Setup test data
sentence = "The cow jumped over the moon."


def test_api_is_alive():
    assert client.get("/").status_code == 200


def test_can_get_longest_words_with_length():
    resp = client.get("/longest?sentence={0}".format(sentence))

    resp = resp.json()
    assert resp["check_type"] == "longest"
    assert "jumped" in resp["words"]
    assert resp["word_length"] == 6


def test_can_get_shortest_words_with_length():
    resp = client.get("/shortest?sentence={0}".format(sentence))

    resp = resp.json()
    assert resp["check_type"] == "shortest"
    assert "the" in resp["words"]
    assert "cow" in resp["words"]
    assert resp["word_length"] == 3


def test_returns_valid_error_for_wrong_check_type():
    resp = client.get("/loongest?sentence={0}".format(sentence))

    resp = resp.json()
    assert resp["check_type"] == "Invalid check_type"


def test_returns_no_word_for_empty_string():
    resp = client.get("/shortest?sentence=''")

    resp = resp.json()
    assert resp["words"] == "No word"

    resp_longest = client.get("/longest?sentence=''")
    resp_longest = resp_longest.json()
    assert resp["words"] == "No word"
