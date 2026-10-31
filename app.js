/* Estudo Analista Legislativo | Câmara de Rio Verde (GO) | prova 08/11/2026
   Tudo roda no navegador. Progresso em localStorage (+ exportar/importar). Sem servidor. */
(function(){
'use strict';
const D=window.DATA, Q=D.questoes, PRIO=D.prio;
const topById={}; D.topicos.forEach(t=>topById[t.id]=t);
const temaById={}; D.temas.forEach(t=>temaById[t.id]=t);
const qById={}; Q.forEach(q=>qById[q.id]=q);
const DISC=['Direito Administrativo','Direito Constitucional','Administração Pública','Processo Legislativo e Atividade Parlamentar','Técnica Legislativa e Redação Oficial','Legislação de Rio Verde','Língua Portuguesa','Matemática','Informática'];
const SRC=['Caderno 1','Apostila Vol. 1','Apostila Vol. 2','Apostila Vol. 3'];
const EXAM=new Date(2026,10,8,8,0,0);
const KEY='ael_v1', DAY=86400000, INTERVALS=[0,1,2,4,7,14];
const $=s=>document.querySelector(s);
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const pct=(a,b)=>b?Math.round(100*a/b):0;
const L='ABCD';

/* ---------- estado persistente ---------- */
function blank(){return {at:{},srs:{},ai:{},bm:{},cfg:{key:'',model:'claude-sonnet-5-5'},created:Date.now()};}
function load(){try{const r=localStorage.getItem(KEY);if(r){const s=JSON.parse(r);return Object.assign(blank(),s);}}catch(e){}return blank();}
let S=load();
function save(){try{localStorage.setItem(KEY,JSON.stringify(S));}catch(e){toast('Não consegui salvar no navegador. Exporte um backup.');}}
function toast(m){const t=$('#toast');t.textContent=m;t.classList.add('on');clearTimeout(toast.h);toast.h=setTimeout(()=>t.classList.remove('on'),2800);}

/* ---------- estatísticas ---------- */
function st(id){
  const a=S.at[id]||[]; let ok=0,streak=0;
  a.forEach(x=>{if(x.ok)ok++;});
  for(let i=a.length-1;i>=0&&a[i].ok;i--)streak++;
  return {n:a.length,ok,err:a.length-ok,streak,last:a.length?a[a.length-1]:null};
}
const inNotebook=id=>{const s=st(id);return s.err>0&&s.streak<2;};
const isWeak=id=>{const s=st(id);return s.err>=2&&s.streak<3||(s.n>=3&&s.err/s.n>=.5&&s.streak<3);};
const isDue=id=>{const r=S.srs[id];return r&&r.due<=Date.now();};
const dueIds=()=>Q.filter(q=>isDue(q.id)).map(q=>q.id);
function record(id,sel,ok,conf,mode){
  (S.at[id]=S.at[id]||[]).push({t:Date.now(),ok,sel,conf:conf||null,mode:mode||'p'});
  const r=S.srs[id]||{box:0,due:0};
  r.box=ok?Math.min(r.box+1,INTERVALS.length-1):0;
  r.due=r.box===0?Date.now()+10*60000:Date.now()+INTERVALS[r.box]*DAY;
  S.srs[id]=r; save();
}
function streakDays(){
  const days=new Set(); Object.values(S.at).forEach(a=>a.forEach(x=>days.add(new Date(x.t).toDateString())));
  let n=0,d=new Date(); if(!days.has(d.toDateString()))d=new Date(Date.now()-DAY);
  while(days.has(d.toDateString())){n++;d=new Date(d.getTime()-DAY);} return n;
}
function todayCount(){const d=new Date().toDateString();let n=0;Object.values(S.at).forEach(a=>a.forEach(x=>{if(new Date(x.t).toDateString()===d)n++;}));return n;}
function agg(filter){let n=0,ok=0,seen=0,tot=0;Q.forEach(q=>{if(!filter(q))return;tot++;const s=st(q.id);n+=s.n;ok+=s.ok;if(s.n)seen++;});return {tot,seen,n,ok};}

/* ---------- sessão de questões ---------- */
let SES=null;
function startSession(ids,opt){
  opt=opt||{}; if(!ids.length){toast('Nenhuma questão com esse filtro.');return;}
  SES={ids:ids.slice(),i:0,title:opt.title||'Prática',exam:!!opt.exam,ans:{},rev:{},conf:null,start:Date.now(),limit:opt.exam?ids.length*120000:0,ok:0,done:false};
  if(SES.exam)SES.timer=setInterval(tick,1000);
  location.hash='#/q';
}
function tick(){
  if(!SES||!SES.exam||SES.done){clearInterval(SES&&SES.timer);return;}
  const left=SES.limit-(Date.now()-SES.start); const el=$('#clock');
  if(el)el.textContent=fmt(Math.max(0,left));
  if(left<=0)finishExam();
}
const fmt=ms=>{const s=Math.floor(ms/1000);return String(Math.floor(s/60)).padStart(2,'0')+':'+String(s%60).padStart(2,'0');};
function shuffle(a){a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}

/* ---------- seleção por filtro ---------- */
const F={disc:'',top:'',prio:'',src:'',status:'all',n:20};
function pick(f0){
  const f=Object.assign({disc:'',top:'',prio:'',src:'',status:'all'},f0);
  let ids=Q.filter(q=>{
    const t=topById[q.top];
    if(f.disc&&t.disc!==f.disc)return false;
    if(f.top&&String(q.top)!==String(f.top))return false;
    if(f.prio!==''&&String(t.prio)!==String(f.prio))return false;
    if(f.src&&q.src!==f.src)return false;
    const s=st(q.id);
    if(f.status==='new'&&s.n)return false;
    if(f.status==='wrong'&&!inNotebook(q.id))return false;
    if(f.status==='weak'&&!isWeak(q.id))return false;
    if(f.status==='due'&&!isDue(q.id))return false;
    if(f.status==='bm'&&!S.bm[q.id])return false;
    return true;}).map(q=>q.id);
  return ids;
}

/* ---------- views ---------- */
const V=$('#view');
function badge(p){return `<span class="bd p${p}">${PRIO[p]}</span>`;}
function bar(a,b,cls){return `<div class="bar"><i class="${cls||''}" style="width:${pct(a,b)}%"></i></div>`;}
function nav(){
  const h=location.hash||'#/';
  document.querySelectorAll('nav a').forEach(a=>a.classList.toggle('on',h===a.getAttribute('href')||(a.getAttribute('href')!=='#/'&&h.startsWith(a.getAttribute('href')))));
  const nb=Q.filter(q=>inNotebook(q.id)).length, due=dueIds().length;
  $('#nb-erros').textContent=nb||''; $('#nb-rev').textContent=due||'';
}
function route(){
  nav(); const h=location.hash||'#/'; window.scrollTo(0,0);
  if(h==='#/')return home();
  if(h==='#/praticar')return praticar();
  if(h==='#/q')return question();
  if(h==='#/erros')return erros();
  if(h==='#/revisao')return revisao();
  if(h==='#/simulado')return simulado();
  if(h==='#/stats')return stats();
  if(h==='#/config')return config();
  if(h.startsWith('#/conteudo'))return conteudo(h.split('/')[2]);
  home();
}

function home(){
  const days=Math.ceil((EXAM-Date.now())/DAY), due=dueIds().length;
  const weak=Q.filter(q=>isWeak(q.id)), nb=Q.filter(q=>inNotebook(q.id));
  const all=agg(()=>true);
  let h=`<section class="hero"><div><h1>Analista Legislativo</h1><p class="mut">Câmara de Rio Verde (GO) · prova em <b>${days>0?days+' dias':'breve'}</b> (08/11/2026)</p></div>
   <div class="kpis"><div><b>${all.n}</b><small>respostas</small></div><div><b>${pct(all.ok,all.n)}%</b><small>acertos</small></div><div><b>${streakDays()}</b><small>dias seguidos</small></div><div><b>${todayCount()}</b><small>hoje</small></div></div></section>`;
  if(weak.length){
    h+=`<section class="alert"><b>⚠ Atenção: ${weak.length} ${weak.length>1?'questões que você erra':'questão que você erra'} com frequência.</b>
     <p>Reincidência é o que mais derruba nota. Resolva essas agora, antes de seguir em frente.</p>
     <button class="btn danger" data-act="weak">Treinar minhas reincidentes</button></section>`;
  }
  h+=`<section class="actions">
   <button class="card act" data-act="due"><b>${due}</b><span>Revisão do dia</span><small>repetição espaçada</small></button>
   <button class="card act" data-act="notebook"><b>${nb.length}</b><span>Caderno de erros</span><small>até acertar 2 seguidas</small></button>
   <a class="card act" href="#/praticar"><b>${Q.length}</b><span>Praticar</span><small>filtre por disciplina e grau</small></a>
   <a class="card act" href="#/simulado"><b>⏱</b><span>Simulado</span><small>sem gabarito até o fim</small></a></section>`;
  const wt=weakTopics();
  if(wt.length){h+=`<section><h2>Seus pontos fracos</h2><div class="chips">`+wt.map(x=>`<a class="chip warn" href="#/conteudo/T${x.t.id}">${esc(x.t.nome)} · ${x.pc}% de acertos</a>`).join('')+`</div></section>`;}
  h+=`<section><h2>Por disciplina (edital)</h2><div class="chips" id="grau">
    <button class="chip ${F.prio===''?'on':''}" data-g="">Todos os graus</button>`+PRIO.map((p,i)=>Q.some(q=>topById[q.top].prio===i)?`<button class="chip ${String(F.prio)===String(i)?'on':''}" data-g="${i}">${p}</button>`:'').join('')+`</div>`;
  DISC.forEach(d=>{
    const tops=D.topicos.filter(t=>t.disc===d&&(F.prio===''||String(t.prio)===String(F.prio))&&Q.some(q=>q.top===t.id)).sort((a,b)=>a.prio-b.prio||a.id-b.id);
    if(!tops.length)return;
    const a=agg(q=>topById[q.top].disc===d&&(F.prio===''||String(topById[q.top].prio)===String(F.prio)));
    h+=`<details class="disc" ${tops.length&&F.prio!==''?'open':''}><summary><span class="dn">${esc(d)}</span><span class="mut">${a.seen}/${a.tot} vistas · ${pct(a.ok,a.n)}% acertos</span></summary>
      ${bar(a.seen,a.tot)}<div class="tops">`;
    tops.forEach(t=>{
      const g=agg(q=>q.top===t.id), hasC=D.temas.some(x=>x.top===t.id);
      h+=`<div class="trow"><div class="tin"><div>${badge(t.prio)} <b>${esc(t.nome)}</b></div>
        <small class="mut">${g.seen}/${g.tot} vistas · ${g.n?pct(g.ok,g.n)+'% de acertos':'sem respostas'}</small>${bar(g.ok,g.n||1,g.n&&pct(g.ok,g.n)<60?'bad':'')}</div>
        <div class="tbtn"><button class="btn sm" data-top="${t.id}">Praticar</button>${hasC?`<a class="btn sm ghost" href="#/conteudo/T${t.id}">Resumo</a>`:''}</div></div>`;
    });
    h+=`</div></details>`;
  });
  h+=`</section>`;
  V.innerHTML=h;
  V.querySelectorAll('[data-g]').forEach(b=>b.onclick=()=>{F.prio=b.dataset.g;home();});
  V.querySelectorAll('[data-top]').forEach(b=>b.onclick=()=>{const ids=shuffle(pick({top:b.dataset.top,status:'all'}));startSession(ids.slice(0,30),{title:topById[b.dataset.top].nome});});
  V.querySelectorAll('[data-act]').forEach(b=>b.onclick=()=>{
    const a=b.dataset.act;
    if(a==='weak')startSession(shuffle(Q.filter(q=>isWeak(q.id)).map(q=>q.id)),{title:'Reincidentes'});
    if(a==='due')startSession(shuffle(dueIds()),{title:'Revisão do dia'});
    if(a==='notebook')location.hash='#/erros';
  });
}
function weakTopics(){
  const out=[];D.topicos.forEach(t=>{const g=agg(q=>q.top===t.id);if(g.n>=4&&pct(g.ok,g.n)<65)out.push({t,pc:pct(g.ok,g.n)});});
  return out.sort((a,b)=>a.pc-b.pc).slice(0,6);
}

function sel(name,opts,val){return `<select data-f="${name}">`+opts.map(o=>`<option value="${esc(o[0])}" ${String(val)===String(o[0])?'selected':''}>${esc(o[1])}</option>`).join('')+`</select>`;}
function praticar(){
  const dOpts=[['','Todas as disciplinas']].concat(DISC.map(d=>[d,d]));
  const tOpts=[['','Todos os tópicos']].concat(D.topicos.filter(t=>(!F.disc||t.disc===F.disc)&&Q.some(q=>q.top===t.id)).sort((a,b)=>a.prio-b.prio||a.id-b.id).map(t=>[t.id,`[${PRIO[t.prio]}] ${t.nome}`]));
  const pOpts=[['','Todos os graus']].concat(PRIO.map((p,i)=>[i,p]));
  const sOpts=[['','Todas as origens']].concat(SRC.map(s=>[s,s]));
  const stOpts=[['all','Todas'],['new','Ainda não respondidas'],['wrong','Caderno de erros'],['weak','Reincidentes'],['due','Revisão pendente'],['bm','Marcadas ★']];
  const ids=pick(F);
  V.innerHTML=`<h2>Praticar</h2><div class="card form">
   <label>Disciplina ${sel('disc',dOpts,F.disc)}</label><label>Tópico ${sel('top',tOpts,F.top)}</label>
   <label>Grau (prioridade no edital) ${sel('prio',pOpts,F.prio)}</label><label>Origem ${sel('src',sOpts,F.src)}</label>
   <label>Situação ${sel('status',stOpts,F.status)}</label>
   <label>Quantidade ${sel('n',[[10,'10'],[20,'20'],[30,'30'],[50,'50'],[999,'Todas']],F.n)}</label>
   <p><b>${ids.length}</b> questões disponíveis.</p><button class="btn" id="go">Começar</button></div>`;
  V.querySelectorAll('[data-f]').forEach(s=>s.onchange=()=>{F[s.dataset.f]=s.value;if(s.dataset.f==='disc')F.top='';praticar();});
  $('#go').onclick=()=>startSession(shuffle(ids).slice(0,+F.n),{title:'Prática'});
}

function question(){
  if(!SES){location.hash='#/';return;}
  if(SES.done)return resultado();
  const id=SES.ids[SES.i], q=qById[id], t=topById[q.top], s=st(id), exam=SES.exam;
  const rev=SES.rev[id], chosen=SES.ans[id];
  let h=`<div class="qtop"><span>${esc(SES.title)} · <b>${SES.i+1}/${SES.ids.length}</b></span>${exam?`<span class="clock" id="clock">${fmt(Math.max(0,SES.limit-(Date.now()-SES.start)))}</span>`:''}<button class="star ${S.bm[id]?'on':''}" id="bm" title="Marcar">★</button></div>
   <div class="meta">${badge(t.prio)}<span class="tag">${esc(t.disc)}</span><span class="tag">${esc(t.nome)}</span><span class="tag mut">${esc(q.src)} · ${q.num}</span></div>`;
  if(!exam&&s.err>=1){
    h+=`<div class="${isWeak(id)?'alert':'note'} slim">${isWeak(id)?'⚠ <b>Reincidente:</b> ':''}você já errou esta questão <b>${s.err}×</b> em ${s.n} tentativa${s.n>1?'s':''}${s.streak?` (acertou as últimas ${s.streak})`:''}.</div>`;
  }
  h+=`<div class="stem">${esc(q.stem)}</div><div class="opts">`;
  q.opts.forEach((o,i)=>{
    let c='opt';
    if(rev){if(i===q.ci)c+=' right';else if(i===chosen)c+=' wrong';else c+=' dim';}
    else if(i===chosen)c+=' pick';
    h+=`<button class="${c}" data-i="${i}" ${rev?'disabled':''}><b>${L[i]}</b><span>${esc(o)}</span></button>`;
  });
  h+=`</div>`;
  if(!rev){
    h+=`<div class="conf"><span class="mut">Confiança:</span>`+['C','D','X'].map(c=>`<button class="chip ${SES.conf===c?'on':''}" data-c="${c}">${{C:'Certeza',D:'Dúvida',X:'Chute'}[c]}</button>`).join('')+`</div>
     <div class="row"><button class="btn" id="ok" ${chosen===undefined?'disabled':''}>${exam?'Salvar resposta':'Responder'}</button>
     ${exam&&SES.i<SES.ids.length-1?'':''}</div>`;
  }else{
    const right=chosen===q.ci;
    h+=`<div class="fb ${right?'okk':'bad'}"><b>${right?'✔ Correto!':'✘ Errou. Gabarito: '+L[q.ci]}</b></div>
     <div class="why"><b>Comentário:</b> ${esc(q.why)}</div><div class="study">Se errou, estude: ${esc(q.study)}${q.tema?` · <a href="#/conteudo/${q.tema}">ler resumo do tema</a>`:''}</div>
     <div id="ai">${aiBlock(q)}</div>`;
  }
  h+=`<div class="row nav2"><button class="btn ghost" id="prev" ${SES.i===0?'disabled':''}>←</button>
   ${exam?`<button class="btn danger" id="fin">Encerrar simulado</button>`:`<button class="btn ghost" id="exit">Sair</button>`}
   <button class="btn" id="next">${SES.i===SES.ids.length-1?(exam?'Fim':'Concluir'):'Próxima →'}</button></div>`;
  V.innerHTML=h;
  V.querySelectorAll('.opt').forEach(b=>b.onclick=()=>{if(SES.rev[id])return;SES.ans[id]=+b.dataset.i;
    if(exam)SES.rev[id]=false; question();});
  V.querySelectorAll('[data-c]').forEach(b=>b.onclick=()=>{SES.conf=SES.conf===b.dataset.c?null:b.dataset.c;question();});
  const ok=$('#ok');
  if(ok)ok.onclick=()=>{
    if(exam){toast('Resposta salva.');if(SES.i<SES.ids.length-1){SES.i++;}question();return;}
    const right=SES.ans[id]===q.ci; record(id,SES.ans[id],right,SES.conf,'p'); if(right)SES.ok++; SES.rev[id]=true; SES.conf=null; nav(); question();
  };
  $('#bm').onclick=()=>{if(S.bm[id])delete S.bm[id];else S.bm[id]=1;save();question();};
  $('#prev').onclick=()=>{if(SES.i>0){SES.i--;SES.conf=null;question();}};
  $('#next').onclick=()=>{
    if(!exam&&!SES.rev[id]&&SES.ans[id]===undefined){toast('Escolha uma alternativa.');return;}
    if(SES.i<SES.ids.length-1){SES.i++;SES.conf=null;question();}
    else if(exam)finishExam(); else {SES.done=true;question();}
  };
  const f=$('#fin');if(f)f.onclick=()=>{if(confirm('Encerrar e corrigir o simulado agora?'))finishExam();};
  const e=$('#exit');if(e)e.onclick=()=>{if(confirm('Sair desta sessão? O que você respondeu já está salvo.')){SES.done=true;question();}};
  const ex=$('#aiBtn');if(ex)ex.onclick=()=>explain(q);
}
function finishExam(){
  if(!SES||SES.done)return; clearInterval(SES.timer);
  SES.ids.forEach(id=>{const q=qById[id],a=SES.ans[id];const ok=a===q.ci;record(id,a===undefined?-1:a,ok,null,'s');if(ok)SES.ok++;SES.rev[id]=true;});
  SES.done=true; question();
}
function resultado(){
  const n=SES.ids.length, ok=SES.ids.filter(id=>{const a=SES.ans[id];return a===qById[id].ci;}).length;
  const by={};SES.ids.forEach(id=>{const q=qById[id],d=topById[q.top].disc;(by[d]=by[d]||[0,0]);by[d][1]++;if(SES.ans[id]===q.ci)by[d][0]++;});
  const wrong=SES.ids.filter(id=>SES.ans[id]!==qById[id].ci);
  let h=`<h2>Resultado: ${esc(SES.title)}</h2><div class="hero"><div class="kpis"><div><b>${ok}/${n}</b><small>acertos</small></div><div><b>${pct(ok,n)}%</b><small>aproveitamento</small></div><div><b>${fmt(Date.now()-SES.start)}</b><small>tempo</small></div></div></div>
   <div class="card"><h3>Por disciplina</h3>`+Object.keys(by).map(d=>`<div class="trow"><div class="tin"><b>${esc(d)}</b><small class="mut">${by[d][0]}/${by[d][1]}</small>${bar(by[d][0],by[d][1],pct(by[d][0],by[d][1])<60?'bad':'')}</div></div>`).join('')+`</div>`;
  if(wrong.length){h+=`<div class="note slim">${wrong.length} erro${wrong.length>1?'s foram':' foi'} para o seu <b>Caderno de erros</b> e entra${wrong.length>1?'m':''} na revisão espaçada.</div><div class="row"><button class="btn" id="re">Refazer os erros</button><a class="btn ghost" href="#/erros">Abrir caderno</a></div>`;}
  h+=`<div class="row"><a class="btn ghost" href="#/">Início</a></div>`;
  V.innerHTML=h; const re=$('#re');if(re)re.onclick=()=>startSession(wrong,{title:'Refazendo erros'});
  clearInterval(SES.timer);
}

/* ---------- caderno de erros / revisão / simulado ---------- */
function erros(){
  const list=Q.filter(q=>st(q.id).err>0).map(q=>({q,s:st(q.id)})).sort((a,b)=>(isWeak(b.q.id)-isWeak(a.q.id))||(b.s.err-a.s.err));
  const open=list.filter(x=>inNotebook(x.q.id)), done=list.filter(x=>!inNotebook(x.q.id));
  let h=`<h2>Caderno de erros</h2><p class="mut">Cada erro entra aqui sozinho. A questão sai quando você acerta <b>2 vezes seguidas</b>. As reincidentes aparecem primeiro.</p>
   <div class="row"><button class="btn" id="all" ${open.length?'':'disabled'}>Refazer todas (${open.length})</button><button class="btn danger" id="wk" ${open.some(x=>isWeak(x.q.id))?'':'disabled'}>Só reincidentes</button></div>`;
  if(!open.length)h+=`<div class="card">Nenhum erro pendente. Continue praticando.</div>`;
  open.forEach(x=>{const t=topById[x.q.top];h+=`<div class="card er ${isWeak(x.q.id)?'weak':''}"><div class="meta">${badge(t.prio)}<span class="tag">${esc(t.nome)}</span>${isWeak(x.q.id)?'<span class="tag red">Reincidente</span>':''}<span class="tag mut">${x.s.err}× errada · ${x.s.n} tent.</span></div>
    <div class="stem sm">${esc(x.q.stem)}</div><button class="btn sm" data-r="${x.q.id}">Refazer</button></div>`;});
  if(done.length){h+=`<details><summary>Já dominadas (${done.length})</summary>`+done.map(x=>`<div class="card er"><div class="stem sm">${esc(x.q.stem)}</div><small class="mut">${x.s.err}× errada · última sequência de acertos: ${x.s.streak}</small></div>`).join('')+`</details>`;}
  V.innerHTML=h;
  $('#all').onclick=()=>startSession(shuffle(open.map(x=>x.q.id)),{title:'Caderno de erros'});
  $('#wk').onclick=()=>startSession(shuffle(open.filter(x=>isWeak(x.q.id)).map(x=>x.q.id)),{title:'Reincidentes'});
  V.querySelectorAll('[data-r]').forEach(b=>b.onclick=()=>startSession([b.dataset.r],{title:'Refazendo'}));
}
function revisao(){
  const due=dueIds(), sched=Object.keys(S.srs).filter(id=>S.srs[id].due>Date.now()).length;
  V.innerHTML=`<h2>Revisão espaçada</h2><p class="mut">Questão errada volta em minutos. Acertou, volta em 1, 2, 4, 7 e 14 dias. Quanto mais você acerta, mais espaçada fica.</p>
   <div class="hero"><div class="kpis"><div><b>${due.length}</b><small>para hoje</small></div><div><b>${sched}</b><small>agendadas</small></div></div></div>
   <div class="row"><button class="btn" id="go" ${due.length?'':'disabled'}>Começar revisão</button></div>${due.length?'':'<p class="mut">Nada pendente agora. Pratique para alimentar a revisão.</p>'}`;
  $('#go').onclick=()=>startSession(shuffle(due).slice(0,40),{title:'Revisão do dia'});
}
function simulado(){
  const p=F.simN||30;
  V.innerHTML=`<h2>Simulado</h2><div class="card form"><p class="mut">Questões sorteadas de todas as disciplinas, com mais peso para os graus Muito alta e Alta. Tempo: 2 min por questão. O gabarito só aparece ao final; os erros vão para o caderno.</p>
   <label>Número de questões ${sel('simN',[[20,'20'],[30,'30'],[40,'40'],[60,'60']],p)}</label><button class="btn" id="go">Iniciar</button></div>`;
  V.querySelector('[data-f]').onchange=e=>{F.simN=+e.target.value;simulado();};
  $('#go').onclick=()=>{
    const w=Q.map(q=>({id:q.id,w:[5,4,2.5,1.5,.5][topById[q.top].prio]*(1+Math.min(st(q.id).err,3)*.4)*(st(q.id).n?1:1.2)*Math.random()}));
    w.sort((a,b)=>b.w-a.w); startSession(w.slice(0,p).map(x=>x.id),{title:'Simulado',exam:true});
  };
}

/* ---------- estatísticas ---------- */
function stats(){
  let h=`<h2>Desempenho</h2><div class="card"><h3>Por grau (prioridade no edital)</h3>`;
  PRIO.forEach((p,i)=>{const a=agg(q=>topById[q.top].prio===i);if(!a.tot)return;h+=`<div class="trow"><div class="tin"><div>${badge(i)} <small class="mut">${a.seen}/${a.tot} vistas · ${a.n?pct(a.ok,a.n)+'%':'—'}</small></div>${bar(a.ok,a.n||1,a.n&&pct(a.ok,a.n)<60?'bad':'')}</div></div>`;});
  h+=`</div><div class="card"><h3>Por origem</h3>`;
  SRC.forEach(s=>{const a=agg(q=>q.src===s);h+=`<div class="trow"><div class="tin"><b>${s}</b> <small class="mut">${a.seen}/${a.tot} vistas · ${a.n?pct(a.ok,a.n)+'%':'—'}</small>${bar(a.ok,a.n||1)}</div></div>`;});
  h+=`</div><div class="card"><h3>Últimos 14 dias</h3><div class="days">`;
  const cnt={};Object.values(S.at).forEach(a=>a.forEach(x=>{const k=new Date(x.t).toDateString();(cnt[k]=cnt[k]||[0,0])[x.ok?0:1]++;}));
  let mx=1;const ds=[];for(let i=13;i>=0;i--){const d=new Date(Date.now()-i*DAY);const c=cnt[d.toDateString()]||[0,0];ds.push([d,c]);mx=Math.max(mx,c[0]+c[1]);}
  ds.forEach(([d,c])=>{h+=`<div class="day"><div class="col"><i class="e" style="height:${100*c[1]/mx}%"></i><i class="a" style="height:${100*c[0]/mx}%"></i></div><small>${d.getDate()}</small></div>`;});
  h+=`</div><small class="mut">Verde: acertos. Vermelho: erros.</small></div>`;
  V.innerHTML=h;
}

/* ---------- conteúdo (resumos) ---------- */
function conteudo(arg){
  let list=[];
  if(!arg){list=D.temas;}
  else if(arg[0]==='T'){const id=+arg.slice(1);list=D.temas.filter(t=>t.top===id);}
  else list=D.temas.filter(t=>t.id===arg);
  let h=`<h2>Resumos</h2>`;
  if(!list.length)h+=`<div class="card">Sem resumo para este tópico (as questões vêm do Caderno 1). Use o campo “Se errou, estude” no gabarito.</div>`;
  list.forEach(t=>{const n=Q.filter(q=>q.tema===t.id);
    h+=`<div class="card"><div class="meta">${badge(topById[t.top].prio)}<span class="tag">${esc(t.src)}</span></div><h3>${esc(t.titulo)}</h3><small class="mut">${esc(t.fonte)}</small>
     <ul>`+t.itens.map(i=>`<li>${i}</li>`).join('')+`</ul><button class="btn sm" data-t="${t.id}">Praticar este tema (${n.length})</button></div>`;});
  V.innerHTML=h;
  V.querySelectorAll('[data-t]').forEach(b=>b.onclick=()=>startSession(shuffle(Q.filter(q=>q.tema===b.dataset.t).map(q=>q.id)),{title:temaById[b.dataset.t].titulo}));
}

/* ---------- IA: explicação de cada alternativa ---------- */
function aiBlock(q){
  const c=S.ai[q.id];
  if(c)return aiHtml(q,c);
  return `<button class="btn ghost" id="aiBtn">✨ Explicar cada alternativa com IA</button><small class="mut"> usa sua chave da Anthropic (Configurações). A resposta fica salva.</small>`;
}
function aiHtml(q,c){
  let h=`<div class="aiBox"><b>✨ Explicação por alternativa</b>`;
  q.opts.forEach((o,i)=>{h+=`<div class="aiopt ${i===q.ci?'r':'w'}"><div><b>${L[i]}) ${i===q.ci?'CERTA':'ERRADA'}</b> · ${esc(o)}</div><p>${esc(c[L[i]]||'—')}</p></div>`;});
  if(c.dica)h+=`<div class="tip">💡 ${esc(c.dica)}</div>`;
  return h+`<small class="mut">Gerado por IA a partir do comentário do gabarito. Confira no texto legal em caso de dúvida.</small></div>`;
}
async function explain(q){
  if(!S.cfg.key){toast('Cole sua chave da Anthropic em Configurações.');location.hash='#/config';return;}
  const box=$('#ai');box.innerHTML='<div class="mut">Gerando explicação…</div>';
  const prompt=`Você é professor de concursos (Legislativo municipal). Explique, para cada alternativa da questão abaixo, por que está certa ou errada. Use SOMENTE o gabarito e o comentário oficial fornecidos como base de fatos; não invente números de artigo, prazos ou quóruns que não estejam no material. Se algo não puder ser confirmado, diga isso. Cada explicação: 1 a 3 frases, em português. Para as erradas, aponte a pegadinha (o que foi trocado). Termine com uma dica de memorização curta.
Responda APENAS com JSON válido: {"A":"...","B":"...","C":"...","D":"...","dica":"..."}

Questão: ${q.stem}
A) ${q.opts[0]}
B) ${q.opts[1]}
C) ${q.opts[2]}
D) ${q.opts[3]}
Gabarito: ${L[q.ci]}
Comentário oficial: ${q.why}
Fonte de estudo: ${q.study}`;
  try{
    const r=await fetch('https://api.anthropic.com/v1/messages',{method:'POST',headers:{'content-type':'application/json','x-api-key':S.cfg.key,'anthropic-version':'2023-06-01','anthropic-dangerous-direct-browser-access':'true'},
      body:JSON.stringify({model:S.cfg.model||'claude-sonnet-5-5',max_tokens:1200,messages:[{role:'user',content:prompt}]})});
    if(!r.ok){const t=await r.text();throw new Error(r.status+' '+t.slice(0,200));}
    const j=await r.json(); const txt=(j.content||[]).map(x=>x.text||'').join('');
    const m=txt.match(/\{[\s\S]*\}/); if(!m)throw new Error('Resposta sem JSON');
    const o=JSON.parse(m[0]); if(!o.A||!o.B||!o.C||!o.D)throw new Error('JSON incompleto');
    S.ai[q.id]=o; save(); box.innerHTML=aiHtml(q,o);
  }catch(e){box.innerHTML=`<div class="alert slim">Não consegui gerar: ${esc(e.message)}</div><button class="btn ghost" id="aiBtn">Tentar de novo</button>`;$('#aiBtn').onclick=()=>explain(q);}
}

/* ---------- configurações / backup ---------- */
function config(){
  V.innerHTML=`<h2>Configurações</h2><div class="card form"><h3>IA (explicação por alternativa)</h3>
   <label>Chave da API da Anthropic<input type="password" id="key" value="${esc(S.cfg.key)}" placeholder="sk-ant-..." autocomplete="off"></label>
   <label>Modelo<input id="model" value="${esc(S.cfg.model)}"></label>
   <small class="mut">A chave fica só neste navegador (localStorage) e é enviada apenas à Anthropic. Não coloque a chave no código nem no GitHub.</small>
   <button class="btn" id="sv">Salvar</button></div>
   <div class="card form"><h3>Backup do progresso</h3><p class="mut">O progresso mora neste navegador. Exporte de vez em quando e guarde o arquivo; para trocar de aparelho, importe-o lá.</p>
   <div class="row"><button class="btn" id="ex">Exportar backup</button><label class="btn ghost">Importar<input type="file" id="im" accept="application/json" hidden></label></div>
   <button class="btn danger" id="rs">Apagar todo o progresso</button></div>
   <p class="mut">${Q.length} questões · versão 1</p>`;
  $('#sv').onclick=()=>{S.cfg.key=$('#key').value.trim();S.cfg.model=$('#model').value.trim()||'claude-sonnet-5-5';save();toast('Salvo.');};
  $('#ex').onclick=()=>{const b=new Blob([JSON.stringify(Object.assign({},S,{cfg:Object.assign({},S.cfg,{key:''})}),null,1)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='progresso-'+new Date().toISOString().slice(0,10)+'.json';a.click();};
  $('#im').onchange=e=>{const f=e.target.files[0];if(!f)return;const r=new FileReader();r.onload=()=>{try{const o=JSON.parse(r.result);if(!o.at)throw 0;const k=S.cfg.key;S=Object.assign(blank(),o);S.cfg.key=k||'';save();toast('Backup importado.');nav();}catch(x){toast('Arquivo inválido.');}};r.readAsText(f);};
  $('#rs').onclick=()=>{if(confirm('Apagar TODO o progresso? Isso não pode ser desfeito.')){const k=S.cfg;S=blank();S.cfg=k;save();toast('Zerado.');nav();}};
}

window.addEventListener('hashchange',route);
route();
})();
