import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

try:
    res.raise_for_status()
    print('Download succesful')
except Exception as exc:
    print('There was a problem: %s' % (exc))

folder = 'C:\\Users\\ecues\\OneDrive\\Documentos\\03 Academico\\03 Computer Science\\Automation\\Python\\ATBSWP exercises\\Ch11 Web Scraping\\'

destination_file = open(folder + 'RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(100000):
    destination_file.write(chunk)

destination_file.close()