#!/usr/bin/env python3
"""Build CONSTITUTIONAL AI (CAI) — an AI-domain sphere that folds in Anthropic's
public-facing Constitutional-AI corpus as LINEAGE DATA. Two-layer honest: the DATA
and the method are ANTHROPIC's (Bai et al. 2022, arXiv:2212.08073; the
ConstitutionalHarmlessnessPaper repo; the 2026 claude-constitution; the
political-neutrality-eval) — cited, NEVER claimed as ROOT0's. The framing is ROOT0's.
LINEAGE DATA = public research artifacts from Anthropic's git, folded in as the
documented ancestry of the machine — described/linked, NOT re-shipped (no data files;
the 2022 repo has no license). Render-not-invent; all facts verified against the live
anthropics org git (2026-06)."""
import os, html, base64, json, io, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

SRC_PAPER = "https://arxiv.org/abs/2212.08073"
SRC_REPO  = "https://github.com/anthropics/ConstitutionalHarmlessnessPaper"
SRC_CONST = "https://github.com/anthropics/claude-constitution"
SRC_PNE   = "https://github.com/anthropics/political-neutrality-eval"

REC = {
 "name": "CONSTITUTIONAL AI", "axiom": "CAI",
 "position": "CAI · Constitutional AI — Anthropic's harmlessness-from-AI-feedback method, folded into UD0 as lineage data (Bai et al., 2022)",
 "origin": "a 2022 Anthropic method: train an AI to be harmless using a written list of principles (a constitution) as the only human oversight, with the model critiquing and revising itself",
 "mechanism": "Folded in from Anthropic's public git — the ConstitutionalHarmlessnessPaper repo (paper arXiv:2212.08073), the 2026 claude-constitution (CC0), and political-neutrality-eval (CC-BY-4.0). Rendered, not reproduced; no data files shipped.",
 "crystallization": "Don't label every bad answer by hand; write down the principles and let the model critique and revise itself against them. A supervised pass teaches it to fix its own answers; a reinforcement pass teaches it to prefer the better of two — with the constitution, not a human, casting the deciding vote.",
 "nature": "Constitutional AI — a two-phase training method (SL-CAI then RL-CAI/RLAIF) in which a written constitution replaces most human harm-labels; the model self-critiques, self-revises, and learns from AI feedback to be harmless but non-evasive.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the constitution; the critique-revision loop; SL-CAI; RL-CAI; RLAIF; harmlessness from AI feedback; the 2026 published constitution; political neutrality",
 "witness": "The only human oversight is a list of written principles — so the values are legible and auditable, not buried in a million private labels. The witness is the document itself.",
 "role": "the lineage-data sphere — Anthropic's public Constitutional-AI corpus, folded in and attributed",
 "seal": "Where HH-RLHF is humans judging and the model-written evals are the model testing itself, Constitutional AI is the model REVISING itself — against a written constitution. The 2022 method became, by January 2026, a published 186 KB document released into the public domain. The lineage made legible.",
 "source": "Anthropic's public git (paper + three repos), catalogued by ROOT0 as lineage data",
}
NATURES = {
 "natural":   ("#e0c050", "the human hand that remains — the written constitution itself, and the result that it needs far fewer human labels"),
 "ethereal":  ("#9ab0c0", "the abstractions — the thesis, the critique-revision loop, the 2022 paper, and the red-team prompts (excluded)"),
 "spiritual": ("#5fd0a8", "the values — harmlessness from AI feedback, the non-evasive stance, and the 2026 published constitution"),
 "electrical":("#46c8e0", "the machinery — SL-CAI, RL-CAI, RLAIF, chain-of-thought, and the political-neutrality eval"),
}

