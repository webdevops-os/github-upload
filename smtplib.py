from smtplib import SMTP_SSL
import os
# env 
email = os.environ.get( "SMTP_EMAIL" )
password = os.environ.get( "SMTP_PASSWORD" )

# connect to google
with SMTP_SSL( 'smtp.gmail.com', 465 ) as smtp:
    #server ident
    smtp.ehlo()
    # acc
    smtp.login( email, password )
    smtp.sendmail( from_addr=email,to_addrs=email, msg="Hello world!" )
    # close
    smtp.quit()