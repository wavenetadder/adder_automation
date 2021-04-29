Feature: we are working on Aim box and updrade/downgarde Rx and Tx

Scenario: user should see the Aim login screen
  Given user is in aim login page or not
  Given user enter the username "admin"
#  Given user enter the password "123"
  Then user click on login button

Scenario: user verify login done sucessfully or not
  Then user verify the login done or not


Scenario: user verify and click the dashboard
  Then user verify dashboard heading
  Then user click on dashboard

Scenario: user update the aim build
  Then user verify the update option
  Then user click on update option and verify the update page is open
  Then user select aim image "C:\\Users\\Pankaj\\Desktop\\AIM build\\rx_tx\\upgrade_dvix2_backup_adder.bin.txs.5.0.46844"
#  Then user select aim image
  Then user verify the upload button
  Then user click on upload button
  Then user verify upgrade selected transmitter is shown or not
  Then user click on upgrade checkbox
  Then user click on upgrade selected transmitter option