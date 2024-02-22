import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


@allure.title('Test search on iPhone 12')
def test_search_ios(mobile_management_ios):
    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Button')).click()

    with allure.step('Input text hello!'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Input')).type('hello!' + '\n')

    with allure.step('Check output text'):
        text_output = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Output')).should(be.clickable)
        text_output.should(have.text('hello!'))
