# 👀 O QUE VOCÊ VAI VER NO GITHUB - Guia Visual Completo

> **Diferença importante**: GitHub Pages = hospedar sites estáticos | GitHub Actions = rodar código/automações

Você não vai criar um site, vai usar o GitHub Actions para rodar seu código Python automaticamente!

---

## 📍 TELA 1: Criar Repositório

Quando você clicar em "New repository":

```
┌─────────────────────────────────────────────────────────────┐
│ Create a new repository                                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ Repository name *                                            │
│ ┌──────────────────────────────────────────────────────┐   │
│ │ pos-monitor                                          │   │
│ └──────────────────────────────────────────────────────┘   │
│                                                              │
│ Description (optional)                                       │
│ ┌──────────────────────────────────────────────────────┐   │
│ │ Monitor de pós-graduações EAD gratuitas              │   │
│ └──────────────────────────────────────────────────────┘   │
│                                                              │
│ ◉ Public        ◯ Private   ← ESCOLHA PRIVATE!             │
│                                                              │
│ ☑ Add a README file                                         │
│ ☐ Add .gitignore                                            │
│ ☐ Choose a license                                          │
│                                                              │
│                    [Create repository]                       │
└─────────────────────────────────────────────────────────────┘
```

**O que preencher:**
- Nome: `pos-monitor`
- Descrição: "Monitor de pós-graduações EAD gratuitas"
- ✅ Marque "Private" (para seus dados ficarem privados)
- ✅ Marque "Add a README file"

---

## 📍 TELA 2: Repositório Vazio (Inicial)

Após criar, você verá:

```
┌─────────────────────────────────────────────────────────────┐
│ seu-usuario / pos-monitor                              🔒 Private │
├─────────────────────────────────────────────────────────────┤
│ <> Code    Issues    Pull requests    Actions    Settings  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ [Add file ▼]  [<> Code ▼]  [About ⚙]                       │
│                                                              │
│ 📄 README.md                                                 │
│                                                              │
│ pos-monitor                                                  │
│ ─────────────────────────                                   │
│ Monitor de pós-graduações EAD gratuitas                     │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Aqui você vai:**
1. Clicar em "Add file" (botão verde)
2. Escolher "Upload files"

---

## 📍 TELA 3: Upload de Arquivos

```
┌─────────────────────────────────────────────────────────────┐
│ Upload files                                                 │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│    ┌─────────────────────────────────────────────────┐     │
│    │                                                  │     │
│    │         📁 Arraste arquivos aqui                │     │
│    │              ou clique para selecionar          │     │
│    │                                                  │     │
│    └─────────────────────────────────────────────────┘     │
│                                                              │
│ Commit changes                                               │
│ ┌──────────────────────────────────────────────────────┐   │
│ │ Add files via upload                                 │   │
│ └──────────────────────────────────────────────────────┘   │
│                                                              │
│ ◉ Commit directly to the main branch                        │
│                                                              │
│                    [Commit changes]                          │
└─────────────────────────────────────────────────────────────┘
```

**O que fazer:**
1. Arraste TODOS os arquivos do ZIP descompactado
2. IMPORTANTE: Mantenha as pastas! (`.github/workflows/`)
3. Clique "Commit changes"

---

## 📍 TELA 4: Repositório com Arquivos

Depois do upload:

```
┌─────────────────────────────────────────────────────────────┐
│ seu-usuario / pos-monitor                              🔒 Private │
├─────────────────────────────────────────────────────────────┤
│ <> Code    Issues    Pull requests    Actions    Settings  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ 📁 .github                                                   │
│ 📄 .gitignore                                                │
│ 📄 INICIO-RAPIDO.md                                          │
│ 📄 README.md                                                 │
│ 📄 SITES-UTEIS.md                                            │
│ 📄 historico.json                                            │
│ 📄 requirements.txt                                          │
│ 📄 scraper.py                                                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

Agora você vê todos os arquivos! ✅

---

## 📍 TELA 5: Criar Secrets

Clique em **Settings** (topo) > **Secrets and variables** (menu esquerdo) > **Actions**

