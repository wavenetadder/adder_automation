Feature: we are working on Aim box and allocate the DHCP ip

Scenario: user should see the Aim login screen
  Given user is in aim login page or not
  Given user enter the username "admin"
#  Given user enter the password "123"
  Then user click on login button

Scenario: user verify login done sucessfully or not
  Then user verify the login done or not



Scenario: user verify and click the dashboard and perform opertaion
  Then user verify dashboard heading
  Then user click on dashboard
  Then user verify setting option
  Then user click on setting option and verify setting page is open or not
  Then user verify network option
  Then user click on network option
  Then user click on DHCP checkbox
  Then user verify the save button
  Then user save the details
  Then user verify save done or not
  Then user get the ip genrate by DHCP

