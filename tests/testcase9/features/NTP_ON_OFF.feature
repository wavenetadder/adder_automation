Feature: we are working on Aim box and enable and disable the syslog

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
  Then user verify time option
  Then user click on time option
  Then user enable NTP option
#  Then user click on set ntp server 1
  Then user enter server one address "192.168.17.212"
  Then user set time zone area
  Then user set time zone location
  Then user verify the save button
  Then user save the details
  Then user verify save done or not
  Then user click on dashboard

Scenario: user disable the NTP

  Then user verify setting option
  Then user click on setting option and verify setting page is open or not
  Then user verify time option
  Then user click on time option
  Then user disable NTP option
  Then user verify the save button
  Then user save the details
  Then user verify save done or not
  Then user click on dashboard