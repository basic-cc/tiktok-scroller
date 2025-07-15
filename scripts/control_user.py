def run_control_user(context):
    page = context.new_page()
    page.goto("https://www.tiktok.com")

    for _ in range(20):  # Scroll through 20 videos
        page.mouse.wheel(0, 800)
        page.wait_for_timeout(5000)  # 5 seconds per video

    context.close()
