import requests
import pytest

# URLs das APIs reais que escolhi para realizar os testes de integração:

# 1. NASA API: fornece dados e imagens sobre astronomia. Precisa de uma chave de API.
# (Usei uma chave pública 'DEMO_KEY', mas idealmente uma chave personalizada seria configurada).
SPACE_API_URL = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"  # Substitua "DEMO_KEY" por chave. OBS: Deve ser trocada

# 2. Dog CEO API: API pública que retorna uma lista de todas as raças de cães conhecidas.
DOG_BREEDS_API_URL = "https://dog.ceo/api/breeds/list/all"

# 3. Cat Facts API: esta API retorna fatos aleatórios sobre gatos, útil para simular interações simples.
CAT_FACTS_API_URL = "https://catfact.ninja/fact"

# 4. COVID-19 API: fornece dados atualizados sobre casos de COVID-19 por país. Aqui, utilizei o exemplo do Brasil.
COVID_API_URL = "https://disease.sh/v3/covid-19/countries/Brazil"

# 5. Rick and Morty API: escolhi essa API pois retorna dados sobre personagens, episódios e locais 
# do universo da série Rick and Morty.
SERIES_API_URL = "https://rickandmortyapi.com/api/character"

# 1. Testes para a API de Imagens e Dados Espaciais
def test_space_api_success():
    """Testa se a API de espaço retorna status code 200."""
    response = requests.get(SPACE_API_URL)
    assert response.status_code == 200, "O status code deve ser 200."

def test_space_api_data_verification():
    """Valida se a resposta contém informações esperadas como 'url' e 'title'."""
    response = requests.get(SPACE_API_URL)
    data = response.json()
    assert "url" in data, "A chave 'url' deve estar presente."
    assert "title" in data, "A chave 'title' deve estar presente."

# 2. Testes para a API de Raças de Cães
def test_dog_breeds_api_success():
    """Testa se a API de raças de cães retorna status code 200."""
    response = requests.get(DOG_BREEDS_API_URL)
    assert response.status_code == 200, "O status code deve ser 200."

def test_dog_breeds_api_data_verification():
    """Valida se a resposta contém 'message'."""
    response = requests.get(DOG_BREEDS_API_URL)
    data = response.json()
    assert "message" in data, "A chave 'message' deve estar presente."

# 3. Testes para a API de Fatos sobre Gatos
def test_cat_facts_api_success():
    """Testa se a API de fatos sobre gatos retorna status code 200."""
    response = requests.get(CAT_FACTS_API_URL)
    assert response.status_code == 200, "O status code deve ser 200."

def test_cat_facts_api_data_verification():
    """Verifica se a resposta contém uma chave 'fact' com um fato sobre gatos."""
    response = requests.get(CAT_FACTS_API_URL)
    data = response.json()
    assert "fact" in data, "A chave 'fact' deve estar presente."

# 4. Testes para a API de Casos de COVID-19
def test_covid_api_success():
    """Testa se a API de COVID-19 retorna status code 200 para um país específico."""
    response = requests.get(COVID_API_URL)
    assert response.status_code == 200, "O status code deve ser 200."

def test_covid_api_data_verification():
    """Valida se a resposta contém dados como 'cases' e 'deaths'."""
    response = requests.get(COVID_API_URL)
    data = response.json()
    assert "cases" in data, "A chave 'cases' deve estar presente."
    assert "deaths" in data, "A chave 'deaths' deve estar presente."

# 5. Testes para a API de Séries
def test_series_api_success():
    """Testa se a API de séries retorna status code 200."""
    response = requests.get(SERIES_API_URL)
    assert response.status_code == 200, "O status code deve ser 200."

def test_series_api_data_verification():
    """Verifica se a resposta contém 'name' e 'status'."""
    response = requests.get(SERIES_API_URL)
    data = response.json()
    assert "name" in data["results"][0], "A chave 'name' deve estar presente."
    assert "status" in data["results"][0], "A chave 'status' deve estar presente."
