/* 同一双语故事的确定性画面。所有帧只依赖场景时间；数学例子与公开 Lean 特例分别标明依据。 */
'use strict';
FILM.hud = false;
function heading(en, zh, a) {
  txt(en, 960, 215, {size: 43, fam: F.disp, w: 700, align: 'center', c: C.white, a});
  txt(zh, 960, 270, {size: 32, fam: F.zh, align: 'center', c: C.dim, a});
}
function math(s, x, y, a, c = C.white, size = 48) {
  txt(s, x, y, {size, fam: F.math, align: 'center', c, a});
}
function node(x, y, label, a, c = C.cyan) {
  chip(x, y, 230, 90, label, c, a, 37, F.math);
}
SCENES.chain = S => {
  const a = clamp(S.u / 0.5);
  badge(a, 'computed');
  heading('KILLED DOES NOT MEAN SPLIT OFF', '被消掉，不等于能独立拆出', a);
  math('J(a,b) = (b,0)', 960, 360, a);
  node(530, 500, 'e₁', a); node(1080, 500, 'e₀', a);
  arrow(660, 500, 940, 500, C.cyan, at(S, 0, 1.4), 5);
  arrow(1210, 500, 1470, 500, C.cyan, at(S, 1, 1.0), 5);
  math('0', 1520, 510, at(S, 1, 1), C.dim);
  panel(390, 635, 1140, 145, at(S, 1, 0.6), C.argued);
  math('K = I = span(e₀)', 960, 695, at(S, 1, 0.6), C.argued, 42);
  txt('No invariant complementary line / 没有不变补直线', 960, 748, {size: 27, fam: F.zh, align: 'center', c: C.white, a: at(S, 1, 0.6)});
};
SCENES.tensor = S => {
  const a = clamp(S.u / 0.5), p = at(S, 1, 1.0);
  badge(a, 'computed'); heading('TWO SLOTS, FOUR BASIS WORDS', '两个位置，四个基词', a);
  node(480, 430, 'e₁ ⊗ e₁', a); node(1120, 430, 'e₀ ⊗ e₀', a);
  arrow(615, 430, 985, 430, C.cyan, p, 5);
  arrow(1250, 430, 1475, 430, C.cyan, p, 5); math('0', 1520, 442, p, C.dim);
  node(600, 650, 'e₀ ⊗ e₁', a, C.argued); node(1320, 650, 'e₁ ⊗ e₀', a, C.argued);
  ring(600, 650, 150, C.argued, p, 3); ring(1320, 650, 150, C.argued, p, 3);
  txt('Z: independent null line', 600, 825, {size: 24, fam: F.disp, align: 'center', c: C.argued, a:p});
  txt('Z: 独立零作用直线', 1320, 825, {size: 24, fam: F.zh, align: 'center', c: C.argued, a:p});
};
SCENES.split = S => {
  const a = clamp(S.u / 0.5), p = at(S, 1, 1.2), q = at(S, 2, 1.0);
  badge(a, 'argued'); heading('KEEP THE OUTPUTS IN THE COMPLEMENT', '把所有输出留在补空间', a);
  panel(250, 355, 1420, 385, a, C.cyan);
  fillBox(300, 405, 360, 175, C.argued, 0.13*a);
  fillBox(660, 405, 340, 175, C.mag, 0.17*a);
  fillBox(1000, 405, 360, 175, C.cyan, 0.1*a);
  fillBox(1360, 405, 260, 175, C.dim, 0.08*a);
  math('L', 480, 510, p, C.argued, 64);
  math('K ∩ I', 830, 510, a, C.mag, 42);
  math('I₀', 1180, 510, a, C.cyan, 64);
  txt('extra / 其他',1490,505,{size:28,fam:F.zh,align:'center',c:C.dim,a});
  line(660, 385, 660, 600, C.argued, p, 4);
  math('K = L ⊕ (K ∩ I)', 650, 650, a, C.white, 37);
  math('I = (K ∩ I) ⊕ I₀', 1190, 705, p, C.cyan, 37);
  txt('U contains the last three pieces / U 包含右侧三部分',960,765,{size:27,fam:F.zh,align:'center',c:C.cyan,a:q});
  math('W = L ⊕ U', 960, 825, q, C.white, 48);
};
SCENES.budget = S => {
  const a = clamp(S.u/0.5), p = at(S,1,1.2);
  badge(a,'argued'); heading('TWO LOSSES OF AT MOST R', '两次损失，各至多为 R', a);
  const x=300,y=430,w=1320;
  box(x,y,w,120,C.cyan,a);
  fillBox(x+2,y+2,w*0.16,116,C.mag,a*0.8);
  fillBox(x+w*0.16,y+2,w*0.16,116,C.argued,p*0.8);
  fillBox(x+w*0.32,y+2,w*0.68-2,116,C.cyan,p*0.3);
  txt('≤ R',x+w*0.08,y+75,{size:37,fam:F.math,align:'center',c:C.white,a});
  txt('≤ R',x+w*0.24,y+75,{size:37,fam:F.math,align:'center',c:C.white,a:p});
  txt('null summand L / 零作用直和项',x+w*0.66,y+75,{size:30,fam:F.zh,align:'center',c:C.white,a:p});
  txt('reach K / 取共同核',400,610,{size:27,fam:F.zh,align:'center',c:C.mag,a});
  txt('remove K ∩ I / 去交集',740,660,{size:27,fam:F.zh,align:'center',c:C.argued,a:p});
  math('μ(W) ≥ dim(W) − 2R',960,780,p,C.argued,54);
  txt('Schematic dimensions / 维数示意，非比例',960,350,{size:24,fam:F.zh,align:'center',c:C.dim,a});
};
SCENES.decay = S => {
  const a=clamp(S.u/0.5), p=at(S,1,1), q=at(S,2,1);
  badge(a,'argued'); heading('DIMENSION OUTGROWS EVERY ACTION RANK', '总维数比每个作用秩增长更快', a);
  math('dⁿ − 2 Σ rₛⁿ ≤ μ ≤ b(n) ≤ dⁿ',960,370,p,C.argued,48);
  const n=1+Math.min(4,Math.floor(at(S,1,8)*5));
  const total=2**n,lower=total-2;
  txt('Example / 例：S = {0,J}, d = 2, ranks = 0,1',960,455,{size:28,fam:F.zh,align:'center',c:C.dim,a:p});
  box(320,505,1280,110,C.cyan,p);
  fillBox(322,507,1276*(lower/total),106,C.cyan,0.35*p);
  txt('n = '+n+'     guaranteed null dimension ≥ '+lower+' / '+total,960,575,{size:31,fam:F.disp,align:'center',c:C.white,a:p});
  math('0 ≤ 1 − b(n)/dⁿ ≤ 2 Σ (rₛ/d)ⁿ → 0',960,745,q,C.white,44);
  txt('Displayed numbers: computed example / 显示数值为例子的准确计算',960,815,{size:24,fam:F.zh,align:'center',c:C.dim,a:p});
};
SCENES.correction = S => {
  const a=clamp(S.u/0.5),p=at(S,1,1);
  badge(a,'computed'); heading('ALWAYS ONE SHORT', '每次差一，相对亏量却趋于零', a);
  const ns=[1,2,3,4], xx=[435,785,1135,1485];
  txt('Right-zero example / 右零例子',960,350,{size:29,fam:F.zh,align:'center',c:C.dim,a});
  for(let i=0;i<4;i++) {
    const n=ns[i],total=2**n,b=total-1;
    panel(xx[i]-140,400,280,285,a,C.cyan);
    math('n = '+n,xx[i],460,a,C.dim,36);
    math(b+' / '+total,xx[i],555,a,C.cyan,54);
    txt('b(n) / 2ⁿ',xx[i],630,{size:30,fam:F.math,align:'center',c:C.white,a});
  }
  math('b(n) = 2ⁿ − 1     ≠ 2ⁿ',960,770,p,C.white,52);
  txt('Literal equality corrected; ratio limit retained / 修正等式，保留渐近式',960,830,{size:27,fam:F.zh,align:'center',c:C.argued,a:p});
};
SCENES.scope = S => {
  const a=clamp(S.u/0.5),p=at(S,1,0.6),q=at(S,2,0.6);
  if(p>0) badge(p,'lean');
  heading('PUBLIC LEAN: THE QUALITATIVE CASE', '公开 Lean：原猜想的定性情形', a);
  txt('He–Tubbenhauer: question and prior case · Ma–Zhang: extension',960,345,{size:29,fam:F.disp,align:'center',c:C.white,a});
  panel(300,390,1320,390,p,C.lean);
  txt('Algebraically closed field / 代数闭域',960,455,{size:33,fam:F.zh,align:'center',c:C.white,a:p});
  txt('Finite, nonempty, no identity / 有限、非空、无单位元',960,515,{size:32,fam:F.zh,align:'center',c:C.white,a:p});
  txt('Finite-dimensional multiplicative action, all singular',960,575,{size:31,fam:F.disp,align:'center',c:C.white,a:p});
  math('∃ m ≥ 1: Z splits off',960,650,q,C.lean,42);
  txt('Count sequence exists; every count sequence has ratio limit 1',960,715,{size:28,fam:F.disp,align:'center',c:C.lean,a:q});
  txt('Quantitative formulas: separate manuscript arguments / 定量公式另据论文论证',960,830,{size:26,fam:F.zh,align:'center',c:C.dim,a:q});
};
FILM.poster = () => {
  txt('从共同零空间到独立直和项',960,180,{size:69,fam:F.zh,w:800,align:'center',c:C.white});
  txt('FROM KILLED DIRECTIONS TO NULL SUMMANDS',960,270,{size:42,fam:F.disp,w:700,align:'center',c:C.cyan});
  panel(240,340,1440,470,1,C.cyan);
  node(540,470,'e₁ ⊗ e₁',1);node(1260,470,'e₀ ⊗ e₀',1);
  arrow(680,470,1120,470,C.cyan,1,5);
  node(620,670,'e₀ ⊗ e₁',1,C.argued);node(1300,670,'e₁ ⊗ e₀',1,C.argued);
  txt('independent null lines / 独立零作用直线',960,770,{size:32,fam:F.zh,align:'center',c:C.argued});
  txt('Haobo Ma · Wenlin Zhang',960,900,{size:35,fam:F.disp,align:'center',c:C.white});
  txt('Question and earlier case: David He · Daniel Tubbenhauer',960,960,{size:27,fam:F.disp,align:'center',c:C.dim});
};
