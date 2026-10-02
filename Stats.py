<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Languages spoken at home across Western Australia</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
:root{--ink:#1c2a30;--mute:#5b6b72;--bg:#f3f6f7;--card:#fff;--line:#d5dee1;--red:#a8432b;--sea:#1d6a86;--sand:#c8a24a}
@media (prefers-color-scheme:dark){:root{--ink:#e8eef0;--mute:#9db0b8;--bg:#121b1f;--card:#1a262b;--line:#2c3c43}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 system-ui,-apple-system,"Segoe UI",sans-serif}
header{padding:3rem 1.25rem 2rem;max-width:880px;margin:auto}
h1{font:700 clamp(2rem,6vw,3.4rem)/1.1 Georgia,"Times New Roman",serif;margin:0 0 .75rem;letter-spacing:-.01em}
h2{font:700 1.5rem/1.2 Georgia,serif;margin:0 0 .5rem}
p{max-width:68ch;margin:.4rem 0}
.lede{font-size:1.1rem;color:var(--mute)}
main{max-width:880px;margin:auto;padding:0 1.25rem 3rem}
section{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:1.5rem;margin-bottom:1.5rem}
.controls{display:flex;flex-wrap:wrap;gap:.5rem 1.25rem;margin:1rem 0}
label{font-weight:600;font-size:.9rem;color:var(--mute);display:flex;flex-direction:column;gap:.25rem}
select{font:inherit;padding:.45rem .6rem;border:1px solid var(--line);border-radius:6px;background:var(--card);color:var(--ink)}
.chart{position:relative;height:340px}
ul{padding-left:1.2rem;max-width:68ch}li{margin:.35rem 0}
.note{font-size:.85rem;color:var(--mute)}
:focus-visible{outline:3px solid var(--sea);outline-offset:2px}
</style>
</head>
<body>
<header>
<h1>Languages spoken at home across Western Australia</h1>
<p class="lede">How many Aboriginal and Torres Strait Islander people speak English, an Aboriginal language, or another language at home, in each Indigenous Region of WA.</p>
</header>
<main>
<section aria-labelledby="h-compare">
<h2 id="h-compare">Compare regions</h2>
<p>Pick a census year and a language group to see how the regions compare.</p>
<div class="controls">
<label>Census year<select id="year"><option>2016</option><option>2021</option></select></label>
<label>Language group<select id="measure">
<option value="english">English</option>
<option value="atsi" selected>Aboriginal and Torres Strait Islander languages</option>
<option value="other">Other languages</option>
</select></label>
</div>
<div class="chart"><canvas id="c1" role="img" aria-label="Bar chart comparing regions"></canvas></div>
</section>

<section aria-labelledby="h-region">
<h2 id="h-region">Inside one region</h2>
<p>The most common Aboriginal and Torres Strait Islander languages spoken at home in the region you choose.</p>
<div class="controls"><label>Region<select id="region"></select></label></div>
<div class="chart"><canvas id="c2" role="img" aria-label="Bar chart of top languages in a region"></canvas></div>
</section>

<section aria-labelledby="h-find">
<h2 id="h-find">What the data shows (2016)</h2>
<ul>
<li>Kalgoorlie has the lowest English use of the four regions (57.7%) and the highest use of Aboriginal and Torres Strait Islander languages (35.8%).</li>
<li>In the Kalgoorlie region, Western Desert languages are widely spoken: 18.9% speak Ngaanyatjarra and 6.4% speak Pitjantjatjara.</li>
<li>In Perth, 88.8% speak English at home and 2.3% speak an Aboriginal language, mostly Nyungar. The South-Western WA figure is 1.6%.</li>
<li>Between 2016 and 2021, the share speaking an Aboriginal language rose in Perth (2.3% to 4.4%) and Geraldton (3.0% to 5.1%).</li>
</ul>
</section>

<section>
<h2>About the data</h2>
<p class="note">Source: Australian Bureau of Statistics, <em>Language Statistics for Aboriginal and Torres Strait Islander Peoples, 2021</em> (Tables 1.5 and 2.5, Western Australia). Figures are the percentage of Aboriginal and Torres Strait Islander people in each region, worked out from the counts in the spreadsheet.</p>
<p class="note">People can speak more than one language at home, so the percentages for a region add up to more than 100%. "Not stated" responses are left out of the charts. The charts cover four regions: Geraldton, Kalgoorlie, Perth and South-Western WA. Small random adjustments are applied by the ABS to protect privacy.</p>
</section>
</main>
<script>
const D={"2016":{"Geraldton":{"total":6169,"english":88.2,"atsi":3.0,"other":2.6,"ns":8.3,"top":[["Wajarri",1.1],["Banyjima",0.1],["Martu Wangka",0.1],["Kriol",0.1],["Nyungar",0.0]]},"Kalgoorlie":{"total":5631,"english":57.7,"atsi":35.8,"other":32.7,"ns":6.2,"top":[["Ngaanyatjarra",18.9],["Pitjantjatjara",6.4],["Martu Wangka",3.0],["Wangkatha",2.9],["Nyungar",0.2],["Yumplatok (Torres Strait Creole)",0.2]]},"Perth":{"total":29118,"english":88.8,"atsi":2.3,"other":3.2,"ns":7.4,"top":[["Nyungar",0.9],["Yumplatok (Torres Strait Creole)",0.1],["Wangkatha",0.1],["Kriol",0.1],["Wajarri",0.1],["Yawuru",0.0]]},"South-Western WA":{"total":11795,"english":92.8,"atsi":1.6,"other":1.8,"ns":4.8,"top":[["Nyungar",0.6],["Kriol",0.1],["Wangkatha",0.1],["Walmajarri",0.1],["Bardi",0.0],["Yawuru",0.0]]}},"2021":{"Geraldton":{"total":6114,"english":86.4,"atsi":5.1,"other":5.8,"ns":7.8,"top":[["Wajarri",2.5],["Martu Wangka",0.5],["Wangkatha",0.2],["Nyungar",0.1],["Tjupany",0.1],["Badimaya",0.1]]},"Kalgoorlie":{"total":5221,"english":56.6,"atsi":32.1,"other":32.9,"ns":10.5,"top":[["Ngaanyatjarra",19.0],["Wangkatha",4.3],["Pitjantjatjara",3.1],["Martu Wangka",2.3],["Nyungar",0.6],["Tjupany",0.2]]},"Perth":{"total":38984,"english":85.8,"atsi":4.4,"other":5.9,"ns":8.3,"top":[["Nyungar",2.3],["Wajarri",0.2],["Wangkatha",0.2],["Martu Wangka",0.1],["Kriol",0.1],["Yumplatok (Torres Strait Creole)",0.1]]},"South-Western WA":{"total":14355,"english":89.4,"atsi":3.9,"other":4.9,"ns":5.7,"top":[["Nyungar",2.3],["Wajarri",0.1],["Walmajarri",0.1],["Ngaanyatjarra",0.0],["Banyjima",0.0],["Nyikina",0.0]]}}};
const css=n=>getComputedStyle(document.documentElement).getPropertyValue(n).trim();
const $=id=>document.getElementById(id);
const names={english:'English',atsi:'Aboriginal and Torres Strait Islander languages',other:'Other languages'};
const colors={english:'--sea',atsi:'--red',other:'--sand'};
let c1,c2;
function bar(ctx,labels,vals,color,xtitle){
  return new Chart(ctx,{type:'bar',data:{labels,datasets:[{data:vals,backgroundColor:color,borderRadius:3}]},
  options:{indexAxis:'y',maintainAspectRatio:false,animation:{duration:300},
  plugins:{legend:{display:false},tooltip:{callbacks:{label:i=>i.parsed.x+'% of people'}}},
  scales:{x:{beginAtZero:true,title:{display:true,text:xtitle,color:css('--mute')},ticks:{color:css('--mute'),callback:v=>v+'%'},grid:{color:css('--line')}},
          y:{ticks:{color:css('--ink')},grid:{display:false}}}}});
}
function draw1(){
  const y=$('year').value,m=$('measure').value;
  const rows=Object.entries(D[y]).map(([k,v])=>[k,v[m]]).sort((a,b)=>b[1]-a[1]);
  if(c1)c1.destroy();
  c1=bar($('c1'),rows.map(r=>r[0]),rows.map(r=>r[1]),css(colors[m]),'People speaking '+names[m]+' at home ('+y+')');
}
function fillRegions(){
  const y=$('year').value,sel=$('region'),old=sel.value;
  sel.innerHTML=Object.keys(D[y]).map(k=>`<option>${k}</option>`).join('');
  if(D[y][old])sel.value=old;
}
function draw2(){
  const y=$('year').value,r=D[y][$('region').value];
  if(c2)c2.destroy();
  c2=bar($('c2'),r.top.map(t=>t[0].replace(' (Torres Strait Creole)','')),r.top.map(t=>t[1]),css('--red'),'People speaking each language at home ('+y+')');
}
$('year').onchange=()=>{fillRegions();draw1();draw2()};
$('measure').onchange=draw1;
$('region').onchange=draw2;
fillRegions();draw1();draw2();
</script>
</body>
</html>
