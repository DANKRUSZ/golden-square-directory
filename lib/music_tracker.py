

class MusicTracker():

    def __init__(self):
        # A list of tracks I have listened to
        # A list of dictionaries, key - artist, value - track
        self.song_list = []

    def add(self, artist, track):
        # Add {artist: track} , to the list
        self.song_list.append({artist: track})
        if artist == "" and track == "":
            raise Exception("No artist or track added")
        

    def return_track_list(self):
        # return a list of the artists and tracks
        # Raise exception if nothing added
        
        return self.song_list