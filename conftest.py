__author__ = 'IEUser'
import pytest
from fixture.application import Application

@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    def cleanup():
            fixture.destroy()
    # using request.addfinalizer(fixture.destroy()) causes method destroy()
    # to be invoked right in the set up, so additional function cleanup() was added to avoid that
    request.addfinalizer(cleanup)
    return fixture