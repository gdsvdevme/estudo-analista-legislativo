# -*- coding: utf-8 -*-
# Caderno 2. Q(bloco, enunciado, [CORRETA, errada1, errada2, errada3], comentario, estude)
QS = []
def Q(b, stem, opts, why, study): QS.append(dict(b=b, stem=stem, opts=opts, ans=0, fixed=False, why=why, study=study))

A3 = "Regimento Interno, Aula 03"
A2 = "Regimento Interno, Aula 02"
A0 = "Leis 7.434 e 7.435/2023, Aula 00"

# ============ 1. PROPOSIÇÕES, REQUERIMENTOS, MOÇÕES ============
Q("PROP","Segundo o Regimento Interno, as espécies de proposição são:",
 ["requerimentos, moções, projetos de lei, projetos de decreto legislativo, projetos de resolução e emendas.","requerimentos, indicações, moções, projetos de lei, projetos de decreto legislativo e emendas.","requerimentos, moções, projetos de lei, projetos de resolução, pareceres e emendas, em rol exemplificativo.","requerimentos, moções, projetos de lei, projetos de decreto legislativo, projetos de resolução, emendas e recursos."],
 "Art. 164. São seis espécies e o rol é taxativo: não existe uma sétima criada pela praxe. Pegadinha: acrescentar “indicações”, “pareceres” ou “recursos”, que são coisas do dia a dia, mas não estão no rol.",A3+" (art. 164)")
Q("PROP","Sobre a devolução de proposições ao autor, nos termos do art. 165 do Regimento, é correto afirmar:",
 ["a emenda que não guarde direta relação com a proposição a que se refere deve ser devolvida, e o Presidente fundamenta a devolução por escrito.","a proposição ilegal ou inconstitucional é sempre devolvida, mesmo que a ilegalidade seja controvertida.","as proposições subscritas pela Comissão de Finanças, Justiça e Redação podem ser devolvidas por alegada ilegalidade.","da devolução não cabe recurso, pois o juízo de admissibilidade é privativo do Presidente."],
 "Art. 165 e §§ 1º e 2º. O filtro alcança só o que for “manifestamente” anti-regimental, ilegal ou inconstitucional; o que é controvertido vai para as comissões. Proposição subscrita pela Comissão de Finanças, Justiça e Redação não pode deixar de ser recebida por alegada ilegalidade. Cabe recurso ao plenário (arts. 256 e 257).",A3+" (arts. 165 e 256-257)")
Q("PROP","Quanto à autoria e à subscrição de proposições, o Regimento estabelece que:",
 ["considera-se autor o primeiro signatário, e as assinaturas de apoio não podem ser retiradas depois da entrega da proposição à Mesa.","consideram-se autores todos os signatários, em igualdade de condições.","as assinaturas de apoio podem ser retiradas até o início da votação.","o autor é obrigado a fundamentar a proposição por escrito, sendo vedada a justificativa verbal."],
 "Autor é o primeiro signatário; as demais assinaturas são de apoio e implicam concordância com o mérito. O autor pode fundamentar por escrito ou verbalmente. Pegadinha: “pode retirar até a votação” e “só por escrito”.",A3)
Q("PROP","Um projeto de lei de iniciativa da Câmara foi rejeitado. De acordo com o Regimento, ele:",
 ["só pode ser renovado na mesma sessão legislativa se reapresentado, no mínimo, pela maioria absoluta dos Vereadores.","pode ser renovado a qualquer tempo, por qualquer Vereador.","só pode ser renovado na mesma sessão legislativa se reapresentado por 2/3 dos Vereadores.","nunca pode ser reapresentado, na mesma legislatura."],
 "A regra vale para projetos de lei de iniciativa da Câmara e para requerimentos rejeitados ou não sancionados. Quórum para reapresentar: maioria absoluta, não 2/3.",A3)
Q("PROP","O art. 172 do Regimento classifica os requerimentos segundo os seguintes critérios:",
 ["maneira de formulá-los, competência para decidi-los e fase de formulação.","autor, matéria e prazo de tramitação.","maneira de formulá-los, quórum de aprovação e comissão competente.","competência para decidi-los, número de signatários e fase de formulação."],
 "Art. 172: I, quanto à maneira de formulá-los (verbais ou escritos); II, quanto à competência para decidi-los (despacho de plano do Presidente ou deliberação do plenário); III, quanto à fase de formulação (somente durante o expediente, por exemplo).",A3+" (art. 172)")
Q("PROP","Será despachado de plano pelo Presidente, sem votação do plenário, o requerimento que solicitar:",
 ["retificação de ata.","prorrogação da sessão.","licença do Prefeito.","encerramento de discussão de proposição."],
 "Art. 173, b. As outras três estão no art. 175, ou seja, dependem de deliberação do plenário. Despacho de plano é para atos de condução simples: retirada pelo autor, verificação de presença, juntada de documentos, justificação de falta, entre outros.",A3+" (arts. 173 e 175)")
Q("PROP","Entre os requerimentos sujeitos a despacho de plano, o Regimento exige que seja necessariamente escrito o que solicitar:",
 ["justificação de falta do Vereador às sessões plenárias.","retirada, pelo autor, de requerimento verbal ou escrito.","retificação de ata.","verificação de presença."],
 "Art. 173, parágrafo único: são necessariamente escritos os das alíneas f a l (juntada ou desentranhamento, inclusão na Ordem do Dia, informações oficiais, voto de pesar, convocação de sessão extraordinária ou especial, justificação de falta e volta à tramitação de proposição arquivada). As alíneas a, b e c podem ser verbais.",A3+" (art. 173, parágrafo único)")
Q("PROP","Dependem de deliberação do plenário, mas não admitem discussão, os requerimentos que solicitem:",
 ["inclusão de projeto na pauta em regime de urgência, prorrogação da sessão e inversão da pauta.","convocação do Prefeito, constituição de Comissão de Inquérito e voto de louvor.","convocação do Prefeito, prorrogação da sessão e inversão da pauta.","constituição de Comissão Especial, urgência e destaque."],
 "Art. 175 (sem discussão): urgência, antecipação de discussão ou votação, retirada da pauta, preferência, emendas em bloco, destaque, encerramento de discussão, licença do Prefeito, prorrogação da sessão e inversão da pauta. Art. 176 (podem ser discutidos): convocação do Prefeito, Comissão Especial ou de Inquérito, informações com concordância do plenário, luto, voto de louvor e encerramento excepcional da sessão.",A3+" (arts. 175 e 176)")
Q("PROP","Dos requerimentos do art. 175, que não admitem discussão, encaminhamento de votação nem declaração de voto, o único que comporta encaminhamento de votação é o de:",
 ["encerramento de discussão de proposição.","inclusão de projeto em regime de urgência.","prorrogação da sessão.","licença do Prefeito."],
 "Art. 175, § 1º: a exceção é o requerimento do nº 7, encerramento de discussão. Os demais não admitem nenhuma das três coisas.",A3+" (art. 175, § 1º)")
Q("PROP","Dos requerimentos que dependem de deliberação do plenário, sem discussão, podem ser verbais:",
 ["os de antecipação de discussão ou votação e os de preferência para votação.","os de urgência e os de inversão da pauta.","os de destaque e os de licença do Prefeito.","todos, desde que o plenário concorde em votar de imediato."],
 "Art. 175, § 2º: somente os números 2 (antecipação) e 4 (preferência) podem ser verbais; os demais são necessariamente escritos.",A3+" (art. 175, § 2º)")
Q("PROP","É necessariamente escrito, depende de deliberação do plenário e pode ser discutido o requerimento que solicitar:",
 ["constituição de Comissão Especial ou de Comissão de Inquérito.","destaque para votação em separado de emendas.","inversão da pauta.","prorrogação da sessão."],
 "Art. 176, 2. Os outros três estão no art. 175 e não podem ser discutidos. Quando o requerimento comporta discussão, cada Vereador dispõe de 5 minutos.",A3+" (art. 176)")
Q("PROP","O requerimento que solicitar a inserção de documentos nos anais da Câmara deverá:",
 ["ser escrito e proposto por, no mínimo, 1/3 dos Vereadores.","ser verbal e aprovado por maioria simples.","ser escrito e proposto pela Mesa, com aprovação de 2/3.","ser despachado de plano pelo Presidente."],
 "Art. 176, parte final. Outra vez o quórum de subscrição de 1/3, o mesmo da moção e da convocação do Prefeito.",A3+" (art. 176)")
Q("PROP","A moção, segundo o Regimento, é a proposição em que é sugerida a manifestação da Câmara sobre determinado assunto. Quanto ao seu rito:",
 ["é subscrita por no mínimo 1/3 dos Vereadores, vai à Ordem do Dia da sessão ordinária seguinte independentemente de parecer, com discussão e votação únicas, e não admite emendas.","é subscrita por qualquer Vereador, depende de parecer da Comissão de Finanças, Justiça e Redação e admite emendas.","é subscrita por 1/3 dos Vereadores, depende de parecer e é votada em dois turnos.","é subscrita pela maioria absoluta, vai à Ordem do Dia na própria sessão e admite emendas de redação."],
 "Art. 179. Moção expressa aplauso, solidariedade ou apoio, apelo, protesto ou repúdio; não cria direitos nem obrigações. Cada Vereador tem 5 minutos para discutir.",A3+" (art. 179)")

