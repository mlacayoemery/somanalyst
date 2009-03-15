import sys, os
import smtplib, email

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

if __name__=="__main__":
   email_user=sys.argv[1]
   to=sys.argv[2]
   subject=sys.argv[3]
   text=sys.argv[4]

   if sys.argv[5]!="#":
      attach=sys.argv[5]
   else:
      attach=None
      
   email_pwd=sys.argv[6]
   smtp=sys.argv[7]
   port=int(sys.argv[8])
   
   mail(email_user, to, subject, text, attach, email_pwd, smtp, port)