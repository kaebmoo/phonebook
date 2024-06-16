# Phone Book

## โปรแกรมค้นข้อมูลจาก csv ไฟล์ ซึ่งเป็นข้อมูลสมุดโทรศัพท์ โดยสามารถค้นหาได้จาก ชื่อ ชื่อหน่วยงาน email หรือ หมายเลขโทรศัพท์

-   โดยทำงานร่วมกับ telegram bot

-   สามารถลงทะเบียนด้วย email ผ่านทาง telegram bot (/register email
    โปรแกรมจะส่ง activate code ไปทาง email)

-   ผู้ใช้ยืนยัน code ผ่านทาง telegram bot (/activate code)

-   คำสั่งสร้าง bot ด้วย BotFather `/newbot - create a new bot`
จากนั้นก็ทำตามที่ BotFather แนะนำ (ตั้งชื่อ bot, ตั้งชื่อ username ของ bot โดยชื่อต้องไม่ซ้ำ, BotFather จะสร้าง bot ให้และกำหนด token ที่ใช้สำหรับเข้าถึง HTTP API ของ telegram)
                                  
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
-   Create a bot using BotFather: `/newbot` - create a new bot. Then follow the instructions from BotFather (set the bot's name, set a unique username for the bot. BotFather will create the bot and assign a token used for accessing the Telegram HTTP API).

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


                                                                                             
                                                                                          
                                                                                        
                        https://host.domain.com/webhook/xxxxx                           
     telegram server    nginx for reverse proxy                                         
     ┌──────┐          ┌──────┐         ┌───────┐                                       
     │      │          │      │         │       │                                       
     │      │◄────────►│      │         │       │ http://127.0.0.1:8080                 
     │      │          │      │◄───────►│       │ Web hook server NodeJS or Flask       
     └──────┘          └──────┘         └───┬───┘                                       
         ▲                                  │                                           
         │                                  │                                           
         │                                  │                                           
         │                                  │                                           
         │                                  ▼                                           
         │                              ┌───────┐                                       
         │                              │       │                                       
         │                              │       │ mail.server                           
         │                              │       │                                       
         │                              └───┬───┘                                       
         │                                  │                                           
         │                                  │                                           
         │                                  │                                           
         │                                  │                                           
         │                                  │                                           
         │                                  │                                           
         ▼telegram app                      │                                           
      ┌──────┐                              │                                           
      │      │                              │                                           
      │      │  BotFather                   │                                           
      │      │  /newbot - create a new bot  │                                           
      └──────┘                              │                                           
           /register email@address          │                                           
           /activate code  ◄────────────────┘                                           
                                                                                        
                                                                                        