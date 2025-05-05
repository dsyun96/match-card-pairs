from hotkey import register_exit_hotkey, register_move_hotkey, move_prev
from capture import capture_window
from converter import convert_pil_to_numpy
from detector import detect_cards
from matcher import match_cards
import config
import time


def main():
    register_exit_hotkey()

    image, bbox = capture_window(config.WINDOW_TITLE)
    converted_image = convert_pil_to_numpy(image)

    cards = detect_cards(converted_image, bbox)
    card_pairs = match_cards(cards)

    register_move_hotkey(card_pairs)
    move_prev(card_pairs)

    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
