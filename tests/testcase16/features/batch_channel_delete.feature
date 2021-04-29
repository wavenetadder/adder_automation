Feature: we are working on Aim box create and delete the multiple channel together

Scenario: user should see the Aim login screen
  Given user is in aim login page or not
  Given user enter the username "admin"
#  Given user enter the password "123"
  Then user click on login button

Scenario: user verify login done sucessfully or not
  Then user verify the login done or not

############ channel create #####################

Scenario: user created channel first time
  Then user verify channel heading
  Then user click on channel and verify the channel page is open or not
  Then user verify the add channel option
  Then user click on the add channel option
  Then user add channel name "Pankaj_channel"
  Then user add description "try and test description"
  Then user add location "New Delhi"
  Then user select video1
#  Then user select video2
  Then user select audio
  Then user select usb
  Then user send the channel group not a member of to member of
  Then user allow the permission of single user
  Then user disselect the permission of single user
  Then user allow the permission of all the user
#  Then user selected the user group permission not set to permitted
  Then user verify the save button
  Then user save the details


############## channel create second time #####################

Scenario: user created channel second time
  Then user verify channel heading
  Then user click on channel and verify the channel page is open or not
  Then user verify the add channel option
  Then user click on the add channel option
  Then user add channel name "try_channel"
  Then user add description "try2 and test2 description2"
  Then user add location "New Delhi"
  Then user select video1
#  Then user select video2
  Then user select audio
  Then user select usb
  Then user send the channel group not a member of to member of
  Then user allow the permission of single user
  Then user disselect the permission of single user
  Then user allow the permission of all the user
#  Then user selected the user group permission not set to permitted
  Then user verify the save button
  Then user save the details


Scenario: user select the batch mode and delete all the channel
  Then user verify delete batch mode option is present or not
  Then user click on the batch mode option
  Then user click on the manage checkbox
  Then user verify delete selected option is present or not
  Then user click on the delete selected option
  Then user verify delete option is occur or not
  Then user click on the delete option
  Then user click on dashboard