from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from env import key,encrypted_password
from cryptography.fernet import Fernet
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
import os

download_path = r"C:\Users\SOCHAT0\Desktop\Firewall Logs\Automation"  # Specify the download directory here
downloaded_file = os.path.join(download_path, "log.csv")  # Replace "filename.csv" with the actual name of the downloaded file

if os.path.exists(downloaded_file):
    os.remove(downloaded_file)  # Delete the file if it already exists


def decrypt_password(key, encrypted_password):
    # Generate a Fernet key from the given key
    fernet_key = Fernet(key)

    # Decrypt the encrypted password using the Fernet key
    decrypted_password = fernet_key.decrypt(encrypted_password).decode()
    
    # Return the decrypted password
    return decrypted_password


4

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

prefs = {"profile.default_content_settings.popups": 0,    
        "download.default_directory":r"C:\Users\SOCHAT0\Desktop\Firewall Logs\Automation", ### Set the path accordingly
        "download.prompt_for_download": False, ## change the downpath accordingly
        "download.directory_upgrade": True}

options.add_experimental_option("prefs", prefs)
driver = Chrome(service=Service("chromedriver.exe"), options=options)

driver.get("https://10.155.225.13/")
wait = WebDriverWait(driver, 10000)


# Proceeding Unsafe
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='details-button']")))
button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='details-button']")))
time.sleep(1)
button.click()
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='proceed-link']")))
button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='proceed-link']")))
time.sleep(1)
button.click()

# Inputing Credentials
username_field = driver.find_element(By.XPATH,"//*[@id='user']")
username_field.send_keys('admin')
password = decrypt_password(key,encrypted_password)
password_field = driver.find_element(By.XPATH,"//*[@id='passwd']")
password_field.send_keys(password)
print("Credentials input done")

wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='submit']")))
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']")))
button = driver.find_element(By.XPATH, "//*[@id='submit']")
time.sleep(1)
button.click()
print("logged in")

wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='ext-gen351']")))
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ext-gen351']")))
close = driver.find_element(By.XPATH, "//*[@id='ext-gen351']")
time.sleep(1)
close.click()
print("Pop-Up Closed")
time.sleep(1)

wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='monitor_img']")))
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='monitor_img']")))
monitor = driver.find_element(By.XPATH, "//*[@id='monitor_img']")
time.sleep(1)
monitor.click()
wait.until(EC.invisibility_of_element_located((By.XPATH, "//*[@id='ext-comp-1264']")))
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='ext-gen267']")))
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ext-gen267']")))
print("Logs Loaded")

cross=wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/table/tbody/tr/td[1]/table/tbody/tr/td[4]/table/tbody/tr[2]/td[2]/em/button")))
cross.click()
proceed=wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/table/tbody/tr/td[1]/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]/em/button")))
print("Logs Refreshed...")

wait.until(EC.invisibility_of_element_located((By.XPATH, "//*[@id='ext-comp-1264']")))
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='ext-gen267']")))
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ext-gen267']")))
print("Logs are ready to be exported")

export_to_csv=wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/table/tbody/tr/td[1]/table/tbody/tr/td[8]/table/tbody/tr[2]/td[2]/em/button")))
time.sleep(1)
export_to_csv.click()
print("Exporting...")

wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[25]/div[2]/div[1]/div/div/div/div/div[2]/span/a")))
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[25]/div[2]/div[1]/div/div/div/div/div[2]/span/a")))
download = driver.find_element(By.XPATH, "/html/body/div[25]/div[2]/div[1]/div/div/div/div/div[2]/span/a")
download.click()
print("Download Started....")

while not os.path.exists(downloaded_file):
    time.sleep(1)  # Wait for 1 second

print("Download is complete")
print("Creating Policy...")
driver.close()
import EngineCode
EngineCode.f()
print("Policies Created")