import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "count_words",
    Path(__file__).with_name("32_count_words.py")
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_normal_sentence():
    assert module.count_words("I love Python") == 3


def test_empty_string():
    assert module.count_words("") == 0


def test_extra_spaces():
    assert module.count_words("  Hello   World  ") == 2


def test_single_word():
    assert module.count_words("Python") == 1