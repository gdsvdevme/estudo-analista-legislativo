# -*- coding: utf-8 -*-
# Convenção: Q(bloco, enunciado, [CORRETA, errada1, errada2, errada3], comentario, estude)
# QF = ordem fixa (numérica), com índice da correta.
QS = []
def Q(b, stem, opts, why, study): QS.append(dict(b=b, stem=stem, opts=opts, ans=0, fixed=False, why=why, study=study))
def QF(b, stem, opts, ans, why, study): QS.append(dict(b=b, stem=stem, opts=opts, ans=ans, fixed=True, why=why, study=study))

S_LOM="LOM (PDF), Aulas 01–02"; S_REG="Regimento Interno (Res. 33/2000), Aulas 01–03"
S_PL="Dir. Constitucional, Aula 09 (Processo Legislativo)"; S_CC="Dir. Constitucional, Aula 13 + Dir. Legislativo, Aula 03"
S_LIC="Dir. Administrativo, Aulas 08–10 (Lei 14.133/2021)"

# ============ LOM ============
Q("LOM","Nos termos da Lei Orgânica do Município de Rio Verde, são poderes do Município, independentes e harmônicos entre si:",
 ["o Legislativo e o Executivo.","o Legislativo, o Executivo e o Judiciário.","o Executivo, o Legislativo e o Tribunal de Contas dos Municípios.","a Câmara Municipal, a Prefeitura e o Ministério Público."],
 "LOM, art. 5º. O Município não tem Poder Judiciário. Pegadinha: transportar a tripartição federal para o âmbito municipal.",S_LOM)
Q("LOM","Nos termos da LOM, à Câmara Municipal, com sanção do Prefeito, ressalvada a sua competência privativa, cabe legislar sobre todas as matérias de competência municipal e especialmente sobre:",
 ["lei de diretrizes orçamentárias, plano plurianual e orçamento anual.","concessão de título de cidadão honorário.","eleição da Mesa e elaboração do Regimento Interno.","autorização para o Prefeito ausentar-se do Município por mais de 15 dias."],
 "LOM, art. 33, III. O art. 33 traz o que se faz por lei, com sanção. As demais alternativas estão no art. 34 (competência privativa da Câmara, sem sanção). Regra: lei = com sanção; privativa = decreto legislativo ou resolução.",S_LOM)
Q("LOM","O processo legislativo municipal compreende, segundo a LOM, a elaboração de:",
 ["emenda à Lei Orgânica, leis complementares, leis ordinárias, leis delegadas, decretos legislativos e resoluções.","emenda à Lei Orgânica, leis complementares, leis ordinárias, medidas provisórias, decretos legislativos e resoluções.","emenda à Lei Orgânica, leis ordinárias, medidas provisórias, leis delegadas e resoluções.","leis complementares, leis ordinárias, leis delegadas, decretos do Prefeito e portarias."],
 "LOM, art. 41. Não há medida provisória na lista do Município. Decreto e portaria do Prefeito são atos administrativos, não espécies do processo legislativo.",S_LOM)
Q("LOM","Sobre a emenda à Lei Orgânica, é correto afirmar:",
 ["pode ser proposta por 1/3 dos membros da Câmara ou pelo Prefeito, é votada em dois turnos com interstício mínimo de 10 dias, exige 2/3 dos membros e é promulgada pela Mesa.","pode ser proposta por maioria absoluta dos vereadores, exige 3/5 em dois turnos e é promulgada pelo Prefeito.","exige maioria absoluta em turno único e é promulgada pelo Presidente da Câmara.","pode ser aprovada mesmo na vigência de intervenção no Município, desde que por 2/3."],
 "LOM, art. 42. 3/5 é o quórum da emenda à Constituição Federal. Quem promulga é a Mesa. É vedada na vigência de estado de sítio ou de intervenção.",S_LOM)
Q("LOM","Segundo a LOM, é de iniciativa exclusiva da Mesa da Câmara o projeto de lei que disponha sobre:",
 ["organização dos serviços administrativos da Câmara e criação, transformação ou extinção de seus cargos, com fixação da remuneração.","criação de cargos na administração direta e autárquica do Município.","matéria orçamentária do Município.","estruturação das secretarias e dos órgãos da Administração Pública."],
 "LOM, art. 46, II. As demais são de iniciativa exclusiva do Prefeito (art. 45). Tema próximo das Leis 7.434 e 7.435/2023 (estrutura e cargos da Câmara).",S_LOM)
Q("LOM","O Prefeito solicitou urgência para a apreciação de projeto de sua iniciativa. De acordo com a LOM:",
 ["a Câmara deve se manifestar em até 45 dias; esgotado o prazo sem deliberação, a proposição é incluída na ordem do dia, sobrestadas as demais, até a votação.","a Câmara deve se manifestar em até 30 dias; esgotado o prazo, o projeto é considerado aprovado.","o prazo de 45 dias corre normalmente durante o recesso e também para projetos de lei complementar.","esgotado o prazo de 45 dias, o projeto é arquivado automaticamente."],
 "LOM, art. 47. Não existe aprovação nem arquivamento automáticos: a consequência é o sobrestamento da pauta. O prazo não corre no recesso nem vale para lei complementar (§ 3º).",S_LOM)
Q("LOM","Sobre o veto do Prefeito a projeto de lei, segundo a LOM:",
 ["o prazo é de 15 dias úteis, contados do recebimento; o veto parcial abrange apenas texto integral de artigo, parágrafo, inciso ou alínea; o silêncio importa sanção.","o prazo é de 15 dias corridos; o veto parcial pode alcançar palavra ou expressão; o silêncio importa veto.","o prazo é de 30 dias úteis; o veto parcial pode alcançar apenas palavras; o silêncio importa sanção.","o prazo é de 15 dias úteis; o veto pode ser tácito quando o Prefeito silenciar."],
 "LOM, art. 48, §§ 1º a 3º. Pegadinhas clássicas: dias úteis x corridos, veto de palavra isolada (vedado) e “silêncio = veto” (o silêncio é sanção tácita).",S_LOM)
Q("LOM","Rejeitado o veto, o projeto é enviado ao Prefeito para promulgação. Se a lei não for promulgada em 48 horas pelo Prefeito (sanção tácita ou veto rejeitado), segundo a LOM:",
 ["o Presidente da Câmara a promulga e, se não o fizer em igual prazo, caberá ao Vice-Presidente.","a Mesa Diretora a promulga, colegiadamente, no prazo de 15 dias.","o Vice-Prefeito a promulga.","o Presidente da Câmara só a promulga após nova votação em Plenário."],
 "LOM, art. 48, § 7º (espelha o art. 66, § 7º, da CF). Ordem: Prefeito, depois Presidente da Câmara, depois Vice-Presidente.",S_LOM)
