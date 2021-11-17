'''
    使用excel表来进行参数化数据。
    将测试结果回写excel表中。

    使用邮件发送报告

    使用centos系统做定时执行脚本。
    crontab -e
        * 15 * * *  python   自动化开发框架.py

'''
import time

import xlrd, os



class InitPage:
    wb = xlrd.open_workbook("HKR.xls", encoding_override=True)
    st = wb.sheet_by_index(0)
    row = st.nrows
    loginSuccessData = list()
    loginErrorData = list()
    for i in range(1, row):
        # 登陆成功的用例数据
        # loginSuccessData = [
        #     {"username":"jason","password":"1234567","expect":"Student Login"},
        #     {"username": "admin1", "password": "root", "expect": "Student Login"},
        # ]
        login = {"姓名": st.cell(i, 0).value, "密码": st.cell(i, 1).value,
                 "期望数据": st.cell(i, 2).value, "是否通过": i, "测试人员": st.cell(i, 4).value,
                 "测试时间": 2021-11-17}

        if login["期望数据"] == "Student Login":
            loginSuccessData.append(login)
        else:
            loginErrorData.append(login)

    # 登陆失败的用例数据  id=msg_uname
    # loginErrorData = [
    #     {"username": "jason", "password": "123456789", "expect": "账户名错误或密码错误!别瞎弄!"},
    #     {"username": "admin1", "password": "rootw", "expect": "账户名错误或密码错误!别瞎弄!"},
    # ]
