
from selenium import webdriver
from selenium.webdriver.common.by import By
from env import key,encrypted_password
from cryptography.fernet import Fernet
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def decrypt_password(key, encrypted_password):
    # Generate a Fernet key from the given key
    fernet_key = Fernet(key)

    # Decrypt the encrypted password using the Fernet key
    decrypted_password = fernet_key.decrypt(encrypted_password).decode()
    
    # Return the decrypted password
    return decrypted_password

# Set the path of the GeckoDriver (Firefox driver) executable
driver_path = 'geckodriver.exe'
firefox_options = webdriver.FirefoxOptions()
firefox_options.binary_location = 'C://path//to//firefox.exe'
# Create a new instance of the Firefox driver with the specified executable path
driver = webdriver.Firefox(firefox_options)

url = 'https://10.155.225.13'
driver.get(url)

username_field = driver.find_element(By.XPATH,"//*[@id='user']")
username_field.send_keys('admin')

password = decrypt_password(key,encrypted_password)
password_field = driver.find_element(By.XPATH,"//*[@id='passwd']")
password_field.send_keys(password)
print("Credentials input done")
wait = WebDriverWait(driver, 10000) 
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='submit']")))
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']")))
button = driver.find_element(By.XPATH, "//*[@id='submit']")
button.click()
print("logged in")


# wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='ext-gen400']")))
# button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ext-gen400']")))
# button.click()

# monitor=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ext-gen343']")))
# monitor.click()
# print("Loading...")
# element=wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='ext-comp-1312']")))
# element = wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@id='ext-comp-1312']")))
# export_to_csv=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ext-gen490']")))
# export_to_csv.click()
# print("Exporting to csv....");
# wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[26]/div[2]/div[1]/div/div/div/div/div[2]/span/a")))
# download=wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[26]/div[2]/div[1]/div/div/div/div/div[2]/span/a")))
# download.click()
# print("Download started")