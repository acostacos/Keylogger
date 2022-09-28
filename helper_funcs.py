from pynput.keyboard import Key

def convert_key_to_string(key, printing_array) -> str:
    if (key == Key.space or key == Key.enter):
        return '\n'
    
    key_str = str(key).replace("'", "")

    if keyIsSpecialKeyCode(key_str) or keyIsKeyboardShortcut(key_str):
        prefix = ''
        if len(printing_array) > 0:
            last_elem = printing_array[-1]
            if not keyIsSpecialKeyCode(last_elem) and not keyIsKeyboardShortcut(last_elem):
                prefix=f'\n'

        return f'{prefix}{key_str}\n'

    return key_str
       
def keyIsSpecialKeyCode(key_str) -> bool:
    return key_str.find('Key') != -1

def keyIsKeyboardShortcut(key_str) -> bool:
    return key_str.find('\\x') != -1