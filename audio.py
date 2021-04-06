from librespot.core import Session
from librespot.metadata import TrackId
from librespot.player.codecs import AudioQuality, VorbisOnlyAudioQuality
session = Session.Builder() \
    .user_pass("<username>", "<password>") \
    .create()

# The track ID can be obtained by "Copy Spotify URI" in the Share Menu
track_id = TrackId.from_uri("spotify:track:4uLU6hMCjMI75M1A2tKUQC")

stream = session.content_feeder().load(track_id, VorbisOnlyAudioQuality(AudioQuality.AudioQuality.VERY_HIGH), False, None)

# This currently doesn't work - breaks on 
# stream.input_stream.stream().read() to get one byte of the music stream