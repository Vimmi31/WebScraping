import requests
from bs4 import BeautifulSoup
import pandas

list_news = []
response = requests.get('https://g1.globo.com/') # Fazendo requisição ao servidor
content  =  (response.content) # Retorna o conteudo html inteiro do site

site = BeautifulSoup(content, 'html.parser') # Convertendo o conteudo "Bytes"(gerado pelo requests) em html

news = site.findAll('div', attrs={'class': 'feed-post-body'}) # "div" = tag que é para encontrar, "attrs" = atribustos da tag especifica que quero que ele encontre. obs: retorna a primeira ocorrencia apenas
cont = 0
for new in news:
    
    title    = new.find('a', attrs={'class': 'feed-post-link gui-color-primary gui-color-hover'})
    subtitle = new.find('div', attrs={'class': 'feed-post-body-resumo'})
    topic    = new.find('span')
    
    print('\033[1;34m↓↓Titulo da noticia↓↓\033[0;0m')
    print(title.text) # Retorna o texto da tag "a"
    if subtitle: # Verificando se o subtitulo existe
        print('\033[1;34m↓↓Subtitulo da noticia↓↓\033[0;0m')
        print(subtitle.text)  
    print('\033[1;34m↓↓Assunto da noticia↓↓\033[0;0m')
    print(topic.text)
    print('_'*30)
    if subtitle:
        list_news.append([title.text, subtitle.text, topic.text])
    else:
        list_news.append([title.text, '',topic.text])

print('')
news = pandas.DataFrame(list_news, columns=['Titulo', 'Subtitulo', 'Assunto']) # formatando a lista em uma tabela com a Biblioteca pandas
news.to_excel('Noticias.xlsx', index=False) # convertendo a tabela em um arquivo qe pode ser aberto com o excel. Primeiro parametro: Nome do arquivo, Index: Salva sem numeração de linhas(true ou false)