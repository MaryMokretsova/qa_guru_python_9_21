import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.title('Test search on Samsung Galaxy S23')
def test_search_android(mobile_management_android):
    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Appium')
    with allure.step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


@allure.title('Test open on Samsung Galaxy S23')
def test_open_article(mobile_management_android):
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Home')
    results = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
    results.first.should(have.text('Home'))
    results.first.click()
