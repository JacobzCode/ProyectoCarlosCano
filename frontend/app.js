const API_BASE = 'http://127.0.0.1:8001/api'
let TOKEN = null
let HANDLE = null

// helpers
async function postJson(url, body, auth=true){
  const headers = {'Content-Type':'application/json'}
  if(auth && TOKEN) headers['Authorization'] = 'Bearer '+TOKEN
  const res = await fetch(url, {method:'POST', headers, body: JSON.stringify(body)})
  return res
}

function pageName(){ return document.body.id || '' }

// --- Home page ---
function initHome(){ /* no dynamic handlers yet */ }

// --- Register page ---
function initRegister(){
  const form = document.getElementById('formRegister')
  if(!form) return
  form.addEventListener('submit', async (e)=>{
    e.preventDefault()
    const handle = document.getElementById('regHandle').value
    const email = document.getElementById('regEmail').value
    const secret = document.getElementById('regSecret').value
    const res = await postJson(API_BASE+'/accounts', {handle, email, secret}, false)
    if(res.status===201){
      alert('Cuenta creada. Ahora inicia sesión.'); window.location = 'login.html'
    } else {
      const j = await res.json(); alert('Error: '+(j.detail||JSON.stringify(j)))
    }
  })
}

// --- Login page ---
function initLogin(){
  const form = document.getElementById('formLogin')
  if(!form) return
  form.addEventListener('submit', async (e)=>{
    e.preventDefault()
    const handle = document.getElementById('loginHandle').value
    const secret = document.getElementById('loginSecret').value
    const res = await postJson(API_BASE+'/sessions', {handle, secret}, false)
    if(res.ok){
      const j = await res.json(); TOKEN = j.access_token; HANDLE = handle; localStorage.setItem('mk_token', TOKEN); localStorage.setItem('mk_handle', HANDLE); window.location='dashboard.html'
    } else {
      const j = await res.json(); alert('Login failed: '+(j.detail||JSON.stringify(j)))
    }
  })
}

// render nav auth area (login/register or profile dropdown)
function renderNavAuth(){
  const container = document.getElementById('navAuth');
  if(!container) return
  const token = localStorage.getItem('mk_token')
  const handle = localStorage.getItem('mk_handle')
  if(token && handle){
    // show avatar + dropdown
    container.innerHTML = `
      <div class="dropdown">
        <a class="d-flex align-items-center text-decoration-none" href="#" id="profileDropdown" data-bs-toggle="dropdown" aria-expanded="false">
          <div class="profile-avatar me-2" style="width:36px; height:36px; border-radius:50%;"></div>
          <strong style="color: var(--mk-text);">${handle}</strong>
        </a>
        <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="profileDropdown">
          <li><a class="dropdown-item" href="profile.html">Mi perfil</a></li>
          <li><a class="dropdown-item" href="dashboard.html">Dashboard</a></li>
          <li><hr class="dropdown-divider"></li>
          <li><a class="dropdown-item" href="#" id="navLogout">Cerrar sesión</a></li>
        </ul>
      </div>
    `
    // attach logout handler
    setTimeout(()=>{
      const el = document.getElementById('navLogout'); if(el) el.addEventListener('click', async (e)=>{ e.preventDefault(); if(!localStorage.getItem('mk_token')) return; await fetch(API_BASE+'/sessions/logout',{method:'POST', headers:{'Authorization':'Bearer '+localStorage.getItem('mk_token')}}); localStorage.removeItem('mk_token'); localStorage.removeItem('mk_handle'); TOKEN=null; HANDLE=null; renderNavAuth(); window.location='index.html' })
    }, 50)
  } else {
    container.innerHTML = `<a class="btn btn-outline-light me-2" href="login.html">Iniciar Sesión</a><a class="btn btn-light" href="register.html">Registrarse</a>`
  }
}

