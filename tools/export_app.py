# -*- coding: utf-8 -*-
import random, json, re, sys, os
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import data as D1, data2 as D2, data3 as D3, data4 as D4
import conteudo_v1 as C1, conteudo_v2 as C2, conteudo_v3 as C3

# ===== Disciplinas e tópicos conforme o painel do curso (30 tópicos, com prioridade) =====
P=["Muito alta","Alta","Média","Baixa","Muito baixa"]
T30=[
(1,"Direito Constitucional","Sistemas e Espécies de Controle de Constitucionalidade",0),
(2,"Direito Administrativo","Contratos e Licitações Públicas",0),
(3,"Administração Pública","Planejamento Governamental",0),
(4,"Processo Legislativo e Atividade Parlamentar","Espécies Normativas e Proposições Legislativas",0),
(5,"Técnica Legislativa e Redação Oficial","Fundamentos da Técnica Legislativa e Lei Complementar nº 95/1998",0),
(6,"Legislação de Rio Verde","Regimento Interno da Câmara Municipal de Rio Verde",0),
(7,"Direito Constitucional","Separação de Poderes e o Funcionamento do Poder Legislativo",1),
(8,"Direito Administrativo","Atos e Poderes Administrativos",1),
(9,"Administração Pública","Governança, Transparência e Accountability",1),
(10,"Processo Legislativo e Atividade Parlamentar","Iniciativa e Tramitação de Proposições",1),
(11,"Processo Legislativo e Atividade Parlamentar","Deliberação, Sanção, Veto e Promulgação",1),
(12,"Técnica Legislativa e Redação Oficial","Elaboração, Alteração e Consolidação de Atos Normativos",1),
(13,"Legislação de Rio Verde","Lei Orgânica do Município de Rio Verde",1),
(14,"Legislação de Rio Verde","Resolução nº 33/2000 e Dispositivos Regimentais Específicos",1),
(15,"Direito Constitucional","Teoria Geral e Aplicação dos Direitos e Garantias Fundamentais",2),
(16,"Direito Constitucional","Organização Político-Administrativa e o Regime dos Municípios",2),
(17,"Direito Administrativo","Princípios e Organização da Administração Pública",2),
(18,"Direito Administrativo","Processo Administrativo e Agentes Públicos",2),
(19,"Administração Pública","Organização Governamental e Gestão Pública",2),
(20,"Administração Pública","Ciclo e Formulação de Políticas Públicas",2),
(21,"Processo Legislativo e Atividade Parlamentar","Competências e Funções da Câmara Municipal",2),
(22,"Processo Legislativo e Atividade Parlamentar","Sessões Legislativas, Comissões e Mesa Diretora",2),
(23,"Técnica Legislativa e Redação Oficial","Redação Oficial e Redação Legislativa",2),
(24,"Legislação de Rio Verde","Revisão da Lei Orgânica e Normas Institucionais do Município",2),
(25,"Legislação de Rio Verde","Estrutura Organizacional da Câmara (Lei 7.434/2023)",2),
(26,"Direito Administrativo","Serviços, Controle, Improbidade e Bens Públicos",3),
(27,"Processo Legislativo e Atividade Parlamentar","Fiscalização, Controle e Funções Institucionais da Câmara",3),
(28,"Processo Legislativo e Atividade Parlamentar","Controle de Constitucionalidade e Jurisprudência no Processo Legislativo",3),
(29,"Legislação de Rio Verde","Plano de Cargos e Remuneração (Lei 7.435/2023)",3),
(30,"Processo Legislativo e Atividade Parlamentar","Hermenêutica Jurídica e Competências Legislativas",4),
(31,"Língua Portuguesa","Língua Portuguesa",0),
(32,"Matemática","Matemática",1),
(33,"Informática","Informática",0),
]
TOP={t[0]:dict(id=t[0],disc=t[1],nome=t[2],prio=t[3]) for t in T30}

