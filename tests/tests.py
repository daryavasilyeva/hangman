"""Tests"""
from hangman import check_letter, reveal_letter, init, print_result


def test_check_letter():
    """check_letter"""
    assert check_letter("world", "a") == 0


def test_reveal_letter():
    """reveal_letter"""
    assert reveal_letter("te", ['*', 'e'], "t") == ['t', 'e']


def test_init():
    """test init"""
    assert init() == 0


def test_print_result():
    """test print result"""
    assert print_result(5, "word") == 0
