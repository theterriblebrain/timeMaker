#!/usr/bin/python3

#USER VARIABLES:
import userVariables
from userVariables import *
recipientName = userVariables.recipientName
senderName = userVariables.senderName
secondaryName = userVariables.secondaryName
senderEmailName = userVariables.senderEmailName
#recipients = userVariables.testRecipients
recipients = userVariables.recipients

#SMTP SETTINGS VARIABLES
smtpHost = userVariables.smtpHost
smtpPort = userVariables.smtpPort
smtpUser = userVariables.smtpUser
smtpPassword = userVariables.smtpPassword

#AVERAGES VARIABLES
import random
primaryTime = userVariables.primaryTime
primaryPlacements = userVariables.primaryPlacements
primaryStudies =  userVariables.primaryStudies
primaryRvs = userVariables.primaryRvs
#secondary reporter
secondaryTime = userVariables.secondaryTime
secondaryPlacements = userVariables.secondaryPlacements
secondaryStudies = userVariables.secondaryStudies
secondaryRvs = userVariables.secondaryRvs

#CODE
#send email function
import smtplib
from email.mime.text import MIMEText

def send_email():
    smtpServer = smtplib.SMTP(smtpHost, smtpPort)
    smtpServer.ehlo()
    smtpServer.starttls()
    smtpServer.ehlo
    smtpServer.login(smtpUser, smtpPassword)
    subject='default subject'
    message=messageTxt
    msg = MIMEText(message)
    msg['Subject'] = subjectTxt
    msg['From'] = senderEmailName
    msg['To'] = ','.join(recipients)
    smtpServer.sendmail(smtpUser, recipients, msg.as_string())
    smtpServer.close()
    print('Mail is sent successfully!!')

#Get the name of the report month (previous month) and store it in a variable.
from datetime import date, timedelta
firstDayThis = date.today().replace(day=1)
lastDayPrev = firstDayThis -timedelta(days=1)
lastMonthName = lastDayPrev.strftime('%B')


#variations on the message text to simulate a non-automated message.
message1 = """
Hi """ + recipientName + """,

""" + secondaryName + """'s and my time for """ + lastMonthName + """ is as follows:

Me: """ + primaryTime + """ hrs, """ + primaryRvs + """ RVs, """ + primaryStudies + """ study
""" + secondaryName + """: """ + secondaryTime + """ hrs


Thanks!

""" + senderName + """

"""

message2 = """
Hi """ + recipientName + """,

Here is mine and """ + secondaryName + """'s time for """ + lastMonthName + """.

Me: """ + primaryTime + """ hrs, """ + primaryRvs + """ RVs, """ + primaryStudies + """ study
""" + secondaryName + """: """ + secondaryTime + """ hrs


Thanks!

""" + senderName + """

"""

message3 = """
Hi """ + recipientName + """,

Here is """ + secondaryName + """'s and my time for """ + lastMonthName + """.

""" + secondaryName + """: """ + secondaryTime + """ hrs
Me: """ + primaryTime + """hrs, """ + primaryRvs + """ RVs, """ + primaryStudies + """ study

""" + senderName + """

"""

message4 = """
Hi """ + recipientName + """,

""" + secondaryName + """'s and my time is below.

Me: """ + primaryTime + """ hrs, """ + primaryRvs + """ RVs, """ + primaryStudies + """ study
""" + secondaryName + """: """ + secondaryTime + """ hrs


""" + senderName + """

"""

message5 = """
Hi """ + recipientName + """,

Mine and """ + secondaryName + """'s time for """ + lastMonthName + """ is as follows:

""" + secondaryName + """: """ + secondaryTime + """ hrs
Me: """ + primaryTime + """ hrs, """ + primaryRvs + """ RVs, """ + primaryStudies + """ study

Thanks!

""" + senderName + """

"""

##variations on the message subject to simulate a non-automated message.
subject1 = senderName + " and " + secondaryName + "'s Time for " + lastMonthName
subject2 = secondaryName + " and " + senderName + "'s Time for " + lastMonthName
subject3 = senderName + " and " + secondaryName + "'s Time"
subject4 = "Time for " + lastMonthName
subject5 = senderName + " and " + secondaryName + "'s Time for " + lastMonthName

#randomly select message and subject variations
msgNumber = random.randint (1, 5)
subjNumber = random.randint (1, 5)

if msgNumber == 1:
    messageTxt = message1
elif msgNumber == 2:
    messageTxt = message2
elif msgNumber == 3:
    messageTxt = message3
elif msgNumber == 4:
    messageTxt = message4
elif msgNumber == 5:
    messageTxt = message5

if subjNumber == 1:
    subjectTxt = subject1
elif subjNumber == 2:
    subjecTxt = subject2
elif subjNumber == 3:
    subjectTxt = subject3
elif subjNumber == 4:
    subjectTxt = subject4
elif subjNumber == 5:
    subjectTxt = subject5

send_email()
