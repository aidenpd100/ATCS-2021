games = ['monopoly', 'soccer', 'rocket league']

print('I like to play ' + games[0] + ', ' + games[1] + ', and ' + games[2])

new_game = input('What is a game that you like? (enter "done" to end your list) ')
while new_game != 'done':
    games.append(new_game)
    new_game = input('What is a game that you like? (enter "done" to end your list) ')

print('We like to play ', end='')
for game in games:
    if game == games[-1]:
        print('and ' + game)
    else:
        print(game + ', ', end='')

