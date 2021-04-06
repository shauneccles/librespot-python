from librespot.player.codecs import AudioQuality, VorbisOnlyAudioQuality
from librespot.core import Session
from librespot.metadata import TrackId 
import sounddevice as sd
import numpy
assert numpy

def get_session(username,password):
    active_session = Session.Builder().user_pass(username, password).create()
    
    access_token = active_session.tokens().get("playlist-read")
    print(f"Your Spotify Access Token is:{access_token}")
    return active_session

def get_audio_data(session,track_uri):
    
    track_id = TrackId.from_uri(track_uri)
    stream = session.content_feeder().load(track_id, VorbisOnlyAudioQuality(AudioQuality.AudioQuality.VERY_HIGH), False, None)

    return stream

def play_audio(active_session,desired_track_uri):
    try:
        sd.play(get_audio_data(session=active_session,track_uri=desired_track_uri))
    except KeyboardInterrupt:
            print("Exiting!")
    except Exception as e:
           print(f"Error!: type{e}.__name__ + ': ' + {e})")
           raise SystemExit

if __name__ == "__main__":
    active_session = get_session(username="<username>",password="<password>")
    play_audio(active_session=active_session,desired_track_uri="spotify:track:4uLU6hMCjMI75M1A2tKUQC")
