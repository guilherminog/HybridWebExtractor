
# HybridWebExtractor

**HybridWebExtractor** é um script avançado para extração de dados da web, utilizando uma abordagem híbrida com Selenium e BeautifulSoup. Ele emprega boas práticas de programação, incluindo padrões de design como Singleton e Strategy, além de um robusto tratamento de exceções para garantir resiliência.

## 🛠️ Funcionalidades

- **Busca Híbrida de Elementos**: Combina Selenium e BeautifulSoup para garantir a extração dos elementos, mesmo em casos de falha.
- **Modo Headless**: Executa o navegador Chrome sem interface gráfica para maior eficiência.
- **Configurações Personalizadas**: Inclui ajustes detalhados para otimização do WebDriver.
- **Padrão Singleton**: Assegura que apenas uma instância do WebDriver seja criada durante a execução.
- **Fallback Inteligente**: Usa BeautifulSoup como alternativa quando o Selenium não encontra o elemento.
- **Tratamento Avançado de Exceções**: Exceções customizadas para melhor controle de erros e logs detalhados.

## 🚀 Tecnologias Utilizadas

- [Python 3.8+](https://www.python.org/downloads/)
- [Selenium](https://www.selenium.dev/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [WebDriver Manager](https://pypi.org/project/webdriver-manager/)
- [Requests](https://docs.python-requests.org/)

## 📦 Instalação

Antes de iniciar, certifique-se de ter o Python 3.8+ instalado. Em seguida, instale as dependências com o comando:

```bash
pip install selenium webdriver_manager beautifulsoup4 requests
```

## ⚙️ Configuração

O script utiliza o **ChromeDriver** e requer que o navegador Chrome esteja instalado no seu sistema. Ajuste o caminho para o binário do Chrome conforme necessário:

```python
chrome_options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
```

## 🏃‍♂️ Execução

Para executar o script, use o comando:

```bash
python hybrid_web_extractor.py
```

O script acessará a página de promoções da SteamDB e tentará localizar o elemento "Show only historical lows". O texto encontrado será exibido no console.

## 🗃️ Estrutura do Projeto

```plaintext
HybridWebExtractor/
├── hybrid_web_extractor.py
├── README.md
└── requirements.txt
```

## 📋 Exemplo de Uso

```bash
python hybrid_web_extractor.py
```

**Saída esperada:**

```plaintext
2024-11-08 12:30:45 - INFO - WebDriver inicializado com sucesso.
2024-11-08 12:30:47 - INFO - Página acessada com sucesso: https://steamdb.info/sales/
2024-11-08 12:30:48 - INFO - Elemento encontrado com Selenium: Show only historical lows
2024-11-08 12:30:48 - INFO - WebDriver encerrado com sucesso.
```

## 🛠️ Problemas Conhecidos

- **Erro de Inicialização do WebDriver**: Verifique se o Chrome está instalado e atualizado.
- **Elemento não encontrado**: Se o elemento não for encontrado com Selenium, o script tenta novamente usando BeautifulSoup.

## 🧩 Contribuição

Contribuições são bem-vindas! Para colaborar:

1. Faça um fork do repositório.
2. Crie uma branch: `git checkout -b feature/sua-feature`
3. Faça suas alterações e commite: `git commit -m 'Adicionei nova feature'`
4. Envie suas alterações: `git push origin feature/sua-feature`
5. Abra um Pull Request.

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

## 👨‍💻 Autor

Desenvolvido por **Guilhermino Gomes**
- [LinkedIn ](https://www.linkedin.com/in/guilherminog/)

