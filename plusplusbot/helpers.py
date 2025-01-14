import re
import string

from unidecode import unidecode


class ScottFactorExceededException(Exception):
    pass


remove_punctuation = str.maketrans('', '', string.punctuation)

emoji_regex = re.compile(r":[a-zA-Z0-9-_']+:")


def sanitize_text(text):
    # unidecode will normalize to ASCII
    normalized = unidecode(text)

    # Lowercase the text
    lowered = normalized.lower()

    # Strip whitespace
    stripped = lowered.strip()

    # Remove any random misc chars we deem unnessesary
    scrubbed = stripped.translate(remove_punctuation)

    return scrubbed


def match_emojirade(guess, emojirades, scott_factor=2):
    for emojirade in emojirades:
        if len(guess) > (len(emojirade) * scott_factor):
            raise ScottFactorExceededException("Guess exceeded the Scott Factor")

        if re.search(r"\b{0}\b".format(re.escape(emojirade)), guess):
            return True

    return False


def match_emoji(text):
    return bool(emoji_regex.search(text))
