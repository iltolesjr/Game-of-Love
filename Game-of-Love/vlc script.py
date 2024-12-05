import sys
import time

install = 'C:/Program Files/VideoLAN/VLC/'
installvlc: str = install + 'vlc.py'
sys.path.append (installvlc)

import vlc

print (sys.executable)


def play_video_from_last_3_minutes (video_path):
    # Create a VLC instance
    instance = vlc.Instance ()
    player = instance.media_player_new ()

    # Load the media
    media = instance.media_new (video_path)
    player.set_media (media)

    # Start playing the video
    player.play ()

    # Wait for the media to be parsed
    time.sleep (1)

    # Get the duration of the video in milliseconds
    duration = player.get_length ()

    # Calculate the start time (last 3 minutes)
    start_time = max (0, duration - 3 * 60 * 1000)

    # Set the start time
    player.set_time (start_time)

    # Keep the video playing
    while player.get_state () != vlc.State.Ended:
        time.sleep (1)


# Example usage
video_path = 'path_to_your_video.mp4'

play_video_from_last_3_minutes (video_path)