from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser
driver = webdriver.Chrome()
driver.get("https://comic.naver.com/webtoon")

# Wait for page to load
time.sleep(5)

# Get webtoon items
items = driver.find_elements(By.CSS_SELECTOR, "#container ul li")

print("=== WEBTOON DATA ===")

for i, item in enumerate(items[:10], start=1):
    try:
        lines = item.text.split("\n")

        # Expected structure:
        # [New, Title, Author, Description]

        if len(lines) >= 4:
            title = lines[1]
            author = lines[2]
            description = lines[3]

            print(f"{i}. Title       : {title}")
            print(f"   Author      : {author}")
            print(f"   Description : {description}")
            print("-" * 40)

    except:
        pass

# Close browser
driver.quit()