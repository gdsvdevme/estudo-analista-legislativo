# -*- coding: utf-8 -*-
# Volume 2: questões ORIGINAIS (Regimento, partes 1 e 2). Q(bloco, enunciado, [CORRETA, e1, e2, e3], comentário, estude)
QS = []
def Q(b, stem, opts, why, study): QS.append(dict(b=b, stem=stem, opts=opts, ans=0, fixed=False, why=why, study=study))
A1 = "Regimento Interno, Aula 01"
A2 = "Regimento Interno, Aula 02"

# ===== T1 Mesa: composição e eleição (1-4)
Q("MESA","A Mesa da Câmara é composta por:",
 ["Presidente, Vice-Presidente, 1º Secretário e 2º Secretário, eleitos para duas sessões legislativas.","Presidente, Vice-Presidente e Secretário, eleitos para uma sessão legislativa.","Presidente, 1º e 2º Vice-Presidentes e Secretário, eleitos para duas sessões legislativas.","Presidente, Vice-Presidente, 1º Secretário e 2º Secretário, eleitos para quatro sessões legislativas."],
 "A Mesa é formada por quatro cargos e o mandato é de duas sessões legislativas. Para a 3ª e a 4ª sessão há nova eleição.",A1+" (Mesa)")
Q("MESA","A eleição da Mesa é feita por:",
 ["maioria simples, em votação secreta, por cédula.","maioria absoluta, em votação nominal e aberta.","maioria de 2/3, em votação secreta.","maioria simples, em votação aberta por aclamação."],
 "Voto secreto em cédula e maioria simples. Pegadinha: confundir com a destituição, que exige 2/3 e votação aberta.",A1+" (eleição da Mesa)")
Q("MESA","Havendo empate na eleição da Mesa, vence a chapa:",
 ["cujo candidato a Presidente seja o mais idoso.","cujo candidato a Presidente tenha mais mandatos.","decidida por sorteio em plenário.","indicada pelo Presidente em exercício."],
 "O critério de desempate é a idade do candidato a Presidente. Não há sorteio nem voto de qualidade.",A1+" (eleição da Mesa)")
Q("MESA","A eleição da Mesa para a 3ª e a 4ª sessões legislativas deve ocorrer:",
 ["em sessão extraordinária, entre 1º de outubro e 30 de dezembro.","na primeira sessão ordinária de fevereiro da 3ª sessão legislativa.","em sessão solene, em 1º de janeiro.","em sessão ordinária, a qualquer tempo da 2ª sessão legislativa."],
 "A janela é de 1º/10 a 30/12 do ano anterior ao início da 3ª sessão legislativa, em sessão extraordinária.",A1+" (eleição da Mesa)")

# ===== T2 Fim das funções, vaga, atribuições (5-8)
Q("MESA","Cessam as funções da Mesa nas seguintes hipóteses, EXCETO:",
 ["licença médica de qualquer de seus membros por até 30 dias.","morte de membro.","renúncia apresentada por escrito.","ordem judicial."],
 "Art. 7º: morte, posse da Mesa eleita no 3º período, renúncia escrita, destituição, perda de mandato e ordem judicial. Licença curta não está no rol.",A1+" (art. 7º)")
Q("MESA","Surgindo vaga na Mesa, ela será preenchida em:",
 ["30 dias.","15 dias.","48 horas.","60 dias."],
 "Prazo de 30 dias. Cuidado com o prazo de 48h, que aparece em outros procedimentos (convocação de suplente, Resolução de destituição).",A1+" (vagas na Mesa)")
Q("MESA","Quanto à participação dos membros da Mesa nas comissões permanentes:",
 ["os membros da Mesa só podem integrar uma comissão permanente, e o Presidente não integra nenhuma.","todos os membros da Mesa, inclusive o Presidente, integram uma comissão.","a Mesa não pode integrar comissões, em nenhuma hipótese.","os membros da Mesa integram até três comissões, como os demais Vereadores."],
 "Membros da Mesa: uma comissão permanente. Presidente: nenhuma. Os demais Vereadores têm o teto de três comissões.",A1+" (Mesa e comissões)")
