workingList = ['programmer', 'truck driver', 'doctor', 'lawyer']

print('Index of "truck driver": ' + str(workingList.index('truck driver')))
print('"truck driver" in list: ' + str('truck driver' in workingList))

workingList.append('dentist')
workingList.insert(0, 'physical therapist')

print('\nUpdated list: ')
for career in workingList:
    print(career)