import smtplib
import urllib.request as urllib
# Senders email
sender_email = "vishesh8199@gmail.com"
# Receivers email
rec_email = "vishesh8199@gmail.com"

message = "Best Model is being created... Thank You"
# Initialize the server variable
server = smtplib.SMTP('smtp.gmail.com', 587)
# Start the server connection
server.starttls()
# Login
server.login("shivamguptasparklev@gmail.com", "garg9462885915")
print("Login Success!")
# Send Email
server.sendmail("Shivam Gupta", "shivamguptasg1808@gmail.com", message)
print(f"Email has been sent successfully to {rec_email}")