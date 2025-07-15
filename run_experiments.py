# run_experiments.py
from playwright.sync_api import sync_playwright
from scripts.control_user import run_control_user
from scripts.experimental_user import run_experimental_user
import threading

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        # Run control and experiment in separate browser contexts
        context_control = browser.new_context()
        context_experiment = browser.new_context()

        thread_control = threading.Thread(target=run_control_user, args=(context_control,))
        thread_experiment = threading.Thread(target=run_experimental_user, args=(context_experiment,))

        thread_control.start()
        thread_experiment.start()

        thread_control.join()
        thread_experiment.join()

        browser.close()
