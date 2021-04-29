Feature: we are working on Aim box and upgrade/downgrade the aim build

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
  Then select aim image "C:\\Users\\Pankaj\Desktop\\AIM build\\upgrade_4.12.10041.tar.gz.asc"
  Then user verify the upload button
  Then user click on upload button
  Then user verify aim image is upload or not
  Then user verify restart button
  Then user click on restart button and land on login page

Scenario: user verify the build is sucessfully upgarded or not
  Given user enter the username "admin"
  Then user click on login button
  Then user verify the login done or not
  Then user verify the update option
  Then user click on update option and verify the update page is open
  Then user verify the build number in update page
  Then user verify the build number in bottom of page
  Then user click on dashboard


