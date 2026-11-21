"""Regenerate the original Backend README artwork.

Dependencies: Pillow, PyMuPDF.
Run: python Backend/assets/generate_assets.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import fitz
import math
import tempfile

ROOT = Path(__file__).resolve().parent
PREVIEW = Path(tempfile.mkdtemp(prefix='backend-assets-preview-'))
ROOT.mkdir(exist_ok=True)

HERO = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="440" viewBox="0 0 1200 440" role="img" aria-labelledby="title desc">
<title id="title">Backend Development — CIS Team 2026–2027</title>
<desc id="desc">An original backend illustration: a client sends a request to an API server connected to a database, cache, and background worker.</desc>
<defs>
 <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#0D1C30"/><stop offset="1" stop-color="#070E1B"/></linearGradient>
 <linearGradient id="server" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#173750"/><stop offset="1" stop-color="#102237"/></linearGradient>
 <linearGradient id="accent"><stop stop-color="#61E3E6"/><stop offset="1" stop-color="#5B9CF8"/></linearGradient>
</defs>
<rect width="1200" height="440" rx="24" fill="#0D1C30"/>
<rect x=".7" y=".7" width="1198.6" height="438.6" rx="24" fill="none" stroke="#23354D"/>
<g stroke="#173047" stroke-width="1" opacity=".35">GRID</g>
<circle cx="1015" cy="50" r="270" fill="#1C4E6E" opacity=".08"/>
<circle cx="1165" cy="415" r="230" fill="#315A8C" opacity=".06"/>
<g font-family="sans-serif">
 <rect x="48" y="44" width="5" height="15" rx="2.5" fill="#61E3E6"/>
 <text x="66" y="57" font-size="12" letter-spacing="2" fill="#A8C1D6">CIS TEAM / 2026–2027</text>
 <text x="47" y="158" font-size="76" font-weight="bold" letter-spacing="-3" fill="#F3F7FF">BACKEND</text>
 <text x="51" y="210" font-size="27" fill="#D9E7F5">Build the systems</text>
 <text x="51" y="249" font-size="27" fill="#D9E7F5">behind every experience.</text>
 <text x="52" y="292" font-size="14" fill="#87A5BF">APIs. Data. Security. Reliability.</text>
 <rect x="51" y="333" width="134" height="30" rx="15" fill="#112B3C" stroke="#24546A"/>
 <circle cx="68" cy="348" r="3.5" fill="#61E3E6"/>
 <text x="80" y="353" font-size="11" fill="#BFEDEE">5 learning paths</text>
 <rect x="197" y="333" width="164" height="30" rx="15" fill="#162437" stroke="#2B3F57"/>
 <text x="213" y="353" font-size="11" fill="#B9CADB">One shared foundation</text>
 <text x="52" y="405" font-family="monospace" font-size="12" fill="#7B94AA">&gt; learn. build. test. ship.</text>
 <path d="M551 61V379" stroke="#263B53" stroke-dasharray="3 8"/>
 <text x="603" y="58" font-family="monospace" font-size="11" letter-spacing="1.5" fill="#7696AE">INSIDE THE REQUEST</text>
 <path d="M695 160H756 M914 160H1018 M958 160V277H1005 M835 286V326" stroke="#31516A" stroke-width="2" fill="none" stroke-linecap="round"/>
 <path d="M701 180H750" stroke="#31516A" stroke-width="1.4" stroke-dasharray="3 5" fill="none"/>
 <path d="M746 176L741 180L746 184" fill="none" stroke="#789BB6" stroke-width="1.4"/>
 <circle cx="958" cy="160" r="4" fill="#31516A"/>
 <rect x="602" y="117" width="93" height="85" rx="12" fill="#111F33" stroke="#31516A"/>
 <rect x="619" y="134" width="59" height="39" rx="5" fill="#0B1424" stroke="#688AA4"/>
 <path d="M634 147L629 153L634 159 M663 147L668 153L663 159 M650 146L646 160" stroke="#61E3E6" stroke-width="1.8" fill="none"/>
 <path d="M649 174V182 M636 183H662" stroke="#688AA4" stroke-width="1.5"/>
 <text x="648" y="225" font-size="10" letter-spacing="1.5" text-anchor="middle" fill="#9CB4C9">CLIENT</text>
 <rect x="757" y="96" width="158" height="190" rx="15" fill="#17354B" stroke="#4186A4" stroke-width="1.2"/>
 <rect x="772" y="110" width="128" height="25" rx="5" fill="#0C2335"/>
 <circle cx="785" cy="122" r="3" fill="#61E3E6"/>
 <text x="799" y="126" font-size="10" letter-spacing="1" fill="#B7DDE9">API SERVER</text>
 <g fill="#10283B" stroke="#2B5870">
  <rect x="774" y="148" width="124" height="34" rx="6"/>
  <rect x="774" y="191" width="124" height="34" rx="6"/>
 </g>
 <g font-family="monospace" font-size="10" fill="#9CBACC">
  <text x="786" y="169">{ } routes</text><text x="786" y="212">&gt;_ logic</text>
 </g>
 <circle cx="884" cy="165" r="2.5" fill="#61E3E6"/>
 <circle cx="884" cy="208" r="2.5" fill="#89B8FD"/>
 <text x="836" y="260" font-family="monospace" font-size="10" text-anchor="middle" fill="#61E3E6">GET /api/learn</text>
 <path d="M1018 125C1018 109 1133 109 1133 125V189C1133 205 1018 205 1018 189Z" fill="#142A3F" stroke="#5C83B3" stroke-width="1.2"/>
 <ellipse cx="1075.5" cy="125" rx="57.5" ry="13" fill="#1D3C56" stroke="#7CA3D1"/>
 <path d="M1018 151C1018 168 1133 168 1133 151 M1018 173C1018 190 1133 190 1133 173" fill="none" stroke="#406586"/>
 <text x="1076" y="225" font-size="10" letter-spacing="1.3" text-anchor="middle" fill="#9CB4C9">DATABASE</text>
 <rect x="1005" y="249" width="139" height="58" rx="10" fill="#211F30" stroke="#76634E"/>
 <path d="M1024 267L1031 263L1038 267L1031 271Z M1024 272L1031 276L1038 272 M1024 277L1031 281L1038 277" fill="none" stroke="#E7B771" stroke-width="1.5"/>
 <text x="1051" y="274" font-size="11" fill="#E5CBA7">CACHE</text>
 <text x="1051" y="291" font-family="monospace" font-size="9" fill="#9C968E">fast lookups</text>
 <rect x="757" y="326" width="158" height="59" rx="10" fill="#131F34" stroke="#40557C"/>
 <path d="M775 346H786 M775 351H790 M775 356H783" stroke="#98B4ED" stroke-width="1.5" stroke-linecap="round"/>
 <text x="801" y="349" font-size="11" fill="#C4D4F4">WORKER</text>
 <text x="801" y="368" font-family="monospace" font-size="9" fill="#8096B9">background jobs</text>
 <circle cx="1010" cy="364" r="3" fill="#61E3E6"/>
 <text x="1021" y="368" font-family="monospace" font-size="10" fill="#95BECA">request</text>
 <circle cx="1010" cy="384" r="3" fill="#E7B771"/>
 <text x="1021" y="388" font-family="monospace" font-size="10" fill="#95BECA">response</text>
</g>
</svg>'''

grid = ''.join(f'<path d="M{x} 26V414"/>' for x in range(580,1180,30)) + ''.join(f'<path d="M580 {y}H1170"/>' for y in range(42,420,30))
HERO = HERO.replace('GRID',grid)
(ROOT/'backend-hero.svg').write_text(HERO)

FOOTER='''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="190" viewBox="0 0 1200 190" role="img" aria-labelledby="title desc">
<title id="title">Your next commit</title><desc id="desc">Build something you can explain. A terminal lists the learning cycle: learn, build, test, and ship.</desc>
<rect width="1200" height="190" rx="20" fill="#0C1728"/>
<rect x=".5" y=".5" width="1199" height="189" rx="20" fill="none" stroke="#263A52"/>
<g font-family="sans-serif">
<text x="48" y="48" font-size="11" letter-spacing="2" fill="#61E3E6">YOUR NEXT COMMIT</text>
<text x="46" y="96" font-size="29" font-weight="bold" fill="#F3F7FF">Build something</text>
<text x="46" y="135" font-size="29" font-weight="bold" fill="#F3F7FF">you can explain.</text>
<rect x="569" y="24" width="583" height="142" rx="10" fill="#09111F" stroke="#2B4058"/>
<path d="M569 52H1152" stroke="#1C3047"/>
<circle cx="587" cy="39" r="3" fill="#647D98"/><circle cx="600" cy="39" r="3" fill="#647D98"/><circle cx="613" cy="39" r="3" fill="#647D98"/>
<text x="638" y="43" font-family="monospace" font-size="10" fill="#7890AA">backend / learning loop</text>
</g>
</svg>'''
static_lines=[]
for j,(cmd,detail) in enumerate([('learn','understand one concept'),('build','implement one feature'),('test','verify its behavior'),('ship','share it, then improve')]):
    col='#61E3E6' if j==0 else '#829BB3'
    y=81+j*21
    static_lines.append(f'<text x="591" y="{y}" font-family="monospace" font-size="13" fill="{col}">&gt; {cmd}</text><text x="714" y="{y}" font-family="monospace" font-size="13" fill="{col}">{detail}</text>')
FOOTER_STATIC=FOOTER.replace('</svg>',''.join(static_lines)+'</svg>')
(ROOT/'backend-footer.svg').write_text(FOOTER_STATIC)

DIVIDER='''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="112" viewBox="0 0 1200 112" role="presentation">
<rect width="1200" height="112" rx="16" fill="#0D1C30"/>
<rect x=".75" y=".75" width="1198.5" height="110.5" rx="15.25" fill="none" stroke="#29465E" stroke-width="1.5"/>
<g fill="none" stroke-linecap="round" stroke-linejoin="round">
  <path d="M36 56H544 M656 56H1164" stroke="#143C50" stroke-width="9"/>
  <path d="M36 56H544 M656 56H1164" stroke="#57BCCB" stroke-width="2.5"/>
  <path d="M102 25H330L361 56 M181 87H408L439 56 M1098 25H870L839 56 M1019 87H792L761 56" stroke="#416E91" stroke-width="2"/>
  <path d="M252 25H330L361 56 M948 25H870L839 56" stroke="#7AA8D6" stroke-width="2"/>
  <path d="M331 87H408L439 56 M869 87H792L761 56" stroke="#6ECED6" stroke-width="2"/>
</g>
<g fill="#102C40" stroke="#63D5DD" stroke-width="2">
  <circle cx="38" cy="56" r="5"/><circle cx="1162" cy="56" r="5"/>
  <circle cx="102" cy="25" r="3.5"/><circle cx="1098" cy="25" r="3.5"/>
  <circle cx="181" cy="87" r="3.5"/><circle cx="1019" cy="87" r="3.5"/>
</g>
<rect x="466" y="49" width="25" height="14" rx="5" fill="#0D1C30" stroke="#D8B077" stroke-width="1.5"/>
<rect x="709" y="49" width="25" height="14" rx="5" fill="#0D1C30" stroke="#D8B077" stroke-width="1.5"/>
<circle cx="478.5" cy="56" r="2.5" fill="#E7B771"/><circle cx="721.5" cy="56" r="2.5" fill="#E7B771"/>
<rect x="536" y="12" width="128" height="88" rx="18" fill="#61E3E6" opacity=".06"/>
<rect x="544" y="20" width="112" height="72" rx="14" fill="#102D41" stroke="#4C99AF" stroke-width="1.5"/>
<path d="M578 42L564 56L578 70 M607 37L593 75 M622 42L636 56L622 70" fill="none" stroke="#8DEFF0" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''
(ROOT/'backend-divider.svg').write_text(DIVIDER)

def render(svg,scale=1):
    import xml.etree.ElementTree as ET
    root=ET.fromstring(svg)
    text_nodes=[]
    def collect(element, inherited):
        attrs={**inherited,**element.attrib}
        for child in list(element):
            if child.tag.endswith('}text'):
                text_nodes.append(({**attrs,**child.attrib}, ''.join(child.itertext())))
                element.remove(child)
            else:
                collect(child,attrs)
    collect(root,{})
    d=fitz.open(stream=ET.tostring(root),filetype='svg')
    p=d[0].get_pixmap(matrix=fitz.Matrix(scale,scale),alpha=False)
    im=Image.frombytes('RGB',[p.width,p.height],p.samples)
    draw=ImageDraw.Draw(im)
    for a,value in text_nodes:
        mono=a.get('font-family')=='monospace'
        weight='-Bold' if a.get('font-weight')=='bold' else ''
        face='DejaVuSansMono' if mono else 'DejaVuSans'
        font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/'+face+weight+'.ttf',round(float(a.get('font-size','14'))*scale))
        x=float(a.get('x','0'))*scale; y=float(a.get('y','0'))*scale
        spacing=float(a.get('letter-spacing','0'))*scale
        width=draw.textlength(value,font=font)+spacing*max(0,len(value)-1)
        anchor=a.get('text-anchor','start')
        if anchor=='middle': x-=width/2
        elif anchor=='end': x-=width
        if spacing:
            for char in value:
                draw.text((x,y),char,font=font,fill=a.get('fill','#FFFFFF'),anchor='ls')
                x+=draw.textlength(char,font=font)+spacing
        else:
            draw.text((x,y),value,font=font,fill=a.get('fill','#FFFFFF'),anchor='ls')
    return im

hero=render(HERO,2)
footer=render(FOOTER,2)
hero.resize((1200,440),Image.Resampling.LANCZOS).save(PREVIEW/'backend-hero.png')
render(FOOTER_STATIC,2).resize((1200,190),Image.Resampling.LANCZOS).save(PREVIEW/'backend-footer.png')

def position(points,p):
    lengths=[math.dist(a,b) for a,b in zip(points,points[1:])]
    d=p*sum(lengths)
    for a,b,n in zip(points,points[1:],lengths):
        if d<=n: return (a[0]+(b[0]-a[0])*d/n,a[1]+(b[1]-a[1])*d/n)
        d-=n
    return points[-1]

paths=[([(696,160),(756,160)],(97,227,230),0),
       ([(915,160),(1017,160)],(97,227,230),.2),
       ([(958,160),(958,277),(1004,277)],(97,227,230),.45),
       ([(835,287),(835,325)],(152,180,237),.6),
       ([(750,180),(701,180)],(231,183,113),.1)]
frames=[]
for i in range(64):
    im=hero.copy(); draw=ImageDraw.Draw(im)
    for path,color,phase in paths:
        p=(i/64+phase)%1
        x,y=position(path,p); r=3.2
        draw.ellipse(((x-r-3)*2,(y-r-3)*2,(x+r+3)*2,(y+r+3)*2),fill=tuple(int(v*.28) for v in color))
        draw.ellipse(((x-r)*2,(y-r)*2,(x+r)*2,(y+r)*2),fill=color)
    if i%16<10:
        draw.rounded_rectangle((249*2,395*2,256*2,407*2),radius=1,fill=(97,227,230))
    frames.append(im.resize((1200,440),Image.Resampling.LANCZOS))

fontpath='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
font=ImageFont.truetype(fontpath,26)
lines=[('learn','understand one concept'),('build','implement one feature'),('test','verify its behavior'),('ship','share it, then improve')]
footframes=[]
for i in range(64):
    im=footer.copy(); draw=ImageDraw.Draw(im)
    active=int(i/16)
    for j,(cmd,detail) in enumerate(lines):
        col=(97,227,230) if j==active else (90,111,134)
        y=65+j*21
        draw.text((591*2,y*2),'>',font=font,fill=col)
        draw.text((614*2,y*2),cmd.ljust(6),font=font,fill=(219,235,247) if j==active else (123,143,162))
        draw.text((714*2,y*2),detail,font=font,fill=col)
        if j==active:
            draw.ellipse((1129*2,(y+6)*2,1135*2,(y+12)*2),fill=col)
    footframes.append(im.resize((1200,190),Image.Resampling.LANCZOS))

def gif(frames,path):
    sample=Image.new('RGB',(frames[0].width,frames[0].height*3))
    for i,f in enumerate([frames[0],frames[21],frames[42]]): sample.paste(f,(0,i*f.height))
    palette=sample.quantize(colors=128,method=Image.Quantize.MEDIANCUT)
    quant=[f.quantize(palette=palette,dither=Image.Dither.NONE) for f in frames]
    quant[0].save(path,save_all=True,append_images=quant[1:],duration=80,loop=0,optimize=True,disposal=1)

gif(frames,ROOT/'backend-hero.gif')
gif(footframes,ROOT/'backend-footer.gif')

# One contact sheet makes it easy to inspect both animations at several times.
sheet=Image.new('RGB',(1200,440*3+190),'#0C1728')
for j,i in enumerate([0,21,42]): sheet.paste(frames[i],(0,440*j))
sheet.paste(footframes[48],(0,1320))
sheet.save(PREVIEW/'animation-contact-sheet.png')
for p in ROOT.iterdir(): print(p.name,p.stat().st_size)

print('Preview images:', PREVIEW)
