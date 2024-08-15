from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from parser import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from teams import teams, scroll, ss, iframes
from PIL import Image
import pytesseract

if __name__ == '__main__':
    x = input('Press Enter to Start')
    _teams = list(teams)[-1:] if x == 'e' else teams

    for team in _teams:
        t = teams[team]
        url = t['link']

        options = Options()
        # options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(10)

        if team == 'Nets':
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
            time.sleep(5)
            buttons = driver.find_elements(
                By.CSS_SELECTOR,
                "button.focus\\:outline-none.flex.justify-between.w-full.py-5.lg\\:items-center")
            for button in buttons:
                try:
                    driver.execute_script("arguments[0].scrollIntoView(true);", button)
                    time.sleep(1)
                    driver.execute_script("arguments[0].click();", button)
                    time.sleep(1)
                except Exception as e:
                    print(f"An error occurred: {e}")
                    continue

        if team in ss:
            p1 = f'pics/ss{team}1.png'
            p2 = f'pics/ss{team}2.png'
            p3 = f'pics/ss{team}3.png'
            driver.save_screenshot(p1)
            page_height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script(f"window.scrollTo(0, {page_height // 4});")
            time.sleep(2)
            driver.save_screenshot(p2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 300);")
            time.sleep(2)
            driver.save_screenshot(p3)

            xp = [p1, p2, p3]
            text = ''
            for p in xp:
                image = Image.open(p)
                text += pytesseract.image_to_string(image)
            text = text.split('\n')
            job_posts = []
            for t in text:
                if 'Chicago, IL' in t:
                    job_posts.append(t)

        elif team in iframes:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.TAG_NAME, 'iframe'))
            )
            iframes = driver.find_elements(By.TAG_NAME, 'iframe')
            driver.switch_to.frame(iframes[0])  # Adjust index if necessary
            page_source = driver.page_source
            job_posts = driver.find_elements(By.XPATH, ".//a[@class='iCIMS_Anchor']")[:-1]

        else:
            if team in scroll:
                page_height = driver.execute_script("return document.body.scrollHeight")
                driver.execute_script(f"window.scrollTo(0, {page_height // 2});")
                time.sleep(2)

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            driver.quit()

            el = t['element']

            if team == 'Nets':
                job_posts = soup.select(el)
            else:
                job_posts = soup.find_all(**el)

        new_jobs = parse(job_posts, team)

        print(new_jobs)
