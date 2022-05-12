import os
import time

import pytest
from pages.home_page import HomePage
from common.operate_excel import OperateExcel
from common.handle_path import DATADIR
from selenium.webdriver.common.by import By

case_file = os.path.join(DATADIR, "excel.xlsx")


class TestTable:
    excel = OperateExcel(case_file, "Sheet1")
    """
     Create a table for all unique 2.1k items. Fill in the values in blue
    """

    @pytest.mark.main
    def test_table_01(self, get_browser):
        browser = get_browser
        HomePage(browser).login_page()
        for i in range(1, 9):
            i = str(i)
            item_locator = (By.XPATH,
                            "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]/div[" + i + "]/div[1]/article[1]/a[1]")
            HomePage(browser).window_slide()
            time.sleep(1)
            b = HomePage(browser).wait_visible_element(item_locator)
            url = b.get_attribute('href')
            print(url)
            i = int(i)
            self.excel.write_data(row=i + 1, column=1, value=i)
            self.excel.write_data(row=i + 1, column=2, value=url)
            self.excel.write_data(row=i + 1, column=3, value="status")