# ============ 2. PROJETOS E TRAMITAÇÃO ============
Q("PROJ","Segundo o art. 183 do Regimento, a Câmara exerce a sua função legislativa por meio de:",
 ["projetos de lei, projetos de decreto legislativo e projetos de resolução.","projetos de lei, requerimentos e moções.","projetos de lei, projetos de lei complementar e emendas.","projetos de lei, projetos de decreto legislativo e medidas provisórias."],
 "Art. 183. Requerimentos e moções são proposições, mas não são instrumentos da função legislativa. Também não há medida provisória no âmbito municipal.",A3+" (art. 183)")
Q("PROJ","Compete privativamente ao Prefeito a iniciativa de projeto de lei sobre:",
 ["aumento de vencimentos e outras vantagens dos servidores da administração centralizada.","fixação da remuneração dos Vereadores.","mudança do local de funcionamento da Câmara.","alteração do Regimento Interno."],
 "Art. 185. A remuneração dos Vereadores e o Regimento são matéria de resolução; a mudança do local da Câmara, de decreto legislativo. Nenhuma depende de iniciativa do Prefeito.",A3+" (art. 185)")
Q("PROJ","Aos projetos de iniciativa privativa do Prefeito enumerados no art. 185 (orçamento, matéria financeira, cargos, aumento de despesas), o Regimento:",
 ["não admite emendas que aumentem direta ou indiretamente a despesa proposta ou diminuam a receita.","admite quaisquer emendas, desde que aprovadas por maioria absoluta.","admite emendas que alterem os quantitativos de cargos, desde que mantida a despesa.","admite emendas apenas das comissões, ainda que aumentem a despesa."],
 "Art. 185, parágrafo único. Também não se admitem emendas que alterem a criação de cargos e funções quanto a quantitativos ou que resultem em aumento de despesa.",A3+" (art. 185, parágrafo único)")
Q("PROJ","Aprovado o projeto de autoria do Executivo, ou rejeitado na forma regimental, o Presidente da Câmara fará a devida comunicação ao Prefeito no prazo de:",
 ["48 horas.","24 horas.","5 dias úteis.","15 dias úteis."],
 "Prazo de 48 horas. Não confunda com os 15 dias úteis, que são o prazo do Prefeito para sancionar ou vetar.",A3)
Q("PROJ","Sobre os prazos de apreciação de projetos de lei subscritos por parcelas dos membros da Câmara, o Regimento dispõe:",
 ["projetos subscritos por 1/4 devem ter a apreciação concluída em 30 dias corridos; os subscritos por 1/3 podem pedir 20 dias corridos, faculdade que o mesmo Vereador só usa uma vez por ano.","projetos subscritos por 1/3 devem ser concluídos em 30 dias úteis; os subscritos por 1/4, em 20 dias úteis.","projetos subscritos por 1/4 devem ser concluídos em 45 dias corridos, sem limite de uso da faculdade.","projetos subscritos por 1/3 devem ser concluídos em 20 dias, sem limite de uso, e os subscritos por 1/4 não têm prazo."],
 "Atenção a duas armadilhas: os prazos são em dias corridos, contados da apresentação, e a faculdade dos 20 dias é limitada a uma vez por ano para o mesmo Vereador. Esgotado o prazo, o projeto é colocado imediatamente em votação.",A3)
Q("PROJ","Os projetos de lei com prazo de apreciação estabelecido em lei, independentemente de parecer das Comissões:",
 ["devem constar obrigatoriamente da Ordem do Dia.","só entram na Ordem do Dia se houver parecer favorável.","são arquivados se as Comissões não opinarem no prazo.","dependem de requerimento de urgência aprovado pelo plenário para serem votados."],
 "Quem não pode travar o processo é a demora da comissão. O mesmo raciocínio aparece no art. 213, parágrafo único.",A3)
Q("PROJ","O projeto de decreto legislativo, segundo o art. 190 do Regimento:",
 ["destina-se a matéria que exceda os limites da economia interna da Câmara, não é sujeito a sanção e é promulgado pelo Presidente da Câmara.","destina-se a matéria político-administrativa interna da Câmara e é promulgado pelo Prefeito.","é sujeito a sanção ou veto do Prefeito, como o projeto de lei.","regula somente a concessão de títulos honoríficos."],
 "Art. 190. Decreto legislativo tem efeito externo e dispensa sanção. Os títulos honoríficos são apenas um dos exemplos.",A3+" (art. 190)")
Q("PROJ","Constitui matéria de projeto de decreto legislativo:",
 ["mudança do local de funcionamento da Câmara.","destituição de membro da Mesa.","fixação da remuneração dos Vereadores.","constituição de comissões especiais."],
 "Art. 190, parágrafo único, f. As outras três são de projeto de resolução (art. 191, d, g e f). Decreto legislativo trata de contas do município, licença e consentimento ao Prefeito, remuneração do Prefeito e do Vice-Prefeito, representação à Assembleia sobre modificação territorial e mudança do local da Câmara.",A3+" (arts. 190 e 191)")
Q("PROJ","Constitui matéria de projeto de resolução:",
 ["perda do mandato de Vereador.","aprovação ou rejeição das contas do município.","fixação da remuneração do Prefeito e do Vice-Prefeito.","consentimento ao Prefeito nos casos previstos em lei."],
 "Art. 191, c. Pegadinha clássica: remuneração dos Vereadores é resolução (art. 191, g), mas a do Prefeito e do Vice-Prefeito é decreto legislativo (art. 190, d). Contas do município: decreto legislativo.",A3+" (arts. 190 e 191)")
Q("PROJ","Os projetos devem atender a requisitos. Entre eles, o Regimento exige:",
 ["justificação, com a exposição circunstanciada dos motivos de mérito que fundamentam a medida proposta.","parecer prévio da Procuradoria anexado ao texto.","assinatura de, no mínimo, 1/3 dos Vereadores.","redação em artigos de qualquer extensão, dispensada a numeração."],
 "Requisitos: apenas a enumeração da vontade legislativa; artigos numerados, claros e concisos; menção da revogação das disposições em contrário, quando for o caso; assinatura do autor; justificação.",A3)
Q("PROJ","O projeto de resolução que objetive a criação de cargos na secretaria da Câmara depende do voto favorável de:",
 ["maioria absoluta dos membros da Câmara.","2/3 dos membros da Câmara.","maioria simples dos presentes.","1/3 dos membros da Câmara."],
 "Quórum de maioria absoluta. Fique atento: 2/3 aparece em outros casos (títulos honoríficos, responsabilidade do Prefeito, destituição da Mesa).",A3)
Q("PROJ","Nos termos do art. 194, os projetos devem ser protocolados:",
 ["3 dias úteis antes das sessões, condição obrigatória para apresentação no expediente seguinte, quando serão lidos e despachados de plano às Comissões Permanentes.","48 horas antes da sessão, para leitura na Ordem do Dia.","15 dias úteis antes da sessão, para publicação prévia.","a qualquer momento, sendo lidos na própria sessão em que forem protocolados."],
 "Art. 194. Se o prazo não for cumprido, o projeto não é lido na sessão pretendida e fica para a oportunidade seguinte. “De plano” significa sem votação.",A3+" (art. 194)")
Q("PROJ","Quanto à ordem de apreciação dos projetos pelas Comissões, o art. 194, § 1º, determina que são apreciados:",
 ["em primeiro lugar pela Comissão de Finanças, Justiça e Redação, quanto ao aspecto legal e constitucional, e em último pela Comissão específica, quando for o caso.","em primeiro lugar pela Comissão específica e em último pela Comissão de Finanças, Justiça e Redação.","somente pela Comissão específica, dispensado o exame de legalidade.","simultaneamente por todas as Comissões, sem ordem."],
 "O filtro de legalidade e constitucionalidade vem antes do mérito. As emendas constantes de voto em separado ou voto vencido não são consideradas (§ 2º), e é admitida a apresentação de emendas no transcorrer das discussões (§ 3º).",A3+" (art. 194)")
Q("PROJ","Nenhum projeto será dado por definitivamente aprovado antes de passar por duas discussões e votações, além da redação final. A exceção é:",
 ["projetos de resolução e de decreto legislativo, que têm uma discussão e votação, além da redação final.","projetos de decreto legislativo e de lei complementar, que têm uma discussão e votação.","projetos de resolução, que dispensam a redação final.","projetos de lei de iniciativa do Prefeito, que têm discussão única."],
 "Regra geral: dois turnos. Resolução e decreto legislativo: um turno, mas com redação final. Os projetos rejeitados em qualquer fase são arquivados.",A3)
Q("PROJ","Nenhuma alteração, reforma ou substituição do Regimento Interno será dada por definitivamente aprovada sem que seja discutida:",
 ["pelo menos em 2 sessões ordinárias, ou em extraordinária convocada para tal fim.","em sessão única, por 2/3 dos membros.","em 3 sessões ordinárias consecutivas.","em duas sessões extraordinárias convocadas pelo Prefeito."],
 "Discussão em pelo menos duas sessões ordinárias (ou extraordinária convocada para isso). Veja também os arts. 312 e 313, sobre iniciativa.",A3)
