from lib.count_words import count_words
#tests if string has correct number of words
def test_count_words_correct():
    result = count_words("This string has five words")
    assert result == 5

