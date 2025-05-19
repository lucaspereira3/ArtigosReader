import requests
from bs4 import BeautifulSoup
import sys
import re

def fetch_medium_article(url):
    """Busca o conteúdo HTML de um artigo do Medium."""
    headers = {
        # Simula um navegador comum para evitar bloqueios simples
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status() # Verifica se houve erro HTTP (4xx ou 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar a URL: {e}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None

def extract_article_text(html_content):
    """Extrai o texto principal de um artigo do Medium a partir do HTML."""
    if not html_content:
        return "Erro: Conteúdo HTML vazio ou inválido."

    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # O Medium usa diferentes estruturas, tentamos algumas comuns.
        # A tag <article> é frequentemente usada.
        article_body = soup.find('article')
        
        # Se <article> não for encontrado, tentar seletores mais específicos
        # (Estes podem mudar com o tempo, inspecionar a página é recomendado)
        if not article_body:
             # Tentar por classes comuns em seções de conteúdo
             possible_containers = soup.find_all("section") 
             # Heurística: encontrar a seção com mais parágrafos pode funcionar
             best_section = None
             max_p_count = 0
             for section in possible_containers:
                 p_count = len(section.find_all("p"))
                 if p_count > max_p_count:
                     max_p_count = p_count
                     best_section = section
             article_body = best_section

        if not article_body:
            return "Erro: Não foi possível encontrar o corpo principal do artigo. A estrutura do Medium pode ter mudado."

        # Extrai parágrafos, títulos e listas do corpo do artigo
        paragraphs = article_body.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li'])
        
        article_text = "\n".join([p.get_text() for p in paragraphs])
        
        # Limpeza básica: remover múltiplos espaços em branco e linhas vazias
        article_text = re.sub(r'\s{2,}', ' ', article_text) # Substitui múltiplos espaços por um único
        article_text = "\n".join([line for line in article_text.splitlines() if line.strip()]) # Remove linhas vazias
        
        return article_text

    except Exception as e:
        return f"Erro ao processar o HTML: {e}"

if __name__ == "__main__":
    print("--- Leitor de Artigos do Medium (Simplificado) ---")
    
    if len(sys.argv) > 1:
        article_url = sys.argv[1]
        print(f"Buscando artigo em: {article_url}")
    else:
        article_url = input("Digite a URL do artigo do Medium: ")

    if not article_url.startswith(("http://", "https://")):
        print("URL inválida. Certifique-se de incluir http:// ou https://")
    else:
        html = fetch_medium_article(article_url)
        if html:
            print("\n--- Texto do Artigo ---")
            text = extract_article_text(html)
            print(text)
            print("----------------------")
        else:
            print("Não foi possível obter o conteúdo do artigo.")
            
    print("--- Fim do programa ---")
