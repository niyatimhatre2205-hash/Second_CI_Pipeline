import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "rotate_string",
    Path(__file__).with_name("37_rotate_string.py")
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_rotate_by_two():
    assert module.rotate_string("abcdef", 2) == "efabcd"


def test_rotate_by_one():
    assert module.rotate_string("hello", 1) == "ohell"


def test_rotate_by_full_length():
    assert module.rotate_string("abc", 3) == "abc"


def test_empty_string():
    assert module.rotate_string("", 2) == ""