#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Monitor de Pós-Graduações EAD Gratuitas
Faz scraping de sites de institutos federais em busca de novos editais
"""

import requests
from bs4 import BeautifulSoup
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os
import re

class PosGraduacaoMonitor:
    """
    Classe principal para monitorar sites de pós-graduação
    Equivalente a uma classe C# que você já conhece!
    """
    
    def __init__(self):
        """Construtor - inicializa as configurações"""
        self.sites = self.carregar_sites()
        self.dados_anteriores = self.carregar_dados_historicos()
        self.novas_oportunidades = []
    
    def carregar_sites(self):
        """
        Carrega a lista de sites para monitorar
        Você pode expandir essa lista com mais institutos
        """
        return [
            {
                'nome': 'IFSULDEMINAS',
                'url': 'https://portal.ifsuldeminas.edu.br/index.php/editais',
                'palavras_chave': ['pós-graduação', 'pos-graduacao', 'especialização', 'especializacao', 'ead', 'distância']
            },
            {
                'nome': 'IFSP',
                'url': 'https://www.ifsp.edu.br/editais',
                'palavras_chave': ['pós-graduação', 'pos-graduacao', 'especialização', 'ead']
            },
            {
                'nome': 'IFRS',
                'url': 'https://ifrs.edu.br/editais/',
                'palavras_chave': ['pós-graduação', 'especialização', 'ead', 'seleção']
            }
        ]
    
    def carregar_dados_historicos(self):
        """
        Carrega os dados já processados anteriormente
        Similar a ler de um arquivo JSON ou banco de dados
        """
        try:
            if os.path.exists('historico.json'):
                with open('historico.json', 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Erro ao carregar histórico: {e}")
        return {'editais_encontrados': []}
    
    def salvar_dados_historicos(self):
        """Salva os dados processados para próxima execução"""
        try:
            with open('historico.json', 'w', encoding='utf-8') as f:
                json.dump(self.dados_anteriores, f, ensure_ascii=False, indent=2)
            print("✅ Histórico salvo com sucesso")
        except Exception as e:
            print(f"❌ Erro ao salvar histórico: {e}")
    
    def gerar_json_frontend(self):
        """
        Gera arquivo JSON otimizado para o frontend consumir
        Inclui apenas os dados necessários para exibição
        """
        try:
            # Ordena por data (mais recente primeiro)
            editais_ordenados = sorted(
                self.dados_anteriores['editais_encontrados'],
                key=lambda x: x['data_encontrado'],
                reverse=True
            )
            
            # Estrutura otimizada para o frontend
            dados_frontend = {
                'ultima_atualizacao': datetime.now().isoformat(),
                'total_oportunidades': len(editais_ordenados),
                'oportunidades': editais_ordenados,
                'institutos_unicos': list(set(e['instituto'] for e in editais_ordenados)),
                'estatisticas': {
                    'por_instituto': {}
                }
            }
            
            # Calcula estatísticas por instituto
            for edital in editais_ordenados:
                instituto = edital['instituto']
                if instituto not in dados_frontend['estatisticas']['por_instituto']:
                    dados_frontend['estatisticas']['por_instituto'][instituto] = 0
                dados_frontend['estatisticas']['por_instituto'][instituto] += 1
            
            # Salva o JSON para o frontend
            with open('resultados.json', 'w', encoding='utf-8') as f:
                json.dump(dados_frontend, f, ensure_ascii=False, indent=2)
            
            print("✅ JSON do frontend gerado com sucesso")
            print(f"   Total de oportunidades: {dados_frontend['total_oportunidades']}")
            
        except Exception as e:
            print(f"❌ Erro ao gerar JSON do frontend: {e}")
    
    def fazer_scraping(self, site):
        """
        Faz o scraping de um site específico
        
        Web Scraping = "raspar" (extrair) dados de uma página web
        É como você abrir o DevTools e pegar informações da página, mas automatizado
        """
        try:
            print(f"\n🔍 Analisando: {site['nome']}")
            
            # Faz a requisição HTTP (GET) - como quando você acessa um site no navegador
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(site['url'], headers=headers, timeout=10)
            
            # Verifica se deu certo (status 200 = OK)
            if response.status_code != 200:
                print(f"⚠️ Erro ao acessar {site['nome']}: Status {response.status_code}")
                return []
            
            # BeautifulSoup = biblioteca que "entende" HTML
            # É como ter um parser de HTML em C#
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Procura por links e títulos
            editais_encontrados = []
            
            # Procura por links <a> que contenham as palavras-chave
            links = soup.find_all('a', href=True)
            
            for link in links:
                texto = link.get_text().strip().lower()
                href = link.get('href', '')
                
                # Verifica se contém alguma palavra-chave
                if any(palavra in texto for palavra in site['palavras_chave']):
                    # Verifica se é relacionado a tecnologia/TI
                    if self.e_area_tecnologia(texto):
                        edital = {
                            'titulo': link.get_text().strip(),
                            'url': self.normalizar_url(href, site['url']),
                            'instituto': site['nome'],
                            'data_encontrado': datetime.now().isoformat()
                        }
                        
                        # Verifica se é novo
                        if not self.ja_existe(edital):
                            editais_encontrados.append(edital)
                            print(f"  ✨ NOVO: {edital['titulo'][:80]}...")
            
            return editais_encontrados
            
        except Exception as e:
            print(f"❌ Erro ao fazer scraping de {site['nome']}: {e}")
            return []
    
    def e_area_tecnologia(self, texto):
        """
        Verifica se o edital é da área de tecnologia
        Adicione mais termos conforme necessário
        """
        termos_tech = [
            'tecnologia', 'ti', 'computação', 'computacao', 'informática', 'informatica',
            'sistemas', 'software', 'desenvolvimento', 'programação', 'programacao',
            'dados', 'redes', 'segurança', 'cibersegurança', 'ciber', 'web',
            'inteligência artificial', 'ia', 'machine learning', 'cloud',
            'devops', 'engenharia de software', 'análise de sistemas', 'análise e desenvolvimento'
        ]
        
        return any(termo in texto for termo in termos_tech)
    
    def normalizar_url(self, href, url_base):
        """
        Transforma URLs relativas em URLs absolutas
        Ex: /edital/123 -> https://site.com/edital/123
        """
        if href.startswith('http'):
            return href
        elif href.startswith('/'):
            # Pega apenas o domínio da URL base
            from urllib.parse import urlparse
            parsed = urlparse(url_base)
            return f"{parsed.scheme}://{parsed.netloc}{href}"
        else:
            return f"{url_base.rstrip('/')}/{href}"
    
    def ja_existe(self, edital):
        """Verifica se o edital já foi encontrado anteriormente"""
        for edital_antigo in self.dados_anteriores['editais_encontrados']:
            if edital_antigo['url'] == edital['url']:
                return True
        return False
    
    def enviar_email(self):
        """
        Envia email com as novas oportunidades encontradas
        Usa variáveis de ambiente para segurança (definidas no GitHub Actions)
        """
        if not self.novas_oportunidades:
            print("\n📭 Nenhuma nova oportunidade encontrada.")
            return
        
        # Pega credenciais das variáveis de ambiente (seguro!)
        email_remetente = os.environ.get('EMAIL_REMETENTE')
        email_senha = os.environ.get('EMAIL_SENHA')
        email_destinatario = os.environ.get('EMAIL_DESTINATARIO')
        
        if not all([email_remetente, email_senha, email_destinatario]):
            print("⚠️ Configurações de email não encontradas nas variáveis de ambiente")
            print("🔍 Novas oportunidades encontradas (não enviadas):")
            for oport in self.novas_oportunidades:
                print(f"  - {oport['titulo']} ({oport['instituto']})")
            return
        
        # Monta o conteúdo do email
        html_content = self.montar_html_email()
        
        # Configura a mensagem
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f'🎓 {len(self.novas_oportunidades)} Nova(s) Pós-Graduação(ões) EAD Gratuita(s)!'
        msg['From'] = email_remetente
        msg['To'] = email_destinatario
        
        # Adiciona o conteúdo HTML
        parte_html = MIMEText(html_content, 'html', 'utf-8')
        msg.attach(parte_html)
        
        try:
            # Envia o email via SMTP do Gmail
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
                servidor.login(email_remetente, email_senha)
                servidor.send_message(msg)
            
            print(f"\n📧 Email enviado com sucesso para {email_destinatario}!")
            print(f"   Total de oportunidades: {len(self.novas_oportunidades)}")
            
        except Exception as e:
            print(f"\n❌ Erro ao enviar email: {e}")
            print("💡 Verifique se:")
            print("   - Você habilitou 'Senhas de app' no Google")
            print("   - As credenciais estão corretas")
    
    def montar_html_email(self):
        """Cria um email HTML bonito com as oportunidades"""
        html = """
        <html>
        <head>
            <style>
                body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
                .container { max-width: 600px; margin: 0 auto; padding: 20px; }
                .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                         color: white; padding: 20px; border-radius: 10px 10px 0 0; }
                .oportunidade { background: #f8f9fa; margin: 15px 0; padding: 15px; 
                               border-left: 4px solid #667eea; border-radius: 5px; }
                .instituto { color: #667eea; font-weight: bold; }
                .titulo { font-size: 16px; margin: 10px 0; }
                .link { display: inline-block; margin-top: 10px; padding: 8px 15px; 
                       background: #667eea; color: white; text-decoration: none; 
                       border-radius: 5px; }
                .footer { margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd; 
                         color: #666; font-size: 12px; }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>🎓 Novas Pós-Graduações EAD Encontradas!</h1>
                    <p>Encontramos """ + str(len(self.novas_oportunidades)) + """ nova(s) oportunidade(s) gratuita(s) para você!</p>
                </div>
        """
        
        for oport in self.novas_oportunidades:
            html += f"""
                <div class="oportunidade">
                    <div class="instituto">📍 {oport['instituto']}</div>
                    <div class="titulo">{oport['titulo']}</div>
                    <a href="{oport['url']}" class="link">Ver Edital Completo</a>
                    <div style="margin-top: 10px; font-size: 12px; color: #666;">
                        Encontrado em: {datetime.fromisoformat(oport['data_encontrado']).strftime('%d/%m/%Y às %H:%M')}
                    </div>
                </div>
            """
        
        html += """
                <div class="footer">
                    <p>⚙️ Automação executada em """ + datetime.now().strftime('%d/%m/%Y às %H:%M') + """</p>
                    <p>Este é um email automático. Monitore os sites oficiais para informações atualizadas.</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        return html
    
    def executar(self):
        """Método principal que executa todo o fluxo"""
        print("="*60)
        print("🚀 Iniciando monitoramento de Pós-Graduações EAD")
        print("="*60)
        
        # Faz scraping de cada site
        for site in self.sites:
            editais = self.fazer_scraping(site)
            self.novas_oportunidades.extend(editais)
        
        # Se encontrou novidades, atualiza histórico
        if self.novas_oportunidades:
            for oport in self.novas_oportunidades:
                self.dados_anteriores['editais_encontrados'].append(oport)
            self.salvar_dados_historicos()
        
        # Gera JSON para o frontend (sempre, mesmo sem novidades)
        self.gerar_json_frontend()
        
        # Envia email com as novidades
        self.enviar_email()
        
        print("\n" + "="*60)
        print("✅ Monitoramento concluído!")
        print("="*60)

# Ponto de entrada do script (como o Main em C#)
if __name__ == "__main__":
    monitor = PosGraduacaoMonitor()
    monitor.executar()
