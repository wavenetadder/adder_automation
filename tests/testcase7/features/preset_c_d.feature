Feature: we are working on Aim box and create and delete preset

Scenario: user should see the Aim login screen

  Given user is in aim login page or not
  Given user enter the username "admin"
#  Given user enter the password "123"
  Then user click on login button

Scenario: user verify login done sucessfully or not

  Then user verify the login done or not

Scenario: user verify and click the preset and perform opertaion
  Then user verify preset heading
  Then user click on preset and verify the preset page is open or not
  Then user verify add preset option is present or not
  Then user click on add preset option
  When user enter preset name "qtp"
  Then user enter description "try and test"
  Then user add channel pair 1 receiver
  Then user add channel pair 1 channel
  Then user choose allowed conection mode
  Then user verify the save button
  Then user save the details

Scenario: user connect the preset channel with video-only
  Then user click on video only button
  Then user verify receiver heading on top
  Then user click on receiver and verify the receiver page is open or not
  Then user click on connect to a channel
  Then user verify the channel is connect
  Then user verify preset heading
  Then user click on preset and verify the preset page is open or not
  Then user click on channel disconnect

Scenario: user connect the preset channel with Shared
  Then user click on shared button
  Then user verify receiver heading on top
  Then user click on receiver and verify the receiver page is open or not
  Then user click on connect to a channel
  Then user verify the channel is connect
  Then user verify preset heading
  Then user click on preset and verify the preset page is open or not
  Then user click on channel disconnect

  Scenario: user connect the preset channel with Exclusive
  Then user click on exclusive button
  Then user verify receiver heading on top
  Then user click on receiver and verify the receiver page is open or not
  Then user click on connect to a channel
  Then user verify the channel is connect
  Then user verify preset heading
  Then user click on preset and verify the preset page is open or not
  Then user click on channel disconnect

Scenario: user connect the preset channel with Private
  Then user click on private button
  Then user verify receiver heading on top
  Then user click on receiver and verify the receiver page is open or not
  Then user click on connect to a channel
  Then user verify the channel is connect
  Then user verify preset heading
  Then user click on preset and verify the preset page is open or not
  Then user click on channel disconnect


Scenario: user delete preset
  Then user delete the preset
  Then user verify delete option come or not
  Then user click on delete option
  Then user click on dashboard


