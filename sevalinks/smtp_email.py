import smtplib
import classifieds.settings as settings
import email_templates.reset_pass_confirm as rpc
import email_templates.reg_confirm as rc
from email.mime.text import MIMEText
from django.core.mail import EmailMultiAlternatives
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

senderGmail = settings.CONFIRMATION_EMAIL["email"]
senderYahoo = settings.CONFIRMATION_EMAIL["yahooemail"]
senderPass = settings.CONFIRMATION_EMAIL["password"]
smtpGmail = ["smtp.gmail.com", 587]
smtpYahoo = ["smtp.mail.yahoo.com", 587]
senderName = "Sevalinks<%s>"

resetHtml = rpc.html
resetSubject = "Sevalinks - Reset password request"
resetUrl = settings.BASE_URL + "/seva/resetpassword/?id="

registerHtml = rc.html
registerSubject = "Sevalinks - Registeration confirmation request"
registerUrl = settings.BASE_URL + "/seva/confirmsuccess/?id="

def send_reset_email(id, name, email):
    url = resetUrl + id
    print url
    body = Template(resetHtml)
    bodyStr = body.substitute(username=name, url=url)
    send_mail(resetSubject, bodyStr, email, senderYahoo, senderPass, smtpYahoo)
    #send_mail(resetSubject, bodyStr, email, senderGmail, senderPass, smtpGmail)
    #try:
        #send_mail(resetSubject, bodyStr, email, senderGmail, senderPass, smtpGmail)
    #except:
        #send_mail(resetSubject, bodyStr, email, senderYahoo, senderPass, smtpYahoo)
    
def send_register_confirm_email(id, name, email):
    url = registerUrl + id
    print url
    body = Template(registerHtml)
    bodyStr = body.substitute(username=name, url=url)
    send_mail(registerSubject, bodyStr, email, senderYahoo, senderPass, smtpYahoo)
    
def send_mail(SUBJECT, BODY, TO, FROM, PASSWORD, SMTP):
    """With this function we send out our html email"""   
    
    
    # Create message container - the correct MIME type is multipart/alternative here!
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = SUBJECT
    MESSAGE['To'] = TO
    MESSAGE['From'] = senderName % (FROM)
    MESSAGE.preamble = """
Your mail reader does not support the report format.
Please contact us at <a href="http://www.elemsys.com/contact-us/">Contact us</a>!"""
 
    # Record the MIME type text/html.
    HTML_BODY = MIMEText(BODY, 'html')
 
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    MESSAGE.attach(HTML_BODY)   
    
    server = smtplib.SMTP(SMTP[0], SMTP[1])
    server.ehlo()
    server.starttls()
    server.login(FROM, PASSWORD)    
    server.sendmail(senderName % (FROM), TO, MESSAGE.as_string())
    server.close()
    


#def send_email(recipient, subject, body, id, user=sender, pwd=senderPass):
#    gmail_user = user
#    gmail_pwd = pwd
#    FROM = user
#    TO = recipient if type(recipient) is list else [recipient]
#    SUBJECT = subject
#    TEXT = body
#
    # Prepare actual message
 #   message = """From: %s\nTo: %s\nSubject: %s\n\n%s
#    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
#    try:
#        server = smtplib.SMTP("smtp.gmail.com", 587)
##        server.ehlo()
#        server.starttls()
#        server.login(gmail_user, gmail_pwd)
#        server.sendmail(FROM, TO, message)
 #       server.close()
#        print 'successfully sent the mail'
#    except:
#        print "failed to send mail"
      



