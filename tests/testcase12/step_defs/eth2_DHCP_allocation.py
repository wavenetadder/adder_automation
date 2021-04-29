from pytest_bdd import scenario, given, when, then, scenarios, parsers
import allure

from Pagelocators.adder import *
from tests.testcase1.step_defs.WebDeiverFactory import *

scenarios('../features/eth2_DHCP_allocation.feature')
# scenarios('D:\pythonProject\adderCode1\tests\testcase12\features\eth2_DHCP_allocation.feature')


@given("user is in aim login page or not")
def user_is_in_aim_login_page_or_not():
    driver.implicitly_wait(30)
    expected_login_screen = 'AdderLink Infinity Management Suite'
    actual_login_screen = driver.find_element_by_xpath('//*[@id="admin_logo_left"]').text
    # import pdb; pdb.set_trace()
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
    time.sleep(2)

@then("user verify setting option")
def user_verify_setting_option():

    expected = 'Settings'

    actual = driver.find_element_by_xpath('//*[@id="dashboard_links"]/ul/li[2]/a').text

    if expected == actual:
        print("setting display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("setting is not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@then("user click on setting option and verify setting page is open or not")
def user_click_on_setting_option_and_verify_setting_page_is_open_or_not():

    driver.find_element_by_xpath('//*[@id="dashboard_links"]/ul/li[2]/a').click()
    print("clicked on setting")
    time.sleep(2)
    try:
        assert "setting" in driver.current_url
    finally:
        if (AssertionError):
            allure.attach(driver.get_screenshot_as_png(), name="Invalid Credential",
                          attachment_type=allure.attachment_type.PNG)

@then("user verify network option")
def user_verify_network_option():

    expected = 'Network'

    actual = driver.find_element_by_xpath('//*[@id="tabs"]/li[5]/a').text

    if expected == actual:
        print("network display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("network is not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@then("user click on network option")
def user_click_on_network_option():
    driver.find_element_by_xpath('//*[@id="tabs"]/li[5]/a').click()
    print("clicked on network option")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,400)")


@then("user click on DHCP checkbox")
def user_click_on_DHCP_checkbox():
    driver.find_element_by_xpath('//*[@id="eth1_enabled_1"]').click()
    driver.execute_script("window.scrollTo(0,1000)")


@then("user verify the save button")
def user_verify_the_save_button():
    expected = "Save"

    actual = driver.find_element_by_xpath('//*[@id="save_button"]').text

    if expected == actual:
        print("save display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("save is not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@then("user save the details")
def user_save_the_details():
    driver.find_element_by_xpath('//*[@id="save_button"]').click()
    time.sleep(2)


@then("user verify save done or not")
def user_verify_save_done_or_not():

    expected_message = "Settings updated"

    actual_message = driver.find_element_by_xpath("//span[@class='message_box mb_green error_message']").text
    if expected_message == actual_message:
        print("save message is display properly")
        print("text is :", actual_message)

        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
        time.sleep(65)
        driver.refresh()
    else:
        print("save message is  not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@then("user get the ip genrate by DHCP")
def user_get_the_ip_genrate_by_DHCP():
    ip = driver.find_element_by_xpath('//*[@id="eth1_dhcp_div"]/div[2]/div[2]').text
    print(ip)
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)