Q("MESA","Não havendo número legal para abrir a sessão, o Presidente deve:",
 ["aguardar 15 minutos e, persistindo a falta de quórum, não abrir a sessão.","abrir a sessão com qualquer número de presentes.","suspender a sessão por uma hora.","convocar sessão extraordinária para o mesmo dia."],
 "Aguarda-se 15 minutos (segunda chamada). Persistindo a ausência de quórum, a sessão não se realiza.",A1+" / "+A2+" (abertura de sessões)")

# ===== T3 Presidente (9-12)
Q("PRES","Sobre o voto do Presidente da Câmara:",
 ["só vota nos casos regimentais, e não tem voto em todas as deliberações.","vota sempre, como qualquer Vereador.","nunca vota, em hipótese alguma.","vota apenas para desempatar, em qualquer matéria."],
 "O Presidente só vota nos casos previstos no Regimento. Pegadinha: “voto de qualidade em qualquer empate”.",A1+" (competências do Presidente)")
Q("PRES","Compete ao Presidente da Câmara promulgar:",
 ["resoluções, decretos legislativos e leis cujo veto tenha sido rejeitado.","somente leis sancionadas tacitamente.","apenas resoluções, ficando os decretos legislativos a cargo da Mesa.","leis de iniciativa do Prefeito sancionadas por este."],
 "O Presidente promulga resoluções, decretos legislativos e as leis de veto rejeitado (ou mantidas as condições legais de promulgação). Lei sancionada pelo Prefeito é por ele promulgada.",A1+" (arts. 15 e 16)")
Q("PRES","A resenha dos trabalhos do ano deve ser apresentada pelo Presidente:",
 ["na última sessão ordinária do ano.","na primeira sessão ordinária do ano seguinte.","em sessão solene de encerramento, em dezembro.","por escrito, no recesso de julho."],
 "A resenha é feita na última sessão ordinária do ano.",A1+" (art. 16)")
Q("PRES","Quando o Presidente pretender agir juridicamente em nome da Câmara em situação para a qual não haja autorização regimental, ele deve:",
 ["consultar o Plenário.","agir de ofício, comunicando depois a Mesa.","pedir parecer da Comissão de Ética.","convocar sessão extraordinária da Comissão Processante."],
 "O parágrafo único do art. 16 exige a consulta ao Plenário. As certidões requeridas, por sua vez, devem ser expedidas em 15 dias.",A1+" (art. 16, parágrafo único)")

# ===== T4 Secretário, renúncia, destituição (13-20)
Q("DEST","São atribuições do 1º Secretário, entre outras:",
 ["ler os papéis do expediente, receber e guardar as proposições e redigir as atas.","presidir as sessões na ausência do Vice-Presidente.","promulgar as leis de veto rejeitado.","convocar as sessões especiais."],
 "Art. 25: ler papéis, receber e guardar proposições e redigir atas. Promulgar e convocar são do Presidente.",A1+" (art. 25)")
Q("DEST","A renúncia de membro da Mesa:",
 ["é feita por ofício e só se torna efetiva com a leitura em sessão.","é verbal e produz efeito imediato.","precisa ser aprovada por maioria absoluta do Plenário.","só é admitida no último ano do mandato da Mesa."],
 "Art. 27: renúncia por ofício (escrita), efetiva na leitura em sessão. Não precisa de aprovação.",A1+" (art. 27)")
Q("DEST","A destituição de membro da Mesa exige:",
 ["voto de 2/3 dos Vereadores, assegurada ampla defesa.","maioria simples, sem necessidade de defesa.","maioria absoluta, em votação secreta.","unanimidade da Comissão Processante."],
 "Art. 28: 2/3 e ampla defesa. Quórum de 2/3 em Câmara de 21 Vereadores: 14.",A1+" (art. 28)")
