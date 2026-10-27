import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "pangram",
    Path(__file__).with_name("31_pangram.py")
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def test_pangram():
    assert module.is_pangram(
        "The quick brown fox jumps over the lazy dog"
    )

def test_not_pangram():
    assert not module.is_pangram("Hello World")

def test_empty_string():
    assert not module.is_pangram("")