import os

config = {
    "telegram": {

        "default": {
            "token": os.getenv("TELEGRAM_BOT_TOKEN"),
            "url": os.getenv("TELEGRAM_BOT_URL", os.getenv("APP_URL")),

            "webhooks": {
                "url": os.getenv("TELEGRAM_BOT_WEBHOOK_URL", 'webhook/telegram/bot/{token}')
            },
        }        
    }
}