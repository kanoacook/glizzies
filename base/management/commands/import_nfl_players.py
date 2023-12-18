# from django.core.management.base import BaseCommand, CommandError
# from cbackend.base.models import NFLPlayers  # Replace with your actual model
# import requests

# class Command(BaseCommand):
#     help = 'Import NFL players data into the database'

#     def handle(self, *args, **options):
#     # def load_nfl_players(self):
#         try:
#             # Fetch data from API
#             response = requests.get("https://api.sleeper.app/v1/players/nfl/")
#             if response.status_code != 200:
#                 print("Failed to fetch data from the API")
#                 return

#             # Parse and process the data
#             players_data = response.json()
#             for player_id, player in players_data.items():
#                 if player.get('active') and player.get('sport') == 'nfl':
#                     # Extract the required fields
#                     player_data = {
#                         'first_name': player.get('first_name'),
#                         'last_name': player.get('last_name'),
#                         'search_first_name': player.get('search_first_name'),
#                         'search_last_name': player.get('search_last_name'),
#                         'team': player.get('team'),
#                         'fantasy_positions': player.get('fantasy_positions'),
#                         'stats_id': player.get('stats_id'),
#                         'yahoo_id': player.get('yahoo_id'),
#                         'player_id': player.get('player_id'),
#                         'espn_id': player.get('espn_id'),
#                         'oddsjam_id': player.get('oddsjam_id'),
#                         'gsis_id': player.get('gsis_id'),
#                         'sportradar_id': player.get('sportradar_id'),
#                         'rotowire_id': player.get('rotowire_id'),
#                         'rotoworld_id': player.get('rotoworld_id'),
#                         'pandascore_id': player.get('pandascore_id'),
#                         'fantasy_data_id': player.get('fantasy_data_id'),
#                     }

#                     # Load data into Django Database
#                     NFLPlayers.objects.update_or_create(player_id=player_id, defaults=player_data)

#             print("NFL players data loaded successfully")

#             self.stdout.write(self.style.SUCCESS('Successfully imported NFL players data'))

#         except Exception as e:
#             raise CommandError(f'Error occurred: {e}')


from django.core.management.base import BaseCommand,CommandError
from ...models import NFLPlayers  # Change 'myapp' to the name of your Django app
import requests

class Command(BaseCommand):
    help = 'Load a NFLPlayers data from a CSV file'

    def handle(self, *args, **options):
        try:
            # Fetch data from API
            response = requests.get("https://api.sleeper.app/v1/players/nfl/")
            if response.status_code != 200:
                print("Failed to fetch data from the API")
                return

            # Parse and process the data
            players_data = response.json()
            for player_id, player in players_data.items():
                if player.get('active') and player.get('sport') == 'nfl':
                    # Extract the required fields
                    player_data = {
                        'first_name': player.get('first_name'),
                        'last_name': player.get('last_name'),
                        'search_first_name': player.get('search_first_name'),
                        'search_last_name': player.get('search_last_name'),
                        'team': player.get('team'),
                        'fantasy_positions': player.get('fantasy_positions'),
                        'stats_id': player.get('stats_id'),
                        'yahoo_id': player.get('yahoo_id'),
                        'player_id': player.get('player_id'),
                        'espn_id': player.get('espn_id'),
                        'oddsjam_id': player.get('oddsjam_id'),
                        'gsis_id': player.get('gsis_id'),
                        'sportradar_id': player.get('sportradar_id'),
                        'rotowire_id': player.get('rotowire_id'),
                        'rotoworld_id': player.get('rotoworld_id'),
                        'pandascore_id': player.get('pandascore_id'),
                        'fantasy_data_id': player.get('fantasy_data_id'),
                    }

                    # Load data into Django Database
                    NFLPlayers.objects.update_or_create(player_id=player_id, defaults=player_data)

            print("NFL players data loaded successfully")

            self.stdout.write(self.style.SUCCESS('Successfully imported NFL players data'))

        except Exception as e:
            raise CommandError(f'Error occurred: {e}')
