from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.timezone import now, timedelta

class Command(BaseCommand):
    help = 'Outputs a report of all users who have logged in within the last month'

    def handle(self, *args, **kwargs):
        one_month_ago = now() - timedelta(days=30)
        recent_users = User.objects.filter(last_login__gte=one_month_ago)

        if recent_users.exists():
            self.stdout.write('Users who have logged in within the last month:\n')
            for user in recent_users:
                self.stdout.write(f'Username: {user.username}, Last Login: {user.last_login}')
        else:
            self.stdout.write('No users have logged in within the last month.')