// --- Dashboard page ---
let avgChart=null, tsChart=null
let avgDataCache = { labels:[], values:[] }
async function loadDashboard(){
  // Try to fetch insights with auth when available, otherwise fall back to public fetch
  const headers = {}
  if(TOKEN) headers['Authorization'] = 'Bearer '+TOKEN
  try {
    // avg by handle
    const r1 = await fetch(API_BASE+'/insights/average', {headers})
    if (r1.ok) {
      const avg = await r1.json()
      renderAvgChart(avg)
    } else {
      // render empty chart if endpoint not available
      renderAvgChart({})
    }

    // time series via summary
    const r2 = await fetch(API_BASE+'/insights/summary', {headers})
    if (r2.ok) {
      const sum = await r2.json()
      renderTsChart(sum.time_series||{})
    } else {
      renderTsChart({})
    }

    // alerts
    const r3 = await fetch(API_BASE+'/insights/alerts', {headers})
    if (r3.ok) {
      const alerts = await r3.json()
      renderAlerts(alerts)
    } else {
      renderAlerts({count:0, items:[]})
    }
  } catch (error) {
    console.error('Error loading dashboard:', error)
    // fallback render empty placeholders
    renderAvgChart({})
    renderTsChart({})
    renderAlerts({count:0, items:[]})
  }
}

// Utility: deterministic color from string (hue) -> returns rgba fill and stroke
function hashColor(str, alpha=1){
  // simple hash to integer
  let h = 0
  for(let i=0;i<str.length;i++) h = (h<<5) - h + str.charCodeAt(i) | 0
  const hue = Math.abs(h) % 360
  // use HSL -> convert to rgba via CSS hsl with alpha
  // return rgba string with decent saturation and lightness
  return `hsla(${hue},70%,45%,${alpha})`
}

function paletteForLabels(labels){
  const bg = labels.map(l=>hashColor(l, 0.55))
  const border = labels.map(l=>hashColor(l, 1))
  return {bg, border}
}

function renderAvgChart(data){
  const labels = Object.keys(data||{}).slice(0,10)
  const values = labels.map(l=>data[l])
  // cache
  avgDataCache.labels = labels.slice()
  avgDataCache.values = values.slice()
  // if no data, create placeholder labels
  if(labels.length===0){
    for(let i=1;i<=6;i++){ labels.push('User '+i); values.push(null) }
  }
  const el = document.getElementById('avgChart'); if(!el) return
  const ctx = el.getContext('2d')
  if(avgChart) avgChart.destroy()
  const pal = paletteForLabels(labels)
  avgChart = new Chart(ctx, {
    type:'bar',
    data:{
      labels,
      datasets:[{
        label:'Avg mood',
        data:values,
        backgroundColor: pal.bg,
        borderColor: pal.border,
        borderWidth: 1
      }]
    },
    options: { responsive:true, maintainAspectRatio:false, plugins:{ legend:{ display:false } } }
  })
}

// Switch avg chart type using cached data
function applyAvgChartType(type){
  const labels = avgDataCache.labels.length?avgDataCache.labels.slice():['User 1','User 2','User 3','User 4']
  const values = avgDataCache.values.length?avgDataCache.values.slice():[null,null,null,null]
  const el = document.getElementById('avgChart'); if(!el) return
  const ctx = el.getContext('2d')
  if(avgChart) avgChart.destroy()

  // For scatter, Chart.js expects array of {x,y} points — map index->value
  if(type==='scatter'){
    const dataset = values.map((v,i)=>({x:i+1,y:v}))
    avgChart = new Chart(ctx, { type:'scatter', data:{ datasets:[{ label:'Avg mood', data:dataset, backgroundColor: 'rgba(52,58,64,0.7)' }] }, options:{ responsive:true, maintainAspectRatio:false } })
    return
  }

  // For pie/doughnut/polarArea we provide values directly
  if(['pie','doughnut','polarArea'].includes(type)){
    avgChart = new Chart(ctx, { type, data:{ labels, datasets:[{ data: values, backgroundColor: paletteForLabels(labels).bg }] }, options:{ responsive:true, maintainAspectRatio:false } })
    return
  }

  // fallback to line or bar
  avgChart = new Chart(ctx, { type, data:{ labels, datasets:[{ label:'Avg mood', data: values, borderColor:'rgba(75,192,192,1)', backgroundColor:paletteForLabels(labels).bg, fill:type==='line'?false:true }] }, options:{ responsive:true, maintainAspectRatio:false } })
}

