from imessage_reader import fetch_data
import re
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as uc

class Actions:
    def __init__(self, db_path, phone_number):
        self.fd = fetch_data.FetchData(db_path)
        self.phone_number = phone_number
        self.last_msg = self._fetch_msg()
        self.website_regex = "((https?|ftp|smtp):\/\/)?(www.)?[a-z0-9]+(\.[a-z]{2,}){1,3}(#?\/?[a-zA-Z0-9#]+)*\/?(\?[a-zA-Z0-9-_]+=[a-zA-Z0-9-%]+&?)?"

    def fetch_data(self):
        data = [msg for msg in self.fd.get_messages() if self.phone_number == msg[0]]
        return data
    
    def _fetch_msg(self):
        data = self.fetch_data()
        # returns the most recent msg, data array is already sorted
        return data[-1]
    
    def _parse_url(self, text):
        url = re.search(self.website_regex, text)
        if url:
            return url.group(0)
        print("URL not found")
        return None
    
    def task_macro(self):
        curr_msg = self._fetch_msg()
        print(curr_msg)
        if curr_msg == self.last_msg:
            return
        url = self._parse_url(curr_msg[1])
        print(url)
        if url:
            self._accept_task(url)
        self.last_msg = curr_msg

    def _accept_task(self, url):
        driver = uc.Chrome()
        driver.get(url)
        print(driver.title)
        time.sleep(5)
        driver.close()
    