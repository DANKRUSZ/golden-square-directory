import pytest
from lib.check_grammar import check_grammar

def test_grammar_valid():
    result = check_grammar("This sentence is correct.")
    assert result == True

def test_grammar_capital_valid():
    result = check_grammar("This sentence is not correct")
    assert result == False


def test_grammar_end_punc_valid():
    result = check_grammar("why is this not correct?")
    assert result == False


def test_grammar_end_both_invalid():
    result = check_grammar("this is horribly wrong")
    assert result == False


def test_grammar_end_punc_is_valid():
    result = check_grammar("why is this not correct!")
    assert result == False

def test_grammar_end_punc_valid_only():
    result = check_grammar("why is this not correct.")
    assert result == False

def test_grammar_valid_as_well():
    result = check_grammar("This sentence is correct?")
    assert result == True


def test_grammar_valid_still():
    result = check_grammar("This sentence is correct!")
    assert result == True