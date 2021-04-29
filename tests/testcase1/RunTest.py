import os

# os.system('cmd /d "pytest -k "Skill" --alluredir=my_allure_results"')
# os.system('pytest -v -s tests\step_defs\skill_box.py')
#
# # os.system('pytest D:\pythonProject\pankaj')
import time

os.system('pytest -v -s --alluredir="D:/pythonProject/adderCode1/tests/testcase1/ChannelCC-reports" D:/pythonProject/adderCode1/tests/testcase1/step_defs/ChannelCC.py')
# os.system('"pytest -k "skill" --alluredir=my_allure_results"')
os.system("allure serve ChannelCC-reports")

# -v -s adder.py --html=$WORKSPACE/reports/re
#
# ports.html