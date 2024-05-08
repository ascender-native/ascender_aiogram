from asccore.contracts.foundation.application import Application
from asccore.foundation.application import Application
from asccore.foundation.support.providers.route_service import RouteServiceProvider as BaseRouteServiceProvider
from asccore.routing.router import Router
from asccore.main import config

from .controller import WebhookController

from aiogram import Bot
from asccore.foundation.console.console_kernel import ConsoleKernel


class TelegramBotProvider(BaseRouteServiceProvider):

    def __init__(self, app: Application):
        super().__init__(app)
            # Define the path for the webhook which includes a placeholder for the bot token.
        # self.WEBHOOK_PATH = config('bot.telegram.default.webhooks.name')

    # Composite service provider to register all necessary components for the bot
    async def register(self):
        # Method to register console services
        self.register_console()
        # Method to register services necessary for the bot operation
        await self.register_bot()
        # Publish the bot configuration
        self.publish({'ascaiogram.config.bot': 'config.bot'}, 'config')
        
    def register_console(self):
        if isinstance(self.kernel, ConsoleKernel):
            # Load the console module into the kernel
            self.kernel.load('ascaiogram.console')

    async def register_bot(self):
        token = config('bot.telegram.default.token')  # Retrieve the bot token from the configuration
        if token:
            self.app.bind(Bot, lambda: Bot(token=token))  # Register bot services
            # await self.register_webhook(token)  # Setup the webhook

    # Method to register and update the webhook configuration
    async def register_webhook(self, token: str):
        bot: Bot = self.app.make(Bot)
        # webhook_info = await bot.get_webhook_info()

        # telegram_url = config('bot.telegram.default.url')
        # webhook_url = f"{telegram_url}/{self.WEBHOOK_PATH.replace('{token}', token)}"
        # if webhook_info.url != webhook_url:
        #     info = await bot.set_webhook(url=webhook_url)  # Update the webhook if necessary
        #     print(info)