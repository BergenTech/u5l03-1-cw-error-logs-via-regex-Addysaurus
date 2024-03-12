import csv, json, re
with open('logs.json', 'r') as file:
    data = json.load(file)
    with open('error_logs.csv', 'w') as csv_file:
        for i in data:
            if re.search('ERROR', i['level']):
                i['level'] = 'ERROR'
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys(), delimiter=';')
        writer.writeheader()
        writer.writerows([i for i in data if re.search('ERROR', i['level'])])