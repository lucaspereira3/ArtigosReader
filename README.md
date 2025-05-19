# 📰 medium-article-reader

Uma ferramenta de linha de comando em Python que extrai e exibe o conteúdo de artigos do **Medium.com** diretamente no terminal, sem propagandas ou formatações visuais excessivas.

---

## 📌 Tópicos

- [📖 Sobre o Projeto](#-sobre-o-projeto)
- [🚀 Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [⚙️ Como Executar](#️-como-executar)
- [🧠 Explicação do Código](#-explicação-do-código)
- [🔐 Limitações](#-limitações)
- [📄 Licença](#-licença)
- [🤝 Contribuindo](#-contribuindo)

---

## 📖 Sobre o Projeto

Este script permite que você leia artigos do Medium diretamente do terminal, fazendo scraping do conteúdo principal do artigo e exibindo o texto de forma limpa. Útil para leitura offline, arquivamento de conteúdo ou estudo de scraping com Python.

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- requests (requisições HTTP)
- BeautifulSoup (parse do HTML)
- re (expressões regulares)
- sys (entrada de argumentos)

---

## ⚙️ Como Executar

1. **Clone o repositório:**

```bash
git clone https://github.com/rafaelmoreirax/medium-article-reader.git
cd medium-article-reader
```

2. **Instale as dependências:**

```bash
pip install requests beautifulsoup4
```

3. **Execute o script:**

```bash
python main.py https://medium.com/exemplo-de-artigo
```

Ou, se quiser digitar a URL na hora:

```bash
python main.py
```

---

## 🧠 Explicação do Código

- `fetch_medium_article(url)`: realiza a requisição HTTP ao artigo do Medium, simulando um navegador real para evitar bloqueios.
- `extract_article_text(html_content)`: faz o parsing do HTML com BeautifulSoup e tenta extrair o conteúdo relevante (texto do artigo) de forma estruturada.
- O programa tenta localizar a tag `<article>` ou outras seções com maior número de parágrafos.
- O conteúdo é limpo de espaços e linhas desnecessárias antes de ser exibido.
- O código também lida com erros de rede e estrutura não prevista no HTML.

---

## 🔐 Limitações

- A estrutura do Medium pode mudar com o tempo, exigindo ajustes nos seletores usados.
- O script depende de uma conexão com a internet.
- Não lida com artigos que exigem login ou estão protegidos atrás de paywalls.

---

## 📄 Licença

Este projeto está sob a licença [MIT](LICENSE).

---

## 🤝 Contribuindo

Contribuições são bem-vindas!

1. Fork este repositório.
2. Crie uma branch: `git checkout -b minha-melhoria`.
3. Commit suas alterações: `git commit -m 'feat: melhoria no parser'`.
4. Push na branch: `git push origin minha-melhoria`.
5. Abra um Pull Request.

---

## 👤 Autor

Feito por [Rafael Moreira](https://github.com/rafaelmoreirax)
