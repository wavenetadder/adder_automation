from pytest_bdd import scenario, given, when, then, scenarios, parsers
import allure

from Pagelocators.adder import *
from Pagelocators.update_build import *
# from tests.testcase2.step_defs.WebDeiverFactory import *
from tests.testcase1.step_defs.WebDeiverFactory import *

scenarios('../features/update_build.feature')
# scenarios('D:\pythonProject\adderCode1\tests\testcase2\features\update_build.feature')


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
    time.sleep(5)


@then("user verify the update option")
def user_verify_the_update_option():

    expected ="Updates"

    actual = driver.find_element_by_xpath(update).text
    if expected == actual:
        print("update display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("update not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@then("user click on update option and verify the update page is open")
def user_click_on_update_option_and_verify_update_page():
    driver.find_element_by_xpath(update).click()
    try:
        assert "updates" in driver.current_url
    finally:
        if (AssertionError):
            allure.attach(driver.get_screenshot_as_png(), name="Invalid Credential",
                          attachment_type=allure.attachment_type.PNG)
            time.sleep(2)


@then(parsers.parse('select aim image "{b_image}"'))
def user_select_aim_image(b_image):
    driver.find_element_by_xpath('//*[@id="uploaded_aim_upgrade_file"]').send_keys(b_image)
    allure.attach(driver.get_screenshot_as_png(), name="Invalid Credential",
                       attachment_type=allure.attachment_type.PNG)
    time.sleep(2)


@then("user verify the upload button")
def user_verify_the_upload_button():
    expected = "Upload"

    actual = driver.find_element_by_xpath('//*[@id="admin_body"]/div[1]/span/a').text
    # import pdb; pdb.set_trace()
    if expected == actual:
        print("upload display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("upload not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@then("user click on upload button")
def user_click_on_upload_button():
    # driver.implicitly_wait(300)
    driver.find_element_by_xpath('//*[@id="admin_body"]/div[1]/span/a').click()
    time.sleep(2)
    driver.set_page_load_timeout(480)
    # driver.set_script_timeout(480)
    time.sleep(5)
    driver.refresh()
    print("click done on upload button")
    time.sleep(2)
    # driver.refresh()
    # print("upload is still showing")
    # allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
    # driver.set_page_load_timeout(430)
    # time.sleep(2)
    # time.sleep(430)


@then("user verify aim image is upload or not")
def user_verify_aim_image_is_upload_or_not():
    expected_message = "Upgrade completed successfully"

    actual_message = driver.find_element_by_xpath("//span[@class='message_box mb_green error_message']").text
    # import pdb; pdb.set_trace()
    if expected_message == actual_message:
        print("image upload message is display properly")
        print("text is :", actual_message)

        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',attachment_type=allure.attachment_type.PNG)

    else:
        print("image upload message is  not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                       attachment_type=allure.attachment_type.PNG)
        assert False

@then("user verify restart button")
def user_verify_restart_button():

    expected = 'Restart Now'
    # import pdb;
    # pdb.set_trace()
    actual = driver.find_element_by_xpath('//*[@id="admin_body"]/div[1]/a').text

    if expected == actual:
        print("restart button display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("restart button not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@then('user click on restart button and land on login page')
def user_click_on_restart_button_and_land_on_home_page():
    # driver.find_element_by_xpath('//*[@id="reset_selection"]/a[2]').click()
    # driver.find_element_by_link_text("Restart Now").click()
    driver.find_element_by_xpath('//*[@id="admin_body"]/div[1]/a').click()
    time.sleep(220)
    try:
        assert "login" in driver.current_url
    finally:
        if (AssertionError):
            allure.attach(driver.get_screenshot_as_png(), name="Invalid Credential",
                          attachment_type=allure.attachment_type.PNG)


@then("user verify the build number in update page")
def user_verify_the_build_number_in_update_page():

    expected = '4.12.10041 (last upgrade)'

    actual = driver.find_element_by_xpath(update_buildNo_verify).text
    if expected == actual:
        print("build number is display properly")
        print("update page build number is :", actual)
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        driver.execute_script("window.scrollTo(0,500)")

    else:
        print("build number is not display properly")
        print("update page build number is :", actual)
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        driver.execute_script("window.scrollTo(0,500)")
        assert False

@then("user verify the build number in bottom of page")
def user_verify_the_build_number_in_bottom_of_page():

    expected = 'Solo AIM v4.12.10041'

    actual = driver.find_element_by_xpath(update_buildNo_end).text
    real = actual[:-24]
    print(real)
    # import pdb; pdb.set_trace()
    if expected == real:
        print("bottom build number is display properly")
        print("bottom build number is :", actual)
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("bottom build number is not display properly")
        print("bottom build number is :", actual)
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False