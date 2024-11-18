import requests
from outflank_stage1.bot import BaseBot
from outflank_stage1.implant import Implant

class WebhookNotification(BaseBot):
    WEBHOOK_URL = ""

    def on_new_implant(self, implant: Implant):
        # Prepare the data for the webhook
        title = f"STAGE1 {implant.get_username()} ({implant.get_hostname()})"
        text = (
            f"New beacon:\n\nOS: {implant.get_os()} "
            f"({implant.get_arch()}-bit)\n"
            f"First seen: {implant.get_first_seen().isoformat()}\n"
            f"PID: {implant.get_pid()} ({implant.get_proc_name()})"
        )

        # Create the JSON body
        json_body = {
            "@type": "MessageCard",
            "@context": "http://schema.org/extensions",
            "summary": "New Implant Notification",
            "themeColor": "0078D7",
            "title": title,
            "text": text
        }

        # Send the POST request to the webhook URL
        response = requests.post(
            self.WEBHOOK_URL,
            json=json_body,
            headers={"Content-Type": "application/json"}
        )

        # Check for request success
        if response.status_code != 200:
            raise ValueError(f"Request to webhook returned an error {response.status_code}, the response is:\n{response.text}")

webhook_notification = WebhookNotification()