Q("DEST","A representação contra membro da Mesa, para fins de destituição, deve ser recebida por:",
 ["maioria absoluta, constituindo-se uma Comissão Processante de 3 Vereadores sorteados.","maioria simples, com Comissão de 5 Vereadores indicados pelo Presidente.","2/3, com Comissão de 3 Vereadores eleitos.","maioria absoluta, com Comissão de 5 Vereadores sorteados."],
 "Art. 29: recebimento por maioria absoluta e Comissão Processante de 3 sorteados. Os 2/3 só entram na decisão final.",A1+" (art. 29)")
Q("DEST","Constituída a Comissão Processante, ela se reúne em ___, notifica o acusado em ___ e este tem ___ para defesa prévia. Assinale a alternativa que completa a frase corretamente.",
 ["48 horas; 3 dias; 10 dias.","24 horas; 5 dias; 10 dias.","48 horas; 3 dias; 5 dias.","72 horas; 10 dias; 15 dias."],
 "Reunião em 48h, notificação em 3 dias, defesa prévia em 10 dias. O parecer vem em 20 dias improrrogáveis.",A1+" (art. 29)")
Q("DEST","O parecer da Comissão Processante deve ser apresentado em:",
 ["20 dias, prazo improrrogável.","10 dias, prorrogáveis por igual período.","60 dias, prorrogáveis.","5 dias, improrrogáveis."],
 "20 dias improrrogáveis. Cuidado: a Comissão de Ética tem 60 dias prorrogáveis; a de Inquérito, 5 dias para parecer em fase específica.",A1+" (art. 29)")
Q("DEST","Sendo o parecer da Comissão Processante pela improcedência da representação:",
 ["ele é aprovado por maioria simples, em votação aberta.","ele exige 2/3 para ser aprovado.","ele é arquivado sem votação.","ele só vale com a concordância do acusado."],
 "A improcedência é votada por maioria simples. Já a destituição exige 2/3. Votação sempre aberta nesse procedimento.",A1+" (arts. 30 a 35)")
Q("DEST","No julgamento da destituição, cada Vereador dispõe de ___ para discutir, e o relator e o acusado, de ___ cada um. Assinale a alternativa correta.",
 ["20 minutos; 60 minutos.","10 minutos; 30 minutos.","20 minutos; 30 minutos.","5 minutos; 60 minutos."],
 "20 min por Vereador e 60 min para relator e acusado. Aprovada a destituição, a Resolução é promulgada em 48h.",A1+" (arts. 30 a 35)")

# ===== T5 Comissões permanentes (21-24)
Q("COM","Cada comissão permanente é composta por três membros, que ocupam as funções de:",
 ["Presidente, Relator e Vogal.","Presidente, Vice-Presidente e Secretário.","Presidente, Relator e Suplente.","Coordenador, Relator e Vogal."],
 "Art. 38: Presidente, Relator e Vogal.",A1+" (art. 38)")
Q("COM","Cada Vereador pode integrar, no máximo, quantas comissões permanentes?",
 ["Três.","Duas.","Quatro.","Uma, salvo o Presidente da Câmara."],
 "Teto de três comissões por Vereador. Os membros da Mesa ficam em apenas uma; o Presidente, em nenhuma.",A1+" (art. 38)")
Q("COM","As comissões permanentes são constituídas:",
 ["na primeira sessão ordinária da 1ª e da 3ª sessões legislativas, com votação aberta por cédula.","em sessão solene, em janeiro, com voto secreto.","na primeira sessão ordinária de cada sessão legislativa, com voto secreto.","por indicação do Presidente, sem votação, a cada sessão legislativa."],
 "Constituição na 1ª e na 3ª sessões (começo de cada biênio), em votação aberta por cédula. O mandato dura até o fim da sessão legislativa.",A1+" (art. 38)")
Q("COM","O número de comissões permanentes varia conforme a versão do Regimento: o material do curso (Resolução 01/2026) lista 15, e o site da Câmara, consolidado até a Resolução 05/2026, indica 16. Diante disso, em prova o candidato deve:",
 ["seguir a versão do Regimento citada no enunciado e, na dúvida, o texto do próprio enunciado.","decorar apenas 15, por ser o número do curso.","decorar apenas 16, por ser a versão mais recente.","considerar a questão nula, pois a divergência impede o gabarito."],
 "Questão de estratégia, não de decoreba: o número muda com as resoluções que alteram o Regimento. O que vale é a versão adotada pela banca.",A1+" (art. 38) e site da Câmara")

