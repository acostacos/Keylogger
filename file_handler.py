import threading
import time
from helper_funcs import convert_key_to_string

class FileHandler:
    def __init__(self, filename, timer_count) -> None:
        # Constants
        self.filename = filename
        self.timer_count = timer_count

        self.items_to_print = []
        self.current_time = 0
        self.timer_thread = None

    def print_key_to_file(self, key) -> None:
        key_as_text = convert_key_to_string(key, self.items_to_print)
        self.items_to_print.append(key_as_text)

        if self.timer_thread == None or (not self.timer_thread.is_alive()):
            self.timer_thread = threading.Thread(target=self.__printing_timer)
            self.timer_thread.start()
        else:
            self.current_time = 0

    def __printing_timer(self) -> None:
        while self.current_time < self.timer_count:
            time.sleep(1)
            self.current_time += 1
        
        self.__print()
        self.timer_thread = None

    def __print(self) -> None:
        with open(self.filename, 'a') as out:
            for item in self.items_to_print:
                out.write(item)

        self.current_time = 0
        self.items_to_print = []