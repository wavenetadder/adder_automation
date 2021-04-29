from pytest_bdd import scenario, given, when, then, scenarios, parsers
import allure
from selenium.webdriver.support.select import Select

from Pagelocators.adder import *
from tests.testcase1.step_defs.WebDeiverFactory import *

scenarios('../features/licence.feature')
# scenarios('D:\pythonProject\adderCode1\tests\testcase17\features\licence.feature')


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


@then("user verify setting heading")
def user_verify_the_setting_heading():

    expected ="Settings"

    actual = driver.find_element_by_xpath('//*[@id="dashboard_links"]/ul/li[2]/a').text
    if expected == actual:
        print("setting option display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("setting option not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@then("user click on setting option and verify the setting page is open")
def user_click_on_setting_option_and_verify_update_page():
    driver.find_element_by_xpath('//*[@id="dashboard_links"]/ul/li[2]/a').click()
    try:
        assert "settings" in driver.current_url
    finally:
        if (AssertionError):
            allure.attach(driver.get_screenshot_as_png(), name="Invalid Credential",
                          attachment_type=allure.attachment_type.PNG)
            time.sleep(2)

@then("user verify the general heading")
def user_verify_the_general_heading():

    expected ="General"

    actual = driver.find_element_by_xpath('//*[@id="tabs"]/li[1]/a').text
    if expected == actual:
        print("general option display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("general option not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@then("user click on general option")
def user_click_on_general_option():
    driver.find_element_by_xpath('//*[@id="tabs"]/li[1]/a').click()
    print("cicked on general setting")
    driver.execute_script("window.scrollTo(0,600)")

@then("user click on the upgarde licence link")
def user_click_on_the_upgarde_licence_link():
    driver.find_element_by_xpath('//*[@id="tab_content_general"]/div[18]/div[2]/a').click()
    print("cicked on upgrade licence link")

@given(parsers.parse('user enter the licence key "{key}"'))
def user_enter_the_licence_key(key):
    licence_key = driver.find_element_by_xpath('//*[@id="licence_key"]').clear()
    licence_key = driver.find_element_by_xpath('//*[@id="licence_key"]').send_keys(key)
    time.sleep(3)

@then("user verify the save button")
def user_verify_the_save_button():
    expected = "Save"

    actual = driver.find_element_by_xpath('//*[@id="admin_body"]/div/a[1]').text

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
    driver.find_element_by_xpath('//*[@id="admin_body"]/div/a[1]').click()
    time.sleep(2)


@then("user verify licence is valid or not")
def user_verify_licence_is_valid_or_not():
    expected = "Invalid licence key"

    actual = driver.find_element_by_id('upgrade_licence_ajax_message').text
    if expected == actual:
        print("Invalid licence key")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

        assert False

    else:
        print("valid licence Key")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
