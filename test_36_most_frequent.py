import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "most_frequent",
    Path(__file__).with_name("36_most_frequent.py")
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_most_frequent_element():
    assert module.most_frequent([1, 2, 2, 3, 2, 4]) == 2


def test_single_element():
    assert module.most_frequent([7]) == 7


def test_tie_returns_first_element():
    assert module.most_frequent([5, 5, 1, 1]) == 5


def test_empty_list():
    assert module.most_frequent([]) is None