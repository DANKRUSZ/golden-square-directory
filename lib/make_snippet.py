

def make_snippet(string):
    list_of_string = string.split()
    if len(list_of_string) > 5:
        new_string = " ".join(list_of_string[:5])
        return new_string + "..."
    else:
        return string

