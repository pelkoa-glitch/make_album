def make_album(singer_name, album_name, number_of_tracks = None):
	"""Возвращает словарь с информацией об исполнителе, названии альбома,
	 и колличестве композиций, если оно указано."""
	album_info = {'singer': singer_name, 'album': album_name}
	
	if number_of_tracks:
		album_info['number of tracks'] = number_of_t
	return album_info


Poll = True
singers_list = []


while Poll:
	'''Cобирает список со словарями из функции "make_album".'''
	
	print("\nPlease tell me singer and album name:")
	print("\t(enter 'q' at any time to quit)")
	print("\t(enter 's' at any time to see album_info)\n")

	s_name = input("Singer name: ")
	if s_name == 'q':
		break
	if s_name == 's':
		Poll = False	
		continue
	
	a_name = input("Album name: ")
	if a_name == 'q':
		break
	if a_name == 's':
		Poll = False
		continue
	
	number_of_t = input("Number of tracks: ")
	if number_of_t == 'q':
		break	
	if number_of_t == 's':
		Poll = False
		continue	
	
	singers_list.append(make_album(s_name, a_name, number_of_t))
	'''Собирает словари с инфой об исполнителе в список.'''
else:
	'''Выводит собранную инфу.'''	
	print("\n\nAlbum's info: ")
	print('')
	for i in singers_list:	
		for key, value in i.items():
			key_value = '\t' + str(key.capitalize()) + ': ' + str(value.title())
			print(key_value)
		print('')			

print('Bye!')
                
