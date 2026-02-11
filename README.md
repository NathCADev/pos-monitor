# 🎓 Monitor de Pós-Graduação EAD Gratuita

Automação que monitora abertura de inscrições de pós-graduações EAD gratuitas em institutos federais e oferece duas formas de acompanhamento:
- 📧 **Email**: Notificações automáticas de novas oportunidades
- 🌐 **Página Web**: Visualize todas as oportunidades em uma interface moderna

## 🎯 O que este projeto faz?

- ✅ Monitora automaticamente sites de institutos federais (IFSULDEMINAS, IFSP, IFRS, etc.)
- ✅ Detecta novos editais de pós-graduação EAD na área de tecnologia
- ✅ Envia email quando encontra novas oportunidades
- ✅ Publica dados em uma página web bonita e funcional
- ✅ Roda automaticamente 2x por semana (segundas e quintas) **DE GRAÇA** no GitHub Actions
- ✅ Mantém histórico completo do que já foi encontrado

## 🌐 Novidade: Versão Híbrida (Actions + Pages)

Agora você pode escolher **como** quer acompanhar as oportunidades:

### Opção 1: Email (original)
- Recebe notificações apenas de **novas** oportunidades
- Perfeito se você quer ser avisado imediatamente

### Opção 2: Página Web (novo!)
- Acesse quando quiser: `https://seu-usuario.github.io/pos-monitor`
- Vê **todas** as oportunidades acumuladas
- Interface moderna e responsiva
- Filtros por instituto e busca por palavra-chave
- Estatísticas visuais

### Opção 3: Ambos! (recomendado)
- Email te avisa de novidades
- Página mostra tudo organizado
- O melhor dos dois mundos!

## 🚀 Como Configurar (Passo a Passo)

### 1️⃣ Criar conta no GitHub (se não tiver)

1. Acesse https://github.com
2. Clique em "Sign up"
3. Siga as instruções

### 2️⃣ Criar o repositório

1. No GitHub, clique em "New repository" (botão verde)
2. Nome: `pos-graduacao-monitor` (ou qualquer nome que preferir)
3. Deixe como **Private** (privado) se quiser manter seus dados privados
4. Marque "Add a README file"
5. Clique em "Create repository"

### 3️⃣ Fazer upload dos arquivos

**Opção A - Upload manual (mais fácil):**
1. No seu repositório, clique em "Add file" > "Upload files"
2. Arraste os arquivos que você baixou:
   - `scraper.py`
   - `requirements.txt`
   - `.github/workflows/monitor.yml` (mantenha essa estrutura de pastas!)
3. Clique em "Commit changes"

**Opção B - Via Git (se você já usa):**
```bash
git clone https://github.com/SEU-USUARIO/pos-graduacao-monitor.git
cd pos-graduacao-monitor
# Copie os arquivos para cá
git add .
git commit -m "Adicionar monitor de pós-graduação"
git push
```

### 4️⃣ Configurar Email (IMPORTANTE!)

Para enviar emails, você precisa configurar uma "Senha de App" do Gmail:

1. **Acesse sua conta Google**: https://myaccount.google.com/
2. **Segurança** > **Verificação em duas etapas** (você precisa habilitar isso primeiro!)
3. Depois vá em **Senhas de app**: https://myaccount.google.com/apppasswords
4. Crie uma senha de app:
   - Nome: "Monitor Pós-Graduação"
   - Copie a senha gerada (16 caracteres)

### 5️⃣ Adicionar Secrets no GitHub

Os "Secrets" são variáveis seguras que só o GitHub Actions consegue ver.

1. No seu repositório, vá em **Settings** (Configurações)
2. No menu lateral, clique em **Secrets and variables** > **Actions**
3. Clique em **New repository secret** e adicione 3 secrets:

| Nome | Valor | Exemplo |
|------|-------|---------|
| `EMAIL_REMETENTE` | Seu email Gmail | `seuemail@gmail.com` |
| `EMAIL_SENHA` | Senha de app que você criou | `abcd efgh ijkl mnop` |
| `EMAIL_DESTINATARIO` | Email onde quer receber | `seuemail@gmail.com` |

**⚠️ IMPORTANTE**: A senha NÃO é a senha normal do Gmail! É a "Senha de App" de 16 caracteres!

### 6️⃣ Habilitar GitHub Actions

1. No repositório, vá em **Actions**
2. Se pedir para habilitar workflows, clique em "I understand my workflows, go ahead and enable them"
3. Pronto! O GitHub Actions está ativo

