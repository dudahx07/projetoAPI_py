# Testes de Integração para APIs Públicas
Este projeto contém testes de integração desenvolvidos com Python e pytest para diferentes APIs públicas.
O objetivo é simular interações reais com as APIs, verificando o status das respostas e a presença de dados esperados.

# APIs Utilizadas
NASA API: Fornece dados sobre astronomia e imagens. É necessário configurar uma chave 
de API para acessar os dados. Para o propósito deste teste, utilizei uma chave pública (DEMO_KEY), 
mas recomenda-se uma chave personalizada para ter uma maior confiabilidade.
- URL: https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY

Dog CEO API: Retorna uma lista completa de raças de cães.
- URL: https://dog.ceo/api/breeds/list/all

Cat Facts API: Retorna fatos aleatórios sobre gatos.
- URL: https://catfact.ninja/fact

COVID-19 API: Fornece dados atualizados sobre casos de COVID-19 para diferentes países. 
Para este teste, utilizamos o exemplo do Brasil.
- URL: https://disease.sh/v3/covid-19/countries/Brazil

Rick and Morty API: Retorna informações sobre personagens, episódios e locais da série
Rick and Morty.
- URL: https://rickandmortyapi.com/api/character

- requirements.txt: Arquivo para instalação das dependências. Contém pytest e requests.

# Pré-requisitos
- Python
- pytest

# Configuração do Ambiente
Instalei as dependências: pip install -r requirements.txt


# Estrutura dos Testes
Cada teste inclui uma descrição em forma de comentário, indicando o que é esperado em 
cada etapa. Os testes cobrem:

- Verificação de sucesso (status 200)
- Verificação de dados específicos (presença de chaves em JSON)
