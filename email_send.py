# coding=utf-8
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# smtp发送服务器地址
smtp_host = "0.0.0.0"
# 发件邮箱
sender = 'xxxxx@brgroup.com'
# 收件邮箱
receivers = ['hailei1@xxx.com','hailei2@xxx.com']

# 创建一个带附件的实例
message = MIMEMultipart()
# 设置邮件主题
subject = '线上日志报表'
message['Subject'] = Header(subject, 'utf-8')
# 设置邮件正文内容
message.attach(MIMEText('附件为测试邮件，请查收！', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 测试.xlsx 文件
att = MIMEText(open('测试.xlsx', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
# filename可以任意填写
att["Content-Disposition"] = 'attachment; filename="测试"'
message.attach(att)

try:
    # 使用ssl加密的邮箱系统
    smtpObj = smtplib.SMTP_SSL(smtp_host,465)
except:
    # 不进行ssl加密的邮箱系统
    smtpObj = smtplib.SMTP(smtp_host,465)

smtpObj.sendmail(sender, receivers, message.as_string())
