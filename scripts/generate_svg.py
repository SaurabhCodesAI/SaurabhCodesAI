import svgwrite
import datetime
import random
import requests
import json

def generate_sophisticated_header():
    ist_offset = datetime.timedelta(hours=5, minutes=30)
    now = datetime.datetime.now(datetime.timezone.utc) + ist_offset
    timestamp = now.strftime("%B %d, %Y %H:%M:%S IST")
    hour = now.hour
    
    # SOPHISTICATED 900x150 canvas - perfect proportions
    dwg = svgwrite.Drawing('header.svg', profile='full', size=('900px', '150px'))
    
    # === DYNAMIC THEMES BASED ON TIME ===
    themes = {
        'morning': {  # 6-12
            'bg': ['#1e3c72', '#2a5298', '#1e3c72'],
            'accent': '#FFD700',
            'secondary': '#87CEEB',
            'status': '🌅 MORNING CODING SESSION'
        },
        'afternoon': {  # 12-18
            'bg': ['#134e5e', '#71b280', '#134e5e'],
            'accent': '#00FF88',
            'secondary': '#20B2AA',
            'status': '☀️ AFTERNOON PRODUCTIVITY'
        },
        'evening': {  # 18-22
            'bg': ['#2c1810', '#8b4513', '#2c1810'],
            'accent': '#FF6B35',
            'secondary': '#FF8C42',
            'status': '🌆 EVENING INNOVATION'
        },
        'night': {  # 22-6
            'bg': ['#0f0f23', '#1a1a2e', '#16213e'],
            'accent': '#E94057',
            'secondary': '#F27121',
            'status': '🌙 NIGHT OWL MODE'
        }
    }
    
    # Determine theme based on hour
    if 6 <= hour < 12:
        theme = themes['morning']
    elif 12 <= hour < 18:
        theme = themes['afternoon']
    elif 18 <= hour < 22:
        theme = themes['evening']
    else:
        theme = themes['night']
    
    # === SOPHISTICATED GRADIENT BACKGROUND ===
    gradient = dwg.defs.add(dwg.linearGradient(id="sophisticated_bg", x1="0%", y1="0%", x2="100%", y2="100%"))
    gradient.add_stop_color(offset="0%", color=theme['bg'][0])
    gradient.add_stop_color(offset="50%", color=theme['bg'][1])
    gradient.add_stop_color(offset="100%", color=theme['bg'][2])
    
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='url(#sophisticated_bg)'))
    
    # === ELEGANT GEOMETRIC PATTERNS ===
    # Subtle hexagon pattern
    for i in range(5):
        x = 150 + (i * 150)
        y = 75
        hexagon = dwg.polygon(points=[
            (x, y-20), (x+17, y-10), (x+17, y+10), 
            (x, y+20), (x-17, y+10), (x-17, y-10)
        ], fill='none', stroke=theme['accent'], stroke_width='1', opacity='0.1')
        dwg.add(hexagon)
    
    # === SOPHISTICATED TITLE SECTION ===
    # Main title with elegant styling
    title_bg = dwg.rect(insert=(40, 25), size=('500px', '40px'), 
                       fill='#000000', opacity='0.3', rx=20)
    dwg.add(title_bg)
    
    # Elegant title
    main_title = dwg.text("SAURABH PAREEK", insert=(60, 50), 
                         fill=theme['accent'], font_family='Arial, sans-serif', 
                         font_size='24px', font_weight='300', letter_spacing='2px')
    dwg.add(main_title)
    
    # Sophisticated subtitle
    subtitle = dwg.text("LLM Infrastructure Architect", insert=(60, 70), 
                       fill=theme['secondary'], font_family='Arial, sans-serif', 
                       font_size='14px', font_weight='300', letter_spacing='1px')
    dwg.add(subtitle)
    
    # === DYNAMIC STATUS INDICATORS ===
    # Status panel
    status_bg = dwg.rect(insert=(40, 85), size=('400px', '50px'), 
                        fill='#000000', opacity='0.2', rx=15)
    dwg.add(status_bg)
    
    # Dynamic status based on time
    status_text = dwg.text(theme['status'], insert=(60, 105), 
                          fill=theme['accent'], font_family='Arial, sans-serif', 
                          font_size='12px', font_weight='400')
    dwg.add(status_text)
    
    # Timestamp
    time_text = dwg.text(f"Last Updated: {timestamp}", insert=(60, 120), 
                        fill=theme['secondary'], font_family='Arial, sans-serif', 
                        font_size='10px', opacity='0.8')
    dwg.add(time_text)
    
    # === SOPHISTICATED TECH INDICATORS ===
    tech_icons = ['AI', 'ML', 'LLM', 'API', 'AWS']
    for i, tech in enumerate(tech_icons):
        x = 600 + (i * 50)
        y = 75
        
        # Tech bubble
        bubble = dwg.circle(center=(x, y), r=18, fill=theme['accent'], opacity='0.8')
        bubble_border = dwg.circle(center=(x, y), r=18, fill='none', 
                                  stroke=theme['secondary'], stroke_width='2')
        tech_label = dwg.text(tech, insert=(x-len(tech)*3, y+3), 
                             fill='#000000', font_family='Arial, sans-serif', 
                             font_size='10px', font_weight='bold')
        
        dwg.add(bubble)
        dwg.add(bubble_border)
        dwg.add(tech_label)
    
    # === ELEGANT BORDER ===
    border = dwg.rect(insert=(5, 5), size=('890px', '140px'), 
                     fill='none', stroke=theme['accent'], stroke_width='2', 
                     rx=10, ry=10, opacity='0.6')
    dwg.add(border)
    
    dwg.save()
    print(f"🌟 Sophisticated {theme['status']} header generated!")

if __name__ == "__main__":
    generate_sophisticated_header()