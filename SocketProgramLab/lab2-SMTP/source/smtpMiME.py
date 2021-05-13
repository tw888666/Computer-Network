import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

sender = '****@qq.com'
receiver = '***@qq.com'
smtpSocket = smtplib.SMTP_SSL('smtp.qq.com', 465) # SSL
smtpSocket.login(sender, '****') # 授权码自行在qq邮箱申请
# 创建邮件对象
msg = MIMEMultipart() 
# 设置邮件相关信息
msg['From'] = Header(sender)
msg['To'] = Header(receiver)
subject = 'SMTP!🛫'
msg['subject'] = Header(subject)
# 邮件正文
msg.attach(MIMEText('❤I love computer network as like I love you❤', 'plain'))
# 此处为添加本地图片使用的html
# content = """
# <h2>i real love you</h2>
# <p>i love you❤</p>
# <p>as like i love computer</p>
# <img src='cid:image1'>
# """
# html = MIMEText(content, 'html')
# msg.attach(html)

# 添加图片附件
image_data = open('faker.jpg', 'rb').read()
image = MIMEImage(image_data)
image['Content-Disposition'] = 'attachment; filename="faker.jpg"'
# 此句与html一起使用 只需把上一行注释即可
# image.add_header('Content-ID', '<image1>')
msg.attach(image)

try:
    smtpSocket.sendmail(sender, receiver, msg.as_string())
    smtpSocket.quit()
    print('send successful!')
except:
    print('Error!')