# ===== T6 Competências e Ética (25-29)
Q("COM","A Comissão de Ética tem como característica:",
 ["a denúncia deve ser subscrita por 1/3 dos Vereadores, com notificação do acusado em 72 horas.","a denúncia pode ser feita por qualquer cidadão, sem subscrição.","a notificação do acusado é feita em 10 dias.","o prazo de conclusão é de 20 dias improrrogáveis."],
 "Denúncia por 1/3; notificação em 72h; defesa em 10 dias; conclusão em 60 dias prorrogáveis por igual período.",A1+" (arts. 47 e 48)")
Q("COM","No processo na Comissão de Ética, a cassação do mandato exige ___ e a absolvição, ___ . Assinale a alternativa correta.",
 ["2/3; maioria absoluta.","maioria absoluta; 2/3.","2/3; maioria simples.","maioria simples; maioria simples."],
 "Cassação: 2/3 (14 votos). Absolvição: maioria absoluta (11 votos).",A1+" (art. 48)")
Q("COM","O prazo da Comissão de Ética para concluir o processo é de:",
 ["60 dias, prorrogáveis por igual período.","20 dias improrrogáveis.","30 dias, prorrogáveis por 15.","90 dias improrrogáveis."],
 "60 dias, prorrogáveis por igual período, ou seja, até 120 dias.",A1+" (art. 48)")
Q("COM","Na Comissão de Ética, o acusado deve ser notificado em:",
 ["72 horas.","48 horas.","24 horas.","10 dias."],
 "Notificação em 72h; depois, defesa em 10 dias. Cuidado com a Processante da Mesa (reunião em 48h, notificação em 3 dias).",A1+" (arts. 47 e 48)")
Q("COM","Parecer da CFJR pela inconstitucionalidade de projeto:",
 ["vai ao plenário, em discussão e votação única.","arquiva o projeto automaticamente.","é devolvido ao autor, sem apreciação do plenário.","depende da concordância da Comissão de Ética."],
 "O parecer pela inconstitucionalidade é submetido ao plenário em discussão e votação única. Se rejeitado, o projeto segue.",A1+" (pareceres)")

# ===== T7 Pareceres (30-34)
Q("PAR","O parecer de comissão é estruturado em:",
 ["três partes.","duas partes: relatório e voto.","quatro partes: relatório, voto, emenda e redação.","uma única peça, sem divisão."],
 "Art. 66: parecer em três partes (relatório, voto do relator e decisão da comissão).",A1+" (art. 66)")
Q("PAR","O pedido de vista de projeto na comissão suspende o processo por até:",
 ["24 horas, e a suspensão total não pode passar de 6 dias corridos.","48 horas, e a suspensão total não pode passar de 10 dias.","5 dias, uma única vez.","3 dias úteis, sem limite de pedidos."],
 "Vista de 24h, com limite de 6 dias corridos de suspensão. O relator tem 2 dias para emitir seu parecer.",A1+" (prazos nas comissões)")
Q("PAR","O voto em separado, no parecer, pode ser:",
 ["pelas conclusões, aditivo ou contrário.","somente contrário.","somente aditivo ou contrário.","pelas conclusões ou pela rejeição liminar."],
 "Art. 69: voto em separado pelas conclusões, aditivo ou contrário.",A1+" (art. 69)")
Q("PAR","O prazo do relator para emitir o parecer é de:",
 ["2 dias.","5 dias.","10 dias.","24 horas."],
 "Dois dias. Pegadinha clássica: misturar prazos de comissão (2 dias, vista de 24h) com prazos de processos especiais (10, 20, 60 dias).",A1+" (prazos nas comissões)")
Q("PAR","NÃO é modalidade de voto em separado:",
 ["pela rejeição liminar.","pelas conclusões.","aditivo.","contrário."],
 "As três modalidades do art. 69 são: pelas conclusões, aditivo e contrário.",A1+" (art. 69)")

