import pytest
from lib.diary_entry import DiaryEntry

def test_format_is_correct():
    diaryentry = DiaryEntry("Thursday", "I am tired")
    #diaryentry.__init__("Thursday", "I am tired")
    result = diaryentry.format()
    assert result == "Thursday: I am tired"
    #f"{self.title}: {contents}"

def test_count_words_correct():
    diaryentry = DiaryEntry("Today", "I went to the shops")
    result = diaryentry.count_words()
    assert result == 6

def test_count_words_long_correct():
    contents = " ".join(["word" for i in range(0, 100)])
    diaryentry = DiaryEntry("Today", contents)
    result = diaryentry.count_words()
    assert result == 101

def test_reading_time_correct():
    contents = " ".join(["word" for i in range(0, 100)])
    diaryentry = DiaryEntry("Friday", contents)
    result = diaryentry.reading_time(20)
    assert result == 5

def test_reading_time_correct_long():
    contents = " ".join(["word" for i in range(0, 1000)])
    diaryentry = DiaryEntry("Friday", contents)
    result = diaryentry.reading_time(100)
    assert result == 10

def test_reading_chunk_correct():
    pass