function renderTsChart(ts){
  const el = document.getElementById('tsChart'); if(!el) return
  const ctx = el.getContext('2d')
  if(tsChart) tsChart.destroy()

  // detect if ts is multi-series (each value is an object or array per label)
  const vals = Object.values(ts)
  const isMulti = vals.length>0 && (typeof vals[0] === 'object' && !Array.isArray(vals[0]) || Array.isArray(vals[0]) && vals.some(v=>Array.isArray(v)))

  if(isMulti){
    // ts is expected to be {handle1: {date:val,...}, handle2: {...}}
    // build union of dates
    const handles = Object.keys(ts)
    const datesSet = new Set()
    handles.forEach(h=>{ Object.keys(ts[h]||{}).forEach(d=>datesSet.add(d)) })
    const labels = Array.from(datesSet).sort().slice(-90)
    const datasets = handles.map(h=>{
      const data = labels.map(d=>{ const v = ts[h] && ts[h][d]; return (v===undefined)?null:v })
      return { label: h, data, borderColor: hashColor(h,1), backgroundColor: hashColor(h,0.2), fill:false }
    })
    tsChart = new Chart(ctx, { type:'line', data:{ labels, datasets }, options:{ responsive:true } })
    return
  }

  // fallback: ts is mapping date->value
  let labels = Object.keys(ts||{}).slice(-30)
  let values = labels.map(l=>ts[l])
  if(labels.length===0){
    // placeholder timeline
    labels = ['-5d','-4d','-3d','-2d','-1d','Hoy']
    values = [null,null,null,null,null,null]
  }
  tsChart = new Chart(ctx, {type:'line', data:{labels, datasets:[{label:'Avg mood', data:values, borderColor:'rgba(75,192,192,1)', fill:false}]}, options:{ responsive:true }})
}

function renderAlerts(obj){
  const body = document.getElementById('alertsBody'); if(body) body.innerHTML=''
  const summaryEl = document.getElementById('alertsSummary'); if(summaryEl) summaryEl.innerText = `Alertas: ${obj.count||0}`
  // helper to color mood
  const moodColor = (m)=>{ if(m<=3) return 'rgba(220,53,69,0.12)'; if(m<=6) return 'rgba(255,193,7,0.12)'; return 'rgba(25,135,84,0.12)'}
  const moodBorder = (m)=>{ if(m<=3) return 'rgba(220,53,69,0.9)'; if(m<=6) return 'rgba(255,193,7,0.9)'; return 'rgba(25,135,84,0.9)'}

  if(obj.items && body){
    obj.items.slice(0,50).forEach((it,idx)=>{
      const tr = document.createElement('tr')
      const note = it.comment || ''
      const preview = note.length>80? note.slice(0,80)+'…' : note
      tr.innerHTML = `
        <td>${idx+1}</td>
        <td>
          <div class="user-cell">
            <div class="avatar-sm" aria-hidden="true"></div>
            <div><div class="fw-semibold">${it.handle}</div><div class="small text-muted">${it.email||''}</div></div>
          </div>
        </td>
        <td><span class="badge-mood" style="background:${moodColor(it.mood)}; border-color:${moodBorder(it.mood)}">${it.mood}</span></td>
        <td>${it.created}</td>
        <td><div class="note-preview">${preview}</div></td>
        <td class="actions-cell text-end"><button class="btn btn-sm btn-outline-secondary" data-idx="${idx}" data-note="${encodeURIComponent(note)}">Ver</button></td>
      `
      body.appendChild(tr)
    })
    // attach view handlers
    body.querySelectorAll('.actions-cell button').forEach(b=>{
      b.addEventListener('click', (e)=>{
        const note = decodeURIComponent(b.getAttribute('data-note')||'')
        showAlertNoteModal(note)
      })
    })
  }

  const rec = document.getElementById('recommendations')
  if(rec){
    if((obj.count||0) > 0){ rec.innerHTML = `<div class="alert alert-warning">Se encontraron ${obj.count} respuestas con bajo estado de ánimo. Mostrar recursos y contactos locales.</div>` } else { rec.innerHTML = `<div class="alert alert-success">No se encontraron alertas recientes.</div>` }
  }
}

// small modal renderer for full note
function showAlertNoteModal(note){
  let modalEl = document.getElementById('alertNoteModal')
  if(!modalEl){
    modalEl = document.createElement('div')
    modalEl.className = 'modal fade alert-note-modal'
    modalEl.id = 'alertNoteModal'
    modalEl.tabIndex = -1
    modalEl.innerHTML = `
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Nota completa</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body"></div>
        </div>
      </div>`
    document.body.appendChild(modalEl)
  }
  modalEl.querySelector('.modal-body').innerText = note || '(sin nota)'
  try{ const m = new bootstrap.Modal(modalEl); m.show() }catch(e){ showConfirmModal('Nota completa', note || '(sin nota)') }
}