# ===== T8 Comissões especiais e de inquérito (35-39)
Q("ESPEC","A criação de Comissão Especial depende de requerimento:",
 ["subscrito por 1/3 dos Vereadores e aprovado por maioria simples.","subscrito por 2/3 e aprovado por maioria absoluta.","subscrito por qualquer Vereador e aprovado por maioria simples.","subscrito pela Mesa e aprovado por unanimidade."],
 "1/3 para subscrever e maioria simples para aprovar. O requerimento indica a finalidade, o número de membros e o prazo.",A1+" (arts. 72 a 75)")
Q("ESPEC","A Comissão Especial NÃO pode:",
 ["tratar de matéria de competência de comissão permanente.","ter prazo determinado.","ser extinta ao fim do prazo.","ter finalidade definida em requerimento."],
 "Matéria de comissão permanente não pode ser tratada por comissão especial. Se a especial não concluir no prazo, é extinta.",A1+" (arts. 72 a 75)")
Q("ESPEC","A Comissão de Inquérito tem por finalidade:",
 ["processar o Prefeito e os Vereadores por infrações do Decreto-Lei 201/67.","apenas fiscalizar contratos do Executivo.","julgar a prestação de contas do Prefeito.","examinar a redação final dos projetos."],
 "Art. 76: processar Prefeito e Vereadores por infrações previstas no Decreto-Lei 201/67.",A1+" (art. 76)")
Q("ESPEC","A Comissão de Inquérito é composta por:",
 ["5 Vereadores.","3 Vereadores sorteados.","7 Vereadores indicados pelo Presidente.","todos os membros da CFJR."],
 "Cinco Vereadores. A Processante da Mesa, por sua vez, tem três sorteados.",A1+" (art. 76)")
Q("ESPEC","No processo da Comissão de Inquérito, o acusado tem:",
 ["10 dias de defesa e pode arrolar até 10 testemunhas.","5 dias de defesa e até 3 testemunhas.","30 dias de defesa, sem limite de testemunhas.","10 dias de defesa, sem direito a testemunhas."],
 "Defesa em 10 dias, com até 10 testemunhas. A cassação exige 2/3, em votação nominal por infração.",A1+" (art. 76)")

# ===== T9 Maiorias (40-43)
Q("MAIO","Em uma Câmara de 21 Vereadores, maioria absoluta e 2/3 equivalem, respectivamente, a:",
 ["11 e 14 Vereadores.","10 e 14 Vereadores.","11 e 15 Vereadores.","12 e 14 Vereadores."],
 "Maioria absoluta é o primeiro número inteiro acima da metade de 21 (10,5), ou seja, 11. Dois terços de 21 = 14.",A2+" (arts. 82 a 86)")
Q("MAIO","Maioria simples é a maioria:",
 ["dos Vereadores presentes à sessão.","dos membros da Câmara, presentes ou não.","de 2/3 dos presentes.","do maior número de votos, ainda que inferior à metade."],
 "Simples = maioria dos presentes. Absoluta = maioria dos membros. Relativa = maior número de votos entre as alternativas.",A2+" (art. 82)")
Q("MAIO","Maioria relativa é a:",
 ["obtida por quem recebe mais votos que os demais concorrentes.","obtida com metade dos presentes mais um.","exigida para aprovar emenda à Lei Orgânica.","obtida com 2/3 dos membros."],
 "É o simples “mais votado”, usada em escolhas entre várias alternativas.",A2+" (art. 82)")
Q("MAIO","O art. 86 do Regimento trata:",
 ["das competências da Câmara com e sem sanção do Prefeito.","da perda de mandato de Vereador.","das licenças de Vereador.","do funcionamento das sessões extraordinárias."],
 "Art. 86: competências com sanção (leis) e sem sanção (resoluções e decretos legislativos).",A2+" (art. 86)")

