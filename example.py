from librespot.player.codecs import AudioQuality, VorbisOnlyAudioQuality
from librespot.core import Session
from librespot.metadata import TrackId 
from spotify_secrets import Credentials
import sounddevice as sd
import numpy
assert numpy

def get_session(username,password):
    active_session = Session.Builder().user_pass(username, password).create()
    print(f"Logged in Successfully")
    return active_session

def get_audio_stream_session(session,track_uri):
    
    track_id = TrackId.from_uri(track_uri)
    audio_stream_session = session.content_feeder().load(track_id, VorbisOnlyAudioQuality(AudioQuality.AudioQuality.VERY_HIGH), False, None)

    return audio_stream_session

def get_audio_stream_data(audio_stream_session):
    return audio_stream_session.input_stream.stream().read()


# This doesn't work
def play_audio(active_session,desired_track_uri):
    active_session = get_audio_stream_session(session=active_session,track_uri=desired_track_uri)
    data = get_audio_stream_data(active_session)
    try:
        
        sd.play(data)
        print("We're trying to play!")
    except KeyboardInterrupt:
            print("Exiting!")
    except Exception as e:
           print(f"Error!: type{e}.__name__ + ': ' + {e})")
           raise SystemExit

if __name__ == "__main__":
    active_session = get_session(username=Credentials.username,password=Credentials.password)
    play_audio(active_session=active_session,desired_track_uri="spotify:track:4uLU6hMCjMI75M1A2tKUQC")
