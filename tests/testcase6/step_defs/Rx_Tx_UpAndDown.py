from pytest_bdd import scenario, given, when, then, scenarios, parsers
import allure

from Pagelocators.adder import *
from Pagelocators.update_build import *
# from tests.testcase2.step_defs.WebDeiverFactory import *
from tests.testcase1.step_defs.WebDeiverFactory import *

scenarios('../features/Rx_Tx_UpAndDown.feature')
# scenarios('D:\pythonProject\adderCode1\tests\testcase6\features\Rx_Tx_UpAndDown.feature')


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
    # try:
    #     assert "updates" in driver.current_url
    # finally:
    #     if (AssertionError):
    #         allure.attach(driver.get_screenshot_as_png(), name="Invalid Credential",
    #                       attachment_type=allure.attachment_type.PNG)
            # driver.execute_script("window.scrollTo(0,500)")
    print("try")

@then(parsers.parse('user select aim image "{u_d_image}"'))
def user_select_aim_image(u_d_image):
    driver.find_element_by_xpath('//*[@id="uploaded_firmware_file"]').send_keys(u_d_image)
    allure.attach(driver.get_screenshot_as_png(), name="Invalid Credential",
                  attachment_type=allure.attachment_type.PNG)
    time.sleep(2)

# @then("user select aim image")
# def user_select_aim_image():
#     driver.find_element_by_xpath('//*[@id="uploaded_firmware_file"]').send_keys("C:\\Users\\Pankaj\\Desktop\\AIM build\\rx_tx\\upgrade_dvix2_backup_adder.bin.txs.5.0.46844")
#     time.sleep(2)

@then("user verify the upload button")
def user_verify_the_upload_button():
    expected = "Upload"

    actual = driver.find_element_by_xpath('//*[@id="admin_body"]/div[4]/a').text
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
    driver.find_element_by_xpath('//*[@id="admin_body"]/div[4]/a').click()
    time.sleep(2)

@then("user verify upgrade selected transmitter is shown or not")
def user_verify_upgrade_selected_transmitter_is_shown_or_not():
    expected = "Upgrade Selected Transmitters"

    actual = driver.find_element_by_xpath('//*[@id="admin_body"]/div[1]/a').text
    # import pdb; pdb.set_trace()
    if expected == actual:
        print("upgrade selected transmitter display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("upgrade selected transmitter not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@then("user click on upgrade checkbox")
def user_click_on_upgrade_checkbox():
    driver.find_element_by_xpath('//*[@id="select_all"]').click()
    time.sleep(2)

@then('user click on upgrade selected transmitter option')
def user_click_on_upgrade_selected_transmitter_option():
    driver.find_element_by_xpath('//*[@id="admin_body"]/div[1]/a').click()