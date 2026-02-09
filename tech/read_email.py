import imaplib
import email
from email.header import decode_header

# Configs
EMAIL = "zeus.ia.agent@gmail.com"
PASSWORD = "fmtf ixkt ybrp ngue"
SMTP_SERVER = "imap.gmail.com"

def read_latest_email():
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")

    # Search for latest unread
    status, messages = mail.search(None, 'UNSEEN')
    if not messages[0]:
        # No new emails, exit silently
        mail.close()
        mail.logout()
        return

    mail_ids = messages[0].split()
    latest_id = mail_ids[-1]

    status, msg_data = mail.fetch(latest_id, "(RFC822)")
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding if encoding else "utf-8")
            
            print(f"Subject: {subject}")
            
            # Extract body
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        print("Body:", part.get_payload(decode=True).decode())
                        break
            else:
                print("Body:", msg.get_payload(decode=True).decode())

    mail.close()
    mail.logout()

if __name__ == "__main__":
    read_latest_email()
