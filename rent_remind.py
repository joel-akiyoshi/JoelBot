import json
from send_email import send_from_joelbot
from pathlib import Path
import datetime

now = datetime.datetime.now()

script_dir = Path(__file__).parent
config_file_path = script_dir / "config/config.json"

absolute_config_path = config_file_path.resolve()

with open(absolute_config_path, "r") as config_file:
    config = json.load(config_file)

email_user = config["EMAIL_USER"]
email_password = config["EMAIL_PASSWORD"]
zelle = config["ZELLE"]
venmo = config["VENMO"]
recipients = config["RENT_RECIPIENTS"]

subject = "Monthly Bill Reminder"
html_body = f"""
<html>
  <body>
    <p>This is an automated reminder regarding the monthly apartment fees.</p>
    <ol>
      <li><strong>Verify Payment</strong>: Double check that payment went through via All at Home. </li>
      <br>
      <li><strong>Utilities Bill</strong>: One person needs to pay the utilities bill using the following link: <a href="https://resident.irvinecompanyapartments.com/s">All At Home</a>. Others will reimburse as needed. Do this BEFORE {now.month}-3-{now.year}.</li>
      <br>
      <li><strong>Electricity Bill</strong>: Joel will cover the electricity bill. Reimbursement can be sent via Zelle or Venmo. Joel's payment details are as follows:
        <ul>
          <li><strong>Zelle</strong>: Joel's Zelle: {zelle}</li>
          <li><strong>Venmo</strong>: Joel's Venmo: {venmo}</li>
        </ul>
      </li>
    </ol>
    <p>-JoelBot</p>
  </body>
</html>
"""

for recipient in recipients:
    send_from_joelbot(email_user, email_password, recipient, subject, html_body)
