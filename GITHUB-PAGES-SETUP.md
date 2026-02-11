# 🌐 Configuração do GitHub Pages - Versão Híbrida

Este guia mostra como configurar a **versão híbrida** que combina:
- **GitHub Actions** → Faz scraping automaticamente
- **GitHub Pages** → Exibe os resultados em uma página bonita

## 🎯 Como Funciona

```
┌─────────────────────────────────────────────────────────┐
│ BACKEND (GitHub Actions)                                │
│ ↓                                                        │
│ 1. Roda scraper.py 2x/semana (seg/qui)                 │
│ 2. Salva resultados.json                                │
│ 3. Commit automático no repositório                     │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│ FRONTEND (GitHub Pages)                                 │
│ ↓                                                        │
│ 1. Você acessa: usuario.github.io/pos-monitor          │
│ 2. JavaScript carrega resultados.json                   │
│ 3. Exibe cards lindos com as oportunidades             │
│ 4. Filtros e busca funcionam no browser                │
└─────────────────────────────────────────────────────────┘
```

---

## 📋 Passo a Passo Completo

### 1️⃣ Fazer Upload dos Arquivos no GitHub

Siga o **INICIO-RAPIDO.md** para:
- Criar repositório
- Fazer upload dos arquivos
- Configurar Secrets
- Configurar permissões

**IMPORTANTE**: O repositório pode ser **Private** ou **Public**. GitHub Pages funciona em ambos!

---

### 2️⃣ Habilitar GitHub Pages

1. No seu repositório, vá em **Settings** (Configurações)

2. No menu lateral esquerdo, clique em **Pages**

3. Você verá uma tela assim:
```
┌──────────────────────────────────────────────────┐
│ GitHub Pages                                      │
├──────────────────────────────────────────────────┤
│                                                   │
│ Source                                            │
│ ┌────────────────────────────────────────────┐  │
│ │ Deploy from a branch ▼                     │  │
│ └────────────────────────────────────────────┘  │
│                                                   │
│ Branch                                            │
│ ┌──────────┐  ┌──────────┐                      │
│ │ main   ▼ │  │ /(root) ▼│         [Save]       │
│ └──────────┘  └──────────┘                      │
└──────────────────────────────────────────────────┘
```

4. Configure:
   - **Source**: Deploy from a branch
   - **Branch**: main
   - **Folder**: / (root)

5. Clique em **Save**

6. Aguarde 1-2 minutos. A página vai mostrar:
```
┌──────────────────────────────────────────────────┐
│ ✅ Your site is live at:                         │
│ https://seu-usuario.github.io/pos-monitor       │
└──────────────────────────────────────────────────┘
```

---

### 3️⃣ Testar o Sistema Completo

#### A. Rodar o GitHub Actions pela primeira vez

1. Vá em **Actions**
2. Clique em "Monitor Pós-Graduação EAD"
3. Clique em **Run workflow**
4. Aguarde a execução terminar (30-40 segundos)
5. Verifique se o arquivo `resultados.json` foi criado/atualizado no repositório

#### B. Acessar a página

1. Abra: `https://seu-usuario.github.io/pos-monitor`
2. Você deve ver:
   - Header com título e status
   - Filtros (instituto e busca)
   - Cards com as oportunidades
   - Estatísticas por instituto

Se aparecer "Nenhuma oportunidade encontrada", rode o workflow novamente em Actions.

---

## 🎨 Prévia da Página

```
┌──────────────────────────────────────────────────────┐
│ 🎓 Monitor de Pós-Graduação EAD                     │
│ Oportunidades gratuitas em institutos federais...   │
│                                                      │
│ ┌──────────────────────────────────────────────┐   │
│ │ ⏰ Última atualização: 11/02/2026 08:16      │   │
│ │ 💾 Total de oportunidades: 3                 │   │
│ └──────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────┐
│ 🏛️ Filtrar por instituto  |  🔍 Buscar palavra...   │
│ [Todos os institutos ▼]   |  [Ex: desenvolvimento]  │
└──────────────────────────────────────────────────────┘

┌─────────────────┐  ┌─────────────────┐  ┌──────────┐
│ 🏛️ IFSULDEMINAS │  │ 🏛️ IFRS         │  │ 🏛️ IFSP  │
│                 │  │                 │  │          │
│ Especialização  │  │ Pós-Graduação  │  │ Especia- │
│ em Desenvolv... │  │ em Segurança... │  │ lização..│
│                 │  │                 │  │          │
│ 📅 há 2 horas   │  │ 📅 há 3 dias    │  │ há 6 dias│
│                 │  │                 │  │          │
│ [Ver edital →]  │  │ [Ver edital →]  │  │ [Ver →]  │
└─────────────────┘  └─────────────────┘  └──────────┘
```

---

## ⚙️ Personalização

### Mudar Cores

Edite `styles.css`, seção de CSS Variables:

