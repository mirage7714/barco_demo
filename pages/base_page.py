class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
