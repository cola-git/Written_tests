import time

from common.base_page import BasePage
from selenium.webdriver.common.by import By


class CollectionPage(BasePage):
    """收藏页面"""
    # MetaMask定位
    meta_mask_locator = (By.XPATH, "//span[contains(text(),'MetaMask')]")
    # Wallet定位
    coinbase_wallet_locator = (By.XPATH, "//span[contains(text(),'Coinbase Wallet')]")
    # WalletConnect定位
    wallet_connect_locator = (By.XPATH, "//span[contains(text(),'WalletConnect')]")
    # Phantom定位
    phantom_locator = (By.XPATH, "//span[contains(text(),'Phantom')]")
    # Glow定位
    glow_locator = (By.XPATH, "//span[contains(text(),'Glow')]")
    # coinbase_wallet定位
    coinbase_wallet_into_locator = (By.XPATH, "//a[contains(text(),'Coinbase Wallet')]")
    # wallet_connect切换定位
    wallet_connect_switch_locator = (By.XPATH, "//a[contains(text(),'桌面')]")
    # wallet_connect关闭定位
    wallet_connect_close_locator = (By.XPATH, "//body/div[@id='walletconnect-wrapper']/div[@id='walletconnect-qrcode-modal']/div[1]/div[1]/div[1]")

    def into_meta_mask(self):
        """进入meta_mask"""
        into_meta_mask_button = self.window_switch(self.meta_mask_locator)

    def into_coinbase_wallet(self):
        """进入coinbase_wallet"""
        into_coinbase_wallet_button = self.wait_clickable_element(self.coinbase_wallet_locator)
        into_coinbase_wallet_button.click()
        into_coinbase_wallet = self.wait_clickable_element(self.coinbase_wallet_into_locator)
        into_coinbase_wallet.click()

    def into_wallet_connect(self):
        """进入wallet_connect"""
        into_wallet_connect_button = self.wait_clickable_element(self.wallet_connect_locator)
        into_wallet_connect_button.click()

    def into_phantom(self):
        """进入phantom"""
        into_phantom_button = self.window_switch(self.phantom_locator)

    def into_glow(self):
        """进入glow"""
        into_glow_button = self.window_switch(self.glow_locator)

    def close_wallet_connect(self):
        """关闭wallet_connect"""
        wallet_connect_button = self.wait_clickable_element(self.wallet_connect_switch_locator)
        wallet_connect_button.click()
        wallet_connect_close_button = self.wait_clickable_element(self.wallet_connect_close_locator)
        wallet_connect_close_button.click()
