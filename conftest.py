__author__ = 'IEUser'
import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    baseUrl = request.config.getoption("--baseUrl")

    if fixture is None:
        fixture = Application(browser=browser, baseUrl=baseUrl)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, baseUrl=baseUrl)
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    # using request.addfinalizer(fixture.destroy()) causes method destroy()
    # to be invoked right in the set up, so additional function fin() was added to avoid that
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost:8080/addressbook/")