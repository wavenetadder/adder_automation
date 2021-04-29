Feature: we are working on Aim box and enable/disable multi user information option

Scenario: user should see the Aim login screen

  Given user is in aim login page or not
  Given user enter the username "admin"
#  Given user enter the password "123"
  Then user click on login button

Scenario: user verify login done sucessfully or not
  Then user verify the login done or not


Scenario: user verify and click the dashboard and enable multi user information
  Then user verify dashboard heading
  Then user click on dashboard
  Then user verify setting heading
  Then user click on setting option and verify the setting page is open
  Then user verify receiver heading
  Then user click on receiver
  Then user click the checkbox show multi user information yes
  Then user verify the save button
  Then user save the details
  Then user verify save done or not

Scenario: user verify and click the dashboard and disabel multi user information
  Then user verify dashboard heading
  Then user click on dashboard
  Then user verify setting heading
  Then user click on setting option and verify the setting page is open
  Then user verify receiver heading
  Then user click on receiver
  Then user click the checkbox show multi user information no
  Then user verify the save button
  Then user save the details
  Then user verify save done or not
  Then user click on dashboard