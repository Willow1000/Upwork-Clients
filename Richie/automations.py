import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tkinter import messagebox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def run_automation(account,log_box,tk):
    # driver.get("https://accounts.google.com/")
    
    email = account['Email']
    password = account['Password']
    excel_file = account['File']

    # try:
    #     services = pd.read_excel(account['file'])["custom_services"].dropna().tolist()
    #     log_box.insert(tk.END,f"Loaded {len(services)} services.\n")
    # except Exception as e:
    #     print(f"Failed to load seervices: {e}")    
    #     log_box.insert(tk.END,f"Failed to load Excel: {e}\n")
    #     return
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    options.add_argument("user-data-dir =C:\\Users\\Willow\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    driver = webdriver.Chrome(options=options)
    driver.get("https://accounts.google.com/signin")  # Replace with the actual login URL

    try:
        wait = WebDriverWait(driver, 10)
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "identifier")))
        email_input.send_keys(email)
        emailNext_input = wait.until(EC.presence_of_element_located((By.NAME, "identifierNext")))
        emailNext_input.click()
        time.sleep(2)  # Wait for the password field to load

        driver.find_element(By.NAME, "password").send_keys(password).send_keys(password)
        driver.find_element(By.NAME,"passwordNext").click()
        time.sleep(5)  # Wait for the login to complete
    except Exception as e:
        print(f"Login failed: {e}")
        log_box.insert(tk.END, f"Login failed: {e}\n")
        driver.quit()
        return
    log_box.insert(tk.END, "Login successful.\n")    