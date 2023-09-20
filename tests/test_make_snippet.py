from lib.make_snippet import make_snippet

def test_make_snippet_correct():
    result = make_snippet("This should only return words before the before")

    assert result == "This should only return words..."
