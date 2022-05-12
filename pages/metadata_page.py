import time

from common.base_page import BasePage
from selenium.webdriver.common.by import By


class MetaDataPage(BasePage):
    """metadata页面"""
    # refresh按钮
    refresh_locator = (By.XPATH, "//i[contains(text(),'refresh')]")
    # refresh返回
    refresh_msg_locator = (By.XPATH, "//body/div[@id='__next']/div[2]/div[1]/div[1]")

    def click_refresh(self):
        """点击refresh"""
        refresh_button = self.wait_presence_element(self.refresh_locator)
        refresh_button.click()

    def get_refresh_msg(self):
        """获取refresh返回"""
        e = self.wait_visible_element(self.refresh_msg_locator)
        print('your program has detected the text “We’ve queued…” ')
        return e.text