Q("PROJ","Na primeira discussão de um projeto, segundo o Regimento:",
 ["cada Vereador dispõe de 5 minutos, a votação é em bloco e as emendas são votadas antes do projeto.","cada Vereador dispõe de 10 minutos, e o projeto é votado artigo por artigo.","cada Vereador dispõe de 5 minutos, e o projeto é votado antes das emendas.","cada Vereador dispõe de 3 minutos, e a votação é sempre nominal."],
 "Arts. 200 a 202. Primeiro as emendas, depois o projeto já com as alterações aprovadas. A segunda discussão também é de 5 minutos por Vereador (art. 204).",A3+" (arts. 200-204)")
Q("PROJ","Se o projeto for aprovado com emendas, o processo é encaminhado à Procuradoria da Câmara, que terá, para redigi-lo conforme o aprovado, o prazo de:",
 ["3 dias.","24 horas.","15 dias úteis.","30 dias."],
 "Art. 205. Atenção para não misturar com os 3 dias úteis das Comissões para parecer em projetos com prazo (arts. 211 a 213).",A3+" (art. 205)")
Q("PROJ","Sobre a redação final, é correto afirmar:",
 ["se houver dúvida quanto à vontade legislativa por incoerência notória, contradição evidente ou manifesto absurdo, a Comissão se exime de oferecer redação final e propõe a reabertura da discussão.","a Procuradoria pode alterar o sentido da matéria aprovada, desde que o justifique em parecer.","a redação final nunca pode corrigir erro de linguagem.","emendas à redação final são livres, podendo tratar de qualquer aspecto do projeto."],
 "Art. 207. A correção de incorreção ou impropriedade de linguagem é permitida desde que não altere a vontade legislativa, com menção expressa e justificação no parecer (art. 206, parágrafo único). Reaberta a discussão, só cabem emendas estritamente relativas ao aspecto reaberto (art. 209).",A3+" (arts. 206-209)")
Q("PROJ","Não havendo emendas à redação final proposta:",
 ["considera-se aprovada a redação final, e a matéria é remetida à sanção do Prefeito ou à promulgação do Presidente.","a redação final é obrigatoriamente submetida a nova votação em plenário.","o projeto retorna à Comissão para novo parecer.","o projeto é arquivado."],
 "Art. 208. Havendo emendas de redação, o projeto volta à Comissão de Finanças, Justiça e Redação para parecer (§ 1º).",A3+" (art. 208)")
Q("PROJ","Projeto de lei com prazo de apreciação recebeu parecer contrário da Comissão de Finanças, Justiça e Redação quanto ao aspecto legal ou constitucional. De acordo com o art. 212:",
 ["será incluído em pauta da sessão seguinte, para discussão e votação únicas do parecer; aprovado o parecer, o projeto é arquivado; rejeitado, segue a tramitação normal.","será arquivado automaticamente, sem votação.","seguirá para as demais Comissões, independentemente de votação do parecer.","será votado em dois turnos, junto com o mérito."],
 "Quem vota é o plenário, e o que ele vota é o parecer. Aprovar o parecer contrário significa concordar que o projeto é ilegal ou inconstitucional, então ele é arquivado.",A3+" (art. 212)")
Q("PROJ","A Comissão de Finanças, Justiça e Redação dispõe, para emitir parecer sobre o aspecto legal ou constitucional de projeto com prazo de apreciação, de:",
 ["3 dias úteis, contados do recebimento do projeto.","2 dias, prorrogáveis por mais 1.","5 dias improrrogáveis.","15 dias úteis."],
 "Art. 211, § 2º, e art. 213. Esgotado o prazo, o projeto é incluído em pauta para primeira discussão, com ou sem parecer, sendo vedado adiar a discussão ou a votação para ouvir as Comissões (art. 213, parágrafo único).",A3+" (arts. 211-213)")
Q("PROJ","Aprovado em primeira discussão, o projeto de lei com prazo de apreciação:",
 ["volta, na sessão ordinária seguinte, à segunda votação; aprovado em segunda discussão, segue para a redação final, e, se rejeitado, vai ao arquivo.","é remetido imediatamente à sanção do Prefeito.","depende de requerimento do autor para ser votado novamente.","é votado em segunda discussão na mesma sessão."],
 "Arts. 215 e 216. O rito dos dois turnos é preservado, e a rejeição em qualquer fase manda o projeto para o arquivo.",A3+" (arts. 215-216)")
Q("PROJ","A retirada de proposições, segundo o art. 220, dá-se por requerimento do autor:",
 ["desde que a proposição não tenha sido submetida à apreciação do plenário.","a qualquer tempo, mesmo durante a votação.","somente após a aprovação em primeira discussão.","somente se aprovada pela maioria absoluta."],
 "Depois que o plenário começa a deliberar, a matéria passa a ser interesse da Casa. Se a autoria for da Mesa ou de Comissão, a retirada obedece à regra da maioria de seus membros.",A3+" (art. 220)")
Q("PROJ","No início de cada legislatura são arquivados os projetos que, até o encerramento da legislatura anterior, não tenham sido aprovados em pelo menos uma discussão. Esse arquivamento:",
 ["não se aplica às proposições de iniciativa do Executivo.","aplica-se inclusive aos projetos do Executivo.","alcança apenas os projetos de iniciativa dos Vereadores com parecer contrário.","alcança apenas os projetos de resolução."],
 "As proposições do Executivo escapam do arquivamento. A volta à tramitação exige requerimento do líder da bancada, ou da maioria dos membros, se a autoria for da Mesa ou de Comissão permanente.",A3)
Q("PROJ","Não podem ser desarquivadas as proposições:",
 ["inquinadas de inconstitucionalidade ou ilegalidade e as que tenham parecer contrário de comissões de mérito.","de autoria da Mesa.","apresentadas por Vereadores que não foram reeleitos.","que tenham recebido emendas."],
 "Duas travas ao desarquivamento: vício de legalidade ou constitucionalidade, e parecer contrário de comissão de mérito.",A3)

# ============ 3. DISCUSSÃO E VOTAÇÃO ============
Q("DV","Na discussão de um projeto, a ordem de uso da palavra do Regimento é:",
 ["primeiro o autor, depois os relatores das comissões na ordem em que se pronunciaram; em projeto da Mesa ou de Comissão, os autores são os respectivos Presidentes.","primeiro os relatores, depois o autor.","primeiro o líder da maioria, depois o autor.","primeiro o Presidente da Câmara, depois o autor e os relatores."],
 "Em projeto do Executivo, considera-se autor, para este fim, o Vereador que goza de prerrogativas de líder, como intérprete do pensamento do Prefeito junto à Câmara.",A3)
Q("DV","O Presidente não interromperá o orador que estiver discutindo qualquer matéria, salvo:",
 ["para dar conhecimento ao plenário de requerimento de prorrogação da sessão e colocá-lo em votação.","para dar a palavra a outro Vereador que a tenha solicitado.","para aparte do Presidente de comissão.","porque o tempo regimental do orador chegou à metade."],
 "Art. 225: três exceções (prorrogação da sessão, comunicação importante, urgente e inadiável, e tumulto grave). O orador interrompido pela votação da prorrogação não perde a vez, se estiver presente quando chamado a continuar.",A3+" (art. 225)")
Q("DV","Sobre os apartes, é correto afirmar:",
 ["são consentidos, não podem passar de 1 minuto, e é vedado ao Presidente, ou a quem o substitua na presidência, apartear o orador.","dependem de autorização do Presidente, e não têm limite de duração.","podem ser feitos durante o expediente, desde que com o consentimento do orador.","são permitidos mesmo quando o orador está encaminhando votação."],
 "Art. 228. Não são permitidos apartes: à palavra do Presidente na direção dos trabalhos, paralelos ou cruzados, quando o orador encaminha votação, faz declaração de voto ou fala sobre a ata, e durante o expediente.",A3+" (art. 228)")
Q("DV","Segundo o Regimento, o encerramento da discussão dá-se:",
 ["por inexistência de orador ou por disposição legal.","por decisão do Presidente, quando julgar a matéria esclarecida.","apenas por requerimento aprovado pelo plenário.","pelo término do tempo da sessão, em qualquer hipótese."],
 "A discussão não será encerrada quando houver requerimento de adiamento pendente de votação por falta de quórum. Já o requerimento de encerramento (art. 175, nº 7) é outro caminho, que depende de deliberação do plenário.",A3)
Q("DV","Se, no curso da votação de uma matéria, esgotar-se o tempo destinado à sessão:",
 ["a sessão é prorrogada até que a votação seja concluída por inteiro, salvo falta de número para deliberar, caso em que é encerrada imediatamente.","a sessão é encerrada, e a votação continua na sessão seguinte.","a sessão só é prorrogada se houver requerimento aprovado pelo plenário.","a votação é suspensa por até 24 horas."],
 "Considera-se a matéria em fase de votação a partir do momento em que o Presidente declara encerrada a discussão (art. 298, § 2º).",A3)
Q("DV","O Vereador presente à sessão não pode escusar-se de votar. Segundo o Regimento, deve abster-se quando:",
 ["ele próprio, ou parente afim ou consanguíneo até o terceiro grau, tiver interesse manifesto na deliberação, sob pena de nulidade da votação quando seu voto for decisivo.","for do partido do autor da proposição.","for parente apenas em primeiro grau do autor.","discordar do mérito da matéria."],
 "O Vereador que se considerar impedido comunica o fato ao Presidente, e sua presença é computada para efeito de quórum. Parentesco até o terceiro grau inclusive, afim ou consanguíneo.",A3)