Q("LOM","Quanto às leis delegadas, a LOM de Rio Verde estabelece que:",
 ["são elaboradas pelo Prefeito, que solicita a delegação à Câmara; a delegação se faz por decreto legislativo, e não podem ser objeto dela atos de competência privativa da Câmara, matéria de lei complementar, planos plurianuais e orçamento.","são elaboradas pela Câmara por delegação do Prefeito, mediante decreto do Executivo.","a delegação se faz por lei ordinária e pode alcançar matéria de lei complementar.","a delegação se faz por resolução e pode alcançar o orçamento anual."],
 "LOM, art. 49. Na CF a delegação é por resolução do Congresso (art. 68, § 2º); na LOM de Rio Verde é por decreto legislativo. Em prova local, vale o texto da LOM.",S_LOM)
Q("LOM","Segundo a LOM, perderá o mandato o Vereador que deixar de comparecer, em cada sessão legislativa:",
 ["à terça parte das sessões ordinárias, salvo licença ou missão autorizada, ou a 5 sessões extraordinárias regularmente convocadas.","à metade das sessões ordinárias da Câmara.","a um quarto das sessões ordinárias ou a 3 sessões extraordinárias.","a um terço das sessões ordinárias e extraordinárias, indistintamente."],
 "LOM, art. 38, III. Atenção: o Regimento (art. 107, IV) trata de outra hipótese, a falta a 3 sessões extraordinárias convocadas pelo Prefeito para matéria urgente. Leia a pergunta: “segundo a LOM” ou “segundo o Regimento”?",S_LOM)
Q("LOM","Sobre o julgamento das contas do Prefeito, segundo a LOM:",
 ["a Câmara delibera sobre o parecer do Tribunal de Contas dos Municípios em até 60 dias do recebimento, e o parecer só deixa de prevalecer por decisão de 2/3 dos vereadores.","o parecer do Tribunal de Contas deixa de prevalecer por maioria absoluta dos vereadores.","o parecer do Tribunal de Contas é vinculante, cabendo à Câmara apenas homologá-lo.","a Câmara julga as contas sem necessidade de parecer prévio do Tribunal de Contas."],
 "LOM, arts. 34, VIII e 52, § 2º (e CF, art. 31, § 2º). O quórum de 2/3 é o que derruba o parecer prévio. Quem julga é a Câmara; o Tribunal apenas auxilia.",S_LOM)
Q("LOM","Os prazos para atender a pedidos de informação da Câmara, segundo a LOM, são:",
 ["30 dias para os Secretários Municipais, com a recusa ou o não atendimento configurando crime de responsabilidade; 15 dias para o Prefeito, salvo prorrogação por complexidade da matéria.","15 dias para os Secretários Municipais e 30 dias para o Prefeito.","30 dias tanto para o Prefeito quanto para os Secretários.","15 dias para ambos, sem possibilidade de prorrogação."],
 "LOM, art. 30 (Secretários: 30 dias, crime de responsabilidade) e art. 65, XIV (Prefeito: 15 dias, prorrogável a pedido). A banca gosta de trocar os números entre os agentes.",S_LOM)
Q("LOM","De acordo com a LOM, o Executivo manterá sistema de controle interno a fim de:",
 ["criar condições para a eficácia do controle externo e a regularidade da receita e da despesa, acompanhar a execução de programas e do orçamento, avaliar resultados e verificar a execução dos contratos.","julgar as contas do Prefeito e aplicar sanções aos ordenadores de despesa.","fiscalizar os atos da Câmara Municipal e do Tribunal de Contas.","emitir parecer prévio sobre as contas anuais, em substituição ao Tribunal de Contas."],
 "LOM, art. 53, I a IV. Controle interno é do próprio Executivo e auxilia o controle externo. Quem julga as contas do Prefeito é a Câmara (art. 34, VIII).",S_LOM)

# ============ REGIMENTO ============
Q("REG","No Regimento Interno da Câmara de Rio Verde, a Mesa:",
 ["é eleita para duas sessões legislativas, composta por Presidente, Vice-Presidente e 1º e 2º Secretários; a eleição é por maioria simples e, em caso de empate, vence a chapa cujo candidato a Presidente seja o mais idoso.","é eleita para um ano, por maioria absoluta, e o empate se resolve por novo turno.","é eleita para quatro anos, composta por Presidente, Vice-Presidente e três Secretários.","é eleita para duas sessões legislativas por 2/3 dos membros, e o empate é decidido pelo mais votado nas eleições."],
 "Regimento, arts. 5º, 11 e 11, § 1º. Pegadinhas: duração (2 anos, não 1 nem 4), quórum (maioria simples) e critério de desempate (idade).",S_REG)
Q("REG","Os membros da Mesa podem ser destituídos, isoladamente ou em conjunto, quando faltosos, omissos ou ineficientes, mediante resolução aprovada por:",
 ["no mínimo 2/3 dos membros da Câmara, assegurada ampla defesa.","maioria simples dos vereadores presentes.","maioria absoluta dos membros da Câmara.","3/5 dos membros da Câmara."],
 "Regimento, arts. 28 e 29 (e LOM, art. 22, § 3º). A representação inicial é subscrita pela maioria absoluta, mas a destituição exige 2/3. Não confunda as duas etapas.",S_REG)
Q("REG","Segundo o Regimento consolidado até a Resolução nº 05/2026, as Comissões Permanentes são:",
 ["em número de 16, compostas cada uma por 3 vereadores: Presidente, Relator e Vogal.","em número de 7, compostas por 5 vereadores cada.","em número de 15, compostas por 3 vereadores cada.","em número de 16, compostas por 5 vereadores cada."],
 "Regimento, art. 38 e § 1º. O número já mudou várias vezes (7, 14, 15 e hoje 16). Se o seu material trouxer outro número, ele está desatualizado.",S_REG)
Q("REG","Quanto aos prazos de tramitação nas Comissões Permanentes, em regra:",
 ["o prazo para parecer é de 2 dias, prorrogável por mais 1 dia pelo Presidente da Câmara, com requerimento fundamentado; o relator tem 2 dias improrrogáveis; a vista é de até 24 horas e só após o projeto estar relatado.","o prazo para parecer é de 5 dias, prorrogável por mais 5, e a vista pode ser concedida antes do relatório.","o prazo para parecer é de 2 dias improrrogáveis e não há pedido de vista.","o prazo para parecer é de 15 dias, e a vista é de 48 horas, prorrogável."],
 "Regimento, art. 56 e §§ 1º a 4º. Pegadinha: a vista só é concedida depois de o projeto estar relatado, e é comum e improrrogável.",S_REG)
Q("REG","Quando o parecer da Comissão de Constituição, Justiça e Redação conclui pela inconstitucionalidade ou ilegalidade de um projeto:",
 ["o parecer é submetido ao Plenário em discussão e votação única; se aprovado, a proposição é arquivada; se rejeitado, segue às demais Comissões.","o projeto é arquivado automaticamente, sem votação.","o Presidente da Câmara decide sozinho se o projeto prossegue.","o projeto segue obrigatoriamente ao Plenário para votação do mérito."],
 "Regimento, arts. 61 e 71. A Comissão de Constituição e Justiça opina primeiro (aspectos legal e constitucional). Quem arquiva é o Plenário, ao aprovar o parecer.",S_REG)
