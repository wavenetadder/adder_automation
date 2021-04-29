from pytest_bdd import scenario, given, when, then, scenarios, parsers
import allure
from selenium.webdriver.support.select import Select

from Pagelocators.adder import *
from Pagelocators.channel_create import *
from tests.testcase1.step_defs.WebDeiverFactory import *

scenarios('../features/RDP_Tx_creation.feature')
# scenarios('D:\pythonProject\adderCode1\tests\testcase8\features\RDO_Tx_creation.feature')


@given("user is in aim login page or not")
def user_is_in_aim_login_page_or_not():
    driver.implicitly_wait(30)
    expected_login_screen = 'AdderLink Infinity Management Suite'
    actual_login_screen = driver.find_element_by_xpath('//*[@id="admin_logo_left"]').text

    if expected_login_screen == actual_login_screen:
        print("user is in aim login page")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("user is not is aim login page")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@given(parsers.parse('user enter the username "{user_id}"'))
def user_should_enter_username(user_id):
    email = driver.find_element_by_xpath(username).clear()
    email = driver.find_element_by_xpath(username).send_keys(user_id)

@given(parsers.parse('user enter the password "{user_password}"'))
def user_should_enter_username(user_password):
    password = driver.find_element_by_xpath(Upassword).clear()
    password = driver.find_element_by_xpath(Upassword).send_keys(user_password)

@then("user click on login button")
def user_click_on_login_button():
    driver.find_element_by_xpath(login_button).click()
    time.sleep(2)
    # assert "admin" in driver.current_url

@then("user verify the login done or not")
def user_verify_the_login_done_or_not():
    expected = 'Logout'

    actual = driver.find_element_by_xpath(login_verify).text

    if expected == actual:

        print("user is login sucessfully")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

    else:
        print("user is not login sucessfully")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False


@then("user verify transmitter heading")
def user_verify_channel_heading():
    expected = 'TRANSMITTERS'

    actual = driver.find_element_by_xpath(transmeter).text

    if expected == actual:
        print("transmitter display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("transmitter not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False


@then("user click on transmitter and verify the transmitter page is open or not")
def user_click_on_transmitter_and_verify_the_transmitter_page_is_open_or_not():
    driver.find_element_by_xpath(transmeter).click()
    print("clicked on transmitter")
    time.sleep(2)
    try:
        assert "t=tx" in driver.current_url
    finally:
        if (AssertionError):
            allure.attach(driver.get_screenshot_as_png(), name="Invalid Credential",
                          attachment_type=allure.attachment_type.PNG)


@then("user verify Add VDI option")
def user_verify_Add_VDI_option():
    expected = 'Add VDI'

    actual = driver.find_element_by_xpath('//*[@id="transmitters_links"]/ul/li[2]/a').text

    if expected == actual:
        print("Add VDI is display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("Add VDI is not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@then("user click on Add VDI option")
def user_click_on_Add_VDI_option():
    driver.find_element_by_xpath('//*[@id="transmitters_links"]/ul/li[2]/a').click()
    time.sleep(2)

@then(parsers.parse('user enter RDP name "{rdp_name}"'))
def user_enter_NMS_address(rdp_name):
    driver.find_element_by_xpath('//*[@id="r_name"]').clear()
    driver.find_element_by_xpath('//*[@id="r_name"]').send_keys(rdp_name)
    time.sleep(2)

@then(parsers.parse('user enter ip address and DNS name "{dns_name}"'))
def user_enter_ip_address_and_DNS_name(dns_name):
    driver.find_element_by_xpath('//*[@id="r_ip"]').clear()
    driver.find_element_by_xpath('//*[@id="r_ip"]').send_keys(dns_name)
    time.sleep(2)

@then(parsers.parse('user enter port number "{port_no}"'))
def user_enter_port_number(port_no):
    driver.find_element_by_xpath('//*[@id="r_port"]').clear()
    driver.find_element_by_xpath('//*[@id="r_port"]').send_keys(port_no)
    time.sleep(2)

@then(parsers.parse('user enter domain name "{domain_name}"'))
def user_enter_domain_name(domain_name):
    driver.find_element_by_xpath('//*[@id="r_domain"]').clear()
    driver.find_element_by_xpath('//*[@id="r_domain"]').send_keys(domain_name)

@then("user select maximum resolution")
def user_select_maximum_resolution():
    resolution = Select(driver.find_element_by_xpath('//*[@id="r_resolution"]'))
    resolution.select_by_visible_text('USE GLOBAL SETTINGS')

@then("user verify the save button")
def user_verify_the_save_button():
    expected = "Save"

    actual = driver.find_element_by_xpath('//*[@id="save_button"]').text

    if expected == actual:
        print("save display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(2)

    else:
        print("save is not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@then("user save the details")
def user_save_the_details_and_land_to_transmitter():
    driver.find_element_by_xpath('//*[@id="save_button"]').click()
    print("click on save button")

@then("user verify same RDP already reated or not")
def user_verify_same_RDP_already_reated_or_not():
    expected = "RDP Name already in use"

    actual = driver.find_element_by_id('configure_channel_ajax_message').text
    if expected == actual:
        print("RDP name already in use")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

    else:
        print("RDP is created")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)


@then("user delete the rdp which is created")
def user_delete_the_rdp_which_is_created():
    driver.find_element_by_xpath("//tr[starts-with(@class, 'odd')]/td[11]/a/img").click()
    print("click on rdp delete option")
    time.sleep(1)

@then("user verify delete option come or not")
def user_verify_delete_option_come_or_not():
    expected = "Delete"

    actual = driver.find_element_by_xpath('//*[@id="delete_device_confirm_link"]').text

    if expected == actual:
        print("delete option is display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("delete option is not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@then("user click on delete option")
def user_click_on_delete_option():
    driver.find_element_by_xpath('//*[@id="delete_device_confirm_link"]').click()
    print("click on final delete")
    time.sleep(1)
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)

@then("user verify dashboard heading")
def user_verify_channel_heading():
    expected = 'DASHBOARD'

    actual = driver.find_element_by_xpath(dashboard).text

    if expected == actual:
        print("dashboard display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("dashboard not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False


@then("user click on dashboard")
def user_click_on_dashboard():
    driver.find_element_by_xpath(dashboard).click()
    print("clicked on dashboard")
    time.sleep(5)
