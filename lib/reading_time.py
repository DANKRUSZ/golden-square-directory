

def estimated_reading_time(text):
    speed = 200
    words = text.split()
    estimate = len(words) / speed
    if len(text) == 0:
        raise Exception("No text length to estimate!")
    return estimate