import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("Beli Ciki, Beli Koyo", 0.1),
        ("Sukiyo", 0.1),
        ("Ima anata ni omoi nosete", 0.1),
        ("Hora", 0.1),
        ("sunao ni naru no watashi", 0.1),
        ("Kono saki motto ", 0.1),
        ("soba ni ite mo ii ka na?", 0.1),
        ("Koi to koi ga kasanatte", 0.1),
        ("Suki yo", 0.1),
    ]
    # Total time delays including the cumulative sum of previous delays
    delays = [0.1, 1.5, 0.5, 1.0, 0.5, 1.0, 0.5 , 1.0, 0.5]
    
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        delay = delays[i]
        t = Thread(target=sing_lyric, args=(lyric, delay, speed))
        t.start()
        t.join()  # Ensure each lyric is displayed sequentially

if __name__ == "__main__":
    sing_song()
