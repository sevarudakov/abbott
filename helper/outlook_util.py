import imaplib
import email
import logging
import re
import time


class OutlookUtil:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.imap_url = 'imap-mail.outlook.com'
        self.mail = None

    def login(self):
        logging.info(f"Login to '{self.imap_url}' with email '{self.username}' and password' {self.password}'")
        self.mail = imaplib.IMAP4_SSL(self.imap_url)
        self.mail.login(self.username, self.password)

    def logout(self):
        logging.info("Logout outlook")
        self.mail.logout()

    def get_verification_code(self, timeout=60):
        logging.info("Get verification code")
        start_time = time.time()
        while True:
            self.login()
            self.mail.select('inbox')
            typ, data = self.mail.search(None, 'UNSEEN')
            for num in data[0].split():
                typ, data = self.mail.fetch(num, '(RFC822)')
                raw_email = data[0][1]
                email_message = email.message_from_bytes(raw_email)
                if email_message['From'] == 'LibreView <do-not-reply@libreview.io>':
                    match = re.search(r'Your security code is: (\d{6})', email_message.get_payload()[0].as_string())
                    if match:
                        verification_code = match.group(1)
                        self.mail.store(num, '+FLAGS', '\\Seen')
                        self.logout()
                        return verification_code

            self.logout()

            elapsed_time = time.time() - start_time
            if elapsed_time >= timeout:
                break

            time.sleep(5)  # Wait for 5 seconds before checking again

        return None
