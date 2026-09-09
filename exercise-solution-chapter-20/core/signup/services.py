def is_valid_email(email):
    return "@" in email and "." in email.split("@")[1]

def normalize_email(email):
    return email.strip().lower()

def process_emails(lines):
    valid_emails = []
    for line in lines:
        email = normalize_email(line)
        if is_valid_email(email):
            valid_emails.append(email)
    return valid_emails
