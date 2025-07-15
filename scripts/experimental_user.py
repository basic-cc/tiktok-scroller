import random
from scripts.utils import log_event

def run_experimental_user(context):
    page = context.new_page()
    page.goto("https://www.tiktok.com")

    for i in range(20):
        wait_time = random.choice([2000, 4000, 8000])
        page.wait_for_timeout(wait_time)
        log_event("logs/experiment_log.csv", "Watched video", f"{wait_time}ms")

        page.mouse.wheel(0, 800)

    context.close()
