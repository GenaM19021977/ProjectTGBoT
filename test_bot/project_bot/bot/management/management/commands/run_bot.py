import asyncio

from django.core.management.base import BaseCommand

from test_bot.project_bot.bot.main_bot import bot


class Command(BaseCommand):
    help = "Запускаем бот"

    def handle(self, *args, **options):
        asyncio.run(bot.polling())
