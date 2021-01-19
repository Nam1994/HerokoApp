from selenium.webdriver.common.by import By

class ProductsPageLocators(object):

    def CLICK_IMG_ERROR(index):
        x = "//div[@class = 'inventory_list']//div[@class = 'inventory_item']["
        z = "]/div[@class = 'inventory_item_img']"
        # print("abc" + str(index))
        # print(x + str(index) + z)
        return (By.XPATH, (x + str(index) + z))