Q("DV","O Presidente da Câmara só tem voto:",
 ["na eleição da Mesa, nas votações em que a matéria exigir quórum de dois terços e quando ocorrer empate.","em todas as votações, como qualquer Vereador.","somente em caso de empate.","na eleição da Mesa e nas votações de maioria absoluta."],
 "Essas mesmas normas se aplicam ao Vereador que substituir o Presidente na direção dos trabalhos. Não confunda com a maioria absoluta: nela o Presidente não vota, a não ser que haja empate.",A3)
Q("DV","Votada uma proposição, as demais que tratem do mesmo assunto na mesma sessão legislativa, ainda que não anexadas a ela:",
 ["são consideradas prejudicadas e remetidas ao arquivo.","seguem a tramitação normal.","são votadas em conjunto na sessão seguinte.","são devolvidas aos autores."],
 "É a chamada prejudicialidade. Não se confunde com a devolução ao autor do art. 165, que trata de proposições com vício de admissibilidade.",A3)
Q("DV","Sobre o encaminhamento de votação, o Regimento estabelece que:",
 ["terão preferência o líder ou vice-líder de cada bancada ou Vereador indicado pela liderança, e, havendo emendas, haverá apenas um encaminhamento sobre todas as peças do projeto.","cada emenda tem seu encaminhamento próprio, por qualquer Vereador.","somente o autor do projeto pode encaminhar a votação.","o encaminhamento ocorre antes do encerramento da discussão."],
 "O encaminhamento só cabe depois de o Presidente declarar encerrada a discussão. Tempo: 2 minutos, sem apartes (art. 251, e).",A3)
Q("DV","Os dois processos de votação previstos no Regimento são o simbólico e o nominal. Quanto a eles:",
 ["no simbólico, os que concordam permanecem sentados e os contrários se levantam; no nominal há consignação do nome e do voto de cada Vereador. A votação secreta foi suprimida pela Resolução nº 17/2003.","no simbólico, há consignação do nome de cada Vereador; no nominal, apenas a contagem global.","o voto secreto é permitido para a apreciação de vetos.","a votação nominal é feita por chamada em ordem de inscrição."],
 "Palavras-chave: simbólico = sentar e levantar; nominal = chamada e nome. A votação nominal é feita por chamada em ordem alfabética, e, se não houver quórum ao fim da chamada, o secretário faz uma segunda e última chamada dos que ainda não votaram.",A3)
Q("DV","Se algum Vereador tiver dúvida quanto ao resultado da votação simbólica proclamada, poderá requerer:",
 ["verificação nominal de votação; se o requerimento ficar prejudicado pela ausência do autor ou por pedido de retirada, qualquer outro Vereador pode reformulá-lo.","nova votação simbólica, que o Presidente pode indeferir.","anulação da sessão, perante a Mesa.","votação secreta."],
 "Art. 246. Pelas regras do painel eletrônico, o Presidente não pode indeferir o requerimento de verificação e não se admite segunda verificação; em caso de dúvida, pode repetir de ofício a votação simbólica.",A3+" (art. 246)")
Q("DV","Quanto à declaração de voto, o Regimento determina que:",
 ["é feita de uma só vez, depois de concluída por inteiro a votação de todas as peças do projeto, com 1 minuto para cada Vereador, vedados apartes.","pode ser feita antes da votação, com 5 minutos e apartes.","é feita a cada emenda votada, com 2 minutos.","é obrigatória para todo Vereador que vote contra."],
 "A declaração de voto serve para registrar as razões depois de a decisão estar tomada, e não para retomar o debate. Ela consta da ata.",A3+" (art. 251, f)")
Q("DV","Quanto ao controle do tempo de uso da palavra, o Regimento determina que:",
 ["o tempo é controlado pelo secretário, para conhecimento do Presidente, e começa a fluir quando for dada a palavra; interrupções, exceto aparte concedido, não são computadas.","o tempo é controlado pelo próprio orador.","o tempo é controlado pelo Presidente, sem auxílio, e inclui as interrupções.","o tempo só começa a correr depois do primeiro aparte."],
 "A interrupção por aparte consome o tempo do orador; qualquer outra interrupção, não.",A3)
Q("DV","Na discussão de veto, cada Vereador dispõe de:",
 ["5 minutos, sem apartes.","5 minutos, com apartes.","10 minutos, sem apartes.","2 minutos, sem apartes."],
 "Art. 251, b, 1. Pegadinha: na discussão de projeto (b, 2), também são 5 minutos, mas com apartes. O que muda é o aparte.",A3+" (art. 251)")
Q("DV","Nos processos de destituição da Mesa ou de membros da Mesa e de cassação de mandato de Vereador, o tempo para discussão é, respectivamente:",
 ["10 minutos para cada Vereador e 20 para o denunciado, na destituição; 15 minutos para cada Vereador e 30 para o denunciado ou seu procurador, na cassação.","5 e 10 minutos, para ambos os processos.","15 minutos para cada Vereador e 30 para o denunciado, na destituição; 10 e 20 na cassação.","10 minutos para todos os envolvidos, nos dois processos."],
 "Art. 251, b, 5 e 6. Nos dois casos há apartes. Macete: o processo de maior gravidade (cassação) tem os maiores tempos.",A3+" (art. 251)")
Q("DV","Nos assuntos parlamentares, para encaminhamento de votação e para a palavra pela ordem, os tempos do Regimento são, respectivamente:",
 ["10 minutos, 2 minutos e 1 minuto, todos sem apartes.","5 minutos, 2 minutos e 1 minuto, todos com apartes.","10 minutos, 5 minutos e 2 minutos, sem apartes.","5 minutos, 1 minuto e 1 minuto, todos sem apartes."],
 "Art. 251, c, e e g. Para solicitar esclarecimentos ao Prefeito e a auxiliares: 5 minutos, sem apartes (h). Para pedir retificação ou impugnar a ata: 5 minutos, sem apartes (a).",A3+" (art. 251)")
Q("DV","Pela ordem, o Vereador só poderá falar para:",
 ["solicitar a censura do Presidente a qualquer pronunciamento de outro Vereador que contenha expressão, frase ou conceito que considerar injurioso.","discutir o mérito da proposição em pauta.","pedir licença para ausentar-se da sessão por mais de 15 dias.","apresentar projeto de lei durante a Ordem do Dia."],
 "Art. 252: sete hipóteses taxativas (reclamar contra preterição de formalidade, suscitar dúvida de interpretação, comunicação de líder à Mesa, prorrogação de Comissão Especial, retificação de voto ou ata, censura, esclarecimentos do Presidente).",A3+" (art. 252)")
Q("DV","Não se admitirão questões de ordem:",
 ["quando houver orador na tribuna, quando o Presidente estiver com a palavra na direção dos trabalhos ou quando se estiver procedendo a qualquer votação.","durante o expediente.","quando houver aparte em curso.","durante o intervalo regimental."],
 "Art. 252, parágrafo único. Além disso: a questão de ordem de censura só será publicada se o Presidente não promover a censura solicitada.",A3+" (art. 252, parágrafo único)")
Q("DV","Da decisão ou omissão do Presidente em questão de ordem, representação ou proposição de Vereador, cabe recurso ao plenário. Esse recurso:",
 ["deve ser escrito e proposto no prazo improrrogável de 2 dias úteis; até a deliberação do plenário, prevalece a decisão do Presidente.","pode ser verbal, a qualquer tempo, e suspende a decisão.","deve ser proposto no prazo de 15 dias úteis, com efeito suspensivo.","é julgado pelo próprio Presidente."],
 "Parecer da Comissão de Finanças, Justiça e Redação em 2 dias úteis improrrogáveis, e inclusão obrigatória na Ordem do Dia da sessão ordinária seguinte. Rejeitado por maioria simples, a decisão é mantida. Aprovado, o Presidente deve cumprir, sob pena de destituição.",A3+" (arts. 256-257)")
Q("DV","Ao final de cada sessão legislativa, a Mesa fará, por meio de ato, a:",
 ["consolidação de todos os precedentes regimentais firmados, publicando-os em avulso para distribuição aos Vereadores.","revisão geral do Regimento Interno.","revogação dos precedentes que não tenham sido reiterados.","consolidação das leis aprovadas, para publicação no diário oficial."],
 "Os precedentes resolvem os casos omissos decididos pelo plenário e orientam situações semelhantes.",A3)

# ============ 4. SANÇÃO, VETO E PROMULGAÇÃO ============
Q("VETO","O projeto aprovado pela Câmara será enviado ao Prefeito, para sanção ou veto, no prazo de:",
 ["15 dias úteis, contados da data de sua aprovação; o período de recesso não é reconhecido como dia útil.","48 horas da aprovação.","30 dias corridos da aprovação.","10 dias da aprovação, improrrogáveis."],
 "Não confunda os 15 dias úteis (envio ao Prefeito) com os 10 dias para promulgação e publicação de decretos legislativos e resoluções e com as 48 horas de promulgação da lei.",A3)