Q("REG","Sobre as Comissões Especiais, segundo o Regimento:",
 ["são constituídas por requerimento subscrito por no mínimo 1/3 dos membros, aprovado por maioria simples; o requerimento deve indicar finalidade, número de membros e prazo; não cabem para assunto de competência de Comissão Permanente.","são constituídas por requerimento de qualquer vereador, aprovado por 2/3.","têm prazo indeterminado e não se extinguem pelo fim do prazo.","podem tratar de assunto de competência específica de Comissão Permanente."],
 "Regimento, arts. 73, 74 e 75, §§ 5º e 6º. Sem concluir no prazo, a Comissão Especial se extingue automaticamente, salvo prorrogação aprovada em tempo hábil.",S_REG)
Q("REG","O Plenário da Câmara tem 21 vereadores. Segundo o Regimento, para aprovar a alteração do Regimento Interno (maioria absoluta) e para a cassação do mandato de vereador (2/3), são necessários, no mínimo, respectivamente:",
 ["11 e 14 votos.","10 e 14 votos.","11 e 13 votos.","10 e 15 votos."],
 "Regimento, arts. 83 e 84. Maioria absoluta = primeiro número inteiro acima da metade dos componentes (21/2 = 10,5, logo 11). 2/3 de 21 = 14. Pegadinha: maioria absoluta é dos membros, não dos presentes.",S_REG)
Q("REG","Exigem voto mínimo de 2/3 dos membros da Câmara, segundo o Regimento:",
 ["alienação de bens imóveis, cassação do mandato de vereador e destituição da Mesa.","aprovação do Regimento Interno e do Código Tributário.","rejeição de veto e concessão de serviços públicos.","criação de cargos no quadro da secretaria da Câmara."],
 "Regimento, art. 84. Exigem maioria absoluta: Regimento, Código de Obras, Estatuto dos Servidores, Código Tributário, criação de cargos da Câmara, concessão de serviços, Plano Diretor e rejeição de veto (inciso I).",S_REG)
Q("REG","Sobre as sessões ordinárias da Câmara, segundo o Regimento:",
 ["compõem-se de Expediente, Ordem do Dia e Assuntos Parlamentares; na Ordem do Dia, os vetos vêm em primeiro lugar; não há sessões ordinárias em janeiro e julho.","compõem-se apenas de Ordem do Dia e Assuntos Parlamentares; os projetos em primeira discussão vêm antes dos vetos.","realizam-se também em janeiro e julho, por serem meses de recesso parcial.","os Assuntos Parlamentares vêm antes da Ordem do Dia e podem prorrogar a sessão."],
 "Regimento, arts. 126, 127, 134 e 146. A ordem da pauta é: vetos, redação final, segunda discussão, primeira discussão, depois moções, requerimentos e recursos. As sessões ordinárias não são prorrogadas para assuntos parlamentares.",S_REG)
Q("REG","Sobre as sessões extraordinárias, segundo o Regimento:",
 ["podem ser convocadas pela Mesa, por 1/3 dos membros ou pelo Prefeito; exigem antecedência mínima de 3 dias, salvo extrema urgência; tratam só da matéria da convocação e não têm assuntos parlamentares.","só podem ser convocadas pelo Prefeito, com antecedência de 24 horas.","podem tratar de qualquer matéria e incluem assuntos parlamentares.","são abertas com qualquer número de vereadores presentes."],
 "Regimento, arts. 147 a 155. Abertura exige maioria absoluta dos membros (art. 152). Na LOM, a convocação por requerimento em caso de urgência fala em maioria dos membros (art. 15, § 3º, III): atenção à fonte citada.",S_REG)
Q("REG","No processo de cassação do mandato de vereador, segundo o Regimento:",
 ["a denúncia pode ser feita por qualquer eleitor; recebida por maioria absoluta, o Presidente afasta o vereador apenas quanto à matéria objeto da denúncia, até o julgamento; a cassação exige 2/3 dos membros, com votações abertas.","a denúncia só pode ser feita pelo Ministério Público; o vereador é afastado totalmente do mandato desde o recebimento.","a cassação exige maioria simples dos presentes, com votação secreta.","a denúncia é recebida pelo Presidente isoladamente e o afastamento é automático."],
 "Regimento, arts. 107 a 111 (art. 111, parágrafo único, alterado pela Res. 10/2001, votações abertas). Se o denunciante for vereador, fica impedido de votar e de integrar a Comissão Processante (art. 109, § 1º).",S_REG)

# ============ PROCESSO LEGISLATIVO ============
Q("PL","Um vereador apresenta projeto de lei que cria cargo em comissão na estrutura de uma secretaria municipal, e o Prefeito o sanciona. Segundo a jurisprudência do STF e o princípio da simetria:",
 ["a lei é inconstitucional por vício de iniciativa, matéria reservada ao Chefe do Executivo, e a sanção não convalida o vício.","a lei é válida, pois a sanção do Prefeito convalida o vício de iniciativa.","a lei é válida se aprovada por 2/3 dos vereadores.","a lei só seria inconstitucional se houvesse aumento de despesa."],
 "CF, art. 61, § 1º, II (aplicado por simetria aos Municípios) e LOM, art. 45. A Súmula 5 do STF (sanção sana o vício) foi superada. Pegadinha: tratar o vício de iniciativa como sanável.",S_PL)
Q("PL","Segundo a tese do STF (Tema 917), a lei de iniciativa parlamentar que cria despesa para a Administração, mas não trata de sua estrutura, da atribuição de seus órgãos nem do regime jurídico dos servidores:",
 ["não usurpa a competência privativa do Chefe do Executivo, pois a reserva de iniciativa é taxativa e não alcança toda lei que gere despesa.","é sempre inconstitucional, porque somente o Chefe do Executivo pode criar despesas.","é inconstitucional por tratar de matéria orçamentária.","só é válida se tiver aprovação prévia do Prefeito."],
 "STF, RE 878.911 (Tema 917). A reserva de iniciativa é exceção e deve ser interpretada de forma restrita. Cuidado com a regra simplista “criou despesa = vício”.",S_PL)
Q("PL","A iniciativa popular de projetos de lei de interesse específico do Município exige a manifestação de, pelo menos:",
 ["5% do eleitorado.","1% do eleitorado.","1% do eleitorado, distribuído por pelo menos 5 bairros.","10% do eleitorado."],
 "CF, art. 29, XIII, e LOM, art. 43. O 1% (em 5 Estados) é a iniciativa popular federal. Pegadinha: trocar os percentuais.",S_PL)
Q("PL","Sobre o veto no processo legislativo, é correto afirmar:",
 ["o veto é sempre expresso e fundamentado em inconstitucionalidade (veto jurídico) ou contrariedade ao interesse público (veto político); o silêncio do Chefe do Executivo importa sanção tácita.","o veto pode ser tácito, quando o Chefe do Executivo deixa transcorrer o prazo.","o veto parcial pode incidir sobre palavra ou expressão isolada do dispositivo.","a sanção expressa convalida eventual vício de iniciativa do projeto."],
 "CF, art. 66, §§ 1º a 3º e LOM, art. 48. Veto jurídico = inconstitucionalidade; político = interesse público. Não existe veto tácito, nem veto de palavra solta.",S_PL)
