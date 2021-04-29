from pytest_bdd import scenario, given, when, then, scenarios, parsers
import allure
from selenium.webdriver.support.select import Select

from Pagelocators.adder import *
from Pagelocators.channel_create import *
from tests.testcase1.step_defs.WebDeiverFactory import *

scenarios('../features/AddUser.feature')
# scenarios('D:\pythonProject\adderCode1\tests\testcase3\features\AddUser.feature')



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


@then("user verify user heading")
def user_verify_channel_heading():

    expected = 'USERS'

    actual = driver.find_element_by_xpath(user).text

    if expected == actual:
        print("user is display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("user is not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False


@then("user click on user and verify the user page is open or not")
def user_click_on_channel_and_verify_the_channel_page_is_open_or_not():
    driver.find_element_by_xpath(user).click()
    print("clicked on user")
    time.sleep(2)
    try:
        assert "users" in driver.current_url
    finally:
        if (AssertionError):
            allure.attach(driver.get_screenshot_as_png(), name="Invalid Credential",
                          attachment_type=allure.attachment_type.PNG)

@then("user verify add user button")
def user_verify_add_user_button():
    expected = "Add User"

    # actual = driver.find_element_by_xpath('//*[@id="admin_body"]/div[1]/a').text
    actual = driver.find_element_by_link_text('Add User').text
    # import pdb; pdb.set_trace()
    if expected == actual:
        print("add user button is display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)

    else:
        print("add user button is not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)
        assert False

@then("user click on add user button")
def user_click_on_add_user_button():
    driver.find_element_by_link_text('Add User').click()
    # driver.find_element_by_xpath('//*[@id="admin_body"]/div[1]/a').click()
    time.sleep(2)

@then(parsers.parse('user add username "{user_name}"'))
def user_should_enter_username(user_name):
    username = driver.find_element_by_xpath('//*[@id="u_username"]').click()
    username = driver.find_element_by_xpath('//*[@id="u_username"]').send_keys(user_name)
    time.sleep(3)

@then(parsers.parse('user add first name "{first_name}"'))
def user_should_enter_username(first_name):
    firstname = driver.find_element_by_xpath('//*[@id="u_firstname"]').click()
    firstname = driver.find_element_by_xpath('//*[@id="u_firstname"]').send_keys(first_name)
    time.sleep(3)

@then(parsers.parse('user add last name "{last_name}"'))
def user_should_enter_username(last_name):
    lastname = driver.find_element_by_xpath('//*[@id="u_lastname"]').click()
    lastname = driver.find_element_by_xpath('//*[@id="u_lastname"]').send_keys(last_name)
    time.sleep(3)

@then(parsers.parse('user add email "{e_mail}"'))
def user_should_enter_username(e_mail):
    email = driver.find_element_by_xpath('//*[@id="u_email"]').click()
    email = driver.find_element_by_xpath('//*[@id="u_email"]').send_keys(e_mail)
    time.sleep(3)

@then('user click on checkbox required password no')
def user_click_on_checkbox_required_password_no():
    driver.find_element_by_xpath('//*[@id="password_mode_none"]').click()
    time.sleep(3)

@then("user click on checkbox aim admin required yes")
def user_click_on_checkbox_aim_admin_required_yes():
    driver.find_element_by_xpath('//*[@id="u_admin_1"]').click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,500)")

@then("user give permission of user group not a member of to member of")
def user_give_permission_of_user_group_not_a_member_of_to_member_of():
    driver.find_element_by_xpath('//*[@id="add_all_user_groups"]/img').click()
    time.sleep(3)

@then("user give permission of channel permission not set to permitted")
def user_give_permission_of_channel_permission_not_set_to_permitted():
    driver.find_element_by_xpath('//*[@id="add_all_channels"]/img').click()
    time.sleep(3)

@then("user give permission channel group permission not set to permitted")
def user_give_permission_channel_group_permissin_not_set_to_permitted():
    driver.find_element_by_xpath('//*[@id="add_all_channel_groups"]/img').click()
    time.sleep(3)

@then("user verify the save button")
def user_verify_the_save_button():
    expected = "Save"

    actual = driver.find_element_by_xpath('//*[@id="save_button"]').text

    if expected == actual:
        print("add channel display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("add channel is not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@then("user click on save button")
def user_save_the_details():
    driver.find_element_by_xpath('//*[@id="save_button"]').click()
    time.sleep(5)

@then("user verify same user is created or not")
def user_verify_same_channel_is_created_or_not():
    expected = "A User with that username already exists"

    actual = driver.find_element_by_xpath('//*[@id="configure_user_ajax_message"]').text
    if expected == actual:
        print("A channel with that name already exists")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

        driver.execute_script("window.scrollTo(500,0)")
        assert False

    else:
        print("user is created")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        driver.execute_script("window.scrollTo(500,0)")

    # import pdb; pdb.set_trace()
    # if expected != actual:
    #     assert True
    #     print("user is created")
    #
    #     allure.attach(driver.get_screenshot_as_png(), name='screenshot',
    #                       attachment_type=allure.attachment_type.PNG)
    #     # driver.execute_script("window.scrollTo(500,0)")
    #
    # else:
    #     # print("A channel with that name already exists")
    #     # assert True
    #     print("A User with that username already existsd")
    #     allure.attach(driver.get_screenshot_as_png(), name='screenshot',
    #                       attachment_type=allure.attachment_type.PNG)
    #
    #     driver.execute_script("window.scrollTo(500,0)")
    #     assert False


@then("user click on logout")
def user_click_on_logout():
    driver.find_element_by_xpath('//*[@id="logout"]/a').click()


@then(parsers.parse('user enter the username after add user "{user_id}"'))
def user_should_enter_username(user_id):
    email = driver.find_element_by_xpath(username).clear()
    email = driver.find_element_by_xpath(username).send_keys(user_id)

@then("user verify the login done or not")
def user_verify_the_login_done_or_not():
    expected = 'Logout'

    actual = driver.find_element_by_xpath(login_verify).text

    if expected == actual:

        print("user is login sucessfully , user add sucessfully")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

    else:
        print("user is not login sucessfully , user add sucessfully")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

