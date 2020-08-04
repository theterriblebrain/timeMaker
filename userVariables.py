#!/usr/bin/python3

#USER VARIABLES:
recipientName = "Jim"
senderName = "Bill"
secondaryName = "Taylor"
senderEmailName = "Bill Smith <bill@billsmithemail.com>" #formatted so receiving email client shows the name of the sender
testRecipients = ['bill@billsmithemail.com', 'bill@billsotheremail.com', 'bill@anotheroneofbillsemails.com'] #for testing
recipients = ['steve@billssgo.com', 'jason@billssgosassistant.com', 'bill@billsmithemail.com'] #live

#ABOUT THE USER VARIABLES SECTION
# It is recommended that you include yourself in the recipient list so you have a record.
# Add as many email addresses as needed.

#SMTP SETTINGS VARIABLES
smtpHost='smtp.example.com'
smtpPort=587
smtpUser='bill@billsmithemail.com'
smtpPassword='billsPassword'

#AVERAGES VARIABLES
import random
primaryTime = str(random.randint (4, 9)) #enter the average hours in a range, [low, high]
primaryPlacements = str(random.randint (0, 0)) #enter the average placements in a range, [low, high]
primaryStudies =  str(random.randint (1, 1)) #enter the average studies in a range, [low, high]
primaryRvs = str(random.randint (4, 4)) #enter the average rvs in a range, [low, high]
#secondary reporter
secondaryTime = str(random.randint (1, 5)) #enter the average hours in a range, [low, high]
secondaryPlacements = str(random.randint (0, 0)) #enter the average placements in a range, [low, high]
secondaryStudies = str(random.randint (0, 0)) #enter the average studies in a range, [low, high]
secondaryRvs = str(random.randint (0, 0)) #enter the average rvs in a range, [low, high]

#ABOUT THE AVERAGES SECTION
# Secondary averages are for turning in another person's time along with yours (this program was
# written to turn in the author and his son's time.)
# Edit this section according to your needs. The current values reflect the author's needs.
# Keep in mind that you will most likely need to edit the text in the messages in the main file
# to meet your individual needs.
# If you need the number to stay the same month-to-month, format the average like: "1, 1" or "2, 2".
