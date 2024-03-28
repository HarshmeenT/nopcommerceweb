
##adding common/generic code in this file which will be used inmultiple cases
import pytest
from selenium import webdriver

@pytest.fixture
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    return driver

####Support for running on desired browser#####
# this will get the value from CLI hooks
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def browser(request):  # this will return the browser value to set up method CLI hooks
    return request.config.getoption("--browser")

######Pytest HTML Report###

#This is the hook for adding environment info to HTML reports
def pytest_configure(config):
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        from pytest_metadata.plugin import metadata_key
        config.stash[metadata_key]['Project Name'] = 'nop Commerce'
        config.stash[metadata_key]['Module Name'] = 'Customers'
        config.stash[metadata_key]['Tester'] = 'HT'

#This is the hook for adding environment info to HTML reports
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
        metadata.pop("JAVA_HOME", None)
        metadata.pop("Plugins", None)