Q("PL","O instrumento adequado para a Câmara Municipal conceder título de cidadão honorário, segundo a LOM e o Regimento, é:",
 ["decreto legislativo, aprovado por 2/3 dos membros e promulgado pelo Presidente da Câmara.","lei ordinária, sancionada pelo Prefeito.","resolução, aprovada por maioria simples.","lei complementar, aprovada por maioria absoluta."],
 "LOM, arts. 34, XX e 50; Regimento, art. 84, II, “d”. Resolução trata de assuntos internos da Câmara; decreto legislativo, dos demais casos de competência privativa com efeitos externos.",S_PL)
Q("PL","Projeto de lei rejeitado pela Câmara Municipal:",
 ["somente poderá constituir objeto de novo projeto, na mesma sessão legislativa, mediante proposta da maioria absoluta dos membros da Câmara.","não pode ser reapresentado em nenhuma hipótese.","pode ser reapresentado na mesma sessão legislativa por qualquer vereador.","pode ser reapresentado na mesma sessão legislativa mediante proposta de 1/3 dos vereadores."],
 "CF, art. 67 e LOM, art. 51. O que se restringe é a reapresentação na mesma sessão legislativa; na seguinte, pode ser reapresentado normalmente.",S_PL)

# ============ CONTROLE ============
Q("CC","Lei municipal que contraria a Constituição Federal pode ser questionada no STF, em controle concentrado, por meio de:",
 ["arguição de descumprimento de preceito fundamental (ADPF).","ação direta de inconstitucionalidade (ADI).","ação declaratória de constitucionalidade (ADC).","ação direta de inconstitucionalidade por omissão (ADO)."],
 "A ADI do STF alcança lei ou ato normativo federal ou estadual. Contra lei municipal em face da CF cabe ADPF (Lei 9.882/99).",S_CC)
Q("CC","A representação de inconstitucionalidade de lei municipal julgada pelo Tribunal de Justiça tem como parâmetro:",
 ["a Constituição do Estado.","a Constituição Federal, diretamente.","a Lei Orgânica do Município.","qualquer tratado internacional."],
 "CF, art. 125, § 2º. O TJ faz controle de leis municipais em face da Constituição Estadual. Note a LOM, art. 32, VIII: o Presidente da Câmara representa sobre inconstitucionalidade por decisão da Câmara.",S_CC)
Q("CC","Não possui legitimidade para propor ação direta de inconstitucionalidade perante o STF:",
 ["a Mesa da Câmara Municipal.","a Mesa de Assembleia Legislativa.","o Governador de Estado.","o Conselho Federal da OAB."],
 "CF, art. 103. Mesa de Câmara Municipal não consta do rol. Legitimados: Presidente da República, Mesas do Senado, da Câmara e de Assembleia, Governadores, PGR, OAB, partido com representação no Congresso e confederação sindical ou entidade de classe nacional.",S_CC)
Q("CC","No controle difuso, a declaração de inconstitucionalidade de lei por tribunal:",
 ["exige voto da maioria absoluta dos membros do tribunal ou do órgão especial (cláusula de reserva de plenário), salvo se já houver pronunciamento do plenário ou do STF sobre a questão.","pode ser feita por qualquer órgão fracionário, por maioria simples.","exige sempre decisão de 2/3 dos membros do tribunal.","depende de prévia manifestação do Senado Federal."],
 "CF, art. 97, Súmula Vinculante 10 e CPC, art. 949, parágrafo único. O Senado só suspende a execução da lei (art. 52, X) depois da decisão definitiva do STF.",S_CC)
Q("CC","Constitui exemplo de controle preventivo de constitucionalidade:",
 ["o parecer da comissão de constituição e justiça do Legislativo e o veto jurídico do Chefe do Executivo.","a ação direta de inconstitucionalidade julgada pelo STF.","a arguição de descumprimento de preceito fundamental.","a suspensão da execução da lei pelo Senado Federal."],
 "Preventivo ocorre antes de a lei existir (CCJ, veto jurídico e, excepcionalmente, mandado de segurança de parlamentar). Repressivo ocorre depois (ADI, ADPF, controle difuso). Sustar ato do Executivo que exorbita (LOM, art. 34, X) é controle político repressivo.",S_CC)

# ============ LICITAÇÕES ============
Q("LIC","São modalidades de licitação previstas na Lei nº 14.133/2021:",
 ["pregão, concorrência, concurso, leilão e diálogo competitivo.","concorrência, tomada de preços, convite, concurso e leilão.","pregão, convite, concorrência, leilão e RDC.","concorrência, pregão, convite, concurso e leilão."],
 "Lei 14.133/2021, art. 28. Tomada de preços e convite não existem mais na lei nova. O diálogo competitivo é novidade.",S_LIC)
Q("LIC","Segundo a Lei 14.133/2021, o pregão é a modalidade obrigatória para a contratação de:",
 ["bens e serviços comuns, exceto serviços técnicos especializados de natureza predominantemente intelectual e obras e serviços de engenharia (salvo os serviços comuns de engenharia).","obras e serviços técnicos especializados de natureza predominantemente intelectual.","alienação de bens móveis inservíveis.","trabalho técnico, científico ou artístico, com prêmio ou remuneração."],
 "Lei 14.133/2021, arts. 6º, XLI e 29. Alternativa C é leilão; D é concurso. Critério de julgamento do pregão: menor preço ou maior desconto.",S_LIC)
Q("LIC","Segundo a Lei 14.133/2021, em regra, as fases da licitação seguem a ordem:",
 ["preparatória, divulgação do edital, apresentação de propostas e lances, julgamento, habilitação, recursal e homologação.","preparatória, divulgação do edital, habilitação, apresentação de propostas, julgamento, recursal e homologação.","divulgação do edital, julgamento, habilitação, adjudicação e contratação.","preparatória, habilitação, divulgação do edital, julgamento, recursal e homologação."],
 "Lei 14.133/2021, art. 17. A habilitação pode anteceder as propostas, mas só por ato motivado, com explicitação dos benefícios (art. 17, § 1º). Pegadinha: tratar a exceção como regra.",S_LIC)
Q("LIC","É hipótese de inexigibilidade de licitação, segundo a Lei 14.133/2021:",
 ["contratação de serviços técnicos especializados de natureza predominantemente intelectual com profissionais ou empresas de notória especialização (vedada para publicidade e divulgação).","contratação em caso de emergência ou calamidade pública.","contratação de compras de pequeno valor, dentro do limite legal.","contratação após licitação deserta, quando não surgirem interessados."],
 "Lei 14.133/2021, art. 74, III. Inexigibilidade = inviabilidade de competição. Emergência, pequeno valor e licitação deserta são casos de dispensa (art. 75).",S_LIC)
