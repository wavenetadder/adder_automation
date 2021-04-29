Feature: we are working on Aim box create and connect the channel

Scenario: user should see the Aim login screen
  Given user is in aim login page or not
  Given user enter the username "admin"
#  Given user enter the password "123"
  Then user click on login button

Scenario: user verify login done sucessfully or not
  Then user verify the login done or not

############ channel create #####################

Scenario: user verify and click the channel and fill the details
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
  Then user selected the user group permission not set to permitted
  Then user verify the save button
  Then user save the details


###### again create channel ########

Scenario: user verify and click the channel and fill the details again
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
  Then user verify same channel is created or not


######### channel connect #############


Scenario: user connect the channel by video-only
  Then user verify receiver heading
  Then user click on receiver and verify the receiver page is open or not
  Then user click on connect to a channel
  Then user verify video-only button is present or not
  Then user click on video-only button
  Then user click on connect to a channel
  Then user verify the channel is connect
  Then user verify receiver heading
  Then user click on receiver and verify the receiver page is open or not
  Then user click on channel disconnect

Scenario: user connect the channel by shared
  Then user click on connect to a channel
  Then user verify shared button is present or not
  Then user click on shared button
  Then user click on connect to a channel
  Then user verify the channel is connect
  Then user verify receiver heading
  Then user click on receiver and verify the receiver page is open or not
  Then user click on channel disconnect

Scenario: user connect the channel by exclusive
  Then user click on connect to a channel
  Then user verify exclusive button is present or not
  Then user click on exclusive button
  Then user click on connect to a channel
  Then user verify the channel is connect
  Then user verify receiver heading
  Then user click on receiver and verify the receiver page is open or not
  Then user click on channel disconnect

Scenario: user connect the channel by private
  Then user click on connect to a channel
  Then user verify private button is present or not
  Then user click on private button
  Then user click on connect to a channel
  Then user verify the channel is connect
  Then user verify receiver heading
  Then user click on receiver and verify the receiver page is open or not
  Then user click on channel disconnect


########## Delete the channel #################



Scenario: user delete the channel which is created
  Then user verify channel heading
  Then user click on channel and verify the channel page is open or not
  Then user delete the channel which is created
  Then user verify delete option is occur or not
  Then user click on the delete option
  Then user verify dashboard heading
  Then user click on dashboard





