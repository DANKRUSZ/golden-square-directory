import pytest 
from lib.music_tracker import MusicTracker

def test_one_pair_added():
    musictracker = MusicTracker()
    musictracker.add("Black Sabbath", "Paranoid")
    result = musictracker.return_track_list()
    assert result == [{"Black Sabbath": "Paranoid"}]

def test_multiple_pairs_added():
    musictracker = MusicTracker()
    musictracker.add("Black Sabbath", "Paranoid")
    musictracker.add("Fleetwood Mac", "Dreams")
    musictracker.add("ABBA", "Waterloo")
    musictracker.add("Taylor Swift", "22")
    result = musictracker.return_track_list()
    assert result == [{"Black Sabbath": "Paranoid"}, {"Fleetwood Mac": "Dreams"}, 
                    {"ABBA": "Waterloo"}, {"Taylor Swift": "22"}]
    


def test_add_artist_track():
    musictracker = MusicTracker()
    with pytest.raises(Exception) as e:
        musictracker.add("", "")
    error_message = str(e.value)
    assert error_message == "No artist or track added"