def shuffle(QS,seed):
    rng=random.Random(seed); N=len(QS); tg=([0,1,2,3]*(N//4+1))[:N]; rng.shuffle(tg)
    for q,t in zip(QS,tg):
        if q.get("fixed"): q["final"]=list(q["opts"]); q["ci"]=q["ans"]
        else:
            w=q["opts"][1:]; q["final"]=w[:t]+[q["opts"][0]]+w[t:]; q["ci"]=t
shuffle(D1.QS,11); shuffle(D2.QS,23); shuffle(D3.QS,37); shuffle(D4.QS,41)

def rx(p,s): return re.search(p,s,re.I) is not None
def c1_topic(q):
    b=q["b"]; s=q["stem"]+" "+q["why"]
    if b=="LOM": return 13
    if b=="REG": return 6
    if b=="PL": return 10 if not rx("veto|sanç|promulga",s) else 11
    if b=="CC": return 1
    if b=="LIC": return 2
    if b=="DADM":
        if rx("improbidade|bens públicos|serviço público|controle",s): return 26
        if rx("princíp|administração direta|indireta|autarquia",s): return 17
        if rx("servidor|agente|processo administrativo",s): return 18
        return 8
    if b=="ADMP":
        if rx("PPA|LDO|LOA|orçament|planejamento",s): return 3
        if rx("governan|transparên|accountab",s): return 9
        if rx("política pública|ciclo",s): return 20
        return 19
    if b=="LC95": return 23 if rx("redação oficial|ofício|memorando|pronome de tratamento",s) else 5
    if b=="CONST":
        if rx("direitos|garantias",s): return 15
        if rx("separação|Legislativo",s): return 7
        return 16
    return {"PORT":31,"MAT":32,"INFO":33}[b]

V1={1:10,2:10,3:10,4:10,5:10,6:10,7:10,8:10,9:10,10:10,11:10,12:11,13:27,14:22,15:14,16:14,17:14,18:25,19:29}
V2={i:22 for i in range(1,16)}; V2.update({9:6,10:6,11:6})
V3={1:16,2:16,3:16,4:13,5:21,6:22,7:22,8:21,9:13,10:13,11:10,12:11,13:27,14:13,15:13,16:18,17:13,18:3}

out=[]; temas={}
for q in D1.QS:
    pass
for i,q in enumerate(D1.QS,1):
    out.append(dict(id=f"c1-{i:02d}",src="Caderno 1",num=i,top=c1_topic(q),tema=None,stem=q["stem"],opts=q["final"],ci=q["ci"],why=q["why"],study=q["study"]))
def add(QS,TOP_,MAP,src,tag):
    for ti,(title,fonte,items,(a,b)) in enumerate(TOP_,1):
        tid=f"{tag}-{ti:02d}"
        temas[tid]=dict(id=tid,src=src,titulo=title,fonte=fonte,itens=items,top=MAP[ti])
        for n in range(a,b+1):
            q=QS[n-1]
            out.append(dict(id=f"{tag}-q{n:03d}",src=src,num=n,top=MAP[ti],tema=tid,stem=q["stem"],opts=q["final"],ci=q["ci"],why=q["why"],study=q["study"]))
add(D2.QS,C1.TOPICS,V1,"Apostila Vol. 1","v1")
add(D3.QS,C2.TOPICS,V2,"Apostila Vol. 2","v2")
add(D4.QS,C3.TOPICS,V3,"Apostila Vol. 3","v3")
for q in out:
    assert len(q["opts"])==4 and 0<=q["ci"]<4
    assert len(set(q["opts"]))==4, q["id"]
from collections import Counter
print(len(out),Counter(q["src"] for q in out)); print(Counter(TOP[q["top"]]["disc"] for q in out)); print(Counter(P[TOP[q["top"]]["prio"]] for q in out)); print(Counter("ABCD"[q["ci"]] for q in out))
js="window.DATA="+json.dumps(dict(prio=P,topicos=list(TOP.values()),temas=list(temas.values()),questoes=out),ensure_ascii=False)+";\n"
open(os.path.join(HERE,"..","data.js"),"w").write(js); print(len(js)//1024,"KB")