# ===== T10 Vereadores: deveres, faltas, licenças (44-48)
Q("VER","A posse do Vereador exige:",
 ["declaração de bens.","certidão negativa de débitos tributários.","aprovação do Plenário.","comparecimento a três sessões consecutivas."],
 "Na posse, o Vereador apresenta declaração de bens. Os deveres do Vereador estão no art. 88.",A2+" (posse e deveres)")
Q("VER","A licença do Vereador para tratamento de saúde, missão ou cargo (art. 92):",
 ["só se efetiva com a leitura em sessão, e o suplente é convocado se a licença superar 120 dias.","é automática, sem necessidade de leitura em sessão.","permite convocação de suplente desde o primeiro dia.","depende de aprovação de 2/3 do Plenário."],
 "Efetiva com a leitura em sessão. Suplente só após 120 dias, e a convocação ocorre em 48h.",A2+" (art. 92)")
Q("VER","O suplente convocado deve tomar posse em:",
 ["48 horas.","15 dias.","5 dias.","30 dias."],
 "Convocação do suplente em 48h. Pegadinha: confundir com os 30 dias para preenchimento de vaga na Mesa.",A2+" (art. 92)")
Q("VER","Para justificar faltas por óbito de parente, o Vereador tem direito a:",
 ["3 dias.","8 dias.","1 dia.","15 dias."],
 "Três dias por óbito, mediante documento. Faltas justificadas exigem documentos.",A2+" (faltas)")
Q("VER","É vedado ao Vereador, entre outras proibições:",
 ["firmar ou manter contrato com a Câmara, ressalvado o de cláusulas uniformes.","comparecer às sessões da Comissão de Ética.","apresentar projetos de lei.","falar na tribuna durante o Expediente."],
 "Vedações constam do texto constitucional, da Lei Orgânica e do Regimento. A vedação a contratos com o Poder Público é a clássica.",A2+" (vedações)")

# ===== T11 Vagas, perda, líderes, remuneração (49-52)
Q("PERDA","Ocorre vaga no cargo de Vereador por:",
 ["morte, renúncia ou perda do mandato.","licença para tratamento de saúde.","falta justificada.","afastamento para missão oficial."],
 "Art. 105: vaga por morte, renúncia ou perda de mandato. Licenças não geram vaga.",A2+" (art. 105)")
Q("PERDA","A decisão de cassação do mandato de Vereador, nos casos do art. 107, exige:",
 ["voto de 2/3 dos membros da Câmara.","maioria absoluta dos presentes.","maioria simples dos presentes.","unanimidade."],
 "Cassação: 2/3 (14 votos) dos membros da Câmara. O art. 107 elenca sete hipóteses de perda de mandato.",A2+" (arts. 107 a 112)")
Q("PERDA","A remuneração dos Vereadores é fixada:",
 ["por resolução, até 30 dias antes das eleições.","por lei de iniciativa do Prefeito.","por decreto do Presidente da Câmara, em qualquer época.","por resolução, até 30 dias depois das eleições."],
 "Resolução da Câmara aprovada até 30 dias antes do pleito, para vigorar na legislatura seguinte.",A2+" (remuneração)")
Q("PERDA","Os líderes de bancada são indicados:",
 ["no início da sessão legislativa.","no início de cada sessão ordinária.","após 120 dias de sessão legislativa.","pelo Prefeito, em cada legislatura."],
 "A indicação dos líderes ocorre no início da sessão legislativa.",A2+" (líderes)")

# ===== T12 Sessões: regras gerais (53-57)
Q("SESS","A duração normal das sessões da Câmara é de:",
 ["duas horas, com segunda chamada em 15 minutos.","três horas, com segunda chamada em 30 minutos.","quatro horas, sem segunda chamada.","duas horas, sem possibilidade de prorrogação."],
 "Duas horas. Segunda chamada em 15 minutos.",A2+" (art. 113)")
Q("SESS","O requerimento de prorrogação da sessão deve ser apresentado:",
 ["até 10 minutos antes do término, e a prorrogação não pode passar de 24 horas.","a qualquer momento, sem limite de duração.","antes do início da sessão, por escrito.","até 5 minutos antes do término, pelo prazo máximo de 2 horas."],
 "Pedido de prorrogação 10 minutos antes do fim. A prorrogação não passa de 24h.",A2+" (prorrogação)")
