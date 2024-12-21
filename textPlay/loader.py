'''
# 1. Displays a loading progress bar in the terminal 
# 2. 


'''

import itertools
import sys
import time
from threading import Thread, Event

# ProgressBar class
class ProgressBar:
    """
    A class to display a progress bar in the terminal.

    Attributes:
        length (int): The total length of the progress bar.
        symbol (str): The symbol used for the completed portion of the bar.
        empty_symbol (str): The symbol used for the incomplete portion of the bar.
        color_on_completion (str): The color used when the bar reaches 100%.
    """

    def __init__(self, length=50, symbol="█", empty_symbol="-", color_on_completion="\033[92m"):
        """
        Initializes the ProgressBar object.

        Args:
            length (int): The total length of the progress bar. Default is 50.
            symbol (str): The symbol for the completed portion. Default is '█'.
            empty_symbol (str): The symbol for the incomplete portion. Default is '-'.
            color_on_completion (str): The color for the bar at 100% completion. Default is green.
        """
        self.length = length
        self.symbol = symbol
        self.empty_symbol = empty_symbol
        self.color_on_completion = color_on_completion
        self._stop_event = Event()

    def start(self):
        """
        Starts the progress bar simulation in a separate thread.
        """
        self._stop_event.clear()
        self._progress_thread = Thread(target=self._simulate_progress)
        self._progress_thread.start()

    def stop(self):
        """
        Stops the progress bar animation and ensures the terminal is ready for new lines.
        """
        self._stop_event.set()
        self._progress_thread.join()
        sys.stdout.write("\n")  # Move to a new line after the progress bar

    def _display(self, progress):
        """
        Displays the progress bar with the current progress value.

        Args:
            progress (float): The current progress as a float between 0 and 1.
        """
        filled_length = int(self.length * progress)
        bar = self.symbol * filled_length + self.empty_symbol * (self.length - filled_length)
        color = self.color_on_completion if progress == 1 else ''
        reset = "\033[0m"
        sys.stdout.write(f"\r|{color}{bar}{reset}| {progress:.1%}")
        sys.stdout.flush()

    def _simulate_progress(self):
        """
        Simulates a progress bar incrementing from 0% to 100%.
        """
        for i in range(101):
            if self._stop_event.is_set():
                break
            progress = i / 100
            self._display(progress)
            time.sleep(0.01)  # Simulate some processing time


# Spinner class
class Spinner:
    """
    A class to create a terminal spinner animation.

    Attributes:
        frames (list): The sequence of characters or symbols to display as spinner frames.
        interval (float): The time interval (in seconds) between frames.
        _stop_event (threading.Event): An internal event object to control the spinner's state.
    """

    def __init__(self, frames= None, interval:float=0.1):
        """
        Initializes the Spinner object.

        Args:
            frames (list, optional): A list of symbols to use as frames for the spinner animation.
                                     Defaults to a predefined list of braille-style symbols.
            interval (float, optional): Time interval in seconds between each frame. Defaults to 0.1 seconds.
        """
        self.frames = frames or ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        self.interval = interval
        self._stop_event = Event()

    def start(self):
        """
        Starts the spinner animation in a separate thread.
        """
        self._stop_event.clear()
        self._spinner_thread = Thread(target=self._spin)
        self._spinner_thread.start()

    def stop(self):
        """
        Stops the spinner animation and clears the spinner line in the console.
        """
        self._stop_event.set()
        self._spinner_thread.join()
        sys.stdout.write("\r")  # Clears the spinner line
        sys.stdout.flush()

    def _spin(self):
        """
        Private method that cycles through the spinner frames and displays them in the console.

        This method is run in a separate thread and stops when the `_stop_event` is set.
        """
        for frame in itertools.cycle(self.frames):
            if self._stop_event.is_set():
                break
            sys.stdout.write(f"\r{frame} ")
            sys.stdout.flush()
            time.sleep(self.interval)

# Example usage
if __name__ == "__main__":
    spinner = Spinner()
    try:
        spinner.start()
        # Simulate a long-running task
        time.sleep(5)
    finally:
        spinner.stop()
        print("Done!")