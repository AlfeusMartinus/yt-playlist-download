import pytube

playlist_url = "https://youtube.com/playlist?list=PLjRBWix725xo8F3mPC44JmlNHC3fXmnD_"

playlist = pytube.Playlist(playlist_url)
for video in playlist.videos:
    video.streams.get_highest_resolution().download()
