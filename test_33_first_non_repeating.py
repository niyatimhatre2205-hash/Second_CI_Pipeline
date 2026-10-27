import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "first_non_repeating",
    Path(__file__).with_name("33_first_non_repeating.py")
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_normal_string():
    assert module.first_non_repeating("aabbcdd") == "c"


def test_first_character():
    assert module.first_non_repeating("abcd") == "a"


def test_all_repeating():
    assert module.first_non_repeating("aabbcc") is None


def test_empty_string():
    assert module.first_non_repeating("") is None