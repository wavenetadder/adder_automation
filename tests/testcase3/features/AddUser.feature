Feature: we are working on Aim box and create user

Scenario: user should see the Aim login screen
  Given user is in aim login page or not
  Given user enter the username "admin"
#  Given user enter the password "123"
  Then user click on login button

Scenario: user verify login done sucessfully or not
  Then user verify the login done or not


Scenario: user verify and click the channel
  Then user verify user heading
  Then user click on user and verify the user page is open or not
  Then user verify add user button
  Then user click on add user button
  Then user add username "admin123"
  Then user add first name "pankaj"
  Then user add last name "kumar"
  Then user add email "pankajk0692@gmail.com"
  Then user click on checkbox required password no
  Then user click on checkbox aim admin required yes
  Then user give permission of user group not a member of to member of
  Then user give permission of channel permission not set to permitted
  Then user give permission channel group permission not set to permitted
  Then user verify the save button
  Then user click on save button


Scenario: Again create user and verify already present or not
  Then user verify user heading
  Then user click on user and verify the user page is open or not
  Then user verify add user button
  Then user click on add user button
  Then user add username "admin123"
  Then user add first name "pankaj"
  Then user add last name "kumar"
  Then user add email "pankajk0692@gmail.com"
  Then user click on checkbox required password no
  Then user click on checkbox aim admin required yes
  Then user give permission of user group not a member of to member of
  Then user give permission of channel permission not set to permitted
  Then user give permission channel group permission not set to permitted
  Then user verify the save button
  Then user click on save button
  Then user verify same user is created or not

Scenario: user again login and verify user add or not
  Then user click on logout
  Then user enter the username after add user "admin123"
  Then user click on login button

Scenario: user verify login done sucessfully or not after add user
  Then user verify the login done or not



