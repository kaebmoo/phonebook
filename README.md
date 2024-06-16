# Phone Book

## โปรแกรมค้นข้อมูลจาก csv ไฟล์ ซึ่งเป็นข้อมูลสมุดโทรศัพท์ โดยสามารถค้นหาได้จาก ชื่อ หน่วยงาน email หรือ โทรศัพท์

-   โดยทำงานร่วมกับ telegram bot

-   สามารถลงทะเบียนด้วย email ผ่านทาง telegram bot (/register email
    โปรแกรมจะส่ง activate code ไปทาง email)

-   ผู้ใช้ยืนยัน code ผ่านทาง telegram bot (/activate code)

การกำหนด web hook ให้กับ telegram bot ทำได้โดย

-   <https://api.telegram.org/botYOUR_TELEGRAM_BOT_TOKEN/setWebhook?url=YOUR_WEB_APP_URL>

### รายละเอียดไฟล์ .env

```
YOUR_TELEGRAM_BOT_TOKEN=xxxxx # token obtained from creating a Telegram bot in BotFather
YOUR_CSV_FILE=Phonebook.csv
DEBUG_MODE=false
EMAIL_USER=user@domain.com
EMAIL_PASS=xxxxx # password of the email used for sending
WEBHOOK_URL=xxxxxxxxxx # can use a UUID
```


# Phone Book

## A CSV-based phone book search program that allows searching by name, department, email, or phone number.

-   Integrated with a Telegram bot for user interaction.

-   User registration via Telegram bot using email (`/register email`) to receive an activation code.

-   User activation through the Telegram bot (`/activate code`).

### Setting up a Webhook for the Telegram Bot

-   Use the following URL: `https://api.telegram.org/botYOUR_TELEGRAM_BOT_TOKEN/setWebhook?url=YOUR_WEB_APP_URL`

### .env File Details

```
YOUR_TELEGRAM_BOT_TOKEN=xxxxx (token obtained from creating a Telegram bot in BotFather)
YOUR_CSV_FILE=Phonebook.csv
DEBUG_MODE=false
EMAIL_USER=user@domain.com
EMAIL_PASS=xxxxx (password of the email used for sending)
WEBHOOK_URL=xxxxxxxxxx (can use a UUID)
```