// Reusable confirmation modal: title, message, optional callback when user confirms/ok
function showConfirmModal(title, message, onOk){
  let id = 'mkConfirmModal'
  let modalEl = document.getElementById(id)
  if(!modalEl){
    modalEl = document.createElement('div')
    modalEl.className = 'modal fade'
    modalEl.id = id
    modalEl.tabIndex = -1
    modalEl.innerHTML = `
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">${title}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">${message}</div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
            <button type="button" class="btn btn-primary" id="mkConfirmOk">OK</button>
          </div>
        </div>
      </div>`
    document.body.appendChild(modalEl)
  } else {
    modalEl.querySelector('.modal-title').innerText = title
    modalEl.querySelector('.modal-body').innerText = message
  }
  try{
    const m = new bootstrap.Modal(modalEl)
    m.show()
    const okBtn = modalEl.querySelector('#mkConfirmOk')
    if(okBtn){
      const handler = ()=>{ try{ if(onOk) onOk(); } catch(e){} m.hide(); okBtn.removeEventListener('click', handler) }
      okBtn.addEventListener('click', handler)
    }
  }catch(err){
    // fallback when bootstrap is not available: use lightweight custom modal
    try{ showMkModal(title, message, onOk) }catch(e){ try{ if(onOk) onOk() }catch(_){} }
  }
}

  // lightweight custom modal implementation (used as fallback)
  function showMkModal(title, message, onOk){
    let overlay = document.getElementById('mkModalOverlay')
    if(!overlay){
      overlay = document.createElement('div')
      overlay.id = 'mkModalOverlay'
      overlay.className = 'mk-modal-overlay'
      overlay.innerHTML = `
        <div class="mk-modal">
          <div class="mk-modal-header"><h5 class="mk-modal-title"></h5><button class="btn btn-close mk-close" aria-label="Close">×</button></div>
          <div class="mk-modal-body"></div>
          <div class="mk-modal-footer"><button class="btn btn-secondary mk-close">Cerrar</button><button class="btn btn-primary mk-ok">OK</button></div>
        </div>`
      document.body.appendChild(overlay)
      overlay.querySelectorAll('.mk-close').forEach(b=>b.addEventListener('click', ()=>{ overlay.classList.remove('show') }))
    }
    overlay.querySelector('.mk-modal-title').innerText = title
    overlay.querySelector('.mk-modal-body').innerText = message
    const ok = overlay.querySelector('.mk-ok')
    const handler = ()=>{ try{ if(onOk) onOk(); }catch(e){} overlay.classList.remove('show'); ok.removeEventListener('click', handler) }
    ok.removeEventListener && ok.removeEventListener('click', handler)
    ok.addEventListener('click', handler)
    overlay.classList.add('show')
  }


