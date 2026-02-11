# 🎓 Monitor de Pós-Graduação EAD Gratuita

Automação que monitora abertura de inscrições de pós-graduações EAD gratuitas em institutos federais e oferece duas formas de acompanhamento:
- 📧 **Email**: Notificações automáticas de novas oportunidades
- 🌐 **Página Web**: Visualize todas as oportunidades em uma interface moderna

## 🎯 O que este projeto faz?

- ✅ Monitora automaticamente sites de institutos federais (IFSULDEMINAS, IFSP, IFRS, etc.)
- ✅ Detecta novos editais de pós-graduação EAD na área de tecnologia
- ✅ Publica dados em uma página web bonita e funcional
- ✅ Roda automaticamente 2x por semana (segundas e quintas) no GitHub Actions
- ✅ Mantém histórico completo do que já foi encontrado


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

## 📝 Licença

Livre para usar e modificar como quiser! 🎉

---

**Criado com 💜 para automatizar sua busca por qualificação profissional!**