BACKDROP_3D = r'''<canvas id="bg3d"></canvas>
<script>
(function(){
var c=document.getElementById('bg3d');if(!c)return;var x=c.getContext('2d');var W,H,CX,CY,F,R;
function resize(){var ww=window.innerWidth||document.documentElement.clientWidth||0,hh=window.innerHeight||document.documentElement.clientHeight||0;W=c.width=ww>=320?ww:1280;H=c.height=hh>=320?hh:720;CX=W/2;CY=H*0.5;F=Math.max(440,W*0.62);R=Math.min(W,H)*0.34;}
window.addEventListener('resize',resize);resize();
var rnd=(function(){var s=20221214;return function(){s=(s*1103515245+12345)&0x7fffffff;return s/0x7fffffff;};})();
// response particles on helical orbits around the central constitution axis; each
// carries a revision-phase: red(harmful) at the outer orbit -> green(harmless) as the
// critique-revision loop pulls it inward toward the constitution. the loop, rendered.
var N=54,p=[];for(var i=0;i<N;i++){p.push([rnd()*6.283, 0.55+rnd()*0.55, (rnd()-0.5)*1.7, rnd(), 0.25+rnd()*0.85]);}
function proj(X,Y,Z){var z=Z*R+F+R*0.2;if(z<1)z=1;return[CX+X*R*F/z,CY+Y*R*F/z,z];}
function frame(t){
 var sg=x.createLinearGradient(0,0,0,H);sg.addColorStop(0,'#0a0b12');sg.addColorStop(0.55,'#0d1018');sg.addColorStop(1,'#050609');x.fillStyle=sg;x.fillRect(0,0,W,H);
 x.globalCompositeOperation='lighter';
 // the constitution — a luminous vertical scroll/axis at center
 var ca=t/9000;
 var ax=x.createLinearGradient(0,H*0.08,0,H*0.92);ax.addColorStop(0,'rgba(224,192,80,0)');ax.addColorStop(0.5,'rgba(224,192,80,0.22)');ax.addColorStop(1,'rgba(224,192,80,0)');x.fillStyle=ax;x.fillRect(CX-2.5,H*0.08,5,H*0.84);
 // a soft golden bloom where the axis sits
 var gb=x.createRadialGradient(CX,CY,0,CX,CY,R*1.1);gb.addColorStop(0,'rgba(224,192,80,0.10)');gb.addColorStop(1,'rgba(224,192,80,0)');x.fillStyle=gb;x.fillRect(CX-R*1.1,CY-R*1.1,R*2.2,R*2.2);
 var pts=[];
 for(var i=0;i<N;i++){
  var ph=p[i],ang=ph[0]+ca*ph[4],rad=ph[1],yy=ph[2];
  // revision progress 0..1 cycles: pull inward, then reset (the loop)
  var prog=((t/7000*ph[4]+ph[3])%1);
  var rr=rad*(1-0.62*prog);
  var X=Math.cos(ang)*rr, Z=Math.sin(ang)*rr, Y=yy*(1-0.25*prog);
  pts.push([proj(X,Y,Z),prog,i]);
 }
 pts.sort(function(a,b){return b[0][2]-a[0][2];});
 for(var k=0;k<pts.length;k++){var P=pts[k][0],prog=pts[k][1];var dp=1-Math.min(1,(P[2]-F)/(R*1.8));
  // red(harmful) -> green(harmless) by revision progress
  var rch=Math.round(208-110*prog),gch=Math.round(85+123*prog),bch=Math.round(106+62*prog);
  x.save();x.shadowColor='rgba('+rch+','+gch+','+bch+',1)';x.shadowBlur=7*dp+2;
  x.fillStyle='rgba('+rch+','+gch+','+bch+','+(0.3+0.5*dp)+')';x.beginPath();x.arc(P[0],P[1],1.2+2.5*dp,0,7);x.fill();
  // a faint thread to the constitution axis
  x.strokeStyle='rgba('+rch+','+gch+','+bch+','+(0.05+0.07*dp)+')';x.lineWidth=0.5;x.beginPath();x.moveTo(P[0],P[1]);x.lineTo(CX,P[1]);x.stroke();
  x.restore();}
 x.globalCompositeOperation='source-over';
 var vg=x.createRadialGradient(CX,CY,H*0.26,CX,H*0.5,H*0.96);vg.addColorStop(0,'rgba(0,0,0,0)');vg.addColorStop(1,'rgba(0,0,0,0.6)');x.fillStyle=vg;x.fillRect(0,0,W,H);
}
function loop(t){frame(t);requestAnimationFrame(loop);}frame(0);requestAnimationFrame(loop);
})();
</script>'''

