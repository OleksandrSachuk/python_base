from urllib import request

csv_url = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'


def download_file(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split('\\n')
    dest_url = r'csv.csv'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + '\n')
    fx.close()


download_file(csv_url)
