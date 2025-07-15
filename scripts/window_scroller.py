import pygetwindow as gw
import pyautogui
import time

def prepare_windows():
    all_windows = gw.getAllWindows()
    tiktok_windows = [w for w in all_windows if w.visible and 'TikTok' in w.title][:4]
    screen_width, screen_height = pyautogui.size()
# 
#     for i, win in enumerate(tiktok_windows):
#         x = 0 if i % 2 == 0 else screen_width // 2
#         y = 0 if i < 2 else screen_height // 2
#         win.resizeTo(screen_width // 2, screen_height // 2)
#         win.moveTo(x, y)
# 
# 
def scroll_all_windows():
    tiktok_windows = [w for w in gw.getAllWindows() if w.visible and 'TikTok' in w.title][:4]
    screen_width, screen_height = pyautogui.size()

    for i, win in enumerate(tiktok_windows):
        x = 0 if i % 2 == 0 else screen_width // 2
        y = 0 if i < 2 else screen_height // 2
        pyautogui.moveTo(x + screen_width // 4, y + screen_height // 4)
        time.sleep(0.5)
        pyautogui.scroll(-800)  # Use scroll instead of drag
        time.sleep(0.5)
