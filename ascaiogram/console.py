from asccore.main import cli, click, config, app
from typing import Any

from asccore.routing.router import Router
from aiogram import Bot

import asyncio

@cli.command("bot.register")
@click.argument('url', required=False)
@click.option('--ip_address')
@click.option('--max_connections')
@click.option('--secret_token')
def set_webhook_telegram(url: str|None = None, ip_address: str|None = None,  max_connections: int|None = None, 
                         secret_token: str|None = None, bot: Bot=None, **extra_data: Any):
    secret_token = secret_token or config('bot.telegram.default.token')
    url = url or app.make(Router).url('webhook.bot.telegram', token=secret_token)
    bot = bot or app.make(Bot)

    set_webhook_task = bot.set_webhook(
        url=url, 
        ip_address=ip_address, 
        max_connections=max_connections, 
        secret_token=secret_token, 
        **extra_data
    )

    asyncio.run(set_webhook_task)
    