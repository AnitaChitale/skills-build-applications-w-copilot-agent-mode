from django.core.management.base import BaseCommand
from core.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='Team DC Superheroes')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create workouts
        run = Workout.objects.create(name='Running', description='Run fast!', difficulty='Medium')
        lift = Workout.objects.create(name='Weight Lifting', description='Lift heavy weights', difficulty='Hard')

        # Create activities
        Activity.objects.create(user=users[0], workout=run, date=timezone.now(), duration_minutes=30, calories_burned=300)
        Activity.objects.create(user=users[1], workout=lift, date=timezone.now(), duration_minutes=45, calories_burned=500)
        Activity.objects.create(user=users[2], workout=run, date=timezone.now(), duration_minutes=25, calories_burned=250)
        Activity.objects.create(user=users[3], workout=lift, date=timezone.now(), duration_minutes=60, calories_burned=600)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, total_points=800)
        Leaderboard.objects.create(team=dc, total_points=850)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data!'))
