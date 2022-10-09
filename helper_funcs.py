from pynput.keyboard import Key
from datetime import datetime

def convert_key_to_string(key, printing_array) -> str:
    if (key == None):
        return None

    last_elem = printing_array[-1] if len(printing_array) > 0 else ''

    if (key == Key.space or key == Key.enter or key == Key.backspace):
        return '\n' if last_elem != '\n' else None

    key_str = str(key).replace("'", "")
    if keyIsSpecialKeyCode(key_str) or keyIsKeyboardShortcut(key_str):
        prefix = ''
        if not keyIsSpecialKeyCode(last_elem) and not keyIsKeyboardShortcut(last_elem):
            prefix=f'\n'

        return f'{prefix}{key_str}\n'

    return key_str
       
def keyIsSpecialKeyCode(key_str) -> bool:
    return key_str.find('Key') != -1

def keyIsKeyboardShortcut(key_str) -> bool:
    return key_str.find('\\x') != -1

def generateFilename() -> str:
    current_time = datetime.now()
    filename = current_time.strftime('%d-%m-%Y')
    return f'{filename}.txt'
