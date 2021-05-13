## Optional Exercises 2
---

>Your current SMTP mail client only handles sending text messages in the email body. Modify your 
client such that it can send emails with both text and images.

 

---


## 实现方法

 1. 将图片以附件的形式上传
 2. 将图片以本地文件的形式上传

---
方法1：

```python
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

sender = '***@qq.com'
receiver = '***@qq.com'
smtpSocket = smtplib.SMTP_SSL('smtp.qq.com', 465)
smtpSocket.login(sender, '*&***')
# 创建邮件对象
msg = MIMEMultipart()
msg['From'] = Header(sender)
msg['To'] = Header(receiver)
subject = 'SMTP!🛫'
msg['subject'] = Header(subject)
# 邮件正文
msg.attach(MIMEText('❤I love computer network as like I love you❤'))

# 添加图片附件
image_data = open('faker.jpg', 'rb').read()
image = MIMEImage(image_data)
image['Content-Disposition'] = 'attachment; filename="faker.jpg"'
msg.attach(image)
try:
    smtpSocket.sendmail(sender, receiver, msg.as_string())
    smtpSocket.quit()
    print('send successful!')
except:
    print('Error!')
```

---
实现效果


![](https://img-blog.csdnimg.cn/20210513175210723.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjY2MjMxOA==,size_16,color_FFFFFF,t_70#pic_center)

---
方法2：

```python
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
# 此处为添加本地图片使用的html
 content = """
 <h2>i real love you</h2>	
 <p>i love you❤</p>
 <p>as like i love computer</p>
 <img src='cid:image1'>
 """
 html = MIMEText(content, 'html')
 msg.attach(html)

# 添加图片附件
image_data = open('faker.jpg', 'rb').read()
image = MIMEImage(image_data)
image.add_header('Content-ID', '<image1>')
msg.attach(image)

try:
    smtpSocket.sendmail(sender, receiver, msg.as_string())
    smtpSocket.quit()
    print('send successful!')
except:
    print('Error!')
```

---
实现效果
![](https://img-blog.csdnimg.cn/20210513175547647.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjY2MjMxOA==,size_16,color_FFFFFF,t_70#pic_center)

