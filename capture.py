import pygetwindow as gw
from PIL import ImageGrab


def capture_window(title):
    windows = gw.getWindowsWithTitle(title)
    if not windows:
        print(f'No window with title {title} found')
        return None

    window = windows[0]
    if window.isMinimized:
        window.restore()

    window.activate()

    error = 10
    bbox = (window.left + error, window.top + error, window.right - error, window.bottom - error)
    img = ImageGrab.grab(bbox=bbox)

    return img, bbox
