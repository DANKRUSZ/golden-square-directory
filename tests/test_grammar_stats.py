import pytest
from lib.grammar_stats import GrammarStats


def test_grammar_valid():
    grammar = GrammarStats()
    result = grammar.check("This sentence is correct.")
    assert result == True

def test_grammar_invalid_cap():
    grammar = GrammarStats()
    result = grammar.check("this sentence is not correct.")
    assert result == False

def test_grammar_invalid_punc():
    grammar = GrammarStats()
    result = grammar.check("This sentence is not correct")
    assert result == False

def test_grammar_invalid():
    grammar = GrammarStats()
    result = grammar.check("this sentence is not correct")
    assert result == False


def test_percentage_good():
    grammar = GrammarStats()
    grammar.check("This sentence is correct.")
    grammar.check("This sentence is also correct!")
    grammar.check("This sentence is wrong")
    grammar.check("this is also wrong.")
    result = grammar.percentage_good()
    assert result == 50


def test_percentage_good():
    grammar = GrammarStats()
    grammar.check("This sentence is correct.")
    grammar.check("This sentence is also correct!")
    grammar.check("This sentence is wrong")
    grammar.check("this is also wrong.")
    grammar.check("Still not right")
    grammar.check("nope")
    result = grammar.percentage_good()
    assert result == 33