```
┌─────────────────────────────────────────────────────────────┐
│ Actions secrets and variables                                │
├─────────────────────────────────────────────────────────────┤
│ Secrets   Variables                                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ Secrets são variáveis de ambiente criptografadas            │
│                                                              │
│ [New repository secret]                                      │
│                                                              │
│ No secrets yet                                               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

Clique em **[New repository secret]**, você verá:

```
┌─────────────────────────────────────────────────────────────┐
│ New secret                                                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ Name *                                                       │
│ ┌──────────────────────────────────────────────────────┐   │
│ │ EMAIL_REMETENTE                                      │   │
│ └──────────────────────────────────────────────────────┘   │
│                                                              │
│ Secret *                                                     │
│ ┌──────────────────────────────────────────────────────┐   │
│ │ seuemail@gmail.com                                   │   │
│ └──────────────────────────────────────────────────────┘   │
│                                                              │
│                    [Add secret]                              │
└─────────────────────────────────────────────────────────────┘
```

**Repita 3 vezes para criar:**
1. `EMAIL_REMETENTE` = seu-email@gmail.com
2. `EMAIL_SENHA` = abcd efgh ijkl mnop (senha de 16 caracteres do Gmail)
3. `EMAIL_DESTINATARIO` = seu-email@gmail.com

Depois de criar os 3, você verá:

```
┌─────────────────────────────────────────────────────────────┐
│ Repository secrets                                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ [New repository secret]                                      │
│                                                              │
│ NAME                      UPDATED                            │
│ EMAIL_DESTINATARIO       now                                │
│ EMAIL_REMETENTE          now                                │
│ EMAIL_SENHA              now                                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 📍 TELA 6: Habilitar Permissões

Settings > Actions > General (role até o final da página):

```
┌─────────────────────────────────────────────────────────────┐
│ Workflow permissions                                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ Choose the default permissions granted to the GITHUB_TOKEN  │
│                                                              │
│ ◯ Read repository contents and packages permissions         │
│ ◉ Read and write permissions  ← SELECIONE ESTA!            │
│                                                              │
│ ☑ Allow GitHub Actions to create and approve pull requests │
│                                                              │
│                         [Save]                               │
└─────────────────────────────────────────────────────────────┘
```

**Marque**: Read and write permissions
**Clique**: Save

---

## 📍 TELA 7: Actions Tab (A MÁGICA!)

Clique na aba **Actions** (topo da página):

### Antes de executar:

```
┌─────────────────────────────────────────────────────────────┐
│ Actions                                                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ All workflows    Monitor Pós-Graduação EAD                  │
│                                                              │
│ ┌──────────────────────────────────────────────────────┐   │
│ │ Monitor Pós-Graduação EAD                             │   │
│ │ ─────────────────────────────────────────────────────│   │
│ │ This workflow has a workflow_dispatch event trigger   │   │
│ │                                                       │   │
│ │                      [Run workflow ▼]                 │   │
│ └──────────────────────────────────────────────────────┘   │
│                                                              │
│ No workflow runs yet                                         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

Clique em **[Run workflow ▼]**, aparece:

```
┌─────────────────────────────────────────────────────────────┐
│ Use workflow from                                            │
│ ◉ Branch: main                                              │
│                                                              │
│                    [Run workflow]                            │
└─────────────────────────────────────────────────────────────┘
```

Clique no botão verde **[Run workflow]**

---

## 📍 TELA 8: Workflow Executando (TEMPO REAL!)

Após alguns segundos, atualize a página:

```
┌─────────────────────────────────────────────────────────────┐
│ All workflows                                                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ 🟡 Monitor Pós-Graduação EAD                                │
│    #1: Workflow run                                          │
│    main                                                      │
│    seu-usuario triggered via workflow_dispatch              │
│    • In progress - 15s                                       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Clique no workflow** para ver os detalhes:

