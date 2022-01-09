
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print(
    """Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details"""
)
APP_ID = int(input("Enter APP ID here: "12196082")
API_HASH = input("Enter API HASH here: "6520184457ed0a6b7fb6f40269350c20")

with TelegramClient(StringSession("1AZWarzsBuz8f7SbfUCb38Nun8KMUXJpBWDwkxOpXUqqfhzLRfXr_cIfM7BWeUQdYRwpnE46srOUuOQqq8l6F7ACE3nG-1tVoCK-xFLD7nsS4Xi-JD2exGkTIYgn00MXODJLCocVBVpIK1P33MaZWCFwA_MAml_NdftpRRzG8gM4H4vM8Fnit9lkWrXPiMdPBQPynAzoquC_VLFKAs8272yM-EmG1lFTcJymOwzF7W0KVK4nfimapgo6DGK0gzUrjZ56b7Yd9y5ss2cwlS7M5C44SYfOg8Ux6f6ifiV-ycL1KrhOhxtqEvAZWyZ5VRASC2IGWEk6bLCUI17V3cOqWhpW_vVoRHHo="), APP_ID, API_HASH) as client:
    print(client.session.save())
    client.send_message("me", client.session.save())
