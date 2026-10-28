import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "missing_number_xor",
    Path(__file__).with_name("38_missing_number_xor.py")
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_missing_middle_number():
    assert module.missing_number([3, 0, 1]) == 2


def test_missing_last_number():
    assert module.missing_number([0, 1]) == 2


def test_missing_zero():
    assert module.missing_number([1, 2, 3]) == 0


def test_larger_list():
    assert module.missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8