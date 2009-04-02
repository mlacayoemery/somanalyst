import os
import smtplib
import email

def mail(email_user, to, subject, text, attach, email_pwd, smtp="smtp.gmail.com",port=587):

   msg = email.MIMEMultipart.MIMEMultipart()
   msg['From'] = email_user
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(email.MIMEText.MIMEText(text))

   if attach:
      part = email.MIMEBase.MIMEBase('application', 'octet-stream')
      part.set_payload(open(attach, 'rb').read())
      email.Encoders.encode_base64(part)
      part.add_header('Content-Disposition',
              'attachment; filename="%s"' % os.path.basename(attach))
      msg.attach(part)

   mailServer = smtplib.SMTP(smtp, port)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(email_user, email_pwd)
   mailServer.sendmail(email_user, to, msg.as_string())

   mailServer.close()

