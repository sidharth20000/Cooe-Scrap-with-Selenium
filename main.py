import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix , classification_report
import numpy as np
import seaborn as sns 
import warnings
warnings.filterwarnings("ignore")
%matplotlib inline


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://cooe.in/#/login")
driver.maximize_window()
time.sleep(2)


# Find the login elements
username_input = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/main/div/div/form/div[1]/div/div[1]/div[2]/input')
password_input = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/main/div/div/form/div[2]/div/div[1]/div[2]/input')

# # Provide login credentials
username_input.send_keys('81XXXXXXXXX')
password_input.send_keys('password')

time.sleep(15)

# Submit the login form
submit_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/main/div/div/form/div[3]/button/div')
submit_button.click()

time.sleep(2)
submit_butto = driver.find_element(By.XPATH, '//*[@id="app"]/div[6]/div/div/div/a[2]')
submit_butto.click()


l = []
x = 0
while x!= 50: 
    try:
        time.sleep(1)
        Prity= driver.find_elements(By.TAG_NAME, 'tbody')
        for i in Prity:
            v = i.find_elements(By.CLASS_NAME, "text-xs-center")
            for j in v:
                 l.append(bs(j.get_attribute("outerHTML")))

        time.sleep(1)
        next_ = driver.find_elements(By.TAG_NAME, 'button')
        next_[30].click()
        x +=1
    except:
        print(f"Something goes wrong at this iteration {x}")

date = []
pric = []
number = []
rgb = []
for i in l:
    try:
        if len(i.text.strip()) == 11:
            date.append(i.text.strip())
        elif len(i.text.strip()) == 6:
            pric.append(i.text.strip())
        elif len(i.text.strip()) == 1:
            number.append(i.text.strip())
        else:
            rgb.append(i.find("div", class_="point").get("style").split(":")[1].split(";")[0].strip())
    except:
        pass


dic = {"Date_Period" : date,
      "Price":pric,
      "Number": number,
      "Color": rgb}

Parity = pd.DataFrame(dic)

Parity.drop_duplicates(inplace=True)

Parity["Color"] = Parity.Color.map({"rgb(0, 230, 118)": "Green", "rgb(255, 23, 68)":"Red"})

Parity["Period"] = Parity.Date_Period.map(lambda x: int(x[8:]))
Parity["Price"] = Parity.Price.astype(int)
Parity["Number"] = Parity.Number.astype(int)

Parity.to_csv("Parity.csv", index=False)

plt.figure(figsize=(10, 29))
sns.countplot(data=Parity, y = "Price", hue="Color")


Parity = pd.read_csv("Parity.csv")
X_test = Parity["Date_Period"]
y_test = Parity["Color"].map({"Green":1, "Red":0})
df = Parity[["Date_Period", "Color"]]
X = df["Date_Period"].astype(float)
y = df["Color"].map({"Green":1, "Red":0})
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X =np.array(X_train).reshape(-1,1)
rf = RandomForestClassifier(max_depth=5,max_leaf_nodes=10 )
rf.fit(X, y_train)
x= np.array(X_test).reshape(-1,1)
p = rf.predict(x)
print(confusion_matrix(y_test, p))
"""[[233  33]
 [199  35]]"""
