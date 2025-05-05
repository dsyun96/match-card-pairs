import keyboard
import config
import os
import pyautogui


def register_exit_hotkey():
    keyboard.add_hotkey(config.STOP_HOTKEY, exit_program)

def exit_program():
    print(f'{config.STOP_HOTKEY} pressed...')
    os._exit(0)

def register_move_hotkey(card_pairs):
    keyboard.add_hotkey(',', move_prev, args=(card_pairs,))
    keyboard.add_hotkey('.', move_next, args=(card_pairs,))

now = 0

def move_prev(card_pairs):
    global now

    now -= 1
    if now < 0:
        now = 0

    card = card_pairs[now // 2][now & 1]
    pyautogui.moveTo(card[0], card[1], duration=0.1)

def move_next(card_pairs):
    global now

    now += 1
    if now == len(card_pairs) * 2:
        now = len(card_pairs) * 2 - 1

    card = card_pairs[now // 2][now & 1]
    pyautogui.moveTo(card[0], card[1], duration=0.1)
