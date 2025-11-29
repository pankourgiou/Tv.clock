import time
import os

# Greek TV channels + TV5 and BBC
channels = [
    "ERT1", "ERT2", "ERT3", "MEGA", "Ant1", "ALPHA",
    "STAR", "SKAI", "OPEN", "TV5", "CNN", "BBC"
]

def channel_clock():
    while True:
        # Clear screen (works on Windows and Linux/Mac)
        os.system('cls' if os.name == 'nt' else 'clear')

        # Current time
        now = time.localtime()
        hour = now.tm_hour % 12
        minute = now.tm_min
        second = now.tm_sec

        # Get current channel
        current_channel = channels[hour]

        print("="*40)
        print("     📺 Greek TV Channel Clock")
        print("="*40)
        print(f"Time: {now.tm_hour:02}:{minute:02}:{second:02}")
        print(f"Channel of the hour: {current_channel}")
        print("="*40)

        # Wait 1 second
        time.sleep(1)

if __name__ == "__main__":
    channel_clock()
