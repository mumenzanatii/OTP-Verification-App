import random
import smtplib

# Generate a random 6-digit OTP
otp = random.randint(100000, 999999)

# Configure the email details
sender_email = "justformyapp@outlook.com"
sender_password = "momenzanatii98"
receiver_email = input("Please enter your email address: ")
email_subject = "OTP Verification"
message = f"You OTP is {otp}"

# SMTP email details
smtp_server = "smtp-mail.outlook.com"
smtp_port = 587

# SMTP login with the sender_email and sender_password
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, sender_password)

# Sending the OTP
server.sendmail(sender_email, receiver_email,
                f"Subject: {email_subject}\n\n{message}")
print(f"OTP sent successfully to {receiver_email}")

# Verifying the user OTP input
user_otp = input("Enter the OTP received: ")
if int(user_otp) == otp:
    print("Verification Successful!")
else:
    print("Incorrect OTP, Please try again")
