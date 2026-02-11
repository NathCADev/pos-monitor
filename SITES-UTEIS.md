# 📚 Sites Úteis para Adicionar ao Monitor

## Institutos Federais por Região

### Sul
- **IFRS** - Instituto Federal do Rio Grande do Sul
  - https://ifrs.edu.br/editais/
  - https://ifrs.edu.br/ensino/pos-graduacao/

- **IFSC** - Instituto Federal de Santa Catarina
  - https://www.ifsc.edu.br/editais
  - https://www.ifsc.edu.br/pos-graduacao

- **IFPR** - Instituto Federal do Paraná
  - https://reitoria.ifpr.edu.br/menu-de-apoio/editais/
  - https://reitoria.ifpr.edu.br/pos-graduacao/

- **IFSUL** - Instituto Federal Sul-rio-grandense
  - http://www.ifsul.edu.br/editais

### Sudeste
- **IFSULDEMINAS** - Instituto Federal do Sul de Minas Gerais
  - https://portal.ifsuldeminas.edu.br/index.php/editais

- **IFSP** - Instituto Federal de São Paulo
  - https://www.ifsp.edu.br/editais

- **IFMG** - Instituto Federal de Minas Gerais
  - https://www.ifmg.edu.br/portal/ensino/pos-graduacao

- **IFRJ** - Instituto Federal do Rio de Janeiro
  - https://portal.ifrj.edu.br/editais

- **IFES** - Instituto Federal do Espírito Santo
  - https://www.ifes.edu.br/editais

### Centro-Oeste
- **IFB** - Instituto Federal de Brasília
  - https://www.ifb.edu.br/editais

- **IFGOIANO** - Instituto Federal Goiano
  - https://www.ifgoiano.edu.br/home/index.php/editais.html

- **IFMT** - Instituto Federal de Mato Grosso
  - http://www.ifmt.edu.br/editais

### Nordeste
- **IFBA** - Instituto Federal da Bahia
  - https://portal.ifba.edu.br/editais/

- **IFCE** - Instituto Federal do Ceará
  - https://ifce.edu.br/editais

- **IFPB** - Instituto Federal da Paraíba
  - https://www.ifpb.edu.br/editais

- **IFPE** - Instituto Federal de Pernambuco
  - https://www.ifpe.edu.br/editais

### Norte
- **IFPA** - Instituto Federal do Pará
  - https://ifpa.edu.br/editais

- **IFAM** - Instituto Federal do Amazonas
  - http://www2.ifam.edu.br/editais

## Universidades Federais com EAD

- **UFSCAR** - Universidade Federal de São Carlos
  - https://www.ufscar.br/editais
  
- **UFMG** - Universidade Federal de Minas Gerais
  - https://ufmg.br/editais

- **UFRGS** - Universidade Federal do Rio Grande do Sul
  - https://www.ufrgs.br/ufrgs/editais

## Plataformas Agregadoras

- **Portal Nilo Peçanha** - Dados da Rede Federal
  - http://plataformanilopecanha.mec.gov.br/

- **Portal MEC** - Cursos Gratuitos
  - https://www.gov.br/mec/pt-br

- **e-MEC** - Cadastro Nacional de Cursos
  - https://emec.mec.gov.br/

## Dicas para Adicionar no Scraper

Para cada site, você vai precisar:

1. **URL da página de editais**
2. **Palavras-chave específicas** daquele site
3. **Seletores CSS** (se quiser ser mais preciso)

### Exemplo de como adicionar:

```python
{
    'nome': 'IFSC',
    'url': 'https://www.ifsc.edu.br/editais',
    'palavras_chave': [
        'pós-graduação', 
        'pos-graduacao', 
        'especialização',
        'ead',
        'distância',
        'seleção',
        'processo seletivo'
    ]
}
```

## Áreas de Tecnologia - Termos para Buscar

Adicione estes termos no método `e_area_tecnologia()`:

```python
termos_tech = [
    # Geral
    'tecnologia', 'ti', 'informática', 'informatica',
    
    # Computação
    'computação', 'computacao', 'ciência da computação',
    'sistemas de informação', 'sistemas',
    
    # Desenvolvimento
    'desenvolvimento', 'programação', 'programacao',
    'software', 'engenharia de software',
    
    # Dados
    'dados', 'data science', 'ciência de dados',
    'big data', 'analytics', 'análise de dados',
    
    # Segurança
    'segurança', 'cibersegurança', 'cybersecurity',
    'segurança da informação',
    
    # Redes
    'redes', 'infraestrutura', 'cloud', 'nuvem',
    
    # IA/ML
    'inteligência artificial', 'ia', 'machine learning',
    'aprendizado de máquina', 'deep learning',
    
    # Web/Mobile
    'web', 'mobile', 'aplicativos', 'apps',
    
    # DevOps
    'devops', 'automação', 'integração contínua',
    
    # Gestão TI
    'gestão de ti', 'governança', 'itil', 'cobit'
]
```

## Como Descobrir a URL Correta

1. Acesse o site do instituto
2. Procure por "Editais" ou "Processos Seletivos"
3. Acesse a página
4. Copie a URL da barra de endereço
5. Adicione no scraper!

## Teste Individual de Sites

Se quiser testar um site específico antes de adicionar:

```python
# Adicione isso no final do scraper.py temporariamente
if __name__ == "__main__":
    # Teste individual
    teste = {
        'nome': 'TESTE',
        'url': 'URL_AQUI',
        'palavras_chave': ['pós-graduação', 'ead']
    }
    
    monitor = PosGraduacaoMonitor()
    resultados = monitor.fazer_scraping(teste)
    
    print(f"\nEncontrados: {len(resultados)}")
    for r in resultados:
        print(f"- {r['titulo']}")
```

---

**💡 Dica**: Comece com 3-5 sites e vá adicionando aos poucos!
