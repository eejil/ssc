import json, os, sys

if "list" in sys.argv:

	os.system('touch /Users/sylvain/Desktop/ISEN/Cyber/list.json && rm /Users/sylvain/Desktop/ISEN/Cyber/list.json')
	os.system('cat /Users/sylvain/Desktop/ISEN/Cyber/tmp_list.json | /usr/local/bin/jq .items[0].value.stdout >> /Users/sylvain/Desktop/ISEN/Cyber/tmp2_list.json')

	with open('/Users/sylvain/Desktop/ISEN/Cyber/tmp2_list.json', 'r') as file:
    		list = file.read().replace('\n',' ')
    		list = list.replace('\\n',' ')
    		list = list.replace('"','')
    		list = list.split()

	data = {}
	data = []

	i = 0
	for j in range(0,int( len(list) / 2)):
    		data.append({
        	'software': list[i],
        	'actualversion': list[i+1],
    		})
    		i = i + 2

	with open('/Users/sylvain/Desktop/ISEN/Cyber/list.json', 'w') as outfile:
    		json.dump(data, outfile)

	os.system('rm /Users/sylvain/Desktop/ISEN/Cyber/tmp_list.json')
	os.system('rm /Users/sylvain/Desktop/ISEN/Cyber/tmp2_list.json')

if "upgrade" in sys.argv:

	os.system('touch /Users/sylvain/Desktop/ISEN/Cyber/upgrade.json && rm /Users/sylvain/Desktop/ISEN/Cyber/upgrade.json')
	os.system('cat /Users/sylvain/Desktop/ISEN/Cyber/tmp_upgrade.json | /usr/local/bin/jq .items[0].value.stdout >> /Users/sylvain/Desktop/ISEN/Cyber/tmp2_upgrade.json')

	with open('/Users/sylvain/Desktop/ISEN/Cyber/tmp2_upgrade.json', 'r') as file:
    		list = file.read().replace('\n',' ')
    		list = list.replace('\\n',' ')
    		list = list.replace('"','')
    		list = list.split()

	data = {}
	data = []

	i = 0
	for j in range(0,int( len(list) / 3)):
    		data.append({
        	'software': list[i],
        	'actualversion': list[i+1],
		'updateversion': list[i+2]
    		})
    		i = i + 3

	with open('/Users/sylvain/Desktop/ISEN/Cyber/upgrade.json', 'w') as outfile:
    		json.dump(data, outfile)

	os.system('rm /Users/sylvain/Desktop/ISEN/Cyber/tmp_upgrade.json')
	os.system('rm /Users/sylvain/Desktop/ISEN/Cyber/tmp2_upgrade.json')
