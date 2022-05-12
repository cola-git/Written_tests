import pytest
import time
from pages.home_page import HomePage
from pages.metadata_page import MetaDataPage


class TestRefresh:
    """
    Click on top right button (red) refresh metadata
    Verify that “We queued the item for an update”
    Populate status with values
    """

    @pytest.mark.main
    def test_refresh_data_03(self, get_browser):
        browser = get_browser
        expected = "We've queued this item for an update!"
        HomePage(browser).login_page()
        HomePage(browser).join_item1()
        MetaDataPage(browser).click_refresh()
        time.sleep(1)
        success_msg = MetaDataPage(browser).get_refresh_msg()
        try:
            assert expected in success_msg
        except AssertionError as e:
            print("fail")
            raise e
