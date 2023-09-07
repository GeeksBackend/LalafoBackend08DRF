from django.core.management.base import BaseCommand

from apps.telegram.views import dp, executor

class Command(BaseCommand):
    def handle(self, *args, **options) :
        print("START BOT")

        executor.start_polling(dp, skip_updates=True)
        # return super().handle(*args, **options)