Q("VETO","Para deliberar sobre o veto, a Câmara disporá de:",
 ["30 dias úteis, contados do recebimento do ofício; em recesso, conta-se da primeira sessão ordinária após o recesso, e a entrada em recesso interrompe o prazo.","15 dias corridos, contados da publicação.","30 dias corridos, que correm durante o recesso.","45 dias úteis, prorrogáveis por igual período."],
 "O veto, considerado matéria de urgência, é lido em qualquer fase da sessão, tão logo chegue à Câmara. Na volta do recesso, deve ser obrigatoriamente lido na primeira sessão ordinária.",A3)
Q("VETO","O veto cujas razões versem sobre constitucionalidade, legalidade, interesse público ou aspecto financeiro será despachado à Comissão de Finanças, Justiça e Redação, que terá:",
 ["prazo improrrogável de 5 dias para parecer; esgotado, o veto é incluído na pauta da primeira sessão ordinária, com ou sem parecer.","prazo de 3 dias úteis, prorrogáveis por mais 3.","prazo de 15 dias úteis, findo o qual o veto é considerado mantido.","prazo de 2 dias úteis, findo o qual o veto é arquivado."],
 "Incluído em Ordem do Dia, o veto é submetido à votação aberta, única, com uma única discussão.",A3)
Q("VETO","No veto parcial, a votação:",
 ["é necessariamente em bloco quando se tratar de matéria correlata ou idêntica; caso contrário, é possível votar em separado cada disposição autônoma, a requerimento de no mínimo 1/3 dos Vereadores, com assentimento do plenário, sem discussão, encaminhamento nem declaração de voto no requerimento.","é sempre artigo por artigo.","é sempre em bloco, vedada a votação em separado.","pode ser em separado por requerimento de qualquer Vereador, com discussão."],
 "Arts. 277 e seguintes. O quórum de 1/3 é para pedir a votação em separado. Já o quórum para rejeitar o veto é outro: maioria absoluta.",A3+" (art. 277)")
Q("VETO","A votação do veto faz-se mediante:",
 ["voto aberto, com uma única cédula de dizeres antagônicos: “Aceito o Veto” e “Rejeito o Veto”.","voto secreto, com cédula de dizeres antagônicos.","voto simbólico, por sentados e levantados.","voto aberto, por chamada nominal em ordem de inscrição, sem cédula."],
 "Art. 278. A votação secreta foi suprimida do Regimento (Res. 17/2003). Observe que o voto é aberto, mas a cédula existe: não são incompatíveis.",A3+" (art. 278)")
Q("VETO","Para a rejeição do veto é necessário o voto de, no mínimo:",
 ["a maioria absoluta dos Vereadores.","a maioria simples dos presentes.","2/3 dos Vereadores.","3/5 dos Vereadores."],
 "Art. 279. É a mesma exigência do art. 66, § 4º, da CF (maioria absoluta). Rejeitado o veto, o projeto vai ao Prefeito para sanção.",A3+" (art. 279)")
Q("VETO","Rejeitado o veto, o projeto é enviado ao Prefeito para sanção. Se a lei não for sancionada em 48 horas pelo Prefeito:",
 ["o Presidente da Câmara a promulga; se este não o fizer em igual prazo, caberá ao Vice-Presidente.","a Mesa Diretora a promulga em 15 dias.","o Vice-Prefeito a promulga.","o projeto volta ao plenário para nova votação."],
 "Art. 279, § 2º. A ordem é: Prefeito, Presidente da Câmara, Vice-Presidente.",A3+" (art. 279, § 2º)")
Q("VETO","Os decretos legislativos e as resoluções serão promulgados pelo Presidente e enviados à publicação dentro do prazo máximo e improrrogável de:",
 ["10 dias, contados da data de sua aprovação em plenário, ressalvadas as exceções regimentais.","48 horas, contadas da aprovação.","15 dias úteis, contados da aprovação.","30 dias, contados da redação final."],
 "Decretos legislativos e resoluções não passam por sanção do Prefeito; por isso, quem promulga é o Presidente da Câmara.",A3)
Q("VETO","Quanto ao registro dos originais de leis, decretos legislativos e resoluções:",
 ["são registrados em livros próprios, rubricados pelo Presidente, arquivados na secretaria da Câmara, e uma cópia autêntica, assinada pelo Presidente e pelo primeiro secretário, é enviada ao Prefeito.","são registrados no Executivo, que remete cópia à Câmara.","são registrados somente em meio eletrônico.","são assinados pelo Presidente e pelo segundo secretário."],
 "A cópia autêntica vai ao Prefeito “para os fins legais”, assinada pelo Presidente e pelo primeiro secretário, ou seus substitutos legais.",A3)
Q("VETO","Qualquer interpelação de Vereadores sobre os serviços da secretaria ou a situação do respectivo pessoal deve ser:",
 ["dirigida à Mesa, através do Presidente, e formulada obrigatoriamente por escrito.","feita oralmente, em plenário, ao Diretor competente.","dirigida diretamente à Diretoria de Gestão de Pessoas.","dirigida ao Prefeito."],
 "Depois de informada por escrito, a interpelação é encaminhada ao Vereador para conhecimento.",A3)

# ============ 5. PREFEITO, HONRARIAS, ORÇAMENTO, PAINEL, REFORMA ============
Q("ESP","A convocação do Prefeito pela Câmara para prestar informações sobre assunto de sua competência administrativa far-se-á por requerimento:",
 ["subscrito por no mínimo 1/3 dos Vereadores, discutido e votado sem encaminhamento nem declaração de voto, indicando explicitamente o motivo e os quesitos.","subscrito por qualquer Vereador, votado sem discussão.","subscrito pela maioria absoluta, despachado de plano pelo Presidente.","subscrito por 2/3, dispensada a indicação de quesitos."],
 "Art. 283. Aprovado o requerimento, o Presidente oficia o Prefeito e pede que marque dia e hora. O Prefeito deve atender em até 15 dias, improrrogáveis, do recebimento do ofício.",A3+" (art. 283)")
Q("ESP","Na sessão extraordinária destinada a ouvir o Prefeito convocado, o Regimento assegura:",
 ["1 hora para o Prefeito discorrer, prorrogável por igual período mediante deliberação do plenário, sem apartes; 2 minutos para cada Vereador solicitar esclarecimentos e 5 minutos para cada resposta do Prefeito.","30 minutos para o Prefeito, improrrogáveis, com apartes.","1 hora para o Prefeito, com apartes livres; 5 minutos por Vereador.","tempo ilimitado ao Prefeito, e 10 minutos para cada Vereador."],
 "Pegadinha: três números (1 hora, 2 minutos, 5 minutos). O Prefeito e os Vereadores não podem se desviar da matéria da convocação.",A3)
Q("ESP","O Prefeito pode comparecer à Câmara, independentemente de convocação, para prestar esclarecimentos:",
 ["sobre qualquer matéria, quando julgar oportuno fazê-lo pessoalmente, em dia e hora previamente estabelecidos.","somente sobre matéria orçamentária.","somente com aprovação de 2/3 dos Vereadores.","somente durante a Ordem do Dia de sessão ordinária."],
 "Art. 286. Na sessão extraordinária convocada para esse fim, o Prefeito faz exposição inicial e responde às interpelações. Aplicam-se as regras do artigo anterior.",A3+" (art. 286)")
Q("ESP","Sobre as contas do Prefeito, o Regimento dispõe que, rejeitadas as contas, por votação ou pelo decurso de prazo:",
 ["serão imediatamente remetidas ao Ministério Público, para os devidos fins.","serão arquivadas.","serão devolvidas ao Tribunal de Contas.","será instaurado, automaticamente, processo de cassação do Prefeito."],
 "As contas de cada exercício são julgadas pela Câmara. Não confundir com o julgamento político da responsabilidade do Prefeito, que exige 2/3.",A3)
Q("ESP","A responsabilidade do Prefeito, por crime de responsabilidade, só será decretada pelo voto de no mínimo:",
 ["2/3 dos Vereadores.","maioria absoluta dos Vereadores.","maioria simples dos presentes.","3/5 dos Vereadores."],
 "Deliberando a Câmara pela responsabilidade do Prefeito, o Presidente obrigatoriamente iniciará as medidas judiciais cabíveis.",A3)
Q("ESP","Nas sessões extraordinárias convocadas pelo Prefeito, o Regimento prevê que:",
 ["se as Comissões Permanentes estiverem com os mandatos extintos, são consideradas prorrogadas até o final das sessões extraordinárias.","as Comissões Permanentes ficam suspensas até o fim do recesso.","o rito é o dos projetos com prazo de 15 dias úteis.","as normas regimentais comuns ficam todas afastadas."],
 "Arts. 262 a 264. Aplica-se a tramitação dos projetos de lei com prazo de 30 dias, respeitada a fase de tramitação iniciada antes. As disposições regimentais não colidentes aplicam-se aos períodos extraordinários.",A3+" (arts. 262-264)")
