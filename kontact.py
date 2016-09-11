# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import time, unittest
from kon import Kontact
def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class kontact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_kontact(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/delete.php?part=12;13;")
        self.login(wd, username="admin", password="secret")
        self.fill_contact(wd, Kontact(First_name="Alexey", last_name="Kozlov", nick="lolo", title="PM", organization="BHCC", address="250 Boston", cell="8574173906",
                          email="alexey.kozlov@bhcc.mass.edu", birth="1988"))
        self.logout(wd)


    def test_2_kontact(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/delete.php?part=12;13;")
        self.login(wd, username="admin", password="secret")
        self.fill_contact(wd, Kontact(First_name="", last_name="", nick="", title="", organization="", address="", cell="",
                          email="", birth=""))
        self.logout(wd)



    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def fill_contact(self, wd, kon):
        # create contact
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(kon.First_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(kon.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(kon.nick)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(kon.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(kon.organization)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(kon.address)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(kon.cell)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(kon.email)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[32]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[32]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[4]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(kon.birth)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self, wd, username, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