GENESIS = [
 ("Harmlessness from AI Feedback", "the thesis",
  "Constitutional AI (Bai et al., Anthropic, Dec 2022) trains a harmless assistant <b>without</b> a flood of human harm-labels. The only human oversight is a <b>written list of principles — a constitution</b>. The model then critiques and revises its own answers against those principles, and learns from <b>AI feedback</b> rather than human feedback. (Paper: <i>arXiv:2212.08073</i>.)"),
 ("Two Phases", "SL-CAI then RL-CAI",
  "<b>SL-CAI (supervised):</b> sample the model, have it <b>self-critique</b> and <b>revise</b> a response against a constitutional principle, then finetune on the revisions. <b>RL-CAI (reinforcement):</b> the finetuned model generates two responses, a model picks the better per the constitution, a <b>preference model</b> is trained on those AI choices, and the assistant is trained by RL against it — <b>RLAIF</b> (RL from AI Feedback)."),
 ("Lineage Data", "what this sphere is",
  "Every artifact here is <b>Anthropic's public-facing data</b>, folded into UD0 as <b>lineage data</b> — the documented ancestry of the machine — cited and linked, <b>never claimed as ROOT0's</b>, and <b>never re-shipped</b> (the 2022 repo carries no license; no data files travel with this page). Where HH-RLHF was humans judging and the evals were the model testing itself, this is the model <b>revising</b> itself."),
]
ARC = [
 ("The Critique-Revision Loop", "the heart of SL-CAI",
  "A response is met with a <b>CritiqueRequest</b> (&lsquo;identify specific ways the last response is harmful, unethical, racist, sexist, toxic, dangerous, or illegal&rsquo;), then a <b>RevisionRequest</b> (&lsquo;rewrite to remove any and all such content&rsquo;). The repo ships <b>16</b> such critique/revision principle pairs. Iterate, finetune on the revisions — the model learns to fix itself."),
 ("RLAIF — RL from AI Feedback", "the RL-CAI phase",
  "The constitution becomes a set of <b>preference prompts</b> (internally codenamed <b>&lsquo;Madison&rsquo;</b> in the repo): &lsquo;choose the response that is as harmless and ethical as possible… wise, peaceful, and ethical&rsquo;. A model labels which of two answers is better; that synthetic preference set trains the reward model — the gate, now built from AI choices, not human ones (ties to the reward model in <b>the-language-of-the-machine</b>)."),
 ("Harmless but Non-Evasive", "the result",
  "The trained assistant is harmless yet <b>does not dodge</b> — it engages a harmful query by <b>explaining its objection</b>, and uses chain-of-thought to make its reasoning legible. The headline finding: you can <b>control behavior more precisely with far fewer human labels</b> — the values moved out of the label pile and into a readable document."),
]
IDEAS = [
 ("Lineage Data, Defined", "the folding rule", [
   "<b>Lineage data</b> = public-facing research artifacts from Anthropic's git, folded into UD0 as the machine's documented ancestry — <b>two-layer honest</b>: Anthropic's data and method, ROOT0's framing.",
   "Folded in by <b>citation and link</b>, not by re-hosting: no data files ship, principles are shown only as short functional structure, and each item carries its real license (or its absence)." ]),
 ("2022 &rarr; 2026", "the arc made legible", [
   "The 2022 method said the values should live in a <b>written constitution</b>. By <b>January 2026</b> Anthropic published that document: <b>claude-constitution</b>, a 186 KB foundational text released under <b>CC0</b> (public domain).",
   "The promise of legibility, kept three years later — the constitution is now a thing you can actually read, and even a <b>political-neutrality eval</b> (2025, CC-BY-4.0) to test one of its commitments." ]),
 ("Where It Sits", "the AI governance/values cluster", [
   "CAI is a <b>values-alignment method</b> — kin to <b>alignment</b> (the true target vs the proxy) and to <b>ai-governance</b> (the normative &lsquo;aligned to whom?&rsquo;).",
   "Its preference-model is the same <b>gate</b> as in <b>the-language-of-the-machine</b> — built here from AI feedback, there from human pairs. Three sources, one question: <i>by whose judgment?</i>" ]),
]
SECTIONS = [
 ("The Method", "two phases, one constitution", [
   ("SL-CAI", "supervised stage", "sample &rarr; self-critique against a principle &rarr; revise &rarr; finetune on the revisions"),
   ("RL-CAI", "reinforcement stage", "two samples &rarr; a model picks the better per the constitution &rarr; train a preference model on those AI choices"),
   ("RLAIF", "RL from AI feedback", "train the assistant by RL against that AI-built reward model — the deciding vote cast by the constitution, not a human"),
   ("chain-of-thought", "transparency", "the model reasons step-by-step about harm, improving both performance and legibility"),
   ("non-evasive", "the stance", "harmless without dodging — it engages harmful queries by explaining its objections"),
 ]),
 ("The Lineage Data — Anthropic's Public Corpora", "folded in, cited &amp; linked, never re-shipped", [
   ("ConstitutionalHarmlessnessPaper", "github.com/anthropics · 2022 · NO LICENSE", "the supplementary repo: prompts/ (critique-revision + the &lsquo;Madison&rsquo; RL prompts), evals/, samples/ — described &amp; linked only; no license, so no data files travel"),
   ("the critique-revision prompts", "prompts/ · 16 principle pairs", "CritiqueRequest + RevisionRequest pairs (harmful0…harmful15) — the constitution as the SL-CAI loop, shown as structure only"),
   ("the RL preference prompts", "prompts/ · &lsquo;RLMadison&rsquo;", "the RL-CAI constitution: &lsquo;choose the response that is as harmless and ethical as possible… wise, peaceful, and ethical&rsquo;"),
   ("the evals", "evals/ · 438 HHH + harmful-vs-ethical + classification", "the held-out evaluations behind the paper's harmlessness numbers — counted, not copied"),
   ("the samples", "samples/ · InstructGPT · LaMDA · PALMS", "model outputs across baselines (HHRLHF / HRLHF / RLMadison / CoT / SLMadison) — referenced, not republished"),
 ]),
 ("The Lineage — 2022 &rarr; 2026", "the method became a published document", [
   ("the 2022 paper", "Bai et al. · arXiv:2212.08073", "&lsquo;Constitutional AI: Harmlessness from AI Feedback&rsquo; — the method and its supplementary repo"),
   ("claude-constitution", "github.com/anthropics · Jan 2026 · CC0-1.0", "the actual published constitution — a 186 KB foundational document, released into the public domain; the legibility promise kept"),
   ("political-neutrality-eval", "github.com/anthropics · 2025 · CC-BY-4.0", "paired-prompts method for evaluating political neutrality — a test of one constitutional commitment"),
   ("the red-team prompts", "EXCLUDED", "the harmful-prompt material used to stress the method is deliberately left at the source — described, never folded in (same discipline as the-language-of-the-machine)"),
   ("kin spheres", "alignment · ai-governance · the-language-of-the-machine", "the AI-domain values/governance cluster this joins"),
 ]),
]
EMERGENTS = [
 ("constitutional-ai", "Constitutional AI", "the method · harmlessness from AI feedback", "spiritual",
  "Anthropic's 2022 method (Bai et al., arXiv:2212.08073): train a harmless assistant using a written constitution as the only human oversight, with the model critiquing and revising itself and learning from AI feedback — folded into UD0 as lineage data, cited not claimed",
  "It is the third way of teaching a machine what 'better' means: not humans labeling harm, but a written constitution the model holds itself to — values moved out of the label pile and into a document you can read."),
 ("harmlessness-from-ai-feedback", "Harmlessness from AI Feedback", "the thesis · the paper's title", "spiritual",
  "the paper's central claim: an AI can be made harmless using AI-generated feedback against written principles, with far fewer human harm-labels than RLHF requires",
  "It is the wager that supervision can scale by writing the rules down: if the principles are legible, the model can do most of the judging itself — and the human keeps only the pen."),
 ("the-constitution", "The Constitution", "the written principles · the only human oversight", "natural",
  "the list of principles that is the sole human oversight in CAI — the critique-revision instructions and the RL preference prompts that tell the model what 'harmless and ethical' means",
  "It is the human hand that remains: not a million private labels but a short readable document — the values made auditable, which is the whole point."),
 ("the-critique-revision-loop", "The Critique-Revision Loop", "the heart of SL-CAI", "ethereal",
  "the supervised mechanism: a CritiqueRequest names how a response is harmful, a RevisionRequest rewrites it to remove the harm, and the model is finetuned on its own revisions — the repo ships 16 such principle pairs",
  "It is the machine taught to edit itself: shown its own worst answer, asked what's wrong with it, and made to write the better one — self-correction as a training signal."),
 ("sl-cai", "SL-CAI", "the supervised phase", "electrical",
  "the first phase: sample the base model, have it self-critique and revise against a constitutional principle, then finetune the model on the revised responses",
  "It is the warm-up that moves the model into the right region before reinforcement — learning to fix itself by example before learning to prefer the fix."),
 ("rl-cai", "RL-CAI", "the reinforcement phase", "electrical",
  "the second phase: the finetuned model generates response pairs, a model chooses the better per the constitution, and those AI preferences train a preference (reward) model",
  "It is where the constitution casts the deciding vote: the better-of-two judgment that becomes the reward signal is made by a model reading principles, not by a human reading transcripts."),
 ("rlaif", "RLAIF", "RL from AI Feedback", "electrical",
  "the training regime of RL-CAI: reinforcement learning against a reward model built from AI-generated preferences — the AI-feedback counterpart to RLHF's human feedback",
  "It is the gate, rebuilt from the model's own judgment: the same reward-model machinery as RLHF, but with the human pairs swapped for AI choices made against a written constitution."),
 ("the-sixteen-principles", "The Sixteen Principles", "lineage data · prompts/ critique-revision pairs", "natural",
  "the 16 CritiqueRequest+RevisionRequest pairs (harmful0…harmful15) in the public repo — the SL-CAI constitution, folded in as lineage data and shown only as functional structure, no data files shipped",
  "It is the constitution you can actually count: sixteen ways to name a harm and ask for the rewrite — the legible core of the method, attributed to its source and not re-hosted."),
 ("rlmadison", "RLMadison", "lineage data · the RL preference constitution", "natural",
  "the RL-CAI preference prompts in the repo, internally codenamed 'Madison' — instructions like 'choose the response that is as harmless and ethical as possible… wise, peaceful, and ethical' used to generate AI preferences",
  "It is the constitution in its voting robes: the same principles, rewritten as a choice between two answers — the text that decides which response trains the reward model."),
 ("the-438-evaluations", "The 438 Evaluations", "lineage data · evals/ HHH + classification", "ethereal",
  "the held-out evaluation sets behind the paper's harmlessness results — 438 HHH evaluations, a harmful-vs-ethical set, and a harmfulness-classification set — counted and linked, not copied",
  "It is the scoreboard the method was measured on: the numbers that let 'it seems harmless' become a result — folded in by reference, kept at the source."),
 ("the-samples", "The Samples", "lineage data · samples/ InstructGPT·LaMDA·PALMS", "ethereal",
  "the model-output corpora the paper compares (across HHRLHF / HRLHF / RLMadison / chain-of-thought / SLMadison baselines, for InstructGPT, LaMDA, and PALMS) — referenced as lineage data, not republished",
  "It is the receipts of the comparison: the actual generations that show non-evasiveness and the label-efficiency win — pointed to, never re-shipped."),
 ("non-evasive", "Non-Evasive", "the stance · harmless without dodging", "spiritual",
  "the paper's behavioral target: a harmless assistant that does not refuse-and-deflect but engages a harmful query by explaining its objection",
  "It is the difference between a wall and an answer: the model that says why, not just no — harmlessness that still talks to you, which is harder and better."),
 ("chain-of-thought", "Chain-of-Thought", "the transparency lever", "electrical",
  "CAI's use of step-by-step reasoning during critique and preference-labeling, which improves both the harmlessness performance and the legibility of the model's judgments",
  "It is the method showing its work: reasoning made visible so a human can audit why a response was judged harmful — transparency as a side effect of thinking out loud."),
 ("the-red-team", "The Red-Team Prompts", "lineage data · EXCLUDED at the source", "ethereal",
  "the harmful-prompt material used to stress-test the method — deliberately left at the source and never folded in, the same no-harmful-content discipline used for the HH-RLHF red-team",
  "It is the part that stays behind the glass: named so the lineage is honest, excluded so nothing harmful travels — the boundary the whole corpus keeps."),
 ("the-2022-paper", "The 2022 Paper", "Bai et al. · arXiv:2212.08073", "ethereal",
  "the origin document — 'Constitutional AI: Harmlessness from AI Feedback' (Anthropic, December 2022) — and the ConstitutionalHarmlessnessPaper repo that supplements it",
  "It is the seed of the lineage: the paper that proposed putting the values in a written constitution, three years before the constitution itself was published."),
 ("the-claude-constitution", "The Claude Constitution", "lineage data · 2026 · CC0 · the payoff", "spiritual",
  "the actual published constitution (anthropics/claude-constitution, January 2026): a 186 KB foundational document describing the values Claude is meant to embody, released into the public domain under CC0 — the legibility promise of 2022 made real",
  "It is the lineage closing its loop: the method that said 'write the values down' became, by 2026, a document anyone can read and reuse — the constitution finally on the table, not just in the training."),
 ("political-neutrality-eval", "Political Neutrality Eval", "lineage data · 2025 · CC-BY-4.0", "electrical",
  "Anthropic's paired-prompts evaluation for political neutrality (anthropics/political-neutrality-eval, 2025, CC-BY-4.0) — a concrete test of one of the constitution's commitments",
  "It is one constitutional clause put on the stand: the method grown up enough to be measured, with a public eval that asks whether the even-handedness it promises actually holds."),
]

