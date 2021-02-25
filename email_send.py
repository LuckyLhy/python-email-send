# coding=utf-8
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

smtp_host = "0.0.0.0"
sender = 'xxxxx@brgroup.com'
receivers = ['hailei1@xxx.com','hailei2@xxx.com']  # 接收邮件

# 创建一个带附件的实例
message = MIMEMultipart()
subject = '线上日志报表'
message['Subject'] = Header(subject, 'utf-8')
# 邮件正文内容
message.attach(MIMEText('附件为测试邮件，请查收！', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('测试.xlsx', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="changshi.xlsx"'
message.attach(att1)

try:
    smtpObj = smtplib.SMTP_SSL(smtp_host,465)
except:
    smtpObj = smtplib.SMTP(smtp_host,465)

smtpObj.sendmail(sender, receivers, message.as_string())
