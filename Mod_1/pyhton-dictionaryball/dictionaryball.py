game_dictionary = {'home': {'team_name': 'Brooklyn Nets',
                            'colors': ['Black', 'White'],
                            'players': {'Alan Anderson': {
                                            'number': 0,
                                            'shoe': 16,
                                            'points': 22,
                                            'rebounds': 12,
                                            'assists': 12,
                                            'steals': 3,
                                            'blocks': 1,
                                            'slam_dunks': 1
                                        },
                                        'Reggie Evans': {
                                            'number': 30,
                                            'shoe': 14,
                                            'points': 12,
                                            'rebounds': 12,
                                            'assists': 12,
                                            'steals': 12,
                                            'blocks': 12,
                                            'slam_dunks': 7
                                        },
                                        'Brook Lopez': {
                                            'number': 11,
                                            'shoe': 17,
                                            'points': 17,
                                            'rebounds': 19,
                                            'assists': 10,
                                            'steals': 3,
                                            'blocks': 1,
                                            'slam_dunks': 15
                                        },
                                        'Mason Plumlee': {
                                            'number': 1,
                                            'shoe': 19,
                                            'points': 26,
                                            'rebounds': 12,
                                            'assists': 6,
                                            'steals': 3,
                                            'blocks': 8,
                                            'slam_dunks': 5
                                        },
                                        'Jason Terry': {
                                            'number': 31,
                                            'shoe': 15,
                                            'points': 19,
                                            'rebounds': 2,
                                            'assists': 2,
                                            'steals': 4,
                                            'blocks': 11,
                                            'slam_dunks': 1
                                        }
                                        }},
                    'away': {'team_name': 'Charlotte Hornets',
                            'colors': ['Turquoise', 'Purple'],
                            'players': {'Jeff Adrien': {
                                            'number': 4,
                                            'shoe': 18,
                                            'points': 10,
                                            'rebounds': 1,
                                            'assists': 1,
                                            'steals': 2,
                                            'blocks': 7,
                                            'slam_dunks': 2
                                        },
                                        'Bismak Biyombo': {
                                            'number': 0,
                                            'shoe': 16,
                                            'points': 12,
                                            'rebounds': 4,
                                            'assists': 7,
                                            'steals': 7,
                                            'blocks': 15,
                                            'slam_dunks': 10
                                        },
                                        'DeSagna Diop': {
                                            'number': 2,
                                            'shoe': 14,
                                            'points': 24,
                                            'rebounds': 12,
                                            'assists': 12,
                                            'steals': 4,
                                            'blocks': 5,
                                            'slam_dunks': 5
                                        },
                                        'Ben Gordon': {
                                            'number': 8,
                                            'shoe': 15,
                                            'points': 33,
                                            'rebounds': 3,
                                            'assists': 2,
                                            'steals': 1,
                                            'blocks': 1,
                                            'slam_dunks': 0
                                        },
                                        'Brendan Haywood': {
                                            'number': 33,
                                            'shoe': 15,
                                            'points': 6,
                                            'rebounds': 12,
                                            'assists': 12,
                                            'steals': 22,
                                            'blocks': 5,
                                            'slam_dunks': 12
                                        }}}}
def game_dict():
    return game_dictionary
def good_practices():
      for location, team_stats in game_dict().items():
            

    # are you ABSOLUTELY SURE what 'location' and 'team_stats' are? use pdb.set_trace() to find out!
#         import pdb; pdb.set_trace()
        for stats, data in team_stats.items():
#             print(team_stats[stats])
        # are you ABSOLUTELY SURE what 'stats' and 'data' are? use pdb.set_trace() to find out!
#             import pdb; pdb.set_trace()
        # what is 'data' at each level of the for loop block? when will we be able to iterate through a list? 
        # When would the following line of code break?
            for item in data:
                print(data[item])

# print(good_practices())


# def find_stat(player_name, stat):
#     for location, team_stats in game_dict().items():
#         for stats, data in team_stats.items():
#             for item in data:
#                 if item == player_name:
#                     return game_dict()[location][stats][item][stat]

# def num_points_scored(player_name): 
#     return find_stat(player_name, 'points')


# def shoe_size(player_name):
#     return find_stat(player_name, 'shoe')

    
# # print(shoe_size('Reggie Evans'))
# def team_colors(team_name):
#     for location, team_stats in game_dict().items():
#         for stats, data in team_stats.items():
#             if data == team_name:
#                 return game_dict()[location]['colors']
            
# def team_names():
#     names = []
#     for location, team_stats in game_dict().items():
#          for stats, data in team_stats.items():
#                 if data == team_name:
#         name = game_dict()[location][stats]
#         names.append(name)
#     return names
# # print(team_names(
# # def player_numbers():
# #Build a function, player_numbers, that takes in an argument of a team name and returns a list of the jersey number's for that team
# def player_numbers():
#     names = []
#     for location, team_stats in game_dict().items():
#          for stats, data in team_stats.items():
#                 if data == team_name:
#                     print(data)
                
    





      