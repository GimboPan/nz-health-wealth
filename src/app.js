/* A buildless, browser-local reader. No accounts, telemetry or external calls. */
(() => {
  'use strict';
  const { entries, meta, research, episodes } = window.GUIDE_DATA;
  const $ = (s) => document.querySelector(s);
  const esc = (v = '') => String(v).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const storageKey = 'nz-health-wealth-saved-v1';
  let saved = new Set(), storageAvailable = true, toastTimer;
  try { const raw = JSON.parse(localStorage.getItem(storageKey) || '[]'); if (Array.isArray(raw)) saved = new Set(raw.filter(id => entries.some(e => e.id === id))); } catch { storageAvailable = false; }
  const state = { topic: 'all', category: 'all', query: '', saved: false, podcast: false, checked: false, scene: null };
  const scenes = {
    new: { topic:'health', ids:['enrol','closed-books','funding','interpreter'], label:'刚到新西兰' },
    today: { topic:'health', ids:['emergency','healthline','same-day','pharmacist'], label:'今天需要看病' },
    kiwi: { topic:'wealth', ids:['kiwi-rate','kiwi-government','kiwi-fund','kiwi-home'], label:'想弄懂 KiwiSaver' },
    money: { topic:'wealth', ids:['cash-buffer','money-goals','debt-list','couples','investment-scam','ai-money'], label:'想把钱安排好' }
  };
  const searchText = new Map(entries.map(e => [e.id, JSON.stringify([e.title,e.summary,e.category,e.tags,e.steps,e.cost,e.limit,e.official,e.correction,e.sourceGap,e.podcast?.who,e.podcast?.summary,e.podcast?.episodeTitle,e.podcast?.timestamp]).normalize('NFKC').toLowerCase()]));
  function filtered() {
    const terms = state.query.normalize('NFKC').toLowerCase().trim().split(/\s+/).filter(Boolean);
    return entries.filter(e =>
      (state.topic === 'all' || e.topic === state.topic) &&
      (state.category === 'all' || e.category === state.category) &&
      (!state.saved || saved.has(e.id)) && (!state.podcast || e.podcast) &&
      (!state.checked || e.status === '本次核对') &&
      (!state.scene || scenes[state.scene].ids.includes(e.id)) &&
      terms.every(t => searchText.get(e.id).includes(t)));
  }
  function toast(message) {
    $('#toast').textContent = message; $('#toast').classList.add('visible');
    clearTimeout(toastTimer); toastTimer = setTimeout(() => $('#toast').classList.remove('visible'), 3200);
  }
  async function copy(text, message) {
    try {
      if (navigator.clipboard && window.isSecureContext) await navigator.clipboard.writeText(text);
      else {
        const input = document.createElement('textarea'); input.value = text;
        input.style.position = 'fixed'; input.style.opacity = '0'; document.body.append(input); input.select();
        const ok = document.execCommand('copy'); input.remove(); if (!ok) throw Error('Copy unavailable');
      }
      toast(message);
    } catch { toast('浏览器暂不支持复制，请手动选中需要的文字。'); }
  }
  function card(e, i) {
    const p = e.podcast;
    const sourceLinks = e.sources.map(s => `<a href="${esc(s.url)}" target="_blank" rel="noopener noreferrer">${esc(s.label)} ↗</a>`).join('');
    return `<article class="entry" data-id="${esc(e.id)}">
      <button class="bookmark" data-save="${esc(e.id)}" aria-label="${saved.has(e.id)?'取消收藏':'收藏'}：${esc(e.title)}" aria-pressed="${saved.has(e.id)}">${saved.has(e.id)?'★':'☆'}</button>
      <details id="guide-${esc(e.id)}"><summary>
        <div class="entry-meta"><span class="entry-number">${String(entries.indexOf(e)+1).padStart(2,'0')}</span><span class="topic-label">${e.topic==='health'?'HEALTH':'WEALTH'}</span><span> / ${esc(e.category)}</span><span>· ${p?esc(p.sourceRole):'官方补充 · 节目缺口'}</span></div>
        <h3 class="entry-title">${esc(e.title)}</h3><p class="entry-blurb">${esc(e.summary)}</p><span class="entry-more" aria-hidden="true">＋</span>
      </summary><div class="entry-content">
        <h4>下一步，可以这样做</h4><ol>${e.steps.map(s=>`<li>${esc(s)}</li>`).join('')}</ol>
        <div class="practical-grid"><div><h4>费用与成本</h4><p>${esc(e.cost)}</p></div><div><h4>适用边界</h4><p>${esc(e.limit)}</p></div></div>
        <h4>可以这样问 · 编辑撰写</h4><div class="phrase"><p lang="en">${esc(e.english)}</p><button data-copy="${esc(e.id)}" aria-label="复制英文问法">复制</button></div>
        ${e.correction?`<div class="correction"><strong>核对后补充 / 纠正</strong><p>${esc(e.correction)}</p></div>`:''}
        <div class="evidence"><span class="source-label">公共资料 / ${esc(e.status)}</span><p>${esc(e.official)}</p><div class="evidence-links">${sourceLinks}</div><p class="source-meta">${e.checked?`本次网页检索核对：${esc(e.checked)}`:'相关资料供继续查阅；节目经验未完成独立规则核验。'}</p></div>
        ${p?`<div class="evidence"><span class="source-label">${esc(p.sourceRole)} / ${esc(p.show)}</span><p>${esc(p.summary)}</p><p class="source-meta"><strong>${esc(p.who)}</strong> · ${esc(p.role)}<br>${esc(p.dateType)}：${esc(p.date)} · 时段 ${esc(p.timestamp)} · ${esc(p.speaker)}<br>单集：${esc(p.episodeTitle)}<br>${esc(p.provenance)}${p.identityEvidence?`<br>身份自述核对时段：${esc(p.identityEvidence.timestamp)}`:''}</p>${p.sourceRole==='节目背景'?'<p class="source-scope">此时段提供问题背景；本条的现行政策、费用或资格依据上方公共资料。</p>':''}${p.conflict?`<div class="conflict">关系披露：${esc(p.conflict)}</div>`:''}<div class="evidence-links"><a href="${esc(p.url)}" target="_blank" rel="noopener noreferrer">打开这一集 ↗</a><button data-citation="${esc(e.id)}">复制来源与时段</button></div></div>`:`<div class="source-gap">${esc(e.sourceGap)} 没有为此编配节目来源或时间戳。</div>`}
        <div class="entry-bottom"><span><span class="tag">编辑整理</span> 内容核对：${esc(e.edited || meta.observedDate)}</span><button data-link="${esc(e.id)}">复制定位链接 ↗</button></div>
      </div></details></article>`;
  }
  function render() {
    const openIds = [...document.querySelectorAll('.entry details[open]')].map(d=>d.id);
    const base = entries.filter(e=>state.topic==='all'||e.topic===state.topic);
    const categories = [...new Set(base.map(e=>e.category))];
    $('#categories').innerHTML = ['all',...categories].map(cat=>`<button data-category="${esc(cat)}" aria-pressed="${state.category===cat}">${cat==='all'?'所有主题':esc(cat)}<span>${cat==='all'?base.length:base.filter(e=>e.category===cat).length}</span></button>`).join('');
    const list = filtered(); $('#cards').innerHTML = list.map(card).join('');
    openIds.forEach(id=>{const d=document.getElementById(id);if(d)d.open=true;});
    $('#result-count').textContent = `${state.scene?scenes[state.scene].label+' · ':''}${state.saved?'收藏中 · ':''}${list.length} 条指南`;
    $('#empty').hidden = list.length > 0; $('#saved-count').textContent = saved.size;
    $('#saved').setAttribute('aria-pressed',state.saved);
    document.querySelectorAll('[data-topic]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.topic===state.topic));
    $('#podcast-only').checked = state.podcast; $('#checked-only').checked = state.checked;
    $('#health-help').hidden = state.topic==='wealth';
  }
  function reset() {
    Object.assign(state,{topic:'all',category:'all',query:'',saved:false,podcast:false,checked:false,scene:null});
    $('#search').value=''; render();
  }
  document.addEventListener('click',event=>{
    const b=event.target.closest('button'); if(!b)return;
    if(b.dataset.topic){state.topic=b.dataset.topic;state.category='all';state.scene=null;render();}
    else if(b.dataset.category){state.category=b.dataset.category;state.scene=null;render();}
    else if(b.dataset.scene){const k=b.dataset.scene;reset();state.topic=scenes[k].topic;state.scene=k;render();$('#library').scrollIntoView();}
    else if(b.dataset.save){const id=b.dataset.save;if(saved.has(id))saved.delete(id);else saved.add(id);
      try{localStorage.setItem(storageKey,JSON.stringify([...saved]));}catch{storageAvailable=false;}
      render();document.querySelector(`[data-save="${id}"]`)?.focus({preventScroll:true});toast(storageAvailable?(saved.has(id)?'已收藏到当前浏览器':'已取消收藏'):'已更新本次收藏；浏览器未允许持久保存。');
    }
    else if(b.dataset.copy){copy(entries.find(e=>e.id===b.dataset.copy).english,'英文问法已复制。');}
    else if(b.dataset.citation){const p=entries.find(e=>e.id===b.dataset.citation).podcast;copy(`${p.show} · ${p.episodeTitle}\n${p.who} · ${p.date} · ${p.timestamp}\n${p.url}\n${p.sourceRole}；Apple 自动字幕段落，未听音复核。`,'节目来源与时段已复制。');}
    else if(b.dataset.link){copy(location.href.split('#')[0]+'#guide-'+b.dataset.link,'已复制条目定位链接；本地链接需在同一台电脑打开。');}
  });
  $('#search').addEventListener('input',event=>{state.query=event.target.value;render();});
  $('#saved').addEventListener('click',()=>{state.saved=!state.saved;render();});
  $('#podcast-only').addEventListener('change',e=>{state.podcast=e.target.checked;render();});
  $('#checked-only').addEventListener('change',e=>{state.checked=e.target.checked;render();});
  $('#reset').addEventListener('click',reset); $('#empty-reset').addEventListener('click',reset);
  document.addEventListener('keydown',e=>{if(e.key==='/'&&!e.ctrlKey&&!e.metaKey&&!['INPUT','TEXTAREA','SELECT'].includes(e.target.tagName)){e.preventDefault();$('#search').focus();}});
  function markdown(list){
    return `# 在新西兰，好好生活 · Health & Wealth\n\n内容版本 ${meta.version} · ${meta.observedDate}\n来源标注不是专业审阅。完整字幕未随本文件分发。\n\n`+list.map(e=>
      `## ${e.title}\n\n${e.summary}\n\n${e.steps.map((s,i)=>`${i+1}. ${s}`).join('\n')}\n\n费用：${e.cost}\n\n边界：${e.limit}\n\n英文问法：${e.english}\n\n公共资料：${e.official}\n${e.sources.map(s=>`- [${s.label}](${s.url})`).join('\n')}\n核对：${e.checked||'节目经验待核验'}\n`+
      (e.correction?`\n核对后补充/纠正：${e.correction}\n`:'')+
      (e.podcast?`\n${e.podcast.sourceRole}：${e.podcast.summary}\n\n${e.podcast.who} · ${e.podcast.role}\nfeed 日期 ${e.podcast.date} · 时段 ${e.podcast.timestamp} · ${e.podcast.speaker}\n单集：${e.podcast.episodeTitle}\n[${e.podcast.show}](${e.podcast.url})\n${e.podcast.provenance}\n关系披露：${e.podcast.conflict||'本条未标出特定关系；不代表不存在。'}\n`:`\n官方补充：${e.sourceGap}\n` )).join('\n---\n\n');
  }
  $('#export').addEventListener('click',()=>{
    const list=filtered();if(!list.length){toast('当前没有可下载的条目。');return;}
    const blob=new Blob([markdown(list)],{type:'text/markdown;charset=utf-8'});const url=URL.createObjectURL(blob);
    const a=document.createElement('a');a.href=url;a.download='nz-health-wealth-guide.md';document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);toast(`已下载当前筛选的 ${list.length} 条指南。`);
  });
  let printOpen = [];
  window.addEventListener('beforeprint',()=>{printOpen=[...document.querySelectorAll('.entry details[open]')].map(d=>d.id);document.querySelectorAll('.entry details').forEach(d=>d.open=true);});
  window.addEventListener('afterprint',()=>{document.querySelectorAll('.entry details').forEach(d=>d.open=printOpen.includes(d.id));});
  $('#print').addEventListener('click',()=>{if(filtered().length)window.print();else toast('当前没有可打印的条目。');});
  function followHash(){let id;try{id=decodeURIComponent(location.hash.slice(1));}catch{return;}if(!id.startsWith('guide-'))return;const entry=entries.find(e=>'guide-'+e.id===id);if(!entry)return;reset();state.topic=entry.topic;render();const d=document.getElementById(id);d.open=true;requestAnimationFrame(()=>d.scrollIntoView({behavior:'auto',block:'start'}));}
  window.addEventListener('hashchange',followHash);
  $('#corpus-status').innerHTML=meta.corpus.map(c=>`<p><strong>${esc(c.name)}</strong>：本地 ${c.episodes} 集，取得 ${c.available} 份字幕，约 ${(c.words/10000).toFixed(1)} 万词。缺少字幕：${c.missing.map(e=>esc(e.date)+' / '+esc(e.eid)).join('；')}。</p>`).join('');
  $('#research-status').innerHTML=`<p>${esc(research.method)}</p><div class="research-grid">${Object.entries(research.topics).map(([topic,r])=>`<div><h3>${topic==='health'?'Health':'Wealth'} 候选主题</h3><ul>${Object.entries(r.candidateEpisodeCounts).map(([theme,n])=>`<li>${esc(theme)} <span>${n} 份正文匹配</span></li>`).join('')}</ul><p>关键词模式排除 ${r.adPatternExcludedBlocks} 段含广告提示的文字；不是广告人工审计。</p></div>`).join('')}</div>`;
  let episodeLimit=20;
  const episodeStatus={ 'selected-passages':'已引用片段', 'indexed-unreviewed':'已索引待审阅', unavailable:'无可用字幕' };
  const titleById=new Map(entries.map(e=>[e.id,e.title]));
  function renderEpisodes(){
    const q=$('#episode-search').value.normalize('NFKC').toLowerCase().trim();
    const topic=$('#episode-topic').value,status=$('#episode-status').value;
    const rows=episodes.filter(e=>(topic==='all'||e.topic===topic)&&(status==='all'||e.reviewStatus===status)&&`${e.show} ${e.title} ${e.date} ${e.id}`.normalize('NFKC').toLowerCase().includes(q));
    $('#episode-count').textContent=`${rows.length} 集匹配 · 当前显示 ${Math.min(episodeLimit,rows.length)} 集`;
    $('#episode-list').innerHTML=rows.slice(0,episodeLimit).map(e=>`<article class="episode"><div class="episode-meta"><span>${esc(e.show)} · ${esc(e.date)}</span><span>${esc(episodeStatus[e.reviewStatus])}</span></div><h3><a href="${esc(e.url)}" target="_blank" rel="noopener noreferrer">${esc(e.title)} ↗</a></h3>${e.entryIds.length?`<p>所选片段用于：${e.entryIds.map(id=>`<a href="#guide-${esc(id)}">${esc(titleById.get(id))}</a>`).join('；')}</p>`:''}</article>`).join('')||'<p>没有匹配的节目，可以换个关键词。</p>';
    $('#episode-more').hidden=rows.length<=episodeLimit;
  }
  ['episode-search','episode-topic','episode-status'].forEach(id=>$('#'+id).addEventListener(id==='episode-search'?'input':'change',()=>{episodeLimit=20;renderEpisodes();}));
  $('#episode-more').addEventListener('click',()=>{episodeLimit+=20;renderEpisodes();});
  $('#episode-export').addEventListener('click',()=>{
    const cell=v=>'"'+String(v).replace(/^[=+@-]/,"'$&").replace(/"/g,'""')+'"';
    const csv='\ufeff'+[['show','feed_date','episode_id','title','transcript_available','review_status','entry_ids','url'],...episodes.map(e=>[e.show,e.date,e.id,e.title,e.transcriptAvailable,e.reviewStatus,e.entryIds.join(';'),e.url])].map(row=>row.map(cell).join(',')).join('\r\n');
    const url=URL.createObjectURL(new Blob([csv],{type:'text/csv;charset=utf-8'}));const a=document.createElement('a');a.href=url;a.download='nz-health-wealth-episodes.csv';document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);
  });
  renderEpisodes();render();followHash();
})();
