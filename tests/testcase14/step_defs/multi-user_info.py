from pytest_bdd import scenario, given, when, then, scenarios, parsers
import allure
from selenium.webdriver.support.select import Select

from Pagelocators.adder import *
from tests.testcase1.step_defs.WebDeiverFactory import *

scenarios('../features/muti-user_info.feature')
# scenarios('D:\pythonProject\adderCode1\tests\testcase14\features\muti-user_info.feature')


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

@then("user verify receiver heading")
def user_verify_the_receiver_heading():

    expected ="Receivers"

    actual = driver.find_element_by_xpath('//*[@id="tabs"]/li[3]/a').text
    if expected == actual:
        print("receiver option display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("receiver option not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@then("user click on receiver")
def user_click_on_receiver():
    driver.find_element_by_xpath('//*[@id="tabs"]/li[3]/a').click()
    print("clicked on receiver")
    time.sleep(5)


@then("user click the checkbox show multi user information yes")
def user_click_the_checkbox_show_multi_user_information_yes():
    driver.find_element_by_xpath('//*[@id="show_multi_user_info_1"]').click()
    print("click done on the checkbox show multi user information yes")
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,800)")

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

    else:
        print("save message is  not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@then("user click the checkbox show multi user information no")
def user_click_the_checkbox_show_multi_user_information_no():
    driver.find_element_by_xpath('//*[@id="login_required_0"]').click()
    print("click done on the checkbox show multi user information no")
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)
    driver.execute_script("window.scrollTo(0,800)")
    time.sleep(3)