Q("SESS","A suspensão da sessão para parecer dura até ___ e, para reunião de bancada, até ___ . Assinale a alternativa correta.",
 ["15 minutos; 5 minutos.","5 minutos; 15 minutos.","30 minutos; 10 minutos.","10 minutos; 10 minutos."],
 "Suspensão para parecer: 15 min. Para reunião de bancada: 5 min.",A2+" (arts. 117 a 119)")
Q("SESS","As sessões da Câmara são, em regra:",
 ["públicas, admitindo sessão secreta por deliberação da maioria absoluta.","reservadas, com acesso mediante credencial.","públicas, sem exceção.","secretas, quando o Presidente assim decidir."],
 "A regra é a publicidade. O sigilo depende de deliberação da maioria absoluta.",A2+" (art. 113)")
Q("SESS","São espécies de sessão previstas no art. 113:",
 ["solenes, ordinárias e extraordinárias.","solenes, ordinárias e administrativas.","ordinárias, extraordinárias e permanentes.","especiais, permanentes e extraordinárias."],
 "Solenes, ordinárias e extraordinárias. Há ainda sessões especiais e secretas, tratadas em seções próprias.",A2+" (art. 113)")

# ===== T13 Ordinárias e Ordem do Dia (58-63)
Q("ORD","As sessões ordinárias realizam-se:",
 ["na primeira semana útil de cada mês, de segunda a sexta, às 19h, com recesso em janeiro e julho.","todas as quintas-feiras, às 14h, sem recesso.","na última semana útil do mês, às 19h, com recesso em dezembro.","todos os dias úteis, às 19h, exceto em fevereiro."],
 "Primeira semana útil do mês, seg–sex, 19h. Recesso em janeiro e julho. Exigem maioria absoluta para abrir e prosseguir.",A2+" (arts. 125 a 129)")
Q("ORD","A sequência da sessão ordinária é:",
 ["Expediente, Ordem do Dia e Assuntos Parlamentares.","Ordem do Dia, Expediente e Assuntos Parlamentares.","Assuntos Parlamentares, Expediente e Ordem do Dia.","Expediente, Assuntos Parlamentares e Ordem do Dia."],
 "Expediente, Ordem do Dia e, ao final, Assuntos Parlamentares.",A2+" (art. 125)")
Q("ORD","A ordem de matérias na Ordem do Dia é:",
 ["vetos, redação final, 2ª discussão, 1ª discussão e moções, requerimentos e recursos.","1ª discussão, 2ª discussão, redação final, vetos e requerimentos.","requerimentos, vetos, redação final, 1ª discussão e 2ª discussão.","redação final, vetos, 1ª discussão, 2ª discussão e recursos."],
 "A sequência, em regra: vetos, redação final, 2ª discussão, 1ª discussão, moções, requerimentos e recursos.",A2+" (arts. 133 a 138)")
Q("ORD","Dentro de cada fase da Ordem do Dia, a precedência entre as espécies de proposição é:",
 ["Projeto de Lei, Projeto de Resolução e Projeto de Decreto Legislativo.","Projeto de Decreto Legislativo, Projeto de Resolução e Projeto de Lei.","Projeto de Resolução, Projeto de Lei e Projeto de Decreto Legislativo.","Projeto de Lei, Projeto de Decreto Legislativo e Projeto de Resolução."],
 "PL → PR → PDL.",A2+" (arts. 133 a 138)")
Q("ORD","A alteração da Ordem do Dia só é admitida nas hipóteses do art. 135, que são em número de:",
 ["cinco.","três.","sete.","dez."],
 "O art. 135 traz cinco hipóteses taxativas.",A2+" (art. 135)")
Q("ORD","A ordem dos itens do Expediente (art. 129) é:",
 ["taxativa, não podendo ser alterada pelo Presidente.","livre, a critério do Presidente.","definida por votação a cada sessão.","exemplificativa, podendo ser invertida pela maioria."],
 "A ordem do Expediente é taxativa.",A2+" (art. 129)")

