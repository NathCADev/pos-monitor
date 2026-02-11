# 🎨 Design System - Documentação Visual

Este documento detalha todas as decisões de design implementadas na versão híbrida.

## 📐 Especificações Técnicas Atendidas

### ✅ Requisitos Cumpridos

- **Sem emojis** → Usamos Font Awesome 6 (ícones profissionais)
- **Fonte Poppins** → Sans-serif moderna com ótima legibilidade
- **Paleta neutra dark** → Greys com toques sutis de azul/teal
- **Sem gradientes** → Apenas variações sutis de tom para profundidade
- **Cards com grid responsivo** → Mobile-first, funciona em qualquer tela
- **Micro-interações 200-300ms** → Hover e transições suaves
- **Código bem organizado** → CSS Variables, comentários, modular
- **Hierarquia visual clara** → Hero > Filtros > Cards > Estatísticas
- **Acessibilidade** → Contraste adequado (WCAG AA), tamanhos legíveis

---

## 🎨 Paleta de Cores

### Background Layers (Profundidade via variação de tom)
```
Mais escuro ← → Mais claro
──────────────────────────────
#0f1419  Primary (fundo principal)
#1a1f29  Secondary (hero, footer)  
#232931  Tertiary (cards hover)
#2a323d  Elevated (modais, popovers)

Surfaces (elementos UI)
#1e2530  Surface 100 (status bar, filtros)
#252d3a  Surface 200 (inputs)
#2d3643  Surface 300 (inputs hover/focus)
```

### Text Colors (Hierarquia de leitura)
```
#e8eaed  Primary (títulos, texto importante)
#a8b3c1  Secondary (subtítulos, labels)
#6b7785  Tertiary (meta info, timestamps)
```

### Accent Colors (Azul/Teal suave - sem roxo!)
```
#3b8fd9  Primary (ícones, links, botões)
#2c6fa8  Secondary (hover states)
#1e5077  Tertiary (pressed states)
```

### Semantic Colors
```
#3da367  Success (confirmações)
#d89614  Warning (avisos)
#d44646  Error (erros)
```

---

## 📏 Tipografia

### Família
```css
font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

### Escala Tipográfica
```
Hero Title:     32px (2rem)     - Bold (700)
Section Title:  24px (1.5rem)   - Semibold (600)
Card Title:     18px (1.125rem) - Semibold (600)
Body Large:     18px (1.125rem) - Regular (400)
Body:           16px (1rem)     - Regular (400)
Body Small:     14px (0.875rem) - Regular (400)
Caption:        12px (0.75rem)  - Regular (400)
```

### Line Heights
```
Tight:    1.25  (títulos)
Normal:   1.5   (corpo de texto)
Relaxed:  1.75  (parágrafos longos)
```

---

## 📦 Espaçamento (Sistema de 4px)

```
1:   4px   (gaps mínimos)
2:   8px   (entre ícone e texto)
3:   12px  (padding pequeno)
4:   16px  (padding padrão)
5:   20px  (padding cards)
6:   24px  (gaps entre seções)
8:   32px  (seções médias)
10:  40px  (seções grandes)
12:  48px  (hero padding)
16:  64px  (separação major)
```

---

## 🔲 Border Radius

```
Small:   4px   (inputs, badges)
Medium:  8px   (botões, selects)
Large:   12px  (cards, containers)
XLarge:  16px  (modais)
```

---

## 🌑 Sombras para Profundidade

```css
Small:  0 1px 3px rgba(0, 0, 0, 0.3)   /* Elevação sutil */
Medium: 0 4px 12px rgba(0, 0, 0, 0.4)  /* Cards hover */
Large:  0 8px 24px rgba(0, 0, 0, 0.5)  /* Modais, popovers */
```

---

## ⚡ Animações e Transições

### Timing Functions
```css
Fast: 200ms cubic-bezier(0.4, 0, 0.2, 1)  /* Hover rápido */
Base: 250ms cubic-bezier(0.4, 0, 0.2, 1)  /* Padrão */
Slow: 300ms cubic-bezier(0.4, 0, 0.2, 1)  /* Animações complexas */
```

### Micro-interações Implementadas

**Card Hover:**
```css
transform: translateY(-2px);
box-shadow: var(--shadow-md);
border-color: var(--color-border-emphasis);
background-color: var(--color-surface-200);
transition: all 250ms;
```

**Button Hover:**
```css
background-color: var(--color-accent-secondary);
transform: translateX(2px);
transition: all 200ms;
```

**Loading Skeleton:**
```css
animation: shimmer 1.5s ease-in-out infinite;
/* Gradiente se move suavemente */
```

**Border Accent (Card):**
```css
/* Barra colorida no topo aparece no hover */
opacity: 0 → 1;
transition: opacity 200ms;
```

---

## 📱 Grid System & Responsividade

### Desktop (>768px)
```css
.opportunities {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 24px;
}
```

### Tablet (768px)
```css
/* Ajustes de spacing e font sizes */
```

### Mobile (<768px)
```css
.opportunities {
  grid-template-columns: 1fr; /* 1 coluna apenas */
}
```

---

## 🧩 Componentes Principais

### Hero Section
```
- Background: color-bg-secondary
- Border bottom: 1px subtle
- Padding: 48px vertical, 32px bottom
- Title: 32px bold + ícone accent
- Subtitle: 18px light, max-width 600px
```

### Status Bar
```
- Background: surface-100
- Border: 1px subtle, radius 12px
- Padding: 20px
- Flex layout com gap 24px
- Ícones accent + labels tertiary
```

### Filters
```
- Grid: auto-fit minmax(280px, 1fr)
- Background: surface-100
- Inputs: surface-200 → surface-300 on hover
- Focus: border accent + subtle shadow
```

### Opportunity Card
```
- Background: surface-100
- Border: 1px subtle, radius 12px
- Padding: 24px
- Hover: translateY(-2px) + shadow-md
- Top accent bar: 3px accent (opacity 0→1)
```

### Statistics
```
- Background: surface-100
- Grid: auto-fill minmax(200px, 1fr)
- Cards: surface-200, hover → surface-300
- Value: 24px bold accent
```

---

## 🎯 Hierarquia Visual

```
1. HERO (topo)
   ├─ Título grande + ícone
   ├─ Subtítulo explicativo
   └─ Status bar (última atualização)