```css
:root {
  /* Altere estas cores */
  --color-accent-primary: #3b8fd9;  /* Azul principal */
  --color-bg-primary: #0f1419;      /* Fundo principal */
  --color-text-primary: #e8eaed;    /* Texto principal */
}
```

### Mudar Título/Descrição

Edite `index.html`, seção `<header>`:

```html
<h1 class="hero__title">
  <i class="fa-solid fa-graduation-cap"></i>
  Seu Título Aqui
</h1>
<p class="hero__subtitle">
  Sua descrição aqui
</p>
```

### Adicionar Mais Filtros

Edite `index.html` na seção `.filters` e adicione:

```html
<div class="filters__group">
  <label for="novoFiltro" class="filters__label">
    <i class="fa-solid fa-filter"></i>
    Nome do Filtro
  </label>
  <select id="novoFiltro" class="filters__select">
    <option value="">Todas as opções</option>
  </select>
</div>
```

Depois implemente a lógica em `app.js`.

---

## 🔄 Fluxo Automático

### Como a automação funciona:

```
Segunda 8h:
├─ GitHub Actions dispara automaticamente
├─ scraper.py executa
├─ Gera resultados.json com dados atualizados
├─ Commit automático
└─ GitHub Pages atualiza automaticamente (1-2 min)

Você às 8h30:
├─ Abre usuario.github.io/pos-monitor
├─ Página carrega resultados.json (atualizado!)
└─ Vê as novidades lindamente formatadas
```

### Auto-refresh da página

A página verifica automaticamente por atualizações a cada **5 minutos**.

Se quiser desabilitar, remova/comente em `app.js`:

```javascript
// Remova ou comente estas linhas:
setInterval(() => {
  console.log('Verificando atualizações...');
  initializeApp();
}, 5 * 60 * 1000);
```

---

## 📧 Email + Página Web (Ambos!)

Você pode ter **ambos** funcionando:

1. **Email**: Notificações quando encontrar **NOVAS** oportunidades
2. **Página Web**: Ver **TODAS** as oportunidades acumuladas

O scraper já faz os dois:
- `enviar_email()` → Envia apenas novidades
- `gerar_json_frontend()` → Salva todas para a página

---

## 🐛 Troubleshooting

### Página mostra "404 Not Found"

1. Verifique se GitHub Pages está habilitado em Settings > Pages
2. Confirme que o branch está como "main" e folder como "/ (root)"
3. Aguarde 1-2 minutos após habilitar

### Página mostra mas sem dados

1. Verifique se `resultados.json` existe no repositório
2. Rode o workflow manualmente em Actions
3. Abra o DevTools (F12) > Console para ver erros

### "Erro ao carregar dados"

1. Verifique se `resultados.json` está no formato correto (JSON válido)
2. Verifique permissões do repositório
3. Limpe cache do navegador (Ctrl+Shift+R)

### Dados não atualizam

1. Verifique se o workflow está rodando (Actions > Últimas execuções)
2. Veja os logs do workflow para identificar erros
3. Verifique se o commit automático está funcionando

---

## 📱 Responsividade

A página é 100% responsiva e funciona perfeitamente em:

- 💻 Desktop (1920px+)
- 💻 Laptop (1366px - 1920px)
- 📱 Tablet (768px - 1366px)
- 📱 Mobile (320px - 768px)

Teste abrindo no celular: `https://seu-usuario.github.io/pos-monitor`

---

## 🎯 Vantagens da Versão Híbrida

### ✅ Melhor que só Email:
- Você acessa quando quiser
- Vê histórico completo (não só novidades)
- Filtros e busca
- Interface visual bonita
- Compartilhável com amigos

### ✅ Melhor que só GitHub Actions:
- Não precisa entrar no GitHub para ver dados
- Interface amigável para não-técnicos
- Acesso rápido de qualquer dispositivo

### ✅ Melhor dos dois mundos:
- Email te avisa de novidades
- Página mostra tudo de forma organizada
- Automatizado e gratuito
- Dados sempre frescos

---

## 🚀 Próximos Passos

Depois que tudo estiver funcionando:

1. ✅ Compartilhe o link com amigos que buscam pós
2. ✅ Adicione mais institutos em `scraper.py`
3. ✅ Customize as cores no `styles.css`
4. ✅ Adicione mais filtros (por estado, por área específica)
5. ✅ Configure notificações do GitHub (Settings > Notifications)

---

## 📚 Arquivos Importantes

| Arquivo | Função | Você edita? |
|---------|--------|-------------|
| `index.html` | Estrutura da página | Sim, para mudar textos |
| `styles.css` | Visual/design | Sim, para cores/layout |
| `app.js` | Lógica JavaScript | Sim, para adicionar features |
| `resultados.json` | Dados | NÃO! Gerado automaticamente |
| `scraper.py` | Busca dados | Sim, para adicionar sites |

---

**Pronto! Agora você tem um sistema completo e profissional!** 🎉

Qualquer dúvida, consulte os outros guias ou abra uma Issue no GitHub.
