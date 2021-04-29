Feature: we are working on Aim box and upgarde the licence

Scenario: user should see the Aim login screen

  Given user is in aim login page or not
  Given user enter the username "admin"
#  Given user enter the password "123"
  Then user click on login button

Scenario: user verify login done sucessfully or not
  Then user verify the login done or not


Scenario: user verify and click the dashboard and updating the licence
  Then user verify dashboard heading
  Then user click on dashboard
  Then user verify setting heading
  Then user click on setting option and verify the setting page is open
  Then user verify the general heading
  Then user click on general option
  Then user click on the upgarde licence link
  Given user enter the licence key "7fba 73f9 fdf3 6982 c8f0 5a32 9f6b 93d8 0a18 3967"
  Then user verify the save button
  Then user save the details
  Then user verify licence is valid or not

Scenario: user land on the dashboard
  Then user verify dashboard heading
  Then user click on dashboard