Q("LIC","Na dispensa de licitação por emergência ou calamidade pública (art. 75, VIII da Lei 14.133/2021), os contratos:",
 ["podem ter prazo máximo de 1 ano, vedadas a prorrogação e a recontratação de empresa já contratada com base nesse inciso.","podem ser prorrogados por até 5 anos.","têm prazo de 180 dias, renovável por igual período.","não têm prazo máximo, enquanto durar a emergência."],
 "Lei 14.133/2021, art. 75, VIII. Atenção aos dois impedimentos: prorrogação e recontratação.",S_LIC)
Q("LIC","Salvo disposição em contrário, os prazos previstos na Lei nº 14.133/2021 são contados:",
 ["em dias úteis, excluído o dia do começo e incluído o do vencimento.","em dias corridos, incluído o dia do começo.","em dias úteis, incluído o dia do começo e excluído o do vencimento.","em horas, a partir da publicação do edital."],
 "Lei 14.133/2021, art. 183. Conhecer essa regra evita erro em questões sobre impugnação (3 dias úteis antes da abertura) e recursos (3 dias úteis).",S_LIC)
Q("LIC","Nas compras, obras e serviços, o contratado é obrigado a aceitar, nas mesmas condições, acréscimos ou supressões unilaterais de até:",
 ["25% do valor inicial atualizado do contrato (50% para acréscimos em reforma de edifício ou de equipamento).","50% do valor inicial, em qualquer caso.","10% do valor inicial atualizado do contrato.","sem limite, desde que haja interesse público."],
 "Lei 14.133/2021, art. 125. Pegadinha: o limite de 50% vale só para acréscimos em reforma de edifício ou equipamento.",S_LIC)
Q("LIC","As sanções previstas na Lei 14.133/2021 para o contratado que comete infração são:",
 ["advertência, multa (de 0,5% a 30% do valor do contrato), impedimento de licitar e contratar (até 3 anos) e declaração de inidoneidade (de 3 a 6 anos).","advertência, multa (de 1% a 10%), suspensão do direito de licitar (até 2 anos) e inidoneidade (de 2 a 5 anos).","advertência, multa (de 5% a 50%), impedimento (até 5 anos) e inidoneidade (de 5 a 10 anos).","apenas advertência e multa, vedadas as demais sanções."],
 "Lei 14.133/2021, art. 156. Memorize os intervalos: multa 0,5% a 30%; impedimento até 3 anos; inidoneidade 3 a 6 anos.",S_LIC)

# ============ DIREITO ADMINISTRATIVO ============
Q("DADM","Os princípios expressos no caput do art. 37 da Constituição Federal são:",
 ["legalidade, impessoalidade, moralidade, publicidade e eficiência.","legalidade, razoabilidade, moralidade, publicidade e eficiência.","legalidade, supremacia do interesse público, moralidade, publicidade e eficiência.","legalidade, impessoalidade, moralidade, finalidade e publicidade."],
 "CF, art. 37, caput (eficiência incluída pela EC 19/98). Cuidado: a LOM, art. 80, cita apenas legalidade, impessoalidade, moralidade e publicidade. Razoabilidade e supremacia do interesse público são implícitos.","Dir. Administrativo, Aula demo")
Q("DADM","São elementos (requisitos) do ato administrativo:",
 ["competência, finalidade, forma, motivo e objeto.","presunção de legitimidade, imperatividade, autoexecutoriedade e tipicidade.","competência, vontade, forma, objeto e causa.","sujeito, finalidade, motivo, tipicidade e imperatividade."],
 "Lei 4.717/65, art. 2º. Alternativa B lista atributos, não elementos. Pegadinha clássica: misturar os dois grupos.","Dir. Administrativo, Aula 03")
Q("DADM","Sobre os vícios do ato administrativo, é correto afirmar que:",
 ["o vício de competência (não exclusiva) e o de forma (não essencial) são, em regra, convalidáveis; o desvio de finalidade não pode ser convalidado.","todos os vícios são convalidáveis pela própria Administração.","o desvio de finalidade pode ser convalidado se não houver prejuízo.","nenhum vício é convalidável; todo ato viciado deve ser anulado."],
 "Lei 9.784/99, art. 55. Convalidam-se defeitos sanáveis (competência e forma). Finalidade, motivo e objeto viciados não se convalidam.","Dir. Administrativo, Aula 04")
Q("DADM","A revogação do ato administrativo:",
 ["decorre de conveniência e oportunidade, é feita pela própria Administração e, em regra, produz efeitos ex nunc.","decorre de ilegalidade, pode ser feita pelo Judiciário e produz efeitos ex tunc.","pode ser feita pelo Judiciário por motivos de mérito.","alcança atos vinculados e atos que já exauriram seus efeitos."],
 "Súmula 473 do STF. Revogação = mérito, Administração, ex nunc. Anulação = legalidade, Administração ou Judiciário, ex tunc. Atos vinculados não se revogam.","Dir. Administrativo, Aula 04")
Q("DADM","A licença, como espécie de ato administrativo, é ato:",
 ["vinculado e definitivo: preenchidos os requisitos legais, o particular tem direito a ela.","discricionário e precário, revogável a qualquer tempo sem indenização.","discricionário e definitivo, sujeito à conveniência da Administração.","vinculado e precário, revogável por mudança de política."],
 "Licença = vinculado e definitivo. Autorização = discricionário e precário. Pegadinha: trocar os dois conceitos.","Dir. Administrativo, Aula 04")
Q("DADM","O poder de polícia administrativa caracteriza-se, em regra, pelos atributos de:",
 ["discricionariedade, autoexecutoriedade e coercibilidade.","vinculação, tipicidade e imperatividade absolutas.","somente discricionariedade, sem coercibilidade.","delegabilidade integral a particulares."],
 "CTN, art. 78, e doutrina. A autoexecutoriedade exige previsão legal ou urgência; a delegação a particulares é restrita. Atenção às palavras absolutas (“sempre”, “somente”).","Dir. Administrativo, Aula 02")
Q("DADM","O decreto regulamentar expedido pelo Prefeito:",
 ["destina-se à fiel execução da lei e não pode exorbitar do poder regulamentar, sob pena de sustação pela Câmara.","pode inovar originariamente, criando obrigações não previstas em lei.","pode revogar lei municipal incompatível com o decreto.","só pode ser expedido com aprovação prévia da Câmara."],
 "CF, art. 49, V e LOM, art. 34, X. O decreto regulamentar não cria direito novo nem revoga lei.","Dir. Administrativo, Aula 02")
Q("DADM","Segundo a CF (art. 37, XIX), no tocante à Administração Indireta:",
 ["a autarquia é criada por lei específica; a empresa pública, a sociedade de economia mista e a fundação têm sua instituição autorizada por lei específica.","todas as entidades são criadas por decreto do Chefe do Executivo.","a empresa pública é criada por lei, e a autarquia, por autorização legislativa.","somente a sociedade de economia mista depende de lei."],
 "Autarquia: criada por lei. Empresas estatais e fundações: lei autoriza, e a personalidade surge com o registro. A LOM, art. 80, XIX, simplifica dizendo “criadas por lei”; na dúvida, siga a CF.","Dir. Administrativo, Aula 05")
