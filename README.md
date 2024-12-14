
# py_mflx               
## project structure
```                    
py_mflx/
    README.md
    Dockerfile
    last_update.txt
    patch.diff
    requirements.txt
    app.py
    docker-compose.yml
    Python-3.12.5.tar.xz
    templates/
        movies.html
        movie.html
    src/
        get_html_content.py
        clean_text.py
        save_content.py
        movie_service.py
        extract_movie_info.py
    output/
        json/
            map_filme.json
    Misc/
        NEWS.d/
            next/
                macOS/
                    2020-06-24-13-51-57.bpo-41100.mcHdc5.rst                
```
## Projeto: Aplicação Web para Busca e Exibição de Filmes

### Propósito e Descrição do Projeto

Este projeto desenvolve uma aplicação web que permite buscar e exibir informações de filmes.  Utiliza Flask como backend para processamento de requisições e entrega de dados, provavelmente obtidos de um banco de dados externo de filmes (TMDB). A aplicação inclui cache para melhorar o desempenho e oferece interface HTML básica e API RESTful.  A interface HTML inclui funcionalidades de busca, filtragem por ano e paginação.  Detalhes dos filmes são carregados dinamicamente a partir de uma API.  O projeto também inclui scripts para extração de dados HTML, limpeza de texto e salvamento de conteúdo.

### Dependências

* Flask
* python-dotenv
* flask-cors
* requests
* beautifulsoup4


### Como Instalar

1. Clonar o repositório.
2. Instalar dependências: `pip install -r requirements.txt`
3. Criar um arquivo `.env` com as variáveis de ambiente necessárias (chave da API TMDB, etc.).
4. Executar a aplicação: `docker-compose up -d` (assumindo uso de Docker Compose).


### Como Usar

A aplicação web fornece endpoints para: verificação de integridade, busca de filmes, visualização de todos os filmes, visualização de um filme específico e limpeza do cache.  A interface HTML permite busca por título e ano.

### Arquitetura

A aplicação utiliza uma arquitetura cliente-servidor. O backend (Flask) processa as requisições, interage com a API TMDB e o cache, e retorna dados para a interface do usuário.  A interface HTML usa JavaScript para interações dinâmicas e armazenamento em localStorage. O Docker Compose é utilizado para orquestração de containers.


### Pipeline

1. Requisição do cliente.
2. Roteamento (Flask).
3. Processamento de dados (busca em cache ou API, limpeza de dados).
4. Geração da resposta (HTML ou JSON).
5. Retorno da resposta ao cliente.
6. Armazenamento em cache (opcional).
                
                