Q("ESP","A Câmara pode conceder títulos honoríficos, comendas e outras honrarias por meio de:",
 ["projeto de decreto legislativo, aprovado em discussão e votação únicas, pelo voto de no mínimo 2/3 de seus membros.","projeto de lei, aprovado por maioria absoluta, em dois turnos.","projeto de resolução, aprovado por maioria simples.","requerimento aprovado por 1/3 dos Vereadores."],
 "Art. 266. Vale para personalidade nacional ou estrangeira radicada no País, comprovadamente digna da homenagem. A exigência de residência no País cai para estrangeiros mundialmente consagrados pelos serviços prestados à humanidade (§ 2º).",A3+" (art. 266)")
Q("ESP","É vedada a concessão de títulos honoríficos a:",
 ["pessoas no exercício de mandato eletivo ou em cargos executivos por nomeação.","pessoas residentes fora do município.","pessoas falecidas.","servidores efetivos da Câmara."],
 "Art. 266, § 1º. Cada Vereador pode apresentar, no máximo, 2 proposições por ano, por tipo de honraria (§ 3º), e não pode figurar como primeiro signatário em mais de duas vezes por sessão legislativa.",A3+" (art. 266, § 1º)")
Q("ESP","Quanto à instrução do projeto de concessão de título honorífico, o Regimento exige:",
 ["circunstanciada biografia do homenageado e, como condição de recebimento pela Mesa, sua anuência por escrito, exceto quanto a personalidades estrangeiras.","apenas a justificação do autor.","parecer favorável do Tribunal de Contas.","assinatura de todos os Vereadores."],
 "Os signatários são considerados fiadores das qualidades do homenageado e não podem retirar suas assinaturas depois de recebida a propositura pela Mesa. Discussão: 5 minutos por Vereador.",A3)
Q("ESP","Na sessão solene de entrega dos títulos, para falar em nome da Câmara só será permitida a palavra:",
 ["do Vereador designado pelo Presidente como orador oficial, do autor da propositura e de um Vereador indicado por cada partido ou bloco com assento na Câmara.","de qualquer Vereador inscrito.","somente do Presidente.","do orador oficial e do homenageado."],
 "Art. 270, § 3º. No último ano do mandato, a propositura de honrarias deve ser feita até a sessão ordinária do mês de junho, para que sejam entregues dentro do mandato (§ 2º). Sessões solenes devem ser realizadas dentro do mandato do Vereador autor (§ 1º).",A3+" (art. 270)")
Q("ESP","Em relação ao orçamento, o Regimento Interno de Rio Verde:",
 ["não estabelece rito próprio detalhado, remetendo sua disciplina à Lei Orgânica do Município.","estabelece rito detalhado de cinco sessões de discussão.","atribui à Mesa a iniciativa da proposta orçamentária.","dispensa a votação em plenário."],
 "O orçamento é de iniciativa privativa do Prefeito (art. 185), e o rito segue a Lei Orgânica. Não se admite destaque na proposta orçamentária, nas diretrizes, no PPA nem no julgamento das contas.",A3)
Q("ESP","A segurança do edifício da Câmara Municipal compete:",
 ["à Mesa, sob a direção do Presidente, podendo ser feita por servidores do serviço próprio ou por entidade contratada e habilitada.","ao Prefeito, por meio da Guarda Municipal.","à Procuradoria da Câmara.","à Polícia Militar, exclusivamente."],
 "Art. 294. No plenário, durante as sessões, só serão admitidos os Vereadores, os servidores em serviço e os convidados. Quem perturbar a ordem, desacatar a Mesa, Vereadores ou servidores, sendo ineficazes as providências da Presidência, será detido e encaminhado à autoridade competente.",A3+" (arts. 294-295)")
Q("ESP","Qualquer cidadão poderá assistir às sessões das galerias, desde que guarde silêncio e respeito. Quando o Presidente não conseguir manter a ordem por simples advertências, deverá:",
 ["suspender a sessão, adotando as providências cabíveis.","encerrar definitivamente a sessão.","mandar votar a expulsão do público.","convocar a Polícia Militar, sem suspender a sessão."],
 "Art. 295, parágrafo único. Quem perturbar com aplausos ou manifestações de reprovação e não atender à advertência será compelido a sair imediatamente do edifício.",A3+" (art. 295)")
Q("ESP","Segundo o art. 298, as deliberações da Câmara realizam-se, em regra:",
 ["pelo Sistema Eletrônico de Votação (Painel de Votações); o voto assim dado não pode ser modificado depois de proclamado o resultado, e o voto é sempre público.","pelo processo simbólico, com sentados e levantados.","por cédulas, sempre secretas.","por aclamação, quando o Presidente entender conveniente."],
 "Na impossibilidade de usar o sistema eletrônico, aplicam-se as regras do art. 84 e seguintes. Art. 299: o voto será sempre público nas deliberações da Câmara.",A3+" (arts. 298-299)")
Q("ESP","No sistema do Painel Eletrônico, o processo nominal é a regra geral. O processo simbólico:",
 ["pode ser usado a requerimento de Vereador aprovado pelo plenário ou nos casos previstos no Regimento, e não pode ser usado para eleição da Mesa, julgamento das contas do município, perda de mandato, veto, urgência especial e matérias de maioria absoluta ou 2/3.","pode ser usado em qualquer matéria, a critério do Presidente.","é vedado em qualquer hipótese.","pode ser usado na apreciação de veto, por ser matéria de urgência."],
 "A votação não pode ser simbólica nas hipóteses de maior relevância: Mesa, contas, perda de mandato, veto, urgência especial e quórum qualificado (maioria absoluta ou 2/3).",A3)
Q("ESP","Uma vez iniciada a votação no plenário:",
 ["somente se interrompe se for verificada a falta de número legal, e é vedado ao Vereador abandonar o plenário no curso da votação, salvo mal súbito.","pode ser interrompida a qualquer tempo por requerimento verbal.","pode ser interrompida por pedido de vista do autor.","continua mesmo sem número legal, pois já iniciada."],
 "Se faltar número, os votos já colhidos são considerados prejudicados. Se o Vereador acometido de mal súbito sair, é considerado o voto que já tenha proferido.",A3)
Q("ESP","Antes de iniciar a votação, é assegurado a cada bancada, por seu líder ou integrante indicado, falar apenas uma vez, para orientar os compartidários quanto ao mérito da matéria, por:",
 ["3 minutos.","2 minutos.","5 minutos.","10 minutos."],
 "Art. 303. A votação só pode ser aberta após o término dos encaminhamentos, e a orientação de bancada não impede que qualquer Vereador encaminhe a matéria. Não confunda com o encaminhamento do art. 251, e, que é de 2 minutos.",A3+" (art. 303)")
Q("ESP","Qualquer Vereador poderá requerer destaque para votação em separado de parte do texto de uma proposição. Não haverá destaque, porém, quando se tratar de:",
 ["proposta orçamentária, diretrizes orçamentárias, plano plurianual, julgamento das contas do município ou casos em que a providência se revele impraticável.","projeto de decreto legislativo.","emenda de comissão.","projeto de resolução."],
 "Em regra o projeto é votado em bloco. O destaque é a exceção, que serve para isolar um trecho problemático.",A3)
Q("ESP","Quanto à ordem de votação das emendas, terão preferência:",
 ["as emendas supressivas e as emendas e substitutivos oriundos das comissões; se houver duas ou mais emendas sobre o mesmo artigo ou parágrafo, terá preferência a que for protocolada primeiro.","as emendas aditivas, sempre.","as emendas do autor do projeto, sempre.","as emendas protocoladas por último."],
 "Sempre que o parecer da comissão for pela rejeição do projeto, o plenário delibera primeiro sobre o parecer, antes de entrar no projeto.",A3)
Q("ESP","Proclamado o resultado da votação, o Vereador poderá impugná-lo perante o plenário quando dela tenha participado Vereador impedido. Acolhida a impugnação:",
 ["repete-se a votação, sem considerar o voto que motivou o incidente.","anula-se a sessão.","a matéria é arquivada.","o resultado proclamado é mantido, e o Vereador impedido é punido."],
 "Após a proclamação, o Painel Eletrônico exibe os detalhes da votação por no mínimo 20 segundos.",A3)
Q("ESP","Em relação à emenda à redação final, o Regimento admite:",
 ["somente a emenda que se destine a despojá-la de obscuridade, contradição ou impropriedade linguística.","qualquer emenda de mérito.","emendas supressivas e aditivas livremente.","nenhuma emenda, em qualquer hipótese."],
 "Aprovada a emenda, a matéria volta à comissão para nova redação final. Rejeitada a nova redação, o projeto é mais uma vez encaminhado à comissão, e considera-se aprovada a redação se contra ela não votar a maioria absoluta dos componentes da Câmara.",A3)
Q("ESP","Segundo o Regimento, o Regimento Interno da Câmara somente pode ser alterado, reformado ou substituído:",
 ["por Resolução, em projeto proposto por no mínimo 1/3 dos membros da Câmara ou pela Mesa Diretora.","por lei, em projeto de iniciativa do Prefeito.","por Decreto Legislativo, em projeto de qualquer Vereador.","por Resolução, em projeto de qualquer Vereador."],
 "Arts. 312 e 313. Tema recorrente: instrumento (Resolução) e legitimados (1/3 ou Mesa). Vigência: data de publicação (art. 314).",A3+" (arts. 312-314)")

