mountains = {'Mount Everest': 29029,
             'K2': 28251,
             'Kangchenjunga': 28169,
             'Lhotse': 27940,
             'Makalu': 27838
             }

print(sorted(mountains.keys()))
print('Mountain names: ', end='')
for mountain in sorted(mountains.keys()):
    if mountain == sorted(mountains.keys())[-1]:
        print('and ' + mountain)
    else:
        print(mountain + ', ', end='')

print('\nMountain elevations: ', end='')
for elevation in sorted(mountains.values()):
    if elevation == sorted(mountains.values())[-1]:
        print('and ' + str(elevation) + ' feet')
    else:
        print(str(elevation) + ' feet, ', end='')

print('\nMountain names and elevations: ')
for name, elevation in mountains.items():
    print(name + ' is ' + str(elevation) + ' feet tall.')
