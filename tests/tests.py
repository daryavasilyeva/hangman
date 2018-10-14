from hangman import check_letter, reveal_letter, print_result


def test_check_letter():
    assert check_letter("world", "a") == 0


def test_reveal_letter():
    assert reveal_letter("test", ['*', 'e', 's', '*'], "t") \
           == ['t', 'e', 's', 't']


def test_print_result():
    assert print_result(4, "pool") == 1
