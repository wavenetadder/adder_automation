from pytest_bdd import scenario, given, when, then, scenarios, parsers
import allure
from selenium.webdriver.support.select import Select

from Pagelocators.adder import *
from tests.testcase1.step_defs.WebDeiverFactory import *

scenarios('../features/preset_c_d.feature')
# scenarios('D:\pythonProject\adderCode1\tests\testcase7\features\preset_c_d.feature')


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

@then("user verify preset heading")
def user_verify_channel_heading():
    expected = 'PRESETS'

    actual = driver.find_element_by_xpath(preset).text

    if expected == actual:
        print("preset display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("preset not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False


@then("user click on preset and verify the preset page is open or not")
def user_click_on_preset_and_verify_the_preset_page_is_open_or_not():
    driver.find_element_by_xpath(preset).click()
    print("clicked on preset")
    time.sleep(2)
    try:
        assert "presets" in driver.current_url
    finally:
        if (AssertionError):
            allure.attach(driver.get_screenshot_as_png(), name="Invalid Credential",
                          attachment_type=allure.attachment_type.PNG)
print("hello")

@then("user verify add preset option is present or not")
def user_verify_add_preset_option_is_present_or_not():
    expected = 'Add Preset'

    actual = driver.find_element_by_xpath('//*[@id="admin_body"]/div/a').text
    if expected == actual:
        print("Add preset is display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("Add preset is not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@then('user click on add preset option')
def user_click_on_add_preset_option():
    driver.find_element_by_xpath('//*[@id="admin_body"]/div/a').click()
    print("click done on add preset")

@when(parsers.parse('user enter preset name "{preset_name}"'))
def user_enter_preset_name(preset_name):
    driver.find_element_by_xpath('//*[@id="cp_name"]').clear()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="cp_name"]').send_keys(preset_name)
    print("preset name enter done")
    time.sleep(2)


@then(parsers.parse('user enter description "{preset_desc}"'))
def user_enter_preset_name(preset_desc):
    driver.find_element_by_xpath('//*[@id="cp_description"]').clear()
    driver.find_element_by_xpath('//*[@id="cp_description"]').send_keys(preset_desc)
    print("preset description enter done")
    time.sleep(2)

@then("user add channel pair 1 receiver")
def user_add_channel_pair_1_receiver():
    preset_receiver = Select(driver.find_element_by_xpath("//select[starts-with(@id, 'receiver_')]"))
    preset_receiver.select_by_visible_text("rx1")
    print("receiver is added")
    time.sleep(2)


@then("user add channel pair 1 channel")
def user_add_channel_pair_1_channel():
    preset_channel = Select(driver.find_element_by_xpath("//select[starts-with(@id, 'channel_')]"))
    preset_channel.select_by_visible_text("Channel tx1")
    print("channel is added")
    time.sleep(2)


@then("user choose allowed conection mode")
def user_choose_allowed_connection_mode():
    driver.find_element_by_xpath('//*[@id="inherit_allowed_modes_1"]').click()

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
    print("save the details")
    time.sleep(5)

@then("user click on video only button")
def user_click_on_video_only_button():
    driver.find_element_by_xpath("//tr[starts-with(@id, 'row_id_')]/td[5]/a[1]").click()
    print("click on video-only button")
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)
    time.sleep(2)

@then("user verify receiver heading on top")
def user_verify_reciver_heading_on_top():

    expected = 'RECEIVERS'

    actual = driver.find_element_by_xpath(receiver).text

    if expected == actual:
        print("channel display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("channel not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False


@then("user click on receiver and verify the receiver page is open or not")
def user_click_on_channel_and_verify_the_channel_page_is_open_or_not():
    driver.find_element_by_xpath(receiver).click()
    print("clicked on receiver")
    time.sleep(2)
    try:
        assert "t=rx" in driver.current_url
    finally:
        if (AssertionError):
            allure.attach(driver.get_screenshot_as_png(), name="Invalid Credential",
                          attachment_type=allure.attachment_type.PNG)


@then("user click on connect to a channel")
def user_click_on_connect_to_a_channel():
    driver.find_element_by_xpath("//span[starts-with(@id, 'connect_link_')]").click()
    print("click on channel connected option")
    time.sleep(2)


@then("user verify the channel is connect")
def user_verify_the_channel_is_connect_or_not():
    # import pdb;pdb.set_trace()

    expected = 'This receiver is currently connected to Channel tx1'

    actual = driver.find_element_by_xpath('//*[@id="admin_body"]/div[1]').text
    real = actual[:-41]
    print(real)
    # import pdb; pdb.set_trace()
    if expected == real:
        print("channel is connected display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("channel is not connected")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@then("user click on channel disconnect")
def user_click_on_channel_disselect():
    driver.find_element_by_xpath("//tr[starts-with(@id, 'row_id_')]/td[5]/a[1]").click()
    print("channel sucessfully disselect")
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)
    time.sleep(5)

@then("user click on shared button")
def user_click_on_shared_button():
    driver.find_element_by_xpath("//tr[starts-with(@id, 'row_id_')]/td[5]/a[2]").click()
    print("click on a shared button")
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)
    time.sleep(2)

@then("user click on exclusive button")
def user_click_on_exclusive_button():
    driver.find_element_by_xpath("//tr[starts-with(@id, 'row_id_')]/td[5]/a[3]").click()
    print("click on exclusive button")
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)
    time.sleep(2)

@then("user click on private button")
def user_click_on_private_button():
    driver.find_element_by_xpath("//tr[starts-with(@id, 'row_id_')]/td[5]/a[4]").click()
    print("click on a private button")
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)
    time.sleep(2)

@then("user delete the preset")
def user_delete_the_preset():
    driver.find_element_by_xpath("//img[@alt='Delete preset']").click()
    print("click on preset delete option")
    time.sleep(1)

@then("user verify delete option come or not")
def user_verify_delete_option_come_or_not():
    expected = "Delete"

    actual = driver.find_element_by_xpath('//*[@id="delete_connection_preset_confirm_link"]').text

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
    driver.find_element_by_xpath('//*[@id="delete_connection_preset_confirm_link"]').click()
    print("click on final delete")
    time.sleep(1)
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)

@then("user click on dashboard")
def user_click_on_dashboard():
    driver.find_element_by_xpath(dashboard).click()
    print("clicked on dashboard")
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)

