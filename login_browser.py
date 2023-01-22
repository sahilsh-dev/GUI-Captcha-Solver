from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementNotInteractableException
import pytesseract
from PIL import Image, ImageFilter, ImageGrab
import time


class LoginBrowser:

    def __init__(self, uid, pswd):
        self.cuims_id = uid
        self.cuims_pswd = pswd

    def solve_captcha(self):
        box_area = (689, 539, 745, 561)  # Keep X diff - 56, Y diff - 22
        image = ImageGrab.grab(box_area)
        image.save('captcha.png')
        image = Image.open('captcha.png')
        image = image.convert('L')
        image = image.filter(ImageFilter.SMOOTH)
        image = image.filter(ImageFilter.SHARPEN)

        text = (pytesseract.image_to_string(image)).strip()
        if len(text) > 4:
            text = text[:4]
        elif len(text) == 0:
            text = "SET AREA FIRST"
        print("Captcha Text >", text, "<")
        return text

    def login_cuims(self):
        driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
        driver.maximize_window()
        driver.get("https://uims.cuchd.in/UIMS/Login.aspx")

        fill_id = driver.find_element("name", "txtUserId")
        fill_id.send_keys(self.cuims_id)
        submit_btn = driver.find_element("name", "btnNext")
        submit_btn.click()
        enter_pswd = driver.find_element("name", "txtLoginPassword")
        enter_pswd.send_keys(self.cuims_pswd)

        captcha_value = self.solve_captcha()
        captcha = driver.find_element("name", "txtcaptcha")
        captcha.send_keys(captcha_value)

        submit_captcha = driver.find_element("name", "btnLogin")
        submit_captcha.click()
        time.sleep(2)

        try:
            ok_btn = driver.find_element("class name", "confirm")
            ok_btn.click()
        except ElementNotInteractableException:
            print("No Captcha Errors, Continue...")
        else:
            enter_pswd = driver.find_element("name", "txtLoginPassword")
            enter_pswd.send_keys(self.cuims_pswd)

            captcha_value = self.solve_captcha()
            captcha = driver.find_element("name", "txtcaptcha")
            captcha.clear()
            captcha.send_keys(captcha_value)
            submit_captcha = driver.find_element("name", "btnLogin")
            submit_captcha.click()
