# timeMaker
ABOUT:
 This is an automatic time sender program by u/theterriblebrain - there is no license or
 claim of ownership or copyright etc. Responsibility for any resulting DF / reproof / bothered
 conscience belongs to the user not the creator.

 The purpose of this program is allow you to automate the sending of time to one's SGO(s).
 This program picks the quantity of hours, placements, studies and rvs from a specified
 average (see average variables section below), and emails them to the specified email
 recipients (see user variables below).

 This program simulates non-automated messages by randomly picking between 5 variations
 of subjects, and 5 variations of message bodies.

 This program only uses Python's built in libraries; no additional installations are required.

 You should be able to (a) install Python, (b) fill in the variables, and sucessfully run
 the script and send your time. You can add the script to a cron job (Linux) or a Scheduled
 Task (Windows) so that your time is turned in automatically each month.

INSTRUCTIONS:
 1. Edit userVariables.py to specify smtp settings and other user variables.
 2. Review / edit the messages and subjects in generate.py, or any other part of this program
    to meet your individual needs.
 3. Either run the program manually each month to turn in your time, or set up
    a cron job / scheduled task to run it automatically each month.
