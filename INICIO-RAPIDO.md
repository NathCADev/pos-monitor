# ⚡ Guia de Início Rápido - 5 Minutos!

Se você quer começar RÁPIDO, siga apenas estes passos:

## 1. Baixe os arquivos ⬇️

Baixe todo o projeto clicando no botão verde "Download" acima.

## 2. Crie conta no GitHub (se não tiver) 🆕

👉 https://github.com - é grátis!

## 3. Crie um novo repositório 📁

1. Clique em "New repository"
2. Nome: `pos-monitor`
3. Marque: ✅ Private
4. Clique em "Create repository"

## 4. Faça upload dos arquivos 📤

1. No repositório, clique: **Add file** > **Upload files**
2. Arraste TODOS os arquivos que você baixou
3. Clique em "Commit changes"

## 5. Configure email do Gmail 📧

### 5.1 Habilite verificação em 2 etapas
👉 https://myaccount.google.com/security

### 5.2 Crie senha de app
👉 https://myaccount.google.com/apppasswords

- App: "Monitor Pós"
- **COPIE A SENHA** (16 caracteres tipo: `abcd efgh ijkl mnop`)

## 6. Adicione Secrets no GitHub 🔐

No repositório: **Settings** > **Secrets and variables** > **Actions**

Clique em "New repository secret" 3 vezes:

| Secret 1 | |
|----------|---|
| Nome: | `EMAIL_REMETENTE` |
| Valor: | `seuemail@gmail.com` |

| Secret 2 | |
|----------|---|
| Nome: | `EMAIL_SENHA` |
| Valor: | Cole a senha de 16 caracteres |

| Secret 3 | |
|----------|---|
| Nome: | `EMAIL_DESTINATARIO` |
| Valor: | `seuemail@gmail.com` |

## 7. Habilite permissões ⚙️

**Settings** > **Actions** > **General**

Em "Workflow permissions":
- Marque: ✅ **Read and write permissions**
- Clique em **Save**

## 8. Teste agora! 🧪

1. Vá em **Actions**
2. Clique em "Monitor Pós-Graduação EAD"
3. Clique em **Run workflow** (direita)
4. Clique no botão verde **Run workflow**
5. Aguarde 30 segundos e atualize a página
6. Clique no workflow que apareceu

**Ver os logs:**
- Clique em "Monitorar Novas Oportunidades"
- Veja o que aconteceu!

## ✅ Pronto!

Agora a automação vai rodar automaticamente:
- 🕐 **Segundas às 8h**
- 🕐 **Quintas às 11h**

Se encontrar algo, você receberá um email! 📧

---

## ❓ Problemas?

### "Permission denied"
→ Vá no passo 7 novamente

### "Authentication failed"
→ Verifique se usou a **senha de app** (16 caracteres), não a senha normal

### Não recebe emails
→ Verifique spam/lixo eletrônico

### Workflow não aparece
→ Certifique-se que enviou o arquivo `.github/workflows/monitor.yml` na estrutura correta de pastas

---

**🎉 Boa sorte na busca pela sua pós-graduação!**
