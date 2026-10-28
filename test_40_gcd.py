import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "gcd_module",
    Path(__file__).with_name("40_gcd.py")
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_gcd_common_factors():
    assert module.gcd(12, 8) == 4


def test_gcd_fifteen_ten():
    assert module.gcd(15, 10) == 5


def test_gcd_coprime_numbers():
    assert module.gcd(7, 3) == 1


def test_gcd_with_zero():
    assert module.gcd(5, 0) == 5