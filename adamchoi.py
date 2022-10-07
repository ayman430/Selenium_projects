from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import Select

date = []
home_team = []
score = []
away_team = []

web = webdriver.Chrome()
web.get("https://www.adamchoi.co.uk/overs/detailed")

all_matches_button = web.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()
matches = web.find_elements(By.TAG_NAME, "tr")

for match in matches:
    date.append(match.find_element(By.XPATH, './td[1]').text)
    h_team = match.find_element(By.XPATH, './td[2]').text
    home_team.append(h_team)
    print(h_team)
    score.append(match.find_element(By.XPATH, './td[3]').text)
    away_team.append(match.find_element(By.XPATH, './td[4]').text)

df = pd.DataFrame({"Date": date, "Home team": home_team, "Score": score, "Away team": away_team})
df.to_csv("matches table.csv", index=False)

web.quit()


