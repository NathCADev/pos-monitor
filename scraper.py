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
from datetime import datetime, timedelta
import os
import re

class PosGraduacaoMonitor:
    """
    Classe principal para monitorar sites de pós-graduação
    """
    
    def __init__(self):
        """Construtor - inicializa as configurações"""
        self.sites = self.carregar_sites()
        self.dados_anteriores = self.carregar_dados_historicos()
        self.novas_oportunidades = []
        
        # Configuração: buscar editais dos últimos X meses
        # Exibição padrão: 2 meses. Arquivo retido: 6 meses (botão cicla 2→4→6)
        self.meses_retroativos = 2
        self.meses_arquivo = 6
    
    def carregar_sites(self):
        """
        Carrega a lista de TODOS os sites para monitorar
        Organizado por região para facilitar manutenção
        """
        return [
            # ========== REGIÃO SUL ==========
            {
                'nome': 'IFRS',
                'url': 'https://ifrs.edu.br/editais/',
                'palavras_chave': ['pós-graduação', 'pos-graduacao', 'especialização', 'especializacao', 'ead', 'distância', 'seleção']
            },
            {
                'nome': 'IFSC',
                'url': 'https://www.ifsc.edu.br/editais',
                'palavras_chave': ['pós-graduação', 'pos-graduacao', 'especialização', 'especializacao', 'ead', 'distância']
            },
            {
                'nome': 'IFPR',
                'url': 'https://reitoria.ifpr.edu.br/menu-de-apoio/editais/',
                'palavras_chave': ['pós-graduação', 'pos-graduacao', 'especialização', 'ead', 'distância']
            },
            {
                'nome': 'IFSUL',
                'url': 'http://www.ifsul.edu.br/editais',
                'palavras_chave': ['pós-graduação', 'especialização', 'ead', 'distância']
            },
            
            # ========== REGIÃO SUDESTE ==========
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
                'nome': 'IFMG',
                'url': 'https://www.ifmg.edu.br/portal/pesquisa-e-pos-graduacao/editais-abertos/editais-abertos',
                'palavras_chave': ['pós-graduação', 'especialização', 'ead', 'seleção']
            },
            {
                'nome': 'IFES',
                'url': 'https://www.ifes.edu.br/editais',
                'palavras_chave': ['pós-graduação', 'especialização', 'ead']
            },
            
            # ========== REGIÃO CENTRO-OESTE ==========
            {
                'nome': 'IFB',
                'url': 'https://www.ifb.edu.br/reitori/39292-ensino-editais',
                'palavras_chave': ['pós-graduação', 'especialização', 'ead', 'distância']
            },
            {
                'nome': 'IFGOIANO',
                'url': 'https://www.ifgoiano.edu.br/home/index.php/editais.html',
                'palavras_chave': ['pós-graduação', 'especialização', 'ead']
            },
            {
                'nome': 'IFMT',
                'url': 'https://ifmt.edu.br/painel-de-editais/',
                'palavras_chave': ['pós-graduação', 'especialização', 'ead', 'distância']
            },
            
            # ========== REGIÃO NORDESTE ==========
            {
                'nome': 'IFBA',
                'url': 'https://portal.ifba.edu.br/@@search?Subject%3Alist=Not%C3%ADcias',
                'palavras_chave': ['pós-graduação', 'especialização', 'ead', 'distância']
            },
            {
                'nome': 'IFCE',
                'url': 'https://ifce.edu.br/editais',
                'palavras_chave': ['pós-graduação', 'especialização', 'ead']
            },
            {
                'nome': 'IFPB',
                'url': 'https://www.ifpb.edu.br/editais',
                'palavras_chave': ['pós-graduação', 'especialização', 'ead', 'distância']
            },
            {
                'nome': 'IFPE',
                'url': 'https://www.ifpe.edu.br/editais',
                'palavras_chave': ['pós-graduação', 'especialização', 'ead']
            },
            
            # ========== REGIÃO NORTE ==========
            {
                'nome': 'IFPA',
                'url': 'https://ifpa.edu.br/editais',
                'palavras_chave': ['pós-graduação', 'especialização', 'ead', 'distância']
            },
            {
                'nome': 'UNIFAP',
                'url': 'https://www.unifap.br/editais-de-pos-graduacao/',
                'palavras_chave': ['pós-graduação', 'especialização', 'ead', 'distância']
            },
            {
                'nome': 'IFAM',
                'url': 'http://www2.ifam.edu.br/editais',
                'palavras_chave': ['pós-graduação', 'especialização', 'ead']
            },
            
            # ========== UNIVERSIDADES FEDERAIS ==========
            {
                'nome': 'UFMG',
                'url': 'https://ufmg.br/editais',
                'palavras_chave': ['pós-graduação', 'especialização', 'ead']
            },
            {
                'nome': 'UFRGS',
                'url': 'https://www.ufrgs.br/sead/noticias/',
                'palavras_chave': ['pós-graduação', 'especialização', 'ead', 'distância']
            }
        ]
    
    def carregar_dados_historicos(self):
        """
        Carrega os dados já processados anteriormente
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
        Gera arquivo JSON otimizado para o frontend consumir.
        Retém até meses_arquivo (6). Frontend exibe meses_retroativos (2)
        por padrão, com botão que cicla 2→4→6.
        """
        try:
            agora = datetime.now()
            limite_padrao = agora - timedelta(days=self.meses_retroativos * 30)
            limite_arquivo = agora - timedelta(days=self.meses_arquivo * 30)

            def dentro_limite(edital, limite):
                d = self._data_referencia_edital(edital)
                return d is None or d >= limite

            editais_arquivo = [e for e in self.dados_anteriores['editais_encontrados']
                               if dentro_limite(e, limite_arquivo)]
            editais_padrao = [e for e in editais_arquivo
                               if dentro_limite(e, limite_padrao)]

            # Ordena por data (mais recente primeiro) - usa lista de arquivo (6m)
            editais_ordenados = sorted(
                editais_arquivo,
                key=lambda x: (self._data_referencia_edital(x) or datetime.min).isoformat(),
                reverse=True
            )

            # Estatísticas sobre a visão padrão (2m) para bater com o total exibido
            editais_padrao_ord = sorted(
                editais_padrao,
                key=lambda x: (self._data_referencia_edital(x) or datetime.min).isoformat(),
                reverse=True
            )

            # Estrutura otimizada para o frontend
            dados_frontend = {
                'ultima_atualizacao': agora.isoformat(),
                'filtro_padrao_meses': self.meses_retroativos,
                'filtro_extendido_meses': self.meses_arquivo,
                'opcoes_periodo_meses': [2, 4, 6],
                'total_oportunidades': len(editais_padrao),
                'total_extendido': len(editais_arquivo),
                'oportunidades': editais_ordenados,
                'institutos_unicos': list(set(e['instituto'] for e in editais_ordenados)),
                'estatisticas': {
                    'por_instituto': {}
                }
            }

            # Calcula estatísticas por instituto (visão padrão de 2m)
            for edital in editais_padrao_ord:
                instituto = edital['instituto']
                if instituto not in dados_frontend['estatisticas']['por_instituto']:
                    dados_frontend['estatisticas']['por_instituto'][instituto] = 0
                dados_frontend['estatisticas']['por_instituto'][instituto] += 1

            # Salva o JSON para o frontend
            with open('resultados.json', 'w', encoding='utf-8') as f:
                json.dump(dados_frontend, f, ensure_ascii=False, indent=2)

            print("✅ JSON do frontend gerado com sucesso")
            print(f"   Padrão ({self.meses_retroativos}m): {len(editais_padrao)} | Arquivo ({self.meses_arquivo}m): {len(editais_arquivo)}")
            
        except Exception as e:
            print(f"❌ Erro ao gerar JSON do frontend: {e}")
    
    def fazer_scraping(self, site):
        """
        Faz o scraping de um site específico
        """
        try:
            print(f"\n🔍 Analisando: {site['nome']}")
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(site['url'], headers=headers, timeout=10)
            
            if response.status_code != 200:
                print(f"⚠️ Erro ao acessar {site['nome']}: Status {response.status_code}")
                return []
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            editais_encontrados = []
            links = soup.find_all('a', href=True)
            
            for link in links:
                texto = link.get_text().strip().lower()
                href = link.get('href', '')
                
                # Pega contexto ao redor do link (para tentar extrair data)
                parent = link.parent
                contexto = parent.get_text() if parent else ''
                
                # Verifica se contém alguma palavra-chave (palavra isolada, não substring)
                if any(self._contem_termo(texto, palavra) for palavra in site['palavras_chave']):
                    # Verifica se é relacionado a tecnologia/TI
                    if self.e_area_tecnologia(texto):
                        # Verifica se é recente (filtro de data: retém até meses_arquivo)
                        if self.e_edital_recente(texto, contexto):
                            data_pub = self.extrair_data_do_texto(f"{texto} {contexto}".lower())
                            edital = {
                                'titulo': link.get_text().strip(),
                                'url': self.normalizar_url(href, site['url']),
                                'instituto': site['nome'],
                                'data_encontrado': datetime.now().isoformat(),
                                'data_publicacao': data_pub.isoformat() if data_pub else None
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
        Verifica se o edital é das áreas de interesse:
        - Inteligência Artificial / Machine Learning / Data Science
        - Desenvolvimento Web (front-end, back-end, full-stack)
        - Desenvolvimento Mobile (apps iOS/Android)
        - Cybersegurança / Segurança da Informação
        - Cloud / DevOps / Infraestrutura
        
        IMPORTANTE: Usa lista de exclusões para evitar falsos positivos
        """
        
        # LISTA DE EXCLUSÕES - Áreas que NÃO são TI
        areas_excluidas = [
            # Outras engenharias
            'engenharia elétrica', 'engenharia eletrica',
            'engenharia civil',
            'engenharia mecânica', 'engenharia mecanica',
            'engenharia química', 'engenharia quimica',
            'engenharia de produção', 'engenharia de producao',
            'engenharia ambiental',
            'engenharia de alimentos',
            
            # Educação e áreas humanas
            'educação', 'educacao', 'pedagogia', 'ensino',
            'educacional', 'escolar',
            'relações étnico', 'relacoes etnico',
            'quilombola', 'indígena', 'indigena',
            
            # Outras áreas
            'enfermagem', 'medicina', 'saúde', 'saude',
            'direito', 'jurídico', 'juridico',
            'administração', 'administracao', 'gestão pública', 'gestao publica',
            'contabilidade', 'finanças', 'financas',
            'agricultura', 'agronomia', 'veterinária', 'veterinaria',
            
            # Energia (não é TI)
            'energia elétrica', 'energia eletrica',
            'fontes renováveis', 'fontes renovaveis',
            'energia solar', 'energia eólica', 'energia eolica',
            
            # Outros
            'turismo', 'hotelaria',
            'arquitetura', 'urbanismo'
        ]
        
        # Verifica se contém área excluída (palavra isolada)
        if any(self._contem_termo(texto, termo) for termo in areas_excluidas):
            return False
        
        # Termos ESPECÍFICOS de TI - removidos termos muito genéricos
        termos_tech = [
            # IA, ML e Ciência de Dados
            'inteligência artificial', 'inteligencia artificial',
            'machine learning', 'aprendizado de máquina', 'aprendizado de maquina',
            'deep learning', 'redes neurais', 'neural network',
            'data science', 'ciência de dados', 'ciencia de dados',
            'big data', 'analytics', 'análise de dados', 'analise de dados',
            'mineração de dados', 'mineracao de dados',
            'cientista de dados',
            
            # Desenvolvimento Web
            'desenvolvimento web', 'dev web', 'web development',
            'programação web', 'programacao web',
            'front-end', 'frontend', 'back-end', 'backend',
            'full-stack', 'fullstack',
            'javascript', 'typescript', 'react', 'angular', 'vue',
            'node.js', 'nodejs', 'python web', 'django', 'flask',
            'php', 'laravel', 'wordpress',
            'html5', 'css3', 'web design',
            'desenvolvimento de sites', 'desenvolvimento de aplicações web', 'desenvolvimento de aplicacoes web',
            
            # Desenvolvimento Mobile
            'desenvolvimento mobile', 'dev mobile', 'mobile development',
            'aplicativos móveis', 'aplicativos moveis',
            'android development', 'ios development',
            'flutter', 'react native',
            'kotlin', 'swift', 'mobile app',
            
            # Desenvolvimento de Software (específico)
            'desenvolvimento de software',
            'engenharia de software',  # Específico, não confunde com outras engenharias
            'desenvolvimento de aplicações', 'desenvolvimento de aplicacoes',
            'desenvolvimento de apps',
            'programação', 'programacao', 'programador',
            'análise e desenvolvimento de sistemas', 'analise e desenvolvimento de sistemas',
            
            # Cybersegurança
            'cibersegurança', 'ciberseguranca', 'cybersecurity',
            'segurança da informação', 'seguranca da informacao',
            'segurança cibernética', 'seguranca cibernetica',
            'ethical hacking', 'hacking ético', 'hacking etico',
            'pentest', 'penetration test', 'teste de invasão', 'teste de invasao',
            'forense digital', 'perícia digital', 'pericia digital',
            'lgpd', 'proteção de dados', 'protecao de dados',
            'segurança de redes', 'seguranca de redes',
            
            # Cloud e DevOps
            'cloud computing', 'computação em nuvem', 'computacao em nuvem',
            'aws', 'amazon web services', 'azure', 'google cloud', 'gcp',
            'devops', 'sre', 'site reliability',
            'kubernetes', 'docker', 'container',
            'ci/cd', 'integração contínua', 'integracao continua',
            'infraestrutura como código', 'infraestrutura como codigo',
            'terraform', 'ansible',
            
            # Infraestrutura e Redes (TI específico)
            'infraestrutura de ti', 'infraestrutura de tecnologia',
            'redes de computadores', 'administração de redes', 'administracao de redes',
            'servidor', 'servidores', 'datacenter',
            
            # Banco de Dados
            'banco de dados', 'database',
            'sql', 'mysql', 'postgresql', 'mongodb',
            'administração de banco de dados', 'administracao de banco de dados',
            'dba', 'modelagem de dados',
            
            # Sistemas e TI (bem específicos)
            'sistemas de informação', 'sistemas de informacao',
            'tecnologia da informação', 'tecnologia da informacao',
            'ciência da computação', 'ciencia da computacao',
            'análise de sistemas', 'analise de sistemas',
            'administração de sistemas', 'administracao de sistemas',
            
            # Tecnologias específicas
            'java', 'python programming', 'c#', 'c++',
            '.net', 'dotnet',
            'ruby on rails', 'go lang', 'rust programming',
            
            # Outras áreas de TI
            'games', 'desenvolvimento de jogos',
            'realidade virtual', 'realidade aumentada',
            'iot', 'internet das coisas', 'internet of things',
            'blockchain', 'criptomoedas',
            'ui/ux', 'design de interfaces', 'experiência do usuário', 'experiencia do usuario'
        ]
        
        return any(self._contem_termo(texto, termo) for termo in termos_tech)
    
    def _contem_termo(self, texto, termo):
        """Verifica se o termo aparece como palavra/expressão isolada (não como parte de outra palavra).
        Evita falsos positivos como 'ead' em 'sead' ou 'iot' em 'biblioteconomia'."""
        try:
            return re.search(r'(?<!\w)' + re.escape(termo) + r'(?!\w)', texto) is not None
        except:
            return termo in texto

    def _mes_para_numero(self, nome_mes):
        """Converte nome do mês em português para número"""
        mapa = {
            'janeiro': 1, 'jan': 1,
            'fevereiro': 2, 'fev': 2,
            'março': 3, 'marco': 3, 'mar': 3,
            'abril': 4, 'abr': 4,
            'maio': 5, 'mai': 5,
            'junho': 6, 'jun': 6,
            'julho': 7, 'jul': 7,
            'agosto': 8, 'ago': 8,
            'setembro': 9, 'set': 9, 'sept': 9,
            'outubro': 10, 'out': 10, 'oct': 10,
            'novembro': 11, 'nov': 11,
            'dezembro': 12, 'dez': 12, 'dec': 12,
        }
        return mapa.get(nome_mes.strip().lower())

    def extrair_data_do_texto(self, texto):
        """
        Tenta extrair uma data do texto do link ou contexto
        Retorna a data extraída ou None se não encontrar

        Formatos suportados:
        - DD/MM/YYYY ou DD/MM/YY
        - DD-MM-YYYY ou DD-MM-YY
        - YYYY-MM-DD (ISO)
        - DD de mês por extenso de YYYY ("15 de janeiro de 2025")
        - Mês por extenso de YYYY ("outubro de 2026")
        - Relativos: "há X dias/horas", "ontem", "hoje"
        """
        if not texto:
            return None
        t = texto.lower()
        agora = datetime.now()

        # 1. Relativos: "há 2 dias", "ha 3 horas", "há 15 minutos", "2 dias atrás"
        m_rel = re.search(r'h[áa]\s+(\d+)\s+(minuto|hora|dia|semana|m[eê]s)', t)
        if m_rel:
            try:
                qtd = int(m_rel.group(1))
                unidade = m_rel.group(2)
                if 'minuto' in unidade or 'hora' in unidade:
                    return agora
                if 'dia' in unidade:
                    return agora - timedelta(days=qtd)
                if 'semana' in unidade:
                    return agora - timedelta(days=qtd * 7)
                if 'mês' in unidade or 'mes' in unidade:
                    return agora - timedelta(days=qtd * 30)
            except:
                pass
        if re.search(r'\b(ontem)\b', t):
            return agora - timedelta(days=1)
        if re.search(r'\b(hoje)\b', t):
            return agora

        # 2. Padrões numéricos
        padroes = [
            r'\b(\d{1,2})[/\-](\d{1,2})[/\-](\d{2,4})\b',
            r'\b(\d{4})[/\-](\d{1,2})[/\-](\d{1,2})\b',
        ]
        for padrao in padroes:
            match = re.search(padrao, t)
            if match:
                try:
                    grupos = match.groups()
                    if len(grupos[0]) == 4:  # YYYY-MM-DD
                        ano, mes, dia = int(grupos[0]), int(grupos[1]), int(grupos[2])
                    else:  # DD/MM/YYYY
                        dia, mes, ano = int(grupos[0]), int(grupos[1]), int(grupos[2])
                    if ano < 100:
                        ano = 2000 + ano if ano < 50 else 1900 + ano
                    if 1 <= mes <= 12 and 1 <= dia <= 31 and 2000 <= ano <= 2030:
                        return datetime(ano, mes, dia)
                except:
                    continue

        # 3. "15 de janeiro de 2025" / "15 jan 2025" / "15/janeiro/2025"
        m_ext = re.search(
            r'\b(\d{1,2})\s+(?:de\s+)?([a-zçãõéê]+)\s+(?:de\s+)?(20\d{2})\b', t)
        if m_ext:
            try:
                dia = int(m_ext.group(1))
                mes = self._mes_para_numero(m_ext.group(2))
                ano = int(m_ext.group(3))
                if mes and 1 <= dia <= 31 and 2000 <= ano <= 2030:
                    return datetime(ano, mes, dia)
            except:
                pass

        # 4. "outubro de 2026" / "maio/2026" (assume dia 1)
        m_mes_ano = re.search(r'\b([a-zçãõéê]+)\s+(?:de\s+|/)?(20\d{2})\b', t)
        if m_mes_ano:
            try:
                mes = self._mes_para_numero(m_mes_ano.group(1))
                ano = int(m_mes_ano.group(2))
                if mes and 2000 <= ano <= 2030:
                    return datetime(ano, mes, 1)
            except:
                pass

        # 5. Apenas o ano (último recurso)
        match_ano = re.search(r'\b(20\d{2})\b', t)
        if match_ano:
            try:
                ano = int(match_ano.group(1))
                return datetime(ano, 1, 1)
            except:
                pass

        return None

    def e_edital_recente(self, texto, contexto='', meses=None):
        """
        Verifica se o edital é recente.

        Estratégia:
        1. Tenta extrair data do texto do link
        2. Tenta extrair data do contexto ao redor
        3. Se não encontrar data, considera como recente (assume que é novo)
        """
        limite_meses = meses if meses is not None else self.meses_arquivo
        data_limite = datetime.now() - timedelta(days=limite_meses * 30)

        texto_completo = f"{texto} {contexto}".lower()
        data_encontrada = self.extrair_data_do_texto(texto_completo)

        if data_encontrada:
            e_recente = data_encontrada >= data_limite
            if not e_recente:
                print(f"  ⏭️ Ignorado (muito antigo): {texto[:60]}... ({data_encontrada.strftime('%d/%m/%Y')})")
            return e_recente

        return True
    
    def normalizar_url(self, href, url_base):
        """
        Transforma URLs relativas em URLs absolutas
        """
        if href.startswith('http'):
            return href
        elif href.startswith('/'):
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
        """
        if not self.novas_oportunidades:
            print("\n📭 Nenhuma nova oportunidade encontrada.")
            return
        
        email_remetente = os.environ.get('EMAIL_REMETENTE')
        email_senha = os.environ.get('EMAIL_SENHA')
        email_destinatario = os.environ.get('EMAIL_DESTINATARIO')
        
        if not all([email_remetente, email_senha, email_destinatario]):
            print("⚠️ Configurações de email não encontradas nas variáveis de ambiente")
            print("🔍 Novas oportunidades encontradas (não enviadas):")
            for oport in self.novas_oportunidades:
                print(f"  - {oport['titulo']} ({oport['instituto']})")
            return
        
        html_content = self.montar_html_email()
        
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f'🎓 {len(self.novas_oportunidades)} Nova(s) Pós-Graduação(ões) EAD Gratuita(s)!'
        msg['From'] = email_remetente
        msg['To'] = email_destinatario
        
        parte_html = MIMEText(html_content, 'html', 'utf-8')
        msg.attach(parte_html)
        
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
                servidor.login(email_remetente, email_senha)
                servidor.send_message(msg)
            
            print(f"\n📧 Email enviado com sucesso para {email_destinatario}!")
            print(f"   Total de oportunidades: {len(self.novas_oportunidades)}")
            
        except Exception as e:
            print(f"\n❌ Erro ao enviar email: {e}")
    
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
    
    def _data_referencia_edital(self, edital):
        """Retorna a melhor data disponível: data_publicacao se válida, senão data_encontrado"""
        try:
            dp = edital.get('data_publicacao')
            if dp:
                return datetime.fromisoformat(dp)
        except:
            pass
        try:
            return datetime.fromisoformat(edital['data_encontrado'])
        except:
            return None

    def limpar_historico_antigo(self):
        """
        Remove editais antigos do histórico (além de meses_arquivo)
        Mantém até 6 meses para permitir o botão 2→4→6
        """
        if not self.dados_anteriores['editais_encontrados']:
            print("ℹ️ Histórico vazio, nada para limpar")
            return

        data_limite = datetime.now() - timedelta(days=self.meses_arquivo * 30)
        total_antes = len(self.dados_anteriores['editais_encontrados'])

        # Filtra apenas editais recentes
        editais_recentes = []
        for edital in self.dados_anteriores['editais_encontrados']:
            data_edital = self._data_referencia_edital(edital)
            if data_edital is None:
                editais_recentes.append(edital)
            elif data_edital >= data_limite:
                editais_recentes.append(edital)
        
        self.dados_anteriores['editais_encontrados'] = editais_recentes
        total_depois = len(editais_recentes)
        removidos = total_antes - total_depois
        
        print(f"🧹 Limpeza de histórico:")
        print(f"   Antes: {total_antes} editais")
        print(f"   Depois: {total_depois} editais")
        print(f"   Removidos: {removidos} editais antigos")
        
        if removidos > 0:
            self.salvar_dados_historicos()
    
    def executar(self):
        """Método principal que executa todo o fluxo"""
        print("="*60)
        print("🚀 Iniciando monitoramento de Pós-Graduações EAD")
        print(f"📊 Monitorando {len(self.sites)} institutos")
        print(f"📅 Exibição padrão: últimos {self.meses_retroativos} meses | Arquivo: {self.meses_arquivo} meses")
        print("="*60)

        # Limpa itens além do arquivo (6m) antes de processar
        self.limpar_historico_antigo()

        # Faz scraping de cada site
        for site in self.sites:
            editais = self.fazer_scraping(site)
            self.novas_oportunidades.extend(editais)

        # Se encontrou novidades, atualiza histórico
        if self.novas_oportunidades:
            for oport in self.novas_oportunidades:
                self.dados_anteriores['editais_encontrados'].append(oport)
            self.salvar_dados_historicos()
        else:
            # Garante que limpeza de antigos seja persistida mesmo sem novidades
            self.salvar_dados_historicos()
        
        # Gera JSON para o frontend (sempre, mesmo sem novidades)
        self.gerar_json_frontend()
        
        # Envia email com as novidades
        self.enviar_email()
        
        print("\n" + "="*60)
        print("✅ Monitoramento concluído!")
        print("="*60)

# Ponto de entrada do script
if __name__ == "__main__":
    monitor = PosGraduacaoMonitor()
    monitor.executar()