### 7️⃣ [OPCIONAL] Habilitar GitHub Pages

Se você quer a **página web** além do email:

1. Vá em **Settings** > **Pages**
2. Em "Source", selecione: **Deploy from a branch**
3. Em "Branch", selecione: **main** e **/ (root)**
4. Clique em **Save**
5. Aguarde 1-2 minutos
6. Acesse: `https://seu-usuario.github.io/pos-monitor`

📖 Veja instruções completas em: **GITHUB-PAGES-SETUP.md**

### 8️⃣ Testar manualmente (primeiro teste!)

Antes de esperar a automação rodar, vamos testar:

1. Vá em **Actions**
2. Clique em "Monitor Pós-Graduação EAD" (nome do workflow)
3. Clique em **Run workflow** (botão no lado direito)
4. Clique em "Run workflow" verde
5. Aguarde alguns segundos e atualize a página
6. Clique no workflow que apareceu para ver os logs

Se tudo estiver certo:
- ✅ Você verá os logs mostrando que o script rodou
- ✅ Se houver oportunidades novas, você receberá um email!

## 📅 Quando a automação roda?

Por padrão, configurei para rodar:
- **Segundas-feiras às 8h** (horário de Brasília)
- **Quintas-feiras às 11h** (horário de Brasília)

### Como mudar o horário?

Edite o arquivo `.github/workflows/monitor.yml`, na seção `cron`:

```yaml
schedule:
  - cron: '0 11 * * 1'  # Segunda 8h BRT
  - cron: '0 14 * * 4'  # Quinta 11h BRT
```

**Dicas de cron:**
- `0 11 * * *` = Todo dia às 11h UTC (8h BRT)
- `0 14 * * 1,3,5` = Seg/Qua/Sex às 14h UTC (11h BRT)
- Use https://crontab.guru/ para criar outros horários

**⚠️ Lembre-se**: GitHub usa horário UTC. Brasília = UTC-3, então subtraia 3 horas.

## 📧 Como vai ser o email?

Quando o monitor encontrar novas oportunidades, você receberá um email HTML bonito com:

- 🎓 Título do edital
- 📍 Instituto (IFSULDEMINAS, IFSP, etc.)
- 🔗 Link direto para o edital
- 📅 Data/hora que foi encontrado

## 🔧 Como adicionar mais institutos?

Edite o arquivo `scraper.py`, no método `carregar_sites()`:

```python
{
    'nome': 'NOVO INSTITUTO',
    'url': 'https://site.com.br/editais',
    'palavras_chave': ['pós-graduação', 'ead', 'especialização']
}
```

## 📊 Ver o histórico

O arquivo `historico.json` guarda tudo que já foi encontrado. Você pode ver ele no repositório!

## 🐛 Troubleshooting (Resolução de Problemas)

### Não recebi email

1. ✅ Verificou se as Secrets estão configuradas corretamente?
2. ✅ A senha é a "Senha de App" e não a senha normal?
3. ✅ O workflow rodou sem erros? (veja em Actions)
4. ✅ Verifica spam/lixo eletrônico

### O workflow não executa automaticamente

1. O repositório precisa ter pelo menos 1 commit nos últimos 60 dias
2. Se ficar inativo, o GitHub desabilita automaticamente (você reativa em Actions)

### Erro "Permission denied"

1. Vá em Settings > Actions > General
2. Em "Workflow permissions", selecione "Read and write permissions"
3. Salve

## 📚 Conceitos que você aprendeu

- **Web Scraping**: Extrair dados de sites automaticamente
- **BeautifulSoup**: Biblioteca Python para parsing de HTML
- **GitHub Actions**: Automação CI/CD gratuita da cloud
- **Cron**: Agendamento de tarefas (como Task Scheduler)
- **Secrets**: Variáveis seguras para credenciais
- **SMTP**: Protocolo para envio de emails

## 🎓 Próximos passos / Melhorias possíveis

- [ ] Adicionar mais institutos federais
- [ ] Criar versão com Telegram ao invés de email
- [ ] Adicionar filtros por estado/região
- [ ] Salvar histórico em banco de dados (SQLite)
- [ ] Criar dashboard web para visualizar oportunidades
- [ ] Adicionar testes automatizados

## 💡 Dúvidas?

Se tiver algum problema, verifique:
1. Os logs em **Actions** no GitHub
2. Se os Secrets estão configurados
3. Se a senha de app do Gmail está correta

## 📝 Licença

Livre para usar e modificar como quiser! 🎉

---

**Criado com 💜 para automatizar sua busca por qualificação profissional!**