```
┌─────────────────────────────────────────────────────────────┐
│ Monitor Pós-Graduação EAD #1                                │
├─────────────────────────────────────────────────────────────┤
│ Summary    Jobs (1)                                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ Jobs                                                         │
│ 🟡 monitorar / Monitorar Novas Oportunidades  In progress   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Clique em "Monitorar Novas Oportunidades"** para ver os LOGS EM TEMPO REAL:

---

## 📍 TELA 9: LOGS EM TEMPO REAL! 🎬

Esta é a tela mais legal! Você vê tudo acontecendo:

```
┌─────────────────────────────────────────────────────────────┐
│ Monitorar Novas Oportunidades                               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ ▼ Set up job                                    ✅ 2s       │
│ ▼ 📥 Checkout do repositório                    ✅ 1s       │
│ ▼ 🐍 Configurar Python 3.11                     ✅ 4s       │
│ ▼ 📦 Instalar dependências                      ✅ 5s       │
│ ► 🔍 Executar monitoramento                     ⏳ Running  │
│   │                                                          │
│   │ ============================================             │
│   │ 🚀 Iniciando monitoramento de Pós-Graduações EAD      │
│   │ ============================================             │
│   │                                                          │
│   │ 🔍 Analisando: IFSULDEMINAS                            │
│   │   ✨ NOVO: Especialização em Desenvolvimento Web...    │
│   │                                                          │
│   │ 🔍 Analisando: IFSP                                     │
│   │                                                          │
│   │ 🔍 Analisando: IFRS                                     │
│   │   ✨ NOVO: Pós em Segurança da Informação...           │
│   │                                                          │
│   │ ✅ Histórico salvo com sucesso                          │
│   │ 📧 Email enviado com sucesso para seuemail@gmail.com!  │
│   │    Total de oportunidades: 2                            │
│   │                                                          │
│   │ ============================================             │
│   │ ✅ Monitoramento concluído!                             │
│   │ ============================================             │
│                                                              │
│ ▼ 💾 Salvar histórico                           ✅ 2s       │
│ ▼ 📊 Status da execução                         ✅ 1s       │
│                                                              │
│ ✅ Total duration: 34s                                      │
└─────────────────────────────────────────────────────────────┘
```

**VOCÊ CONSEGUE VER TUDO ACONTECENDO!** 🎉

- Quais sites foram verificados
- Quantos editais foram encontrados
- Se o email foi enviado
- Erros (se houver)

---

## 📍 TELA 10: Histórico de Execuções

Voltando para Actions, você verá um histórico:

```
┌─────────────────────────────────────────────────────────────┐
│ All workflows                                                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ ✅ Monitor Pós-Graduação EAD                                │
│    #3: Scheduled                                             │
│    main                                                      │
│    Scheduled - 2 hours ago                                   │
│    ✅ 34s                                                    │
│                                                              │
│ ✅ Monitor Pós-Graduação EAD                                │
│    #2: Scheduled                                             │
│    main                                                      │
│    Scheduled - 3 days ago                                    │
│    ✅ 28s                                                    │
│                                                              │
│ ✅ Monitor Pós-Graduação EAD                                │
│    #1: Workflow dispatch                                     │
│    main                                                      │
│    seu-usuario triggered - 1 week ago                        │
│    ✅ 34s                                                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

Cada linha = uma execução!
- ✅ = Sucesso
- ❌ = Erro
- 🟡 = Executando agora

---

## 📍 TELA 11: Ver o Arquivo historico.json

Clique em `historico.json` no repositório:

```
┌─────────────────────────────────────────────────────────────┐
│ historico.json                                               │
├─────────────────────────────────────────────────────────────┤
│ 1  {                                                         │
│ 2    "editais_encontrados": [                               │
│ 3      {                                                     │
│ 4        "titulo": "Especialização em Desenvolvimento Web", │
│ 5        "url": "https://portal.ifsuldeminas.edu.br/...",  │
│ 6        "instituto": "IFSULDEMINAS",                       │
│ 7        "data_encontrado": "2026-02-11T08:15:00"          │
│ 8      },                                                    │
│ 9      {                                                     │
│ 10       "titulo": "Pós em Segurança da Informação",        │
│ 11       "url": "https://ifrs.edu.br/editais/123",          │
│ 12       "instituto": "IFRS",                                │
│ 13       "data_encontrado": "2026-02-11T08:15:30"          │
│ 14     }                                                     │
│ 15   ]                                                       │
│ 16 }                                                         │
└─────────────────────────────────────────────────────────────┘
```

