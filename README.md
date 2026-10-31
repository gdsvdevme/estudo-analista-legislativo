# Estudo · Analista Legislativo (Câmara de Rio Verde-GO)

Sistema de questões de uso pessoal para a prova de **08/11/2026**. Roda 100% no navegador: abra `index.html` (ou publique no GitHub Pages). Sem servidor, sem cadastro.

## O que faz
- **366 questões** (Caderno 1 + Apostilas 1, 2 e 3), organizadas por **disciplina do edital** e por **grau** (prioridade do tópico: Muito alta, Alta, Média, Baixa).
- **Caderno de erros** automático: o erro entra sozinho e só sai após 2 acertos seguidos.
- **Alerta de reincidência**: questões que você erra com frequência aparecem em destaque no início e dentro da própria questão.
- **Revisão espaçada** (volta em minutos se errou; 1, 2, 4, 7 e 14 dias se acertou).
- **Simulado** cronometrado, com gabarito só no fim, ponderado pelo grau.
- **Resumos** do conteúdo de cada tema das apostilas.
- **IA**: botão que explica por que cada alternativa está certa ou errada (usa sua chave da Anthropic; fica salva no navegador, nunca no código).

## Progresso e dados
Tudo é salvo no `localStorage` do navegador (chave `ael_v1`). Em *Config*, exporte e importe o backup em JSON para trocar de aparelho. Limpar os dados do navegador apaga o progresso: faça backup.

## Arquivos
- `index.html`: tela e estilos.
- `app.js`: lógica (erros, revisão, simulado, IA, backup).
- `data.js`: questões, tópicos e resumos (gerado por `tools/export_app.py`).
- `tools/`: scripts que geram `data.js` a partir das apostilas.

## Atualizar questões
Edite os arquivos em `tools/` e rode `python3 tools/export_app.py` (gera `data.js`). O progresso é ligado ao id da questão, então não se perde.

## Aviso
Os resumos e as questões foram escritos a partir de material do curso Estratégia e do texto legal. Não substituem a leitura do texto legal; confira em caso de dúvida.
