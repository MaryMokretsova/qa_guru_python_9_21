import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from selene import browser
import config


@pytest.fixture(scope='function')
def mobile_management_android():
    options = UiAutomator2Options().load_capabilities(
        {
            'platformVersion': config.settings.platformVersion,
            'deviceName': config.settings.deviceName,
            'app': config.settings.app,
            'bstack:options': {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                "userName": config.settings.USER_NAME,
                "accessKey": config.settings.ACCESS_KEY,
            },
        }
    )

    browser.config.timeout = config.settings.timeout

    browser.config.driver = webdriver.Remote(config.settings.remote_url, options=options)

    yield

    browser.quit()
