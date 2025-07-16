# TikTok Scroll Experiment

## Important!
- Make sure 4 TikTok browser windows are already open and resized to your desire before clicking "Scroll."
- Windows must contain "TikTok" in the title bar (case-sensitive).
- Works with Chrome, Arc, Edge, etc., as long as window titles are matched.
- This project simulates passive scrolling behavior across four TikTok browser windows using only GUI automation — no browser integration or code injection required.

## 🔧 How It Works

- Detects up to **4 visible TikTok browser windows**.
- On pressing the **"Scroll" button**, the script:
  - Activates each window
  - Moves the mouse focus
  - Performs one downward scroll in each

## 🖥️ Interface

The program launches a minimal GUI with a single **"Scroll"** button.

## 📦 Requirements

```txt
pyautogui
pygetwindow
tk