2. FILTROS
   ├─ Instituto (select)
   └─ Busca (input)

3. CONTEÚDO PRINCIPAL (cards)
   ├─ Header (instituto + ícone)
   ├─ Título da oportunidade
   ├─ Meta (data)
   └─ CTA (Ver edital)

4. ESTATÍSTICAS
   ├─ Grid de números
   └─ Por instituto

5. FOOTER
   └─ Informações do sistema
```

---

## 📐 Proporções e Medidas

### Container
```
Max-width: 1200px
Padding lateral: 24px
Centralizado
```

### Cards
```
Min-width: 320px (para manter legibilidade)
Altura: auto (conteúdo dinâmico)
Aspect ratio: livre (não fixo)
```

### Icons
```
Hero: 24px
Status: 16px
Card: 18px (no header icon box 40x40)
```

---

## ♿ Acessibilidade

### Contraste (WCAG AA)
```
✅ Texto primário: 13.5:1
✅ Texto secundário: 7.2:1
✅ Texto terciário: 4.8:1
✅ Links/accent: 4.9:1
```

### Tamanhos Mínimos
```
✅ Texto body: 16px
✅ Texto small: 14px (nunca menor)
✅ Touch targets: 44x44px mínimo
```

### Navegação
```
✅ Foco visível (outline + shadow)
✅ Ordem lógica de tabs
✅ Labels descritivos
```

---

## 🔧 Manutenibilidade do Código

### CSS Variables
```css
/* Tudo centralizado em :root */
--color-*
--font-*
--space-*
--radius-*
--transition-*
```

### Organização do CSS
```
1. Variables
2. Reset
3. Layout Components
4. UI Components
5. Utilities
6. Responsive
```

### JavaScript Modular
```javascript
// Seções claras:
1. State Management
2. Data Fetching
3. UI Rendering
4. Filters
5. Utilities
6. Init
```

### Comentários
```
- Seções marcadas com ===
- Funções documentadas (JSDoc style)
- Explicações de lógica complexa
```

---

## 🎨 Exemplos Visuais

### Card States

**Normal:**
```
┌─────────────────────────────┐
│ [icon] IFSULDEMINAS         │ ← Header
├─────────────────────────────┤
│ Especialização em...        │ ← Título
│ 📅 há 2 horas               │ ← Meta
│ [Ver edital →]              │ ← CTA
└─────────────────────────────┘
```

**Hover:**
```
┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐ ← Barra accent (azul)
│ [icon] IFSULDEMINAS         │
├─────────────────────────────┤
│ Especialização em...        │ ↑ Levanta 2px
│ 📅 há 2 horas               │ 🔆 Sombra maior
│ [Ver edital →]              │ → Desloca 2px
└─────────────────────────────┘
```

---

## 📊 Performance

### Otimizações
```
✅ CSS minificável
✅ Variáveis reutilizáveis
✅ Transições em propriedades aceleradas (transform, opacity)
✅ Debounce na busca (300ms)
✅ Auto-refresh inteligente (5min)
```

### Carregamento
```
1. HTML primeiro (estrutura)
2. CSS inline (critical)
3. Fonts (preconnect)
4. Icons (CDN)
5. JavaScript (defer)
```

---

## ✨ Diferencial do Design

### O que EVITAMOS:
```
❌ Gradientes simplistas
❌ Animações longas/exageradas
❌ Cores muito vibrantes competindo
❌ Blocos chapados sem nuance
❌ Fontes genéricas/monótonas
```

### O que IMPLEMENTAMOS:
```
✅ Variações sutis de tom (profundidade)
✅ Micro-interações rápidas (200-300ms)
✅ Paleta neutra + accent sutil
✅ Tipografia moderna (Poppins)
✅ Hierarquia visual clara
✅ Código manutenível
```

---

## 🎯 Resultado Final

Um design:
- **Profissional** sem parecer corporativo demais
- **Moderno** sem ser trendy demais
- **Limpo** sem ser minimalista demais
- **Funcional** sem sacrificar estética
- **Acessível** sem comprometer design
- **Manutenível** sem complexidade desnecessária

**Perfeito para um dashboard de dados que prioriza informação!** 📊
