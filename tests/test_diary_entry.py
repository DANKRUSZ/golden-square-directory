import pytest
from lib.diary_entry import DiaryEntry

def test_format_is_correct():
    diaryentry = DiaryEntry("Thursday", "I am tired")
    #diaryentry.__init__("Thursday", "I am tired")
    result = diaryentry.format()
    assert result == "Thursday: I am tired"
    #f"{self.title}: {contents}"
