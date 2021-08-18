import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/') # Fazendo requisição ao servidor
content  =  (response.content) # Retorna o conteudo html inteiro do site

site = BeautifulSoup(content, 'html.parser') # Convertendo o conteudo "Bytes"(gerado pelo requests) em html

news = site.find('div', attrs={'class': 'feed-post-body'}) # "div" = tag que é para encontrar, "attrs" = atribustos da tag especifica que quero que ele encontre. obs: retorna a primeira ocorrencia apenas

title = news.find('a', attrs={'class': 'feed-post-link gui-color-primary gui-color-hover'})

subtitle = news.find('div', attrs={'class': 'feed-post-body-resumo'})

topic = news.find('span')

print('\033[1;34m↓↓Código HTML da noticia↓↓\033[0;0m')
print(news.prettify()) # Metodo que organiza o codigo html em algo mais legivel 
print('\033[1;34m↓↓Titulo da noticia↓↓\033[0;0m')
print(title.text) # Retorna o texto da tag "a"
print('\033[1;34m↓↓Subtitulo da noticia↓↓\033[0;0m')
print(subtitle.text)  
print('\033[1;34m↓↓Assunto da noticia↓↓\033[0;0m')
print(topic.text)