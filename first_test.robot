*** Settings ***
Library    Collections

*** Test Cases ***
我的第一个自动化用例
    Log    我成功写出了第一个自动化用例！ 
    Should Be True    1 == 1                     
    Log    用例执行成功！