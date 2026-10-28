import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "check_sorted",
    Path(__file__).with_name("34_check_sorted.py")
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_sorted_list():
    assert module.is_sorted([1, 2, 3, 4])


def test_unsorted_list():
    assert not module.is_sorted([1, 3, 2, 4])


def test_equal_elements():
    assert module.is_sorted([2, 2, 2])


def test_empty_list():
    assert module.is_sorted([])