# ============ 6. LEI 7.434/2023 ============
Q("L34","A Lei nº 7.434/2023 estabelece:",
 ["o Regulamento Interno da Estrutura Organizacional da Câmara Municipal de Rio Verde, definindo atribuições e subordinação das unidades que a compõem.","o Plano de Cargos e Remuneração dos servidores da Câmara.","o Regimento Interno da Câmara.","o Estatuto dos Servidores Públicos do Município."],
 "A Lei 7.434 cuida da estrutura; a Lei 7.435 cuida do plano de cargos. Trocar uma pela outra é a pegadinha mais barata e mais frequente.",A0)
Q("L34","A Direção Superior do Poder Legislativo será exercida:",
 ["pela Mesa Diretora, através de seu Presidente, auxiliado pelos Vereadores, diretores, procuradores, assessores e demais servidores.","pelo Presidente da Câmara, com exclusividade.","pelo Diretor Legislativo.","pelo plenário, por meio de comissões."],
 "Os integrantes da Mesa Diretora estão definidos no Regimento Interno, e não na Lei 7.434.",A0)
Q("L34","Compõem a Estrutura Administrativa do Poder Legislativo, subordinados diretamente ao Presidente e demais membros da Mesa Diretora:",
 ["a Presidência, as Diretorias e as Coordenadorias Setoriais.","a Presidência, as Diretorias e os Gabinetes Parlamentares.","a Presidência, as Gerências e as Coordenadorias Setoriais.","as Diretorias, as Coordenadorias Setoriais e os Gabinetes Parlamentares."],
 "Art. 6º. Gabinetes Parlamentares não compõem a estrutura administrativa: são órgãos independentes, constituídos pelos auxiliares, assistentes e assessores imediatos de um legislador.",A0+" (art. 6º)")
Q("L34","Quanto ao modelo de gestão e à atuação sistêmica previstos na Lei 7.434:",
 ["as competências das unidades de gestão institucional são planejadas, coordenadas e controladas de forma centralizada, por meio de sistemas estruturantes, e as unidades que exercem funções de sistemas estruturantes subordinam-se tecnicamente à unidade central do sistema.","cada unidade administrativa planeja suas competências de forma descentralizada e autônoma.","as unidades de sistemas estruturantes subordinam-se hierarquicamente aos gabinetes parlamentares.","a gestão é exclusivamente centralizada no Presidente, vedada a participação social."],
 "O modelo é marcado pela gestão participativa e pela atuação transparente, que permite controle social do Poder Legislativo.",A0)
Q("L34","Integram a Presidência, no âmbito do Gabinete da Presidência:",
 ["Chefia de Gabinete, Ouvidoria, Corregedoria Parlamentar, Procuradoria Geral, Controle Interno, Assessoria de Plenário e Assessoria de Imprensa da Presidência.","Diretoria Legislativa, Diretoria Parlamentar e Diretoria Financeira.","Coordenadoria de Compras e Licitações e Coordenadoria de Folha de Pagamento.","Chefia de Pessoal e Gerência de Tesouraria."],
 "Pegadinha de enumeração: Ouvidoria, Corregedoria Parlamentar, Procuradoria Geral e Controle Interno estão na Presidência, e não nas Diretorias.",A0)
Q("L34","A Lei 7.434 prevê, entre as Diretorias da Câmara:",
 ["Legislativa, Parlamentar, de Gestão de Pessoas, de Tecnologia em Informação, de Administração e Planejamento, Financeira, de Comunicação Social, de Assuntos Institucionais, de Contratos e Convênios e de Articulação Política.","Legislativa, Parlamentar, Financeira, de Obras e de Saúde.","Legislativa, Jurídica, Financeira e de Almoxarifado e Patrimônio.","Legislativa, Parlamentar, de Compras e Licitações e de Folha de Pagamento."],
 "São 10 Diretorias. Almoxarifado e Patrimônio, Compras e Licitações, Manutenção e Serviços Gerais, Relações Públicas, Folha de Pagamento e Engenharia e Projetos são Coordenadorias Setoriais (6).",A0)
Q("L34","São Coordenadorias Setoriais da Câmara, nos termos da Lei 7.434:",
 ["Almoxarifado e Patrimônio, Compras e Licitações, Manutenção e Serviços Gerais, Relações Públicas, Folha de Pagamento, e Engenharia e Projetos.","Almoxarifado e Patrimônio, Compras e Licitações, Tesouraria e Contabilidade.","Compras e Licitações, Contratos e Convênios e Articulação Política.","Folha de Pagamento, Gestão de Pessoas e Comunicação Social."],
 "Dentro de Compras e Licitações estão o Agente de Contratação e a Gerência de Cotação de Preços. Dentro do Almoxarifado, a Chefia do Núcleo de Almoxarifado.",A0)
Q("L34","Na Diretoria Financeira, a Lei 7.434 prevê as seguintes gerências:",
 ["Tesouraria, Contabilidade, e Planejamento Orçamentário e Financeiro.","Tesouraria, Contratos e Cotação de Preços.","Contabilidade, Arquivo e Documentação, e Folha de Pagamento.","Tesouraria, Expediente e Protocolo, e Suporte de Informática."],
 "São três gerências. A Gerência de Contratos pertence à Diretoria de Contratos e Convênios; a de Arquivo e Documentação, à Diretoria de Gestão de Pessoas.",A0)
Q("L34","A Coordenadoria Legislativa de Plenário, vinculada à Diretoria Legislativa, compreende as gerências de:",
 ["Apoio Legislativo, Processamento e Controle, e Redação de Atas.","Expediente e Protocolo, Imprensa e Comunicação, e Gravação e Som.","Apoio Legislativo, Tesouraria, e Redação de Atas.","Processamento e Controle, Suporte de Informática, e Desenvolvimento de Sistemas."],
 "A Diretoria Legislativa tem ainda a Chefia do Núcleo de Apoio Legislativo e a Gerência de Expediente e Protocolo.",A0)
Q("L34","Na Diretoria de Comunicação Social, a Lei 7.434 prevê:",
 ["a Gerência de Imprensa e Comunicação (com as assessorias de Comunicação, de Imprensa, de Mídias Digitais e de Relações Públicas) e a Gerência de Gravação e Som.","a Gerência de Tesouraria e a Gerência de Contabilidade.","apenas a Assessoria de Imprensa da Presidência.","a Gerência de Suporte de Informática e a de Desenvolvimento de Sistemas."],
 "A Gerência de Suporte de Informática e a de Desenvolvimento de Sistemas são da Diretoria de Tecnologia em Informação.",A0)
Q("L34","Segundo as diretrizes do art. 10 da Lei 7.434, os setores terão desdobramento operativo observando que a estrutura básica de direção superior:",
 ["unifica numa mesma autoridade as funções de comando, coordenação, controle, planejamento estratégico e articulação institucional.","reparte as funções de comando entre as Diretorias.","agrupa as funções de direção intermediária e gerência administrativa.","corresponde às funções de apoio direto de consultoria e assessoria."],
 "Art. 10: direção superior (unificada), gerência intermediária (direção intermediária, planejamento, coordenação, controle, supervisão, orientação técnica e gerência administrativa) e assessoramento (apoio direto, atribuições técnico-especializadas de consultoria, assessoramento e assistência).",A0+" (art. 10)")
Q("L34","Segundo as disposições finais da Lei 7.434, os casos omissos serão resolvidos:",
 ["pela Mesa Diretora; os cargos efetivos e em comissão que ocuparão as unidades e suas remunerações estão previstos no Plano de Cargos e Remuneração.","pelo plenário, em votação de maioria absoluta.","pelo Presidente, isoladamente.","pela Procuradoria Geral."],
 "A ligação entre as duas leis está aqui: a estrutura (7.434) se completa com os cargos e remunerações (7.435).",A0)

# ============ 7. LEI 7.435/2023 ============
Q("L35","O regime jurídico dos servidores de provimento efetivo do Poder Legislativo do Município de Rio Verde é:",
 ["o Estatutário.","o celetista.","o contratual temporário.","o regime especial, previsto em convênio."],
 "O Plano de Cargos e Remuneração organiza os cargos de provimento efetivo em sistema de carreira, fundamentado nos princípios da qualificação profissional, valorização da função pública e aperfeiçoamento do servidor, e os cargos em comissão, de livre nomeação e exoneração.",A0)
Q("L35","Segundo a Lei 7.435, considera-se cargo público:",
 ["aquele composto por um conjunto de atribuições e responsabilidades cometidas ao servidor, criado por lei, com denominação própria, número certo e pagamento pelo Erário Municipal.","a posição do servidor na escala de remuneração, identificada por letra e algarismo arábico.","o conjunto de categorias funcionais que se assemelham quanto à natureza do serviço.","o conjunto de atribuições agrupadas pela espécie de atividade."],
 "As outras alternativas são, respectivamente, os conceitos de padrão, grupo e categoria funcional. A banca costuma trocar definições.",A0)
Q("L35","Quanto aos conceitos do Plano de Cargos, o “padrão” é:",
 ["a posição do servidor na escala de remuneração do cargo, identificada por letra e algarismo arábico.","o conjunto de categorias funcionais do mesmo cargo e da mesma remuneração.","a atividade básica do quadro de pessoal, que individualiza o nível de conhecimento exigível e a remuneração do ocupante.","o grau de instrução formal exigido para o desempenho das funções."],
 "Classe: conjunto de categorias funcionais do mesmo cargo e da mesma remuneração. Cargo: atividade básica do quadro de pessoal. Nível: graus de instrução formal.",A0)
