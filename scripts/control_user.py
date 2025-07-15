from scripts.utils import log_event

def run_control_user(context):
    page = context.new_page()
    page.goto("https://www.tiktok.com")

    for i in range(20):
        page.mouse.wheel(0, 800)
        page.wait_for_timeout(5000)  # 5 seconds per video
        log_event("logs/control_log.csv", "Watched video", "5000ms")

    context.close()
