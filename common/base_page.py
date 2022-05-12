from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.support.select import Select

from common.handle_log import log
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

"""
存储页面通用行为
"""


class BasePage:
    def __init__(self, browser: Chrome):
        self.browser = browser

    def get_element(self, locator):
        """查找元素"""
        try:
            e = self.browser.find_element(*locator)
            return e
        except NoSuchElementException as e:
            log.error("查找元素失败")

    def wait_clickable_element(self, locator, timeout=30, poll=0.2):
        """等待元素可以被点击"""
        try:
            e = WebDriverWait(self.browser, timeout, poll).until(EC.element_to_be_clickable(locator))
            return e
        except TimeoutException as e:
            log.error("查找元素失败")

    def wait_presence_element(self, locator, timeout=30, poll=0.2):
        """等待元素出现"""
        try:
            e = WebDriverWait(self.browser, timeout, poll).until(EC.presence_of_element_located(locator))
            return e
        except TimeoutException as e:
            log.error("查找元素失败")

    def wait_visible_element(self, locator, timeout=30, poll=0.2):
        """等待元素可见"""
        try:
            e = WebDriverWait(self.browser, timeout, poll).until(EC.visibility_of_element_located(locator))
            return e
        except TimeoutException as e:
            log.error("查找元素失败")

    def click(self, locator):
        """点击"""
        e = self.wait_clickable_element(locator)
        e.click()

    def hover(self, locator):
        """鼠标悬停"""
        e = self.wait_visible_element(locator)
        action = ActionChains(self.browser)
        action.move_to_element(e)
        action.perform()

    def window_switch(self, locator):
        """新窗口切换"""
        wait = WebDriverWait(self.browser, timeout=30, poll_frequency=0.1)
        windows = self.browser.window_handles
        element = wait.until(EC.element_to_be_clickable(locator))
        element.click()
        wait.until(EC.new_window_is_opened(windows))
        self.browser.switch_to.window(self.browser.window_handles[-1])

    def window_down(self):
        """窗口滑动到底部"""
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def window_slide(self):
        """窗口滑动500像素"""
        self.browser.execute_script("window.scrollBy(0,500)")

    def window_close(self):
        """窗口关闭"""
        self.browser.close()

    def window_refresh(self):
        """窗口刷新"""
        self.browser.refresh()

    def window_switch_main(self):
        """切换到主窗口"""
        windows = self.browser.window_handles
        self.browser.switch_to.window(self.browser.window_handles[0])

    def window_back(self):
        """页面返回"""
        self.browser.back()
