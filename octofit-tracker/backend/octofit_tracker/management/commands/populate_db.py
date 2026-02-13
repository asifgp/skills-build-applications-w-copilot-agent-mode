from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel.name),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel.name),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc.name),
            User(name='Batman', email='batman@dc.com', team=dc.name),
        ]
        for user in users:
            user.save()

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date='2026-02-13')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date='2026-02-12')
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date='2026-02-11')
        Activity.objects.create(user=users[3], type='Yoga', duration=40, date='2026-02-10')

        # Create workouts
        Workout.objects.create(name='Cardio Blast', description='High intensity cardio', suggested_for='Marvel')
        Workout.objects.create(name='Strength Builder', description='Strength training', suggested_for='DC')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
