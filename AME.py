import smtplib
import ssl
import csv
from email.message import EmailMessage

def email_send(email_receiver, reg_num, room_num, bldg_num):

    # Define email sender and credentials
    email_sender = 'mehnajhridi@gmail.com'
    email_password = 'kbfg inrv wqiv ilib'
    port = 587
    smtp_server = "smtp.gmail.com"

    # Set the subject and body of the email
    subject = 'Confirmation Email'
    body = f"""
    Dear Participants,

    We are delighted to confirm your registration for the Bangladesh National Girls' Mathematics Olympiad 2023, scheduled to take place at Brac University, Mohakhali branch. Your enthusiasm for this event is truly appreciated.

    Here are the important details and guidelines:

    Date: 22 September, 2023
    Venue: Brac University, Mohakhali branch

    Registration and Event Details:

    - Registration Number : {reg_num}
    - Buildging Number : {bldg_num}
    - Room Number : {room_num}

    Important Instructions : 

    - Please ensure you bring proof of your student identity, such as your school ID card, school fee receipt, or any other relevant document.
    - Print out this email and bring it with you as proof of your registration.
    - Bring your own pencil/geometry box. - Calculators are not allowed.
    - Bring your own Rubics cube if you want to participate in the Rubics Cube competition. 
    - Wearing your school uniform is optional.
    - Parents are not allowed inside the campus during the event.

    Event Day Schedule:
    - 8:00 am - 9:00 am: Student arrival in front of Building 2
    - 9:00 am - 10:00 am: Opening ceremony at Building 2 auditorium
    - 10:00 am - 12:30 pm: Exam time
    - 12:30 pm - 2:30 pm: Namaz and lunch break
    - 2:30 pm - 3:30 pm: Activities and cultural event
    - 3:30 pm - 5:00 pm: Closing ceremony

    Please make sure to follow the schedule, and be punctual to ensure a smooth and successful event.

    If you have any questions or require further assistance, please do not hesitate to contact us at 
    1. Walid Hasan Suprov - +880**********
    2. Mehnaj Hridi - ***********

    We extend our best wishes to you for the Olympiad, and we look forward to your participation at Brac University on 22 September.

    Warm regards,

    Gonitkonya, Bangladesh Girls' Mathematics Foundation"""

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Try to log in to the server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_receiver, em.as_string())
        print(f"Email sent to {email_receiver}")
    except Exception as e:
        # Print any error messages to stdout
        print(f"Failed to send email to {email_receiver}: {e}")
    finally:
        server.quit()

# Read emails and other information from a CSV file
#with open('test.csv', newline='') as csvfile:
    #reader = csv.reader(csvfile)
    #next(reader)  # Skip header row if present
    

import csv

with open("C:\\Users\\ASUS\\Desktop\\Automated Email\\Book2.csv", 'r') as file:
  csvreader = csv.reader(file)
    
  for row in csvreader:
            email_receiver = row[0]  # Assuming email addresses are in the first column
            reg_num = row[1]  # Assuming registration numbers are in the second column
            room_num = row[2]  # Assuming room numbers are in the third column
            bldg_num = row[3]  # Assuming building numbers are in the fourth column
            email_send(email_receiver, reg_num, room_num, bldg_num)