Q("DADM","O servidor nomeado para cargo de provimento efetivo em virtude de concurso público adquire estabilidade, segundo a CF:",
 ["após 3 anos de efetivo exercício e avaliação especial de desempenho.","após 2 anos de efetivo exercício.","após 5 anos de efetivo exercício.","imediatamente após a posse."],
 "CF, art. 41 (EC 19/98). A LOM, art. 84, ainda traz 2 anos: texto anterior à EC 19. Em questão sobre a Constituição, vale 3 anos.","Dir. Administrativo, Aula 06")
Q("DADM","Quando um agente público, nessa qualidade, causa dano a terceiro, segundo o STF (Tema 940):",
 ["a ação deve ser proposta contra o Estado (ou a prestadora de serviço público), assegurado o direito de regresso contra o agente nos casos de dolo ou culpa.","a ação deve ser proposta diretamente contra o agente, e o Estado responde subsidiariamente.","o Estado nunca responde, pois a responsabilidade é pessoal do agente.","o Estado só responde se comprovada a culpa do agente e do órgão."],
 "CF, art. 37, § 6º, e RE 1.027.633. É a chamada dupla garantia: a vítima aciona o Estado, que depois cobra do agente em ação de regresso.","Dir. Administrativo, Aula 07")
Q("DADM","Após a Lei nº 14.230/2021, a configuração do ato de improbidade administrativa que causa dano ao erário (art. 10) exige:",
 ["ação ou omissão dolosa que enseje perda patrimonial efetiva e comprovada.","apenas conduta culposa, ainda que sem dano comprovado.","responsabilidade objetiva do agente.","culpa grave, dispensado o dano efetivo."],
 "Lei 8.429/92, art. 10, com a redação da Lei 14.230/2021. A modalidade culposa foi extinta. A prescrição passou a ser de 8 anos (art. 23).","Dir. Administrativo, Aula 14")
Q("DADM","Quanto aos bens públicos dominicais, é correto afirmar que:",
 ["podem ser alienados, observadas as exigências da lei.","são inalienáveis em qualquer hipótese.","são de uso comum do povo.","podem ser adquiridos por usucapião."],
 "Código Civil, arts. 99, III e 101. Imóveis municipais: avaliação, autorização legislativa e licitação (LOM, art. 101; Lei 14.133, art. 76). Bens públicos não são usucapíveis.","Dir. Administrativo, Aula 15")

# ============ ADMINISTRAÇÃO PÚBLICA ============
Q("ADMP","A Lei de Diretrizes Orçamentárias (LDO), segundo a CF (art. 165, § 2º):",
 ["compreende as metas e prioridades da administração, incluindo as despesas de capital do exercício seguinte, orienta a elaboração da LOA e dispõe sobre alterações na legislação tributária.","estabelece diretrizes, objetivos e metas para os próximos quatro anos.","fixa a despesa e estima a receita para o exercício financeiro.","tem vigência de dois anos e substitui o plano plurianual."],
 "A alternativa B descreve o PPA; a C, a LOA. Pegadinha: trocar a função de cada peça do ciclo orçamentário.","Adm. Pública, Aula 07")
Q("ADMP","O plano plurianual (PPA) tem vigência de:",
 ["quatro anos, do início do segundo ano do mandato ao final do primeiro ano do mandato seguinte.","quatro anos, coincidindo exatamente com o mandato.","um ano, o mesmo do exercício financeiro.","dois anos, renováveis."],
 "CF, art. 165, § 1º e ADCT, art. 35, § 2º, I. A vigência atravessa a mudança de governo para dar continuidade aos programas de duração continuada.","Adm. Pública, Aula 07")
Q("ADMP","Os créditos adicionais destinados a despesas imprevisíveis e urgentes, como as decorrentes de calamidade pública, são os:",
 ["extraordinários.","suplementares.","especiais.","ordinários."],
 "CF, art. 167, § 3º. Suplementares reforçam dotação existente; especiais atendem despesas sem dotação específica; extraordinários, as imprevisíveis e urgentes (LOM, art. 140, § 3º).","Adm. Pública, Aula 07")
Q("ADMP","A accountability, na Administração Pública, refere-se a:",
 ["prestar contas e responder pelos atos, abrangendo controles vertical (eleitoral), horizontal (entre instituições) e social.","exclusivamente o controle interno exercido pelo Executivo.","sinônimo de eficiência na aplicação de recursos.","controle realizado apenas pelo Poder Judiciário."],
 "Accountability = responsabilização + prestação de contas + possibilidade de sanção. Não se limita a um único tipo de controle.","Adm. Pública, Aula 02")
Q("ADMP","Em contraste com o modelo burocrático weberiano, a Nova Gestão Pública (NGP) enfatiza:",
 ["resultados e desempenho, orientação ao cidadão, flexibilização e descentralização.","rigidez hierárquica e controle prévio dos procedimentos.","formalismo como garantia da impessoalidade.","centralização das decisões e padronização absoluta."],
 "O modelo burocrático prioriza processos, hierarquia e legalidade estrita; a NGP, resultados e gestão por desempenho. Atenção: os dois coexistem na prática.","Adm. Pública, Aulas demo e 01")
Q("ADMP","No ciclo de políticas públicas, a etapa em que a decisão é transformada em ações concretas, com mobilização de recursos e agentes, é a:",
 ["implementação.","formulação de alternativas.","tomada de decisão.","avaliação."],
 "Ciclo (Secchi): identificação do problema, formação da agenda, formulação, tomada de decisão, implementação, avaliação e extinção.","Adm. Pública, Aulas 04–06")

# ============ LC 95 / REDAÇÃO OFICIAL ============
Q("LC95","Segundo a Lei Complementar nº 95/1998, a respeito do objeto e do âmbito de aplicação da lei:",
 ["excetuadas as codificações, cada lei tratará de um único objeto, sem matéria estranha a ele ou não vinculada por afinidade, pertinência ou conexão.","uma mesma lei deve tratar de todos os assuntos correlatos, para evitar dispersão normativa.","o mesmo assunto deve ser disciplinado por várias leis, para maior especificidade.","o objeto e o âmbito de aplicação devem constar apenas da ementa."],
 "LC 95/1998, art. 7º. O primeiro artigo indica o objeto e o âmbito de aplicação. O mesmo assunto não pode ser tratado por mais de uma lei, salvo lei que complemente a básica por remissão expressa.","LC 95/1998 (leitura da lei)")
