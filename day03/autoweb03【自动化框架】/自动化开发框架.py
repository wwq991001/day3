import time
# from mail1 import *
from HTMLTestRunner import HTMLTestRunner
import unittest
import os, pathlib
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title="HKR测试报告",
    description="hkr登录测试报告",
    verbosity=1,
    stream=open(file="hkr.html",mode="w+",encoding="utf-8")
)


runner.run(tests)


# 邮件发送代码
time.sleep(2)
sender = "1942936605@qq.com"
passwd = "xlklojkmgdwlfbfe"
receivers = "wwq991001@outlook.com"

subject = "hkr登录测试报告"
content = r'E:\PYthon自动化测试\python\python自动化\day03\autoweb03【自动化框架】\hkr.html'
f = open(content, 'rb')
mail_body = f.read()
msg = MIMEMultipart()
# msg = MIMEText(content, "html", 'utf-8')
# msg.attach(part_text)
part_attach1 = MIMEApplication(open('HKR.xls', 'rb').read())  # 打开附件
part_attach1.add_header('Content-Disposition', 'attachment', filename=pathlib.Path('HKR.xls').name)  # 为附件命名
msg.attach(part_attach1)

part_text = MIMEText(mail_body, "html", 'utf-8')
msg.attach(part_text)

msg['Subject'] = Header(subject, "utf-8")
msg['From'] = sender
msg['TO'] = receivers

try:
    s = smtplib.SMTP_SSL('smtp.qq.com', 465)
    s.login(sender, passwd)
    s.sendmail(sender, receivers, msg.as_string())
    s.quit()
    print("发送成功")

except smtplib.SMTPException as e:
    print("发送失败,失败原因", e)






























































