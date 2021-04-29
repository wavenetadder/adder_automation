Feature: we are working on Aim box and doing RDP_TX creation

Scenario: user should see the Aim login screen

  Given user is in aim login page or not
  Given user enter the username "admin"
#  Given user enter the password "123"
  Then user click on login button

Scenario: user verify login done sucessfully or not

  Then user verify the login done or not



######### RDP Creation ###################


Scenario: user verify and click the transmitter and perform opertaion

  Then user verify transmitter heading
  Then user click on transmitter and verify the transmitter page is open or not
  Then user verify Add VDI option
  Then user click on Add VDI option
  Then user enter RDP name "xyz"
  Then user enter ip address and DNS name "192.168.17.212"
  Then user enter port number "3389"
  Then user enter domain name "pankaj"
  Then user select maximum resolution
  Then user verify the save button
  Then user save the details


########## verify name is already present or not #############

Scenario: user verify and click the transmitter again and perform opertaion again
  Then user verify transmitter heading
  Then user click on transmitter and verify the transmitter page is open or not
  Then user verify Add VDI option
  Then user click on Add VDI option
  Then user enter RDP name "xyz"
  Then user enter ip address and DNS name "192.168.17.212"
  Then user enter port number "3389"
  Then user enter domain name "pankaj"
  Then user select maximum resolution
  Then user verify the save button
  Then user save the details
  Then user verify same RDP already reated or not


########### RDP Deletion ################

Scenario: user go to transmitter page
  Then user click on transmitter and verify the transmitter page is open or not
  Then user delete the rdp which is created
  Then user verify delete option come or not
  Then user click on delete option
  Then user verify dashboard heading
  Then user click on dashboard
