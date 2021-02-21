from pydeezer import Deezer ## pip install py-deezer
deezer = Deezer()

def login(arl):
    """
    Gets a user's arl and login to its deezer account.
    """
    return deezer.login_via_arl(arl)

def import_deezer_playlist(playlist_id):
    """
    Gets a deezer playlist id and returns a list of tuple,
    contains all track names in playlist, artist's name and track's album.
    """
    playlist = deezer.get_playlist_tracks(playlist_id)
    tracks_list = []
    for track in playlist:
        track_name = " ".join(track["tag"])
        tracks_list.append(track_name)
    return tracks_list

if __name__ == "__main__":
