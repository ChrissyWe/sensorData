from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime, timedelta

gauth = GoogleAuth(settings_file='/wetter-screen/driveData/settings.yaml')
#gauth.DEFAULT_SETTINGS['client_config_file'] = 'C:\\Users\\Chris\\Documents\\Semester_8\\Bundesgartenschau\\Credentials.json'
drive = GoogleDrive(gauth)

#gfile = drive.CreateFile({'title': 'allgemeine-informationen.txt','parents': [{'id': '1NggFkhUZ1LmAEObTvGU7H9sfLc9QKW-B'}]})
#gfile.SetContentFile('C:\\Users\\Chris\\Documents\\Semester_8\\Bundesgartenschau\\allgemeine-informationen.txt')
#gfile.Upload()

#file = drive.CreateFile({'id': '1H2gFWfNR_tKqlj7HGooZQZy9iZOC-QLt'})
#content_string = file.getContentString()

#print(content_string)
#file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format('1NggFkhUZ1LmAEObTvGU7H9sfLc9QKW-B')}).GetList()
#for file in file_list:
#	print('title: %s, id: %s' % (file['title'], file['id']))

file7 = drive.CreateFile({'id': '1MUtalibYpvJ1FBHQGzDC4wEW19xL0wZw'})
content = file7.GetContentString()
print(content)
#file = drive.CreateFile({'id': '1NggFkhUZ1LmAEObTvGU7H9sfLc9QKW-B'})
#file.GetContentFile('test.txt')