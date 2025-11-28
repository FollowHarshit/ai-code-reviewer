class user:
    def __init__(self, n, e):
        self.n = n
        self.e = e

    def save(self):
        print(f"Saving user {self.n} to database...")
        # Imagine SQL code here

    def send_email(self, msg):
        print(f"Sending email to {self.e}: {msg}")

# This violates Single Responsibility Principle (SRP) 
# because the User class handles logic, database, AND email.
