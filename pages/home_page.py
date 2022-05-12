import time

from common.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    """主页"""
    # item定位
    item1_locator = (By.XPATH,"//body/div[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]/div[5]/div[1]/article[1]/a[1]/div[1]/div[1]/div[1]/div[1]/div[2]")

    # account定位
    account_locator = (By.XPATH, "//i[contains(text(),'account_circle')]")

    # my_collections定位
    my_collections_locator = (By.XPATH, "//span[contains(text(),'My Collections')]")

    def login_page(self):
        """进入主页"""
        self.browser.get('https://opensea.io/collection/catalog-lu-store')
        time.sleep(2)

    def join_item1(self):
        """进入item"""
        join_item_project = self.wait_clickable_element(self.item1_locator)
        join_item_project.click()
        time.sleep(5)

    def move_account(self):
        """移动到我的"""
        move_to_account = self.hover(self.account_locator)
        time.sleep(2)

    def into_collections(self):
        """点击进入我的收藏"""
        into_my_collections = self.wait_presence_element(self.my_collections_locator)
        into_my_collections.click()
        print("your program has clicked on metadata")
        time.sleep(1)
