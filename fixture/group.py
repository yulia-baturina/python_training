__author__ = 'IEUser'

from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def is_groups_page_opened(self):
        wd = self.app.wd
        return wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0

    def return_to_groups_page(self):
        wd = self.app.wd
        if not self.is_groups_page_opened():
            wd.find_element_by_link_text("group page").click()

    def fill_in_fields(self, group):
        wd = self.app.wd
        if group.name:
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(group.name)
        if group.header:
            wd.find_element_by_name("group_header").click()
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(group.header)
        if group.footer:
            wd.find_element_by_name("group_footer").click()
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(group.footer)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill in group fields
        self.fill_in_fields(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache=None

    def open_groups_page(self):
        wd = self.app.wd
        if not self.is_groups_page_opened():
           wd.find_element_by_link_text("groups").click()

    def select_first_group(self):
        self.select_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        # select group by index
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache=None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        # select group by index
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache=None

    def modify_group_by_index(self, group, index):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        # fill in group fields
        self.fill_in_fields(group)
        # submit update
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache=None

    def modify_group_by_id(self, group, id):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.select_group_by_id(id)
        wd.find_element_by_name("edit").click()
        # fill in group fields
        self.fill_in_fields(group)
        # submit update
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache=None

    def edit_first_group(self, group):
        self.modify_group_by_index(group,0)

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache=None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)