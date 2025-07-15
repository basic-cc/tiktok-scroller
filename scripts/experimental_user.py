# scripts/experimental_user.py
import random

def run_experimental_user(context):
    page = context.new_page()
    page.goto("https://www.tiktok.com")

    for _ in range(20):
        wait_time = random.choice([2000, 4000, 8000])
        page.wait_for_timeout(wait_time)

        # Simulate engagement 50% of the time
        if random.random() > 0.5:
            try:
                like_button = page.query_selector("button[data-e2e='like-icon']")
                if like_button:
                    like_button.click()
            except:
                pass

        page.mouse.wheel(0, 800)

    context.close()