function initDashboard(){
  // restore token (optional)
  if(localStorage.getItem('mk_token')){ TOKEN=localStorage.getItem('mk_token'); HANDLE=localStorage.getItem('mk_handle'); const uh = document.getElementById('userHandle'); if(uh) uh.innerText = HANDLE }
  // ensure navbar auth area reflects current session
  try{ renderNavAuth() }catch(e){}
  // logout
  const btnLogout = document.getElementById('btnLogout'); if(btnLogout) btnLogout.addEventListener('click', async ()=>{ if(!TOKEN) return; await fetch(API_BASE+'/sessions/logout', {method:'POST', headers:{'Authorization':'Bearer '+TOKEN}}); TOKEN=null; HANDLE=null; localStorage.removeItem('mk_token'); localStorage.removeItem('mk_handle'); window.location='index.html' })

  // form submit handler (modal will open the form)
  const form = document.getElementById('formSurvey');
  if(form) form.addEventListener('submit', async (e)=>{
    e.preventDefault();
    const mood = parseInt(document.getElementById('mood').value);
    const comment = document.getElementById('comment').value;
    
    // Capturar nuevos campos de hábitos
    const horas_sueno_val = document.getElementById('horas_sueno').value;
    const horas_sueno = horas_sueno_val ? parseFloat(horas_sueno_val) : null;
    const actividad_fisica = parseInt(document.getElementById('actividad_fisica').value);
    const calidad_alimentacion = parseInt(document.getElementById('calidad_alimentacion').value);
    const nivel_socializacion = parseInt(document.getElementById('nivel_socializacion').value);
    
    const payload = {
      mood, 
      comment,
      horas_sueno,
      actividad_fisica,
      calidad_alimentacion,
      nivel_socializacion
    };
    
    const res = await postJson(API_BASE+'/entries', payload);
    if(res.status===201){
      // Reset form
      form.reset();
      document.getElementById('mood').value = 5;
      document.getElementById('moodVal').innerText = 5;
      document.getElementById('actividad_fisica').value = 5;
      document.getElementById('actFisVal').innerText = 5;
      document.getElementById('calidad_alimentacion').value = 5;
      document.getElementById('calAlimVal').innerText = 5;
      document.getElementById('nivel_socializacion').value = 5;
      document.getElementById('socVal').innerText = 5;
      
      // close modal if bootstrap is present
      try{ var modalEl = document.getElementById('surveyModal'); var modal = bootstrap.Modal.getInstance(modalEl); if(modal) modal.hide(); }catch(err){}
      alert('Entry saved'); reloadCharts();
    } else {
      try{ const j=await res.json(); alert('Error: '+(j.detail||JSON.stringify(j))) }catch(err){ alert('Error submitting') }
    }
  })

  // CSV download removed per UX decision

  // chart style controls
  const chartSelect = document.getElementById('chartTypeSelect')
  const chartBtn = document.getElementById('btnApplyChartType')
  if(chartBtn && chartSelect) chartBtn.addEventListener('click', ()=>{ const t = chartSelect.value; applyAvgChartType(t) })

  // histogram type controls
  const histSelect = document.getElementById('histTypeSelect')
  const histBtn = document.getElementById('btnApplyHistType')
  if(histBtn && histSelect){
    histBtn.addEventListener('click', ()=>{
      const t = histSelect.value
      const histImg = document.getElementById('histChartImg')
      if(!histImg) return
      const base = 'http://127.0.0.1:8001/api/insights/plot/hist'
      const params = new URLSearchParams()
      if(t) params.set('type', t)
      params.set('t', Date.now())
      const src = base + '?' + params.toString()
      histImg.setAttribute('src', src)
    })
  }

  // initial data load
  loadDashboard()
}

function reloadCharts(){
  // reload histogram image to get fresh PNG
  const histImg = document.getElementById('histChartImg')
  if(histImg) {
    const src = histImg.getAttribute('src')
    histImg.setAttribute('src', src + (src.includes('?') ? '&' : '?') + 't=' + Date.now())
  }
  
  // reload dashboard data (charts and alerts)
  loadDashboard()
}

// --- Profile page ---
async function initProfile(){
  // restore token
  if(localStorage.getItem('mk_token')){ TOKEN=localStorage.getItem('mk_token'); HANDLE=localStorage.getItem('mk_handle'); const uh = document.getElementById('userHandle'); if(uh) uh.innerText = HANDLE }
  // populate basic info
  const pfHandle = document.getElementById('pfHandle'); if(pfHandle) pfHandle.innerText = HANDLE || '-'
  const pfEmail = document.getElementById('pfEmail'); if(pfEmail && TOKEN){
    // try to fetch account details
    try{ const r = await fetch(API_BASE+'/accounts/me', {headers:{'Authorization':'Bearer '+TOKEN}}); if(r.ok){ const j=await r.json(); pfEmail.innerText = j.email||'-' } }
    catch(e){ /* ignore */ }
  }
  // recent history
  const hist = document.getElementById('pfHistory')
  if(hist && TOKEN){
    try{ const r = await fetch(API_BASE+'/entries', {headers:{'Authorization':'Bearer '+TOKEN}}); if(r.ok){ const items = await r.json(); items.slice(-10).reverse().forEach(it=>{ const li = document.createElement('li'); li.className='list-group-item'; li.innerText = `${it.created} — Mood: ${it.mood} — ${it.comment||''}`; hist.appendChild(li) }) } }
    catch(e){}
  }
}

// bootstrap page init
document.addEventListener('DOMContentLoaded', ()=>{
  renderNavAuth()
  const p = pageName()
  if(p==='page-home') initHome()
  if(p==='page-register') initRegister()
  if(p==='page-login') initLogin()
  if(p==='page-dashboard') initDashboard()
  if(p==='page-profile') initProfile()
})
