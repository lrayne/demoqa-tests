from selene import browser


def hide(element: str):
    browser.driver.execute_script(
        f'''document.querySelector('{element}').style.display = 'none';'''
    )