Q("L35","Os níveis de instrução formal considerados na organização dos Grupos Ocupacionais são:",
 ["básico (ensino fundamental), médio (ensino médio) e superior (curso superior ou técnico).","básico (ensino médio), técnico e superior.","fundamental, médio, técnico e superior, como quatro níveis.","médio e superior, apenas."],
 "São três níveis. Detalhe: o nível superior abrange “formação em curso superior ou técnico”, conforme o texto da lei.",A0)
Q("L35","As funções comissionadas dos grupos de Direção, Chefia e Assessoramento foram transformadas em cargos de provimento em comissão (DAS), que são graduados em:",
 ["4 (quatro) níveis.","3 (três) níveis.","5 (cinco) níveis.","2 (dois) níveis."],
 "Os níveis e símbolos remuneratórios consideram, entre outros critérios, a complexidade das funções e o poder decisório, o grau de responsabilidade, o número de unidades e servidores subordinados e o volume de processos administrativos.",A0)
Q("L35","O servidor efetivo ocupante de cargo de provimento em comissão poderá optar:",
 ["pela remuneração integral do cargo em comissão ou pela remuneração do cargo de origem acrescida de 80% do cargo em comissão.","pela remuneração do cargo de origem acrescida de 50% do cargo em comissão.","somente pela remuneração do cargo em comissão.","pela remuneração do cargo de origem acrescida de 100% do cargo em comissão."],
 "Quem optar pela remuneração do seu cargo efetivo percebe a gratificação de representação pelo exercício do cargo comissionado. O número a lembrar é 80%.",A0)
Q("L35","O ingresso nas categorias do Quadro Permanente dar-se-á:",
 ["no padrão inicial de cada cargo, mediante concurso público de provas e títulos, sendo o tempo de serviço prestado à Câmara computado como título nos termos do edital.","em qualquer padrão, mediante concurso de provas.","mediante processo seletivo simplificado e entrevista.","no padrão intermediário, para quem tiver curso superior."],
 "Art. 13 (parte inicial). Fala-se em “provas e títulos”, e o tempo de serviço na Câmara vale como título.",A0+" (art. 13)")
Q("L35","O desenvolvimento do servidor ocupante de cargo de provimento efetivo dá-se pela transferência de um padrão para o seguinte, no percentual de:",
 ["3%, observados alternadamente os critérios de merecimento (avaliação de desempenho) e antiguidade (interstício de 3 anos).","5%, por merecimento, a cada 2 anos.","3%, somente por antiguidade, a cada 5 anos.","10%, alternadamente por merecimento e antiguidade, a cada 3 anos."],
 "Art. 13, § 1º. Duas vezes o número 3 (percentual e interstício). Alternadamente: um padrão por merecimento, outro por antiguidade.",A0+" (art. 13, § 1º)")
Q("L35","Caberá à Mesa Diretora, juntamente com a Diretoria de Gestão de Pessoas:",
 ["instituir programa permanente de treinamento e desenvolvimento, para elevar a capacitação nas tarefas executadas e preparar o servidor para funções de maior complexidade, incluídas as de direção, chefia e assessoramento.","aprovar a progressão funcional, por decisão sigilosa.","julgar, em última instância, as contas dos servidores.","definir o número de cargos de provimento efetivo, independentemente de lei."],
 "A Lei 7.435 coloca em duas autoridades (Mesa + Diretoria de Gestão de Pessoas) o dever de capacitar.",A0)
Q("L35","Com a Lei 7.435, a nomenclatura do cargo efetivo de Secretária passa a ser Assistente Administrativo. Pelo mesmo comando, passam a existir:",
 ["Ouvidor (antes Telefonista), Operador de Videomonitoramento (antes Vigia) e Supervisor Administrativo (antes Agente Administrativo).","Ouvidor (antes Vigia), Supervisor Administrativo (antes Telefonista) e Operador de Videomonitoramento (antes Agente Administrativo).","Ouvidor (antes Agente Administrativo) e Supervisor Administrativo (antes Secretária).","Operador de Videomonitoramento (antes Telefonista) e Ouvidor (antes Secretária)."],
 "Decore em pares: Secretária para Assistente Administrativo; Telefonista para Ouvidor; Vigia para Operador de Videomonitoramento; Agente Administrativo para Supervisor Administrativo. Além disso, o cargo em comissão de Procurador Adjunto passa a Assessor Jurídico da Procuradoria Geral.",A0)
Q("L35","Os servidores que exercerem atribuições inerentes a outros cargos dos quais foram efetivados, por período superior a 5 anos consecutivos ou 10 anos intercalados:",
 ["poderão ser reenquadrados, por lei específica, observados os requisitos e critérios nela regulamentados.","são automaticamente reenquadrados, por ato da Mesa.","adquirem o direito ao novo cargo, independentemente de lei.","somente podem ser reenquadrados em cargo de nível superior."],
 "Art. 17, § 3º. Cuidado com a inversão dos prazos: 5 consecutivos e 10 intercalados, não o contrário. Observação: o enunciado da Aula 00 do curso cita “LC 237/2021”, mas o dispositivo é da Lei 7.435/2023 (erro de digitação no material).",A0+" (art. 17, § 3º)")
Q("L35","A carga horária dos servidores efetivos da Câmara será de:",
 ["8 horas diárias e 40 semanais, salvo o cargo de Ouvidor, que terá 6 horas diárias e 30 semanais.","6 horas diárias e 30 semanais, salvo o cargo de Ouvidor, que terá 8 horas.","8 horas diárias e 44 semanais, para todos.","8 horas diárias e 40 semanais, sem exceções."],
 "A exceção é o Ouvidor (6 e 30). Lembre que o cargo de Ouvidor surgiu da antiga nomenclatura de Telefonista.",A0)
Q("L35","Suspenderá o prazo de cumprimento do estágio probatório o servidor que ocupar cargo em comissão, bem como o gozo de licenças e afastamentos, exceto se:",
 ["a função for compatível ou correlata com o cargo de origem, tiver exercido função comissionada de maior complexidade do seu cargo de origem (comprovado e justificado) ou for cedido ao Executivo, Fundação ou Autarquia, com ônus para o requisitante.","o servidor tiver mais de 5 anos de casa.","o servidor for cedido a outro órgão, com ônus para a Câmara.","o servidor ocupar cargo em comissão de qualquer natureza."],
 "O estágio probatório é suspenso como regra, e a lei lista três exceções. A cessão só mantém o estágio quando o ônus é do órgão requisitante.",A0)
Q("L35","A Gratificação de Função, criada pela Lei 7.435, é:",
 ["atribuída por ato administrativo do Presidente da Câmara, com justificativa da real necessidade e descrição das atribuições, e não integra a remuneração para fins de aposentadoria.","atribuída por ato da Mesa, sem necessidade de justificativa, e integra a aposentadoria.","destinada a quem ocupa cargo em comissão.","fixada em valor único, sem vínculo com o vencimento base."],
 "Os valores são equivalentes a percentuais sobre o vencimento base e compõem quadro único; destinam-se a remunerar encargos especiais de servidores efetivos com maiores responsabilidades, salvo detentores de cargo em comissão.",A0)
Q("L35","Ao servidor é assegurado o direito de peticionar a revisão de seu enquadramento perante a Diretoria de Gestão de Pessoas, no prazo de:",
 ["30 dias, contados da publicação do respectivo apostilamento.","15 dias, contados da nomeação.","60 dias, contados da posse.","5 dias úteis, contados da ciência."],
 "Da decisão da Diretoria cabe recurso à Presidência da Câmara em 30 dias, da ciência; à Mesa Diretora cabe recurso em última instância administrativa, também em 30 dias. O prazo é sempre de 30 dias, mas a autoridade muda.",A0)
Q("L35","As despesas decorrentes da Lei 7.435 correrão:",
 ["à conta dos recursos consignados no Orçamento-Geral do Município nas rubricas destinadas à Câmara Municipal, obedecidos os preceitos da Lei Complementar nº 101/2000.","à conta do orçamento do Executivo, mediante convênio.","à conta de receitas próprias da Câmara, vedada a utilização de créditos suplementares.","à conta de fundo específico, instituído por decreto."],
 "Fecha a lei: a Mesa fica autorizada a baixar atos e normas complementares. Os direitos e vantagens (diárias, férias, licenças etc.) seguem a legislação pertinente.",A0)

BLOCKS = [
 ("PROP","Proposições, Requerimentos e Moções (Regimento, Título VII em diante)","MA"),
 ("PROJ","Projetos, Tramitação, Redação Final, Retirada e Arquivamento","MA"),
 ("DV","Discussão, Votação, Tempos de Palavra, Questão de Ordem e Recursos","MA"),
 ("VETO","Sanção, Veto, Promulgação e Registro","MA"),
 ("ESP","Prefeito, Honrarias, Orçamento, Segurança, Painel Eletrônico e Reforma do Regimento","A"),
 ("L34","Lei nº 7.434/2023: Estrutura Organizacional da Câmara","MA"),
 ("L35","Lei nº 7.435/2023: Plano de Cargos e Remuneração","MA"),
]
