from pytest_bdd import scenario, given, when, then, scenarios, parsers
import allure
from selenium.webdriver.support.select import Select

from Pagelocators.adder import *
from Pagelocators.channel_create import *
from tests.testcase1.step_defs.WebDeiverFactory import *

scenarios('../features/ChannelCC.feature')
# scenarios('D:\pythonProject\adderCode1\tests\testcase1\features\ChannelCC.feature')


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

@then("user verify channel heading")
def user_verify_channel_heading():

    expected = 'CHANNELS'

    actual = driver.find_element_by_xpath(channel).text

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


@then("user click on channel and verify the channel page is open or not")
def user_click_on_channel_and_verify_the_channel_page_is_open_or_not():
    driver.find_element_by_xpath(channel).click()
    print("clicked on channel")
    time.sleep(2)
    try:
        assert "channels" in driver.current_url
    finally:
        if (AssertionError):
            allure.attach(driver.get_screenshot_as_png(), name="Invalid Credential",
                          attachment_type=allure.attachment_type.PNG)

@then("user verify the add channel option")
def user_verify_the_add_channel_option():
    expected = "Add Channel"

    actual = driver.find_element_by_xpath(add_channel).text

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

@then("user click on the add channel option")
def user_click_on_the_add_channel_option():
    driver.find_element_by_xpath(add_channel).click()
    print("click on channel done")
    time.sleep(2)

@then(parsers.parse('user add channel name "{C_name}"'))
def user_add_channel_name(C_name):
    driver.find_element_by_xpath(channel_name).click()
    driver.find_element_by_xpath(channel_name).send_keys(C_name)
    print("channel name aadded")
    time.sleep(2)

@then(parsers.parse('user add description "{C_description}"'))
def user_add_description(C_description):
    driver.find_element_by_xpath(channel_description).send_keys(C_description)
    print("channel description added")
    time.sleep(2)

@then(parsers.parse('user add location "{C_location}"'))
def user_add_location(C_location):
    driver.find_element_by_xpath(channel_location).send_keys(C_location)
    print("channel location added")
    time.sleep(2)

@then("user select video1")
def user_select_video1():
    video1 = Select(driver.find_element_by_xpath('//*[@id="video_e_id"]'))
    video1.select_by_visible_text("tx1 [1]")
    print("video1 added")
    time.sleep(2)

# @then("user select video2")
# def user_select_video2():
#     video2 = Select(driver.find_element_by_xpath('//*[@id="video1_e_id"]'))
#     video2.select_by_visible_text("q [1]")
#     print("video2 added")
#     time.sleep(3)

@then("user select audio")
def user_select_audio():
    audio = Select(driver.find_element_by_xpath('//*[@id="audio_e_id"]'))
    audio.select_by_visible_text("tx1")
    print("audio added")
    time.sleep(2)

@then("user select usb")
def user_select_usb():
    usb = Select(driver.find_element_by_xpath('//*[@id="usb_e_id"]'))
    usb.select_by_visible_text("tx1 [1]")
    print("usb added")
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)

@then("user send the channel group not a member of to member of")
def user_send_the_channel_group_not_a_member_of_to_member_of():
    driver.find_element_by_xpath('//*[@id="add_all_channel_groups"]/img').click()
    print("channel group added")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,500)")
    time.sleep(2)

@then("user allow the permission of single user")
def user_allow_the_permission_of_single_user():
    single_user = Select(driver.find_element_by_xpath('//*[@id="all_users"]'))
    single_user.select_by_visible_text("admin")
    driver.find_element_by_xpath('//*[@id="add_one_user"]/img').click()
    print("user selected")
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)

@then("user disselect the permission of single user")
def user_disselect_the_permission_of_single_user():
    disselect = Select(driver.find_element_by_xpath('//*[@id="selected_users"]'))
    disselect.select_by_visible_text("admin")
    driver.find_element_by_xpath('//*[@id="remove_one_user"]/img').click()
    print("user disselected")
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)

@then('user allow the permission of all the user')
def user_allow_the_permission_of_all_the_user():
    driver.find_element_by_xpath('//*[@id="add_all_users"]/img').click()
    print("all user selected")
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)

@then("user selected the user group permission not set to permitted")
def user_selected_the_user_group_permission_not_set_to_permitted():
    driver.find_element_by_xpath('//*[@id="add_all_user_groups"]/img').click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)

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
    time.sleep(5)


