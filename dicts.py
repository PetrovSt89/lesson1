dicts={'city': 'Москва', 'temperature': '20'}
print(dicts['city'])
dicts['temperature']=str(int(dicts['temperature'])-5)
print(dicts)

print('country' in dicts)
dicts['country']='Россия'
dicts['date'] = '27.05.2019'
print(len(dicts))
