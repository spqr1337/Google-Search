import re 
import requests 

src = input("Entre com o termo a ser pesquisado: ")
rel = input("Entre com o domínio a ser procurado: ")
cont = input("Entre com o termo procurado na página: ")
rev = [] 

try:
	from googlesearch import search
except ImportError:
	print("Módulo do Google não encontrado")

def procura(item):
	r = requests.get(item)
	s = r.content
	try:
		f1 = re.findall(cont, s.decode('utf-8'))[0]
		print("Termo encontrado em: ", item)
	except IndexError:
		print("Termo não encontrado.")

for j in search(src, tld="co.in", num=80, stop=80, pause=10):
	x = re.search(rel, j)
	if x != None:
		rev.append(j)
		print("Temos um match no link: ", j)

print("Pesquisa finalizada com ", len(rev), "links encontrados.")
print("Iniciando varredura nas páginas.")

for i in range(len(rev)):
	procura(rev[i])

print ("Pesquisa encerrada.")