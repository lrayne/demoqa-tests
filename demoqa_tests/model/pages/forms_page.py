from selene import browser
from demoqa_tests.model.components.panel import Panel


class FormsPage:
    def __init__(self):
        self.panel = Panel()

    def open(self):
        browser.open('/forms')
        return self
