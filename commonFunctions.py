__author__ = 'IEUser'

def open_home_page(wd):
    wd.get("http://localhost:8080/addressbook/")


def login(wd, username, password):
    wd.find_element_by_name("user").click()
    wd.find_element_by_name("user").clear()
    wd.find_element_by_name("user").send_keys(username)
    wd.find_element_by_name("pass").click()
    wd.find_element_by_name("pass").clear()
    wd.find_element_by_name("pass").send_keys(password)
    wd.find_element_by_css_selector("input[type=\"submit\"]").click()


def logout(wd):
    wd.find_element_by_link_text("Logout").click()