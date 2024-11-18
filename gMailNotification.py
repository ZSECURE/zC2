import smtplib
import ssl

from outflank_stage1.bot import BaseBot
from outflank_stage1.implant import Implant


class MailNotification(BaseBot):
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SMTP_USERNAME = "<username>@gmail.com"
    SMTP_PASSWORD = "app password goes here"

    FROM_EMAIL = "<username>@gmail.com"
    TO_EMAILS = ["email1"]

    MESSAGE = "Subject: {subject}\n\n{contents}"

    def on_new_implant(self, implant: Implant):
        context = ssl.create_default_context()

        with smtplib.SMTP(MailNotification.SMTP_SERVER, MailNotification.SMTP_PORT) as server:
            server.starttls(context=context)
            server.login(MailNotification.SMTP_USERNAME, MailNotification.SMTP_PASSWORD)

            for receiver_email in MailNotification.TO_EMAILS:
                server.sendmail(
                    MailNotification.FROM_EMAIL,
                    receiver_email,
                    MailNotification.MESSAGE.format(
                        subject=f"STAGE1 {implant.get_username()}" + f"({implant.get_hostname()})",
                        contents=f"New beacon:\n\nOS: {implant.get_os()} "
                        + f"({implant.get_arch()}-bit)\n"
                        + f"First seen: {implant.get_first_seen().isoformat()}\n"
                        + f"PID: {implant.get_pid()} ({implant.get_proc_name()})",
                    ),
                )
