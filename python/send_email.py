# Copyright  2020  Edoardo Riggio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def send_email(reciever, body):
    strFrom = 'officialercapps@gmail.com'
    strTo = reciever

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Your Daily COVID-19 Update'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo

    msgAlternative = MIMEMultipart('alternative')
    msgAlternative['Subject'] = 'Your Daily COVID-19 Update'
    msgAlternative['From'] = strFrom
    msgAlternative['To'] = strTo
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('Your Daily COVID-19 Update')
    msgAlternative.attach(msgText)

    msgText = MIMEText(body, 'html')
    msgAlternative.attach(msgText)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login()
    s.sendmail(strFrom, strTo, msgText.as_string())
    s.quit()

    # # This example assumes the image is in the current directory
    # fp = open('test.jpg', 'rb')
    # msgImage = MIMEImage(fp.read())
    # fp.close()

    # # Define the image's ID as referenced above
    # msgImage.add_header('Content-ID', '<image1>')
    # msgRoot.attach(msgImage)

    # s = smtplib.SMTP('smtp-relay.sendinblue.com', 587)
    # s.starttls()
    # s.login()
    # message = "Message_you_need_to_send"
    # s.sendmail(strFrom, strTo, message)
    # s.quit()