@then("user verify same channel is created or not")
def user_verify_same_channel_is_created_or_not():
    expected = "A channel with that name already exists"

    actual = driver.find_element_by_id('configure_channel_ajax_message').text
    if expected == actual:
        print("A channel with that name already exists")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

        driver.execute_script("window.scrollTo(500,0)")
        assert False

    else:
        print("channel is created")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        driver.execute_script("window.scrollTo(500,0)")

############ channel connect #####################

@then("user verify receiver heading")
def user_verify_reciver_heading():

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
    # driver.find_element_by_xpath('//*[@id="connect_link_101"]/a').click()
    driver.find_element_by_xpath("//span[starts-with(@id, 'connect_link_')]").click()
    time.sleep(2)


@then("user verify video-only button is present or not")
def user_verify_video_button_is_present_or_not():

    expected = "VIDEO-ONLY"

    actual = driver.find_element_by_xpath('//*[@id="admin_body"]/table/tbody/tr[2]/td[4]/a[1]').text
    # import pdb; pdb.set_trace()
    if expected == actual:
        print("video-only is display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("video-only is not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@then("user click on video-only button")
def user_click_on_video_button():
    driver.find_element_by_xpath('//*[@id="admin_body"]/table/tbody/tr[2]/td[4]/a[1]').click()
    print("video-only channel is create")
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)
    time.sleep(5)

@then("user verify the channel is connect")
def user_verify_the_channel_is_connect_or_not():
    # import pdb;pdb.set_trace()

    expected = 'This receiver is currently connected to Pankaj_channel'

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
    # driver.find_element_by_xpath('//*[@id="disconnect_link_101"]/a').click()
    driver.find_element_by_xpath("//span[starts-with(@id, 'disconnect_link_')]").click()
    print("channel is disconnect")
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)
    time.sleep(5)



########### shared channel ##################

@then("user verify shared button is present or not")
def user_verify_video_button_is_present_or_not():

    expected = "SHARED"

    actual = driver.find_element_by_xpath('//*[@id="admin_body"]/table/tbody/tr[2]/td[4]/a[2]').text
    # import pdb; pdb.set_trace()
    if expected == actual:
        print("shared is display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("shared is not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@then("user click on shared button")
def user_click_on_video_button():
    driver.find_element_by_xpath('//*[@id="admin_body"]/table/tbody/tr[2]/td[4]/a[2]').click()
    print("shared channel is create")
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)
    time.sleep(5)

############### exclusive channel ###################

@then("user verify exclusive button is present or not")
def user_verify_video_button_is_present_or_not():

    expected = "EXCLUSIVE"

    actual = driver.find_element_by_xpath('//*[@id="admin_body"]/table/tbody/tr[2]/td[4]/a[3]').text
    # import pdb; pdb.set_trace()
    if expected == actual:
        print("exclusive button is display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("exclusive button is not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@then("user click on exclusive button")
def user_click_on_video_button():
    driver.find_element_by_xpath('//*[@id="admin_body"]/table/tbody/tr[2]/td[4]/a[3]').click()
    print("exclusive channel is create")
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)
    time.sleep(5)

################# private channel ######################

@then("user verify private button is present or not")
def user_verify_video_button_is_present_or_not():

    expected = "PRIVATE"

    actual = driver.find_element_by_xpath('//*[@id="admin_body"]/table/tbody/tr[2]/td[4]/a[4]').text
    # import pdb; pdb.set_trace()
    if expected == actual:
        print("private button is display properly")
        assert True
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    else:
        print("exclusive button is not display properly")
        allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        assert False

@then("user click on private button")
def user_click_on_video_button():
    driver.find_element_by_xpath('//*[@id="admin_body"]/table/tbody/tr[2]/td[4]/a[4]').click()
    print("private channel is create")
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)
    time.sleep(5)

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



@then("user delete the channel which is created")
def user_delete_the_channel_which_is_created():
    driver.find_element_by_xpath("//tr[starts-with(@class, 'odd')]/td[9]/a[3]/img").click()
    print("channel is deleted")
    time.sleep(3)


@then("user verify delete option is occur or not")
def user_verify_delete_option_is_occur_or_not():
    expected = "Delete"

    actual = driver.find_element_by_xpath('//*[@id="delete_channel_confirm_link"]').text

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

@then("user click on the delete option")
def user_click_on_the_delete_option():
    driver.find_element_by_xpath('//*[@id="delete_channel_confirm_link"]').click()
    print("click on final delete")
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)
    time.sleep(3)


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
    allure.attach(driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)