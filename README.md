# Phone Book

## โปรแกรมค้นข้อมูลจาก csv ไฟล์ ซึ่งเป็นข้อมูลสมุดโทรศัพท์ โดยสามารถค้นหาได้จาก ชื่อ ชื่อหน่วยงาน email หรือ หมายเลขโทรศัพท์

-   โดยทำงานร่วมกับ telegram bot

-   สามารถลงทะเบียนด้วย email ผ่านทาง telegram bot (/register email
    โปรแกรมจะส่ง activate code ไปทาง email)

-   ผู้ใช้ยืนยัน code ผ่านทาง telegram bot (/activate code)

การกำหนด web hook ให้กับ telegram bot ทำได้โดย

-   <https://api.telegram.org/botYOUR_TELEGRAM_BOT_TOKEN/setWebhook?url=YOUR_WEB_APP_URL>

### รายละเอียดไฟล์ .env

```
YOUR_TELEGRAM_BOT_TOKEN=xxxxx token ที่ได้จากการสร้าง telegram bot ใน BotFather
YOUR_CSV_FILE=Phonebook.csv
DEBUG_MODE=false
EMAIL_USER=user@domain.com 
EMAIL_PASS=xxxxx รหัสผ่านของ email ที่จะใช้ส่ง
WEBHOOK_URL=xxxxxxxxxx ใช้เป็น uuid ก็ได้
```

-    `app.js`: โปรแกรมที่ทำด้วย NodeJS
-    `main.py`: โปรแกรมที่ทำด้วย Flask
-    ที่เหลือไม่ได้ใช้ เป็นแค่โปรแกรมตัวอย่าง

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

- `app.js`: NodeJS program.
- `main.py`: Flask program.
- The rest are unused, they are just example programs.
