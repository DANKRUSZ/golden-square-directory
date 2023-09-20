

def count_words(string):
    total = 0
    string_list = string.split()
    for word in string_list:
        total += 1
    return total