Você pode ver **TUDO** que já foi encontrado!

---

## 📧 O EMAIL QUE VOCÊ VAI RECEBER

No seu Gmail:

```
┌─────────────────────────────────────────────────────────────┐
│ De: seuemail@gmail.com                                       │
│ Para: seuemail@gmail.com                                     │
│ Assunto: 🎓 2 Nova(s) Pós-Graduação(ões) EAD Gratuita(s)!   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   ╔═══════════════════════════════════════════════════╗    │
│   ║  🎓 Novas Pós-Graduações EAD Encontradas!        ║    │
│   ║                                                    ║    │
│   ║  Encontramos 2 nova(s) oportunidade(s)           ║    │
│   ║  gratuita(s) para você!                           ║    │
│   ╚═══════════════════════════════════════════════════╝    │
│                                                              │
│   ┌───────────────────────────────────────────────────┐    │
│   │ 📍 IFSULDEMINAS                                   │    │
│   │ Especialização em Desenvolvimento Web             │    │
│   │ [Ver Edital Completo]  (botão azul clicável)     │    │
│   │ Encontrado em: 11/02/2026 às 08:15               │    │
│   └───────────────────────────────────────────────────┘    │
│                                                              │
│   ┌───────────────────────────────────────────────────┐    │
│   │ 📍 IFRS                                            │    │
│   │ Pós-Graduação em Segurança da Informação         │    │
│   │ [Ver Edital Completo]  (botão azul clicável)     │    │
│   │ Encontrado em: 11/02/2026 às 08:15               │    │
│   └───────────────────────────────────────────────────┘    │
│                                                              │
│   ───────────────────────────────────────────────────────   │
│   ⚙️ Automação executada em 11/02/2026 às 08:16            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 RESUMO: O QUE VOCÊ CONSEGUE VER

✅ **Repositório** - Todos os arquivos organizados
✅ **Secrets** - Lista de variáveis (valor fica oculto)
✅ **Actions** - Lista de todas as execuções
✅ **Logs em tempo real** - Ver o script rodando linha por linha
✅ **Histórico de execuções** - Sucesso/erro de cada execução
✅ **historico.json** - Todo o histórico de editais encontrados
✅ **Emails** - Notificações lindas no Gmail

---

## 🎯 DIFERENÇA: GitHub Pages vs GitHub Actions

### GitHub Pages (o que você conhece):
```
Hospeda sites estáticos (HTML/CSS/JS)
→ Você acessa: https://usuario.github.io/repositorio
→ Mostra uma página web
```

### GitHub Actions (o que você vai usar):
```
Executa código (Python, Node, etc)
→ Você NÃO acessa via browser
→ Roda automaticamente em horários definidos
→ Você vê os resultados em "Actions" > Logs
→ Recebe notificação por email
```

---

## 💡 É como se fosse...

**GitHub Pages** = Publicar um site no ar
**GitHub Actions** = Ter um computador na nuvem rodando seu código automaticamente

No seu caso:
- ❌ Você NÃO vai criar um site
- ✅ Você VAI ter um robô que roda 2x por semana
- ✅ Você VAI ver os logs de execução
- ✅ Você VAI receber emails quando encontrar algo

---

## ✨ BONUS: Quer ver rodando AGORA?

Você pode testar localmente ANTES de colocar no GitHub:

1. Instale Python no seu PC: https://www.python.org/downloads/
2. Extraia o ZIP
3. Abra o terminal/prompt na pasta
4. Execute:

```bash
pip install -r requirements.txt
python scraper.py
```

Você verá a mesma coisa que aparece nos logs do GitHub! 🎉

Mas vai dar erro no email porque as variáveis não estão configuradas.
No GitHub, com os Secrets configurados, funciona perfeito!

---

**Ficou mais claro agora?** 😊

Você vai ter várias telas para ver, acompanhar tudo em tempo real, e receber emails lindos!
