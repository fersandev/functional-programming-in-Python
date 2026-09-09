from core.signup.services import process_emails

def process_signups(filepath):
    with open(filepath) as f:
        lines = f.readlines()

    valid_emails = process_emails(lines)

    print(f"{len(valid_emails)} valid emails from {len(lines)}")

    with open("valid_emails.txt", "w") as f:
        for email in valid_emails:
            f.write(email + "\n")

    return valid_emails
