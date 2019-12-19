import urllib.request

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = "https://www.melhorcambio.com/dolar-canadense-hoje"
headers = {'User-Agent': user_agent, }

request = urllib.request.Request(url, None, headers)
response = urllib.request.urlopen(request).read()
response = str(response)

find = '<input type="hidden" value="'
posicao = int(response.index(find) + len(find))
dolar = response[posicao: posicao + 4]

print(f'O valor do dolar é {dolar}')