Q("LC95","Segundo a LC 95/1998, a numeração e a identificação das unidades da lei seguem a forma:",
 ["Art. 9º e Art. 10; parágrafo único por extenso quando houver só um; incisos em algarismos romanos; alíneas em letras minúsculas; itens em algarismos arábicos.","Art. 9 e Art. 10º; incisos em algarismos arábicos; alíneas em letras maiúsculas.","Art. 9º e Art. 10º; “§ único” quando houver só um parágrafo; incisos em letras minúsculas.","Art. 9º e Art. 10; alíneas em algarismos romanos; itens em letras minúsculas."],
 "LC 95/1998, art. 10. Ordinal até o 9º e cardinal a partir do 10. Quando há só um parágrafo, escreve-se “Parágrafo único”, por extenso.","LC 95/1998 (leitura da lei)")
Q("LC95","Para acrescentar um novo artigo entre os arts. 5º e 6º de uma lei em vigor, a LC 95/1998 determina que se:",
 ["numere o novo dispositivo como Art. 5º-A, sem renumerar os demais, pois a renumeração é vedada.","renumerem todos os artigos seguintes, para manter a sequência.","numere como Art. 5º-bis, usando expressão em latim.","renumerem apenas os artigos seguintes que forem recomendáveis."],
 "LC 95/1998, art. 12, III, “b”: é vedada, mesmo quando recomendável, a renumeração; usa-se o número anterior seguido de letra maiúscula. Também é vedado reaproveitar o número de dispositivo revogado ou vetado.","LC 95/1998 (leitura da lei)")
Q("LC95","Segundo o Manual de Redação da Presidência da República (3ª edição), os fechos das comunicações oficiais são:",
 ["“Respeitosamente,” para autoridades superiores e “Atenciosamente,” para autoridades de mesma hierarquia ou inferiores.","“Atenciosamente,” somente para autoridades inferiores e “Cordialmente,” para as demais.","“Respeitosamente,” para todos, sem distinção.","“Sem mais para o momento,” em qualquer comunicação."],
 "Manual de Redação, 3ª ed., seção sobre fechos. O Manual unificou os fechos em dois. O pronome “Vossa Excelência” serve também para Prefeitos e Vereadores.","Redação Oficial, Aula única")

# ============ CONSTITUCIONAL / DIR. LEGISLATIVO ============
Q("CONST","Constitui crime de responsabilidade do Prefeito, segundo o art. 29-A da CF:",
 ["não enviar o repasse do duodécimo à Câmara até o dia 20 de cada mês.","efetuar o repasse do duodécimo até o dia 20 de cada mês.","enviar o duodécimo na proporção fixada na lei orçamentária.","enviar o duodécimo respeitando os limites do art. 29-A."],
 "CF, art. 29-A, § 2º (e LOM, arts. 65, XVII e 141). Também é crime repassar valor que supere os limites ou enviá-lo a menor que a proporção da lei orçamentária.","Dir. Constitucional, Aula 07 (Municípios)")
Q("CONST","O subsídio dos Vereadores é fixado:",
 ["pela própria Câmara Municipal, em cada legislatura para a subsequente, observados os limites constitucionais.","por lei de iniciativa do Prefeito, na mesma legislatura.","por decreto do Prefeito, a cada ano.","pelo Tribunal de Contas dos Municípios."],
 "CF, art. 29, VI e LOM, art. 35 (até 30 dias antes da eleição). Regimento, art. 102: se não aprovado nesse prazo, prevalece a resolução vigente.","Dir. Constitucional, Aula 07 (Municípios)")
Q("CONST","Quanto à competência legislativa dos Municípios, é correto afirmar que cabe a eles:",
 ["legislar sobre assuntos de interesse local e suplementar a legislação federal e a estadual no que couber.","legislar sobre direito civil e processual.","editar normas gerais de licitação e contratação.","legislar sobre direito penal local."],
 "CF, art. 30, I e II. Normas gerais de licitação são da União (art. 22, XXVII); o Município suplementa. Direito civil, processual e penal são privativos da União.","Dir. Legislativo, Aula 02")
Q("CONST","Sobre as prerrogativas dos Vereadores, é correto afirmar que:",
 ["são invioláveis por opiniões, palavras e votos no exercício do mandato e na circunscrição do Município, mas não têm imunidade formal (prisão e processo).","gozam de imunidade material e formal idênticas às dos Deputados Federais.","são invioláveis por suas palavras em qualquer lugar do território nacional.","não gozam de nenhuma inviolabilidade."],
 "CF, art. 29, VIII e LOM, art. 36. A inviolabilidade é só material, limitada ao exercício do mandato e à circunscrição do Município. Pegadinha: estender o regime dos parlamentares federais.","Dir. Constitucional, Aula 07")

# ============ PORTUGUÊS ============
Q("PORT","Assinale a alternativa correta quanto ao emprego do pronome relativo:",
 ["O vereador cujo projeto foi aprovado discursou na sessão.","O vereador cujo o projeto foi aprovado discursou na sessão.","O vereador que o projeto dele foi aprovado discursou na sessão.","O vereador do qual o projeto dele foi aprovado discursou na sessão."],
 "“Cujo” indica posse, concorda com o termo possuído e dispensa o artigo. As alternativas C e D repetem a ideia de posse (pleonasmo).","Português, Aula 02")
Q("PORT","Assinale a frase correta quanto ao emprego dos pronomes pessoais:",
 ["O relator trouxe os pareceres para eu analisar.","A Mesa deu o documento para mim assinar.","Entre eu e o colega não há divergência.","Não há nada contra eu fazer."],
 "Depois de preposição, usa-se mim; mas se o pronome é sujeito de um verbo no infinitivo, usa-se eu (“para eu analisar”). “Entre” pede mim: “entre mim e o colega”.","Português, Aula 02")
Q("PORT","Assinale a alternativa em que a concordância verbal está de acordo com a norma-padrão:",
 ["Houve dúvidas sobre a redação do artigo.","Haviam muitos projetos na pauta.","Fazem dois anos que a lei foi publicada.","Existe vários vereadores novos na Câmara."],
 "“Haver” no sentido de existir e “fazer” indicando tempo são impessoais (ficam no singular). “Existir” concorda com o sujeito: “existem vários vereadores”.","Português, Aula 07")
Q("PORT","Assinale a alternativa correta quanto à regência e ao uso da crase:",
 ["Os servidores aspiram à promoção na carreira.","O vereador assistiu a sessão inteira.","O Prefeito obedeceu as normas da lei.","Prefiro mais a negociação do que o conflito."],
 "“Aspirar” (almejar) pede preposição a: “à promoção”. “Assistir” (ver) também: “assistiu à sessão”. “Obedecer” pede a: “às normas”. “Preferir” dispensa “mais” e “do que”: “prefiro a negociação ao conflito”.","Português, Aula 08")
Q("PORT","Assinale a alternativa em que a regência do pronome relativo está correta:",
 ["Os documentos de que necessito estão sobre a mesa.","Os documentos que necessito estão sobre a mesa.","O cargo que aspiro exige concurso público.","A lei que me referi foi revogada."],
 "Se o verbo exige preposição, ela vem antes do relativo: “necessitar de” (de que), “aspirar a” (a que), “referir-se a” (a que).","Português, Aula 08")
