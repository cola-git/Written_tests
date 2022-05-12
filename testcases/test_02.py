import pytest
import time
from pages.home_page import HomePage
from pages.collection_page import CollectionPage


class TestCollection:
    """Go into each item in the collection """

    @pytest.mark.main
    def test_into_collection_02(self, get_browser):
        browser = get_browser
        HomePage(browser).login_page()
        HomePage(browser).move_account()
        # 进入收藏into_phantom
        HomePage(browser).into_collections()
        time.sleep(1)
        # 进入收藏的MetaMask
        CollectionPage(browser).into_meta_mask()
        time.sleep(1)
        # 切回收藏
        CollectionPage(browser).window_switch_main()
        CollectionPage(browser).window_refresh()
        # 点击coinbase_wallet
        time.sleep(5)
        CollectionPage(browser).into_coinbase_wallet()
        time.sleep(2)
        # 返回收藏
        CollectionPage(browser).window_back()
        CollectionPage(browser).window_refresh()
        time.sleep(3)
        # 进入wallet_connect
        CollectionPage(browser).into_wallet_connect()
        time.sleep(2)
        CollectionPage(browser).close_wallet_connect()
        # 进入phantom
        CollectionPage(browser).into_phantom()
        time.sleep(3)
        # 切回收藏
        CollectionPage(browser).window_switch_main()
        CollectionPage(browser).window_refresh()
        # 进入glow
        CollectionPage(browser).into_glow()
        time.sleep(3)
        # 切回收藏
        CollectionPage(browser).window_switch_main()
        CollectionPage(browser).window_refresh()
        time.sleep(2)