# ===== T14 Assuntos parlamentares (64-66)
Q("ASS","Para que haja Assuntos Parlamentares, exige-se a presença de, no mínimo, ___ dos Vereadores, o que equivale a ___ Vereadores. Assinale a alternativa correta.",
 ["1/3; 7.","1/2; 11.","2/3; 14.","1/3; 8."],
 "1/3 de 21 = 7 Vereadores presentes.",A2+" (arts. 143 a 146)")
Q("ASS","No uso da palavra em Assuntos Parlamentares:",
 ["cada orador tem 15 minutos e são admitidos um aparte da situação e um da oposição.","cada orador tem 5 minutos, com apartes ilimitados.","cada orador tem 30 minutos, sem apartes.","o tempo pode ser prorrogado pelo Presidente."],
 "15 minutos, com um aparte da situação e um da oposição. Não há prorrogação.",A2+" (arts. 143 a 146)")
Q("ASS","A inscrição para Assuntos Parlamentares deve ser feita:",
 ["antes do fim do Expediente.","até o término da Ordem do Dia.","com 24 horas de antecedência.","a qualquer momento da sessão."],
 "A inscrição fecha ao término do Expediente.",A2+" (arts. 143 a 146)")

# ===== T15 Extraordinárias e especiais (67-72)
Q("EXTRA","A sessão extraordinária pode ser convocada:",
 ["pela Mesa, por 1/3 dos Vereadores ou pelo Prefeito.","apenas pelo Presidente.","apenas pelo Prefeito.","por qualquer Vereador."],
 "Mesa, 1/3 dos Vereadores ou Prefeito.",A2+" (arts. 147 a 155)")
Q("EXTRA","A convocação da sessão extraordinária deve ser feita com antecedência mínima de:",
 ["3 dias, salvo extrema urgência.","24 horas, sempre.","5 dias, sem exceção.","48 horas, salvo recesso."],
 "Três dias. Em extrema urgência admite-se prazo menor. A convocação deve indicar dia, hora e Ordem do Dia.",A2+" (arts. 147 a 155)")
Q("EXTRA","Na sessão extraordinária:",
 ["só há Ordem do Dia, e ela se restringe à matéria que motivou a convocação.","há Expediente, Ordem do Dia e Assuntos Parlamentares.","há Expediente e Ordem do Dia, mas não Assuntos Parlamentares.","a pauta pode ser ampliada por requerimento aprovado."],
 "Só Ordem do Dia, fechada. Não há Expediente nem Assuntos Parlamentares.",A2+" (arts. 147 a 155)")
Q("EXTRA","A Ordem do Dia da sessão extraordinária só pode ser alterada ou interrompida para:",
 ["comunicação de licença, posse de Vereador ou suplente e retirada de proposição da pauta.","inversão de pauta e destaque.","qualquer requerimento aprovado pelo Plenário.","apenas para posse de Vereador."],
 "Três hipóteses: comunicação de licença, posse de Vereador ou Suplente e retirada de proposição da pauta.",A2+" (arts. 147 a 155)")
Q("EXTRA","A convocação de sessão extraordinária durante o recesso:",
 ["só é admitida em caso de calamidade pública ou interesse público.","é livre, a critério da Mesa.","é vedada em qualquer hipótese.","depende de autorização do Prefeito."],
 "No recesso, só por calamidade pública ou interesse público.",A2+" (arts. 147 a 155)")
Q("EXTRA","Sobre as sessões especiais, é correto afirmar:",
 ["destinam-se a solenidades, exigem maioria absoluta para abrir e não têm duração fixa.","duram duas horas, com segunda chamada em 15 minutos.","são convocadas apenas pelo Prefeito.","podem deliberar sobre projetos de lei ordinários."],
 "Especiais: solenidades de decretos, resoluções e requerimentos aprovados; maioria absoluta; sem tempo determinado; convocação pelo Presidente de ofício ou por requerimento de 1/3, deferido de plano.",A2+" (arts. 156 e 157)")
