import pygetwindow as gw
import pyautogui
import time

def prepare_windows():
    windows = [w for w in gw.getWindowsWithTitle('TikTok') if w.isVisible][:4]
    screen_width, screen_height = pyautogui.size()

    for i, win in enumerate(windows):
        x = 0 if i % 2 == 0 else screen_width // 2
        y = 0 if i < 2 else screen_height // 2
        win.resizeTo(screen_width // 2, screen_height // 2)
        win.moveTo(x, y)


def scroll_all_windows():
    windows = [w for w in gw.getWindowsWithTitle('TikTok') if w.isVisible][:4]
    for win in windows:
        win.activate()
        time.sleep(1)
        pyautogui.scroll(-10)
