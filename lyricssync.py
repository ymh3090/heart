import sys, os,time

def printlyrics(timestamps=None, default_char_delay=0.05, pause_between=0.5):
    lines = [
        "Is this the real life?",
        "Is this just fantasy?",
        "Caught in a landslide,",
        "No escape from reality.",
        "Open your eyes,",
        "Look up to the skies and see,",
        "I'm just a poor boy, I need no sympathy,",
        "Because I'm easy come, easy go,",
        "Little high, little low,",
        "Any way the wind blows doesn't really matter to me, to me."
    ]

    start = time.time()
    for i, line in enumerate(lines):
        # If timestamps supplied, wait until that timestamp (relative to start)
        if timestamps and i < len(timestamps):
            target = start + timestamps[i]
            now = time.time()
            wait = target - now
            if wait > 0:
                time.sleep(wait)

        # Print the line character-by-character
        for ch in line:
            print(ch, end='', flush=True)
            time.sleep(default_char_delay)
        print()

        # If no timestamps provided, use a simple pause between lines
        if not timestamps:
            time.sleep(pause_between)

if __name__ == "__main__":
    try:
        # Example usage:
        # To use timestamp sync, provide a list of times (seconds from start) for each line:
        # timestamps = [0.0, 3.0, 6.5, 10.0, 13.0, 16.0, 19.0, 23.0, 27.0, 30.0]
        # printlyrics(timestamps=timestamps, default_char_delay=0.04)
        printlyrics(default_char_delay=0.04, pause_between=0.8)
    except KeyboardInterrupt:
        print("\nStopped")
