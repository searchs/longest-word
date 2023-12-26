import re
from fastapi import FastAPI
from pydantic import BaseModel

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from loguru import logger


class WordApp:
    """WordApp application returns the longest and shortest word(s) as well as their
    respective lengths.
    """

    def __init__(self) -> None:
        logger.info("Word apps starting")
        self.longest_words = {}
        self.shortest_words = {}
        self.sentence = None

    def accept_sentence(self, check_line=None) -> str:
        """Accepts a string of texts to be processed

        :params check_line:  String of words to be analyzed
        Return: Returns the string as lowercase sentence only in a set.
        """

        if check_line is None:
            return "Empty words"

        regex = re.compile(r"\w+[aA-zZ]")
        sentence = regex.findall(check_line)
        self.sentence = set(map(lambda x: x.lower(), sentence))
        return self.sentence

    def get_longest_word(self) -> str | tuple(str, str):
        """Checks for the longest words in the sentence.

        Return: a tuple of list of the longest words and the length of each word
        """

        if self.sentence is None:
            return "No word"

        if len(self.sentence) == 0:
            return "No word"

        longest_value = max(list(map(lambda x: len(x), self.sentence)))
        matching_words = set(
            filter(lambda f: len(f) == longest_value, self.sentence)
        )

        return (matching_words, longest_value)

    def get_shortest_word(self) -> str | tuple(str, str):
        """Get the shortest word(s) and the length of such word(s).
        :returns a list of shortest words and the length of the shortest word
        """

        if self.sentence is None:
            return "No word"

        if len(self.sentence) == 0:
            return "No word"

        shortest_value = min(set(map(lambda x: len(x.strip()), self.sentence)))
        matching_words = set(
            filter(
                lambda f: len(f) > 0 and len(f) == shortest_value,
                self.sentence,
            )
        )

        return (matching_words, shortest_value)


# As an API service - easy testing


@dataclass_json
@dataclass
class Result(BaseModel):
    words: list
    word_length: int


app = FastAPI()

word_app = WordApp()
word_app.sentence = None


@app.get("/")
def root():
    """Root of api.  Checkout http://localhost:8000/docs to test it out."""
    return {
        "app": "WordApp",
        "version": "0.0.1",
        "description": "Get longest and shortest words from sentence with lengths.",
        "test_page": "http://localhost:8000/docs",
    }


@app.get("/{check_type}")
def get_words_by_length(check_type: str, sentence: str = None) -> dict:
    word_app.accept_sentence(sentence)
    if check_type == "longest":
        results = word_app.get_longest_word()
    if check_type == "shortest":
        results = word_app.get_shortest_word()

    if check_type is None or check_type not in ["longest", "shortest"]:
        results = "No Type specified"

    if "No word" in results:
        return {"check_type": check_type, "words": "No word"}

    if "No Type specified" in results:
        return {"check_type": "Invalid check_type", "words": "No word"}

    return {
        "check_type": check_type,
        "words": results[0],
        "word_length": results[1],
    }
