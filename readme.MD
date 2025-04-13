```markdown
# BetterAnime Scraper

Este projeto é um scraper para o site [BetterAnime](https://betteranime.net), que permite obter informações sobre os últimos lançamentos de animes diretamente da página inicial do site.

## Funcionalidades

- **Obter últimos lançamentos**: A classe `Betteranime` permite acessar os últimos animes lançados no site, incluindo o título e o episódio.

## Estrutura do Projeto

```
betteranime.net scrapper/
├── betteranime/
│   ├── __init__.py
│   ├── Betteranime.py
│   ├── home.py
├── main.py
└── readme.md
```

- **`betteranime/`**: Contém os módulos principais do scraper.
  - **`Betteranime.py`**: Classe principal que integra as funcionalidades do scraper.
  - **`home.py`**: Contém a lógica para acessar e processar os dados da página inicial do site.
- **`main.py`**: Script de exemplo para executar o scraper.
- **`readme.md`**: Documentação do projeto.

## Como Usar

1. **Instale as dependências necessárias**:
   Certifique-se de ter o Python instalado e execute o seguinte comando para instalar as bibliotecas necessárias:

   ```bash
   pip install requests beautifulsoup4
   ```

2. **Execute o script principal**:
   No terminal, execute o arquivo `main.py`:

   ```bash
   python main.py
   ```

3. **Saída esperada**:
   O script exibirá no terminal os últimos lançamentos de animes, com título e episódio.

## Exemplo de Código

Aqui está um exemplo de como usar a classe `Betteranime`:

```python
from betteranime import Betteranime

# Inicializa o scraper
scraper = Betteranime()

# Obtém os últimos lançamentos
latest_releases = scraper.get_lastest_releases()

# Exibe os resultados
for anime in latest_releases:
    print(f"Anime: {anime.title}, Episódio: {anime.episode}")
```

## Requisitos

- Python 3.7 ou superior
- Bibliotecas:
  - `requests`
  - `beautifulsoup4`

## Observações

- Este projeto foi desenvolvido para fins educacionais e de aprendizado. Certifique-se de respeitar os termos de uso do site [BetterAnime](https://betteranime.net) ao utilizar este scraper.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
```