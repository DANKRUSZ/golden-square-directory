from lib.make_snippet import make_snippet
#tests is string is over 5 words
def test_make_snippet_correct_over_five():
    result = make_snippet("This should only return words before the before")
    assert result == "This should only return words..."

#tests if string is 5 and under
def test_make_snippet_correct_under_five():
    result = make_snippet("This should not have dots")
    assert result == "This should not have dots"