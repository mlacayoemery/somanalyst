import sys
import lib.som.emailme

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
   
   lib.som.emailme.mail(email_user, to, subject, text, attach, email_pwd, smtp, port)