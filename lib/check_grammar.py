

def check_grammar(text):
    valid_punc = ["!", ".", "?"]
    if text == text.capitalize() and text[-1] in valid_punc:
        return True
    elif len(text) == 0:
        raise Exception("There is no string to check for grammar mistakes.")
    else:
        return False