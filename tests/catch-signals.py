#! /usr/bin/env python

import os
import signal
import sys

pid = os.getpid()
print(f"Current process ID: {pid}")

def signal_handler(signum, frame):
    print(f"Caught signal: {signum} - {signal.Signals(signum).name}")
    #sys.exit()

# Register handlers for all possible signals
for sig in range(1, signal.NSIG):
    if sig not in {signal.SIGKILL, signal.SIGSTOP}:
        try:
            signal.signal(sig, signal_handler)
        except OSError:
            # Some signals can't be caught, ignore them
            pass
        except AttributeError:
            # Not all signal numbers have a corresponding name, ignore them
            pass

print("Listening for signals. Press Ctrl+C to exit.")

try:
    # Run an infinite loop to keep the program running
    while True:
        pass
except KeyboardInterrupt:
    print("Exiting...")
    sys.exit()
