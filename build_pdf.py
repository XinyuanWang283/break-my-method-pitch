"""Generate the five-slide offline PDF fallback with native, selectable text."""
import json
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / 'assets/data.json').read_text())
fonts = Path('/System/Library/Fonts/Supplemental')
for name, file in [('Serif','Georgia.ttf'),('Sans','Arial.ttf'),('Bold','Arial Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(fonts/file)))
c = canvas.Canvas(str(ROOT/'pitch.pdf'),pagesize=(1280,720))
c.setTitle('Break My Method - Five-slide pitch')
c.setAuthor('Break My Method')
INK='#14303c'; MUTED='#46626f'; AMBER='#c07f00'; RED='#c02020'; LINE='#ccd9e1'
def text(x,y,s,size=25,font='Sans',color=INK,align='left'):
    c.setFillColor(HexColor(color)); c.setFont(font,size)
    getattr(c,{'left':'drawString','center':'drawCentredString','right':'drawRightString'}[align])(x,720-y-size*.82,s)
def line(x,y,x2,y2):
    c.setStrokeColor(HexColor(LINE)); c.setLineWidth(1); c.line(x,720-y,x2,720-y2)
def page(n):
    c.setFillColor(HexColor('#f3f7f9')); c.rect(0,0,1280,720,stroke=0,fill=1)
    text(1226,682,f'{n} / 5',14,color=MUTED,align='right')
def end(): c.showPage()
page(1)
text(78,54,'B R E A K  M Y  M E T H O D',13,'Bold',AMBER)
text(78,89,'Find what got worse',56,'Serif')
text(78,152,'before you ship what got better.',56,'Serif')
text(78,241,'AI teams ship prompt and model updates constantly.',23,color=MUTED)
text(78,276,'Standard evals can stay green while important user cases regress.',23,color=MUTED)
for x,label in [(435,'Production V1'),(845,'Candidate V2')]:
    text(x,349,label,22,color=MUTED,align='center'); line(x-155,385,x+155,385)
    text(x,397,'100%',74,'Serif',align='center')
text(640,510,'Looks safe to ship.',30,'Serif',AMBER,'center')
text(78,682,'For AI product & ML engineering teams.',14,color=MUTED)
end()
page(2)
text(78,54,'Break My Method actively decides',48,'Serif')
text(78,108,'what to test next.',48,'Serif')
for y,label,size,font,col in [(206,'V1 → V2 change',25,'Sans',INK),(280,'GPT-OSS-120B',35,'Serif',AMBER),(322,'Nebius Token Factory',21,'Sans',INK),(391,'Choose next stress test',25,'Sans',INK),(465,'Real evidence',25,'Sans',INK),(545,'Next decision',25,'Sans',INK)]:
    text(373,y,label,size,font,col,'center')
for y in [244,357,431,513]: text(373,y,'↓',25,'Sans',MUTED,'center')
text(373,496,'Previously executed and frozen',18,color=MUTED,align='center')
text(373,581,'Only revealed results go back to the planner',18,color=MUTED,align='center')
for y,label,col in [(254,'The model chooses',INK),(298,'where to look.',AMBER),(342,'It never invents',INK),(386,'the evidence.',INK)]: text(733,y,label,34,'Serif',col)
for y,label in [(461,'Planning is live.'),(490,'Evidence is executed, saved,'),(519,'and scored against ground truth.')]: text(733,y,label,19,color=MUTED)
end()
page(3)
text(640,304,'Can we break it?',100,'Serif',align='center')
c.linkURL(data['demo_url'],(200,285,1080,435),relative=0)
end()
page(4)
text(78,54,'A U D I T E D  E V I D E N C E',13,'Bold',AMBER)
text(78,102,', '.join(map(str,data['run_lengths'])),86,'Serif',AMBER)
text(355,133,'tests',45,'Serif')
text(78,213,'Nebius planner fresh runs',24,color=MUTED)
text(78,282,f"{data['random_expectation']} tests expected",42,'Serif')
text(78,339,'Random search · without replacement',22,color=MUTED)
line(78,411,738,411)
text(78,434,'Within 2 tests',21,color=MUTED)
text(78,475,'Nebius: '+data['within_two_nebius'],29)
text(343,475,'Random: '+data['within_two_random'],29)
line(802,100,802,535)
text(847,108,'Hidden regression',28,'Serif')
text(847,154,'Instruction-like customer content',18,color=MUTED)
text(847,230,'V1',25,color=MUTED); text(1202,218,'40%',55,'Serif',align='right')
text(847,298,'V2',25,color=MUTED); text(1202,286,'0%',55,'Serif',RED,'right')
line(847,380,1202,380)
text(847,407,'Δ -40 pp',43,'Serif',RED)
text(78,630,'Small synthetic demonstration; n=3 planner runs.',17,color=MUTED)
end()
page(5)
text(78,54,'From static eval suites',48,'Serif')
text(78,108,'to active AI testing',48,'Serif')
for y,label,rows in [(202,'CUSTOMER',['AI teams shipping prompt/model updates']),(255,'PAIN',['Manual regression-test selection consumes','engineering time and inference budget']),(338,'PRODUCT',['Active testing layer on top of existing eval workflows']),(391,'BUSINESS',['Team subscription + evaluation usage','+ enterprise private deployment'])]:
    text(78,y+4,label,17,'Bold',AMBER)
    for i,row in enumerate(rows): text(248,y+34*i,row,25)
line(78,543,1202,543)
text(78,573,'Today: prompt regression testing.',30,'Serif')
text(78,618,'Next: models, RAG systems and AI agents.',30,'Serif')
end(); c.save()
print('Created pitch.pdf: 5 pages')