Q("PORT","Assinale a alternativa em que a vírgula está empregada corretamente:",
 ["O projeto, que foi vetado pelo Prefeito, voltou à Câmara.","O relator da comissão, apresentou o parecer.","Os vereadores, aprovaram o projeto por unanimidade.","Quando o veto foi rejeitado o projeto foi promulgado."],
 "Nunca se separa sujeito de verbo com vírgula isolada (B e C). Na D, falta a vírgula após a oração adverbial antecipada. Na A, a oração explicativa vem entre vírgulas.","Português, Aula 06")
Q("PORT","No período “A proposta é inovadora; contudo, ainda carece de estudos de impacto”, a conjunção estabelece relação de:",
 ["oposição (adversidade), equivalendo a “porém” ou “todavia”.","conclusão, equivalendo a “portanto”.","causa, equivalendo a “porque”.","adição, equivalendo a “além disso”."],
 "“Contudo”, “porém”, “todavia”, “entretanto” e “no entanto” são adversativas. Concessão (embora, ainda que) é diferente: introduz oração subordinada.","Português, Aula 05")
Q("PORT","Complete a frase com a forma verbal correta: “Se os vereadores ____ o parecer, o projeto seguirá ao Plenário.”",
 ["mantiverem","mantêm","mantiveram","mantenham"],
 "“Se” + ideia de condição futura pede futuro do subjuntivo: “mantiverem” (de manter, derivado de ter: tiver, mantiver).","Português, Aula 04")
Q("PORT","Leia o texto: “A divulgação de pautas e votações pelas câmaras municipais não é favor ao cidadão: é obrigação decorrente do princípio da publicidade. Quando o acesso a essas informações exige conhecimento técnico, porém, a transparência é apenas formal. Disponibilizar dados sem torná-los compreensíveis cumpre a lei, mas não necessariamente cumpre sua finalidade.” Depreende-se do texto que:",
 ["divulgar informações é obrigação legal, mas a transparência efetiva requer que elas sejam compreensíveis.","a publicação de dados incompreensíveis descumpre a lei.","a transparência se esgota na divulgação de pautas e votações.","o cidadão deve ter conhecimento técnico para acompanhar as votações."],
 "A alternativa B contraria o texto (ele diz que cumpre a lei). C reduz a ideia central. D inverte a crítica do autor. Pegadinha: extrapolar ou afirmar o contrário do que está dito.","Português, Aula 11")

# ============ MATEMÁTICA ============
QF("MAT","Um tributo sofreu um aumento de 20% e, em seguida, um novo aumento de 10%. O aumento acumulado foi de:",
 ["30%","31%","32%","33%"],2,
 "Aumentos sucessivos se multiplicam: 1,20 × 1,10 = 1,32, ou seja, 32%. Pegadinha: somar os percentuais (30%).","Matemática, Aula 04")
QF("MAT","Quatro servidores analisam 200 processos em 5 dias, trabalhando no mesmo ritmo. Quantos servidores serão necessários para analisar 480 processos em 6 dias?",
 ["6","8","10","12"],1,
 "Cada servidor analisa 200 ÷ (4 × 5) = 10 processos por dia. Para 480 processos em 6 dias: 480 ÷ (6 × 10) = 8 servidores. Regra de três composta: grandezas diretamente proporcionais.","Matemática, Aula 03")
QF("MAT","Um capital de R$ 2.000,00 é aplicado por 2 meses à taxa de 10% ao mês. A diferença entre os juros obtidos no regime composto e no regime simples é de:",
 ["R$ 10,00","R$ 20,00","R$ 21,00","R$ 40,00"],1,
 "Composto: 2.000 × 1,21 = 2.420, juros de R$ 420. Simples: 2.000 × 0,10 × 2 = R$ 400. Diferença: R$ 20,00.","Matemática, Aulas 05–06")
QF("MAT","Uma verba de R$ 7.200,00 será dividida entre três setores, em partes diretamente proporcionais a 2, 3 e 4. O setor que receber a maior parte receberá:",
 ["R$ 2.400,00","R$ 2.800,00","R$ 3.200,00","R$ 3.600,00"],2,
 "Soma das partes: 2 + 3 + 4 = 9. Cada parte vale 7.200 ÷ 9 = R$ 800. A maior (4 partes) recebe 4 × 800 = R$ 3.200,00.","Matemática, Aula 02")

# ============ INFORMÁTICA ============
Q("INFO","Na planilha eletrônica, a fórmula =CONT.SE(B2:B11;\"&gt;100\") retorna:",
 ["a quantidade de células do intervalo B2:B11 com valor maior que 100.","a soma dos valores do intervalo B2:B11 maiores que 100.","a média dos valores maiores que 100.","a quantidade de células não vazias do intervalo."],
 "CONT.SE conta células que atendem a um critério. A soma condicional é SOMASE; a contagem de não vazias é CONT.VALORES.","Informática, Aula 05")
Q("INFO","Na célula C2 foi digitada a fórmula =B2*$E$1. Ao copiar C2 para C3, a fórmula resultante será:",
 ["=B3*$E$1","=B3*E2","=B2*$E$1","=C3*$E$2"],
 "O sinal $ trava a referência (absoluta): $E$1 não muda ao copiar. B2 é relativa e passa a B3.","Informática, Aula 05")
Q("INFO","Em uma mensagem de correio eletrônico, os destinatários inseridos no campo CCO (cópia oculta):",
 ["recebem a mensagem sem que os demais destinatários vejam seus endereços.","são visíveis para todos os demais destinatários.","não recebem a mensagem, apenas o registro dela.","só podem responder ao remetente, e nunca a todos."],
 "CC = cópia visível; CCO = cópia oculta, útil para preservar a privacidade. Quem está em CCO recebe normalmente.","Informática, Aula 02")
Q("INFO","O tipo de malware que criptografa os arquivos do usuário e exige pagamento para devolver o acesso é o:",
 ["ransomware.","spyware.","adware.","keylogger."],
 "Ransomware “sequestra” dados mediante resgate. Spyware espia; adware exibe propaganda; keylogger registra teclas digitadas. Melhor defesa: backup atualizado e offline.","Informática, Aula 04")

BLOCKS = [
 ("LOM","Legislação Específica: Lei Orgânica do Município de Rio Verde","MA"),
 ("REG","Legislação Específica: Regimento Interno (Resolução nº 33/2000)","MA"),
 ("PL","Processo Legislativo (CF, LOM e jurisprudência)","MA"),
 ("CC","Controle de Constitucionalidade","MA"),
 ("LIC","Licitações e Contratos: Lei nº 14.133/2021","MA"),
 ("DADM","Direito Administrativo: atos, poderes, princípios, agentes, improbidade e bens","A"),
 ("ADMP","Administração Pública: orçamento, governança, NGP e políticas públicas","A"),
 ("LC95","Técnica Legislativa (LC 95/1998) e Redação Oficial","MA"),
 ("CONST","Direito Constitucional e Direito Legislativo: Municípios e competências","M"),
 ("PORT","Língua Portuguesa","MA"),
 ("MAT","Matemática","A"),
 ("INFO","Informática","MA"),
]
