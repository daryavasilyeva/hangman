"""Tests"""
from hangman import check_letter, reveal_letter


def test_check_letter():
    """check_letter"""
    assert check_letter("world", "a") == 0


def test_reveal_letter():
    """reveal_letter"""
    assert reveal_letter("te", ['*', 'e'], "t") == ['t', 'e']
