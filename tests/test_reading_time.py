import pytest
from lib.reading_time import estimated_reading_time

#tests reading time for 1000 word text
def test_reading_time_medium():
    text = " ".join(["word" for i in range(0, 1000)])
    result = estimated_reading_time(text)
    assert result == 5


def test_reading_time_short():
    text = " ".join(["word" for i in range(0, 500)])
    result = estimated_reading_time(text)
    assert result == 2.5


def test_reading_time_long():
    text = " ".join(["word" for i in range(0, 11250)])
    result = estimated_reading_time(text)
    assert result == 56.25


def test_reading_time_error():
    with pytest.raises(Exception) as err:
        estimated_reading_time("")
    error_message = str(err.value)
    assert error_message == "No text length to estimate!"