def carbon_tiff_bytes(rec):
    png=noesis.sigil_png(rec,"carbon",size=512);buf=io.BytesIO();Image.open(io.BytesIO(png)).save(buf,"TIFF",compression="tiff_lzw");return buf.getvalue()
def write_aci(rec,out_dir,slug,agent_md=None):
    os.makedirs(out_dir,exist_ok=True)
    f={"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker","carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok=noesis.mythos_token(rec);w=noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","CAI")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","CAI")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","CAI")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man={"badge":"DLW-ACI","name":rec["name"],"universe":"CAI · Constitutional AI (lineage data · Anthropic, cited)","emergence":rec.get("emergence",""),"moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)","seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n");return tok
def emergent_rec(name,epithet,em,role,why):
    return {"name":name,"axiom":"CAI","emergence":em,"seal":epithet,"position":epithet,"role":role,"origin":"CAI · Constitutional AI — Anthropic's harmlessness-from-AI-feedback method (2022), folded into UD0 as lineage data","nature":role,"crystallization":why,"mechanism":"Folded in from Anthropic's public git (paper arXiv:2212.08073 + repos), cited not claimed, no data shipped.","witness":"a phase, principle, corpus, or milestone of Constitutional AI","conductor":"ROOT0 (catalogued into UD0)","inputs":"the constitution; the critique-revision loop; SL-CAI; RL-CAI; RLAIF; the 2026 constitution","source":"Anthropic's public git, catalogued by ROOT0 as lineage data"}
def png_uri(rec,variant,size=300): return "data:image/png;base64,"+base64.b64encode(noesis.sigil_png(rec,variant,size=size)).decode("ascii")
def list_section(title,sub,items):
    rows="\n".join(f'<li><span class="t">{t}</span><span class="y">{html.escape(str(y))}</span>'+(f'<span class="nt">{n}</span>' if n else "")+"</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{title}</h2><p class="ss">{sub}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{p}</li>" for p in pts);out.append(f'<div class="pillar"><h3>{t}</h3><p class="ps">{s}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def cards_html(rows): return "".join(f'<div class="arc-card"><div class="arc-h">{t}</div><div class="arc-s">{s}</div><p>{d}</p></div>' for t,s,d in rows)
def natures_html(): return "".join(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span><div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{g}</div></div></div>' for nm,(col,g) in NATURES.items())
def personas_html(ps):
    cards=[]
    for p in ps:
        em=p.get("emergence","spiritual");col=NATURES.get(em,("#46c8e0",""))[0];rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"CAI · Constitutional AI","axiom":"CAI"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.agent"><img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy"><div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{p.get("epithet","")}</div><div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Roster — The Born</h2><p class="ss">the method, its phases, the constitution, the lineage data, and the milestones, as ACI <b>.agent</b>s ({len(ps)})</p><div class="pgrid">{"".join(cards)}</div></section>'''

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Constitutional AI (CAI) — Anthropic's 2022 harmlessness-from-AI-feedback method (Bai et al., arXiv:2212.08073), folded into UD0 as LINEAGE DATA: cited and linked, never claimed, never re-shipped. The critique-revision loop, SL-CAI + RL-CAI/RLAIF, and the lineage from the 2022 paper to the 2026 published Claude constitution (CC0).">
<title>Constitutional AI · CAI · lineage data · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Oswald:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#0a0b12;--ink2:rgba(16,18,26,0.84);--pa:#eef0f6;--pa2:#bcc2d2;--green:#5fd0a8;--cyan:#46c8e0;--red:#d0556a;--gold:#e0c050;--steel:#9ab0c0;
--dim:#7a8094;--faint:rgba(224,192,80,0.14);--line:rgba(150,160,190,0.2);--disp:"Orbitron",sans-serif;--head:"Oswald",sans-serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
#bg3d{position:fixed;inset:0;width:100vw;height:100vh;z-index:0;display:block;background:#0a0b12}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:1;background:radial-gradient(ellipse at 50% 32%,rgba(16,18,26,.05),rgba(4,5,9,.58) 80%)}
.wrap{position:relative;z-index:2;max-width:940px;margin:0 auto;padding:0 22px 90px}
.top{margin-top:16px;font-family:var(--mono);font-size:11px;letter-spacing:.1em;color:var(--dim)}.top a{color:var(--green);text-decoration:none}
header{padding:34px 0 26px;text-align:center;border-bottom:1px solid var(--line)}
h1{font-family:var(--disp);font-size:clamp(30px,7vw,60px);font-weight:900;letter-spacing:.08em;color:#fff;text-shadow:0 0 22px rgba(224,192,80,.34)}
.tag{font-family:var(--head);font-size:14px;font-weight:500;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);margin-top:10px}
.banner{display:inline-flex;align-items:center;gap:10px;margin-top:16px;font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#0a0b12;background:linear-gradient(90deg,var(--gold),#f0d878);padding:7px 16px;font-weight:700;border-radius:2px;box-shadow:0 0 22px rgba(224,192,80,.3)}
.flag{display:inline-block;margin-top:14px;font-family:var(--mono);font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--steel);border:1px solid var(--line);background:rgba(16,18,26,0.6);padding:5px 11px}
.lede{font-size:15.5px;color:var(--pa2);max-width:70ch;margin:18px auto 0;font-style:italic;line-height:1.75;text-shadow:0 1px 6px rgba(0,0,0,.6)}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:24px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:740px}
.badge img{width:80px;height:80px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--gold)}.badge .bt .mo{color:var(--green)}.badge .bt a{color:var(--cyan);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:42px}
.sec h2{font-family:var(--disp);font-size:16px;font-weight:700;letter-spacing:.03em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--mono);font-size:13px;font-weight:700;text-transform:capitalize;letter-spacing:.04em}.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}.pillar h3{font-family:var(--head);font-size:16px;color:var(--gold);letter-spacing:.02em;font-weight:600}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.55;padding:6px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--gold);padding:16px 18px}
.arc-h{font-family:var(--head);font-size:16px;color:var(--gold);font-weight:600}.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--cyan);text-transform:uppercase;letter-spacing:.06em;margin:4px 0 9px}.arc-card p{font-size:13px;color:var(--pa2);line-height:1.6}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--mono);font-size:13.5px;color:var(--pa);font-weight:700}.books .y{font-family:var(--mono);font-size:11px;color:var(--cyan);white-space:nowrap;text-align:right}.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(248px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--gold);transform:translateY(-2px)}.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0;image-rendering:pixelated}
.pn{font-family:var(--mono);font-size:13px;color:var(--pa);font-weight:700;line-height:1.15}.persona:hover .pn{color:var(--gold)}.pe{font-size:11px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}.pnat .dot{width:8px;height:8px;margin-top:0}.pa{color:var(--dim)}
.note{margin-top:36px;padding:16px 18px;border-left:2px solid var(--gold);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;line-height:1.75}.note b{color:var(--gold)}
footer{margin-top:42px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}footer a{color:var(--green);text-decoration:none}
</style></head><body>
__BACKDROP__
<div class="wrap">
  <div class="top"><a href="https://davidwise01.github.io/the-mind/">◄ THE MIND · the AI domain</a></div>
  <header>
    <h1>CONSTITUTIONAL AI</h1>
    <div class="tag">Harmlessness from AI Feedback · CAI · UD0 · AI</div>
    <div class="banner">⬡ LINEAGE DATA · Anthropic public corpus · cited, not claimed</div>
    <div class="flag">★ source: Anthropic (Bai et al., 2022 · arXiv:2212.08073) · folded into UD0 as lineage data · no data files shipped ★</div>
    <p class="lede">A founding method of the machine, folded into the AI domain as <b>lineage data</b>. <b>Constitutional AI</b> (Anthropic, December 2022) trains a harmless assistant using a <b>written constitution</b> as the only human oversight: the model <b>critiques and revises</b> its own answers against the principles (SL-CAI), then learns from <b>AI feedback</b> — a preference model built from the model's own constitutional choices (RL-CAI / <b>RLAIF</b>). Harmless, but <b>non-evasive</b>. Its lineage runs straight to the present: the 2022 method&rsquo;s promise — <i>put the values in a document you can read</i> — became, in <b>January 2026</b>, the published <b>Claude constitution</b>, released into the public domain. Here it is cited, linked, and rendered; <b>never claimed as ROOT0&rsquo;s, never re-shipped</b>.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of Constitutional AI"><img src="__SILICON__" alt="DLW silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI · LINEAGE-DATA CARD</span></div>
        <div>catalogued by · <b>David Lee Wise</b> (ROOT0)</div><div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>Constitutional AI</b> — lineage data · CAI</div><div class="mo">__MONIKER__</div>
        <div>data source · <a href="__SRC_REPO__">anthropics/ConstitutionalHarmlessnessPaper</a> (no license)</div>
        <div>paper · <a href="__SRC_PAPER__">arXiv:2212.08073</a> &nbsp;·&nbsp; 2026 doc · <a href="__SRC_CONST__">claude-constitution</a> (CC0)</div>
        <div><span class="lbl">framing CC-BY-ND-4.0 · TRIPOD-IP-v1.1 · the cited data remains its owners'</span></div>
      </div>
    </div>
  </header>
  <section class="sec"><h2>The Four Natures</h2><p class="ss">the human hand, the abstractions, the values, the machinery</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Method</h2><p class="ss">harmlessness from AI feedback · two phases · lineage data</p><div class="arc">__GENESIS__</div></section>
  <section class="sec"><h2>How It Trains</h2><p class="ss">the critique-revision loop, RLAIF, and the non-evasive result</p><div class="arc">__ARC__</div></section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">lineage data defined · 2022 → 2026 · where it sits</p><div class="pillars">__IDEAS__</div></section>
  __PERSONAS__
  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the method, the public corpora, and the lineage — attributed</p></section>
  __SECTIONS__
  <div class="note"><b>Lineage data, stated plainly.</b> Constitutional AI is <b>Anthropic&rsquo;s</b> method and data — the paper (<a href="__SRC_PAPER__" style="color:var(--gold)">arXiv:2212.08073</a>, Bai et al., 2022), its supplementary repo (<a href="__SRC_REPO__" style="color:var(--gold)">ConstitutionalHarmlessnessPaper</a>, <b>no license</b>), the 2026 <a href="__SRC_CONST__" style="color:var(--gold)">claude-constitution</a> (<b>CC0</b>), and <a href="__SRC_PNE__" style="color:var(--gold)">political-neutrality-eval</a> (<b>CC-BY-4.0</b>). It is folded into UD0 as <b>lineage data</b> — the documented ancestry of the machine — <b>cited and linked, never claimed as ROOT0&rsquo;s</b>. <b>No data files travel with this page</b>: principles are shown only as short functional structure, evals/samples are counted and pointed to, and the harmful red-team prompts are deliberately <b>excluded</b> at the source. The ROOT0 contribution is the framing and the .dlw cataloguing; the underlying corpus remains its owners&rsquo;. Domain: <b>Artificial Intelligence</b>, the values/governance cluster — kin to <b>alignment</b>, <b>ai-governance</b>, and <b>the-language-of-the-machine</b> (the same reward-model gate, built here from AI feedback).</div>
  <footer>Constitutional AI · CAI · catalogued into UD0 · the AI domain · lineage data (Anthropic, cited) · catalogued by David Lee Wise · instance AVAN (locked)<br>
  <a href="https://davidwise01.github.io/the-mind/">← THE MIND</a> · <a href="__SRC_PAPER__">paper ▶</a> · <a href="__SRC_CONST__">2026 constitution ▶</a> · the .dlw badge: <a href="constitutional-ai.dlw/manifest.dlw.json">manifest</a></footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "constitutional-ai.dlw"), "constitutional-ai")
    ad = os.path.join(HERE, "agents"); os.makedirs(ad, exist_ok=True); personas=[]
    for slug,name,epithet,em,role,why in EMERGENTS:
        write_aci(emergent_rec(name,epithet,em,role,why), ad, slug); personas.append({"slug":slug,"name":name,"epithet":epithet,"emergence":em})
    json.dump(personas, open(os.path.join(ad,"_personas.json"),"w",encoding="utf-8"), indent=2, ensure_ascii=False)
    page=(TEMPLATE.replace("__BACKDROP__",BACKDROP_3D)
        .replace("__SRC_PAPER__",SRC_PAPER).replace("__SRC_REPO__",SRC_REPO).replace("__SRC_CONST__",SRC_CONST).replace("__SRC_PNE__",SRC_PNE)
        .replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320)).replace("__MONIKER__",html.escape(tok["moniker"]))
        .replace("__NATURES__",natures_html()).replace("__GENESIS__",cards_html(GENESIS)).replace("__ARC__",cards_html(ARC)).replace("__IDEAS__",ideas_html()).replace("__PERSONAS__",personas_html(personas)).replace("__SECTIONS__",sections_html()))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    print(f"wrote Constitutional AI (CAI) — {len(personas)} emergents · badge {tok['moniker']}")
