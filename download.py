import pytube

playlist_url = "insert-your-link-here!"

playlist = pytube.Playlist(playlist_url)
for video in playlist.videos:
    video.streams.get_highest_resolution().download()