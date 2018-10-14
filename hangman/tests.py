from Hangman import check_letter, reveal_letter, print_result

def test_check_letter():
    assert check_letter("world", "a") == 1
