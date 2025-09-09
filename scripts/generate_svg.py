import svgwrite
import datetime
import random
import math

def generate_pinnacle_elite_header():
    ist_offset = datetime.timedelta(hours=5, minutes=30)
    now = datetime.datetime.now(datetime.timezone.utc) + ist_offset
    timestamp = now.strftime("%B %d, %Y %H:%M:%S IST")
    hour = now.hour
    day_of_year = now.timetuple().tm_yday
    
    # PINNACLE CANVAS - Ultra-wide cinematic format
    dwg = svgwrite.Drawing('header.svg', profile='full', size=('1400px', '200px'))
    
    # === DYNAMIC QUANTUM THEMES ===
    themes = {
        'dawn': {  # 5-8
            'bg': ['#667db6', '#0082c8', '#0082c8', '#667db6'],
            'accent': '#FFE066',
            'secondary': '#87CEEB',
            'tertiary': '#F0E68C',
            'title': '🌅 QUANTUM ARCHITECT',
            'subtitle': 'Neural Networks • Awakening Systems',
            'effect': 'rising_sun'
        },
        'morning': {  # 8-12
            'bg': ['#74b9ff', '#0984e3', '#6c5ce7', '#a29bfe'],
            'accent': '#00CED1',
            'secondary': '#FFD700',
            'tertiary': '#00FA9A',
            'title': '⚡ SYSTEM ARCHITECT',
            'subtitle': 'AI Infrastructure • Peak Performance',
            'effect': 'energy_flow'
        },
        'afternoon': {  # 12-17
            'bg': ['#fd79a8', '#fdcb6e', '#e17055', '#d63031'],
            'accent': '#00D4FF',
            'secondary': '#FF6B35',
            'tertiary': '#FFE066',
            'title': '🚀 INNOVATION CATALYST',
            'subtitle': 'Scaling Intelligence • Building Tomorrow',
            'effect': 'innovation_burst'
        },
        'evening': {  # 17-21
            'bg': ['#6c5ce7', '#a29bfe', '#fd79a8', '#fdcb6e'],
            'accent': '#FF69B4',
            'secondary': '#9370DB',
            'tertiary': '#FFB6C1',
            'title': '🌆 CREATIVE TECHNOLOGIST',
            'subtitle': 'Artistic AI • Elegant Solutions',
            'effect': 'creative_flow'
        },
        'night': {  # 21-5
            'bg': ['#2d3436', '#636e72', '#00b894', '#00cec9'],
            'accent': '#E94057',
            'secondary': '#0984e3',
            'tertiary': '#00b894',
            'title': '🌙 DEEP LEARNING SAGE',
            'subtitle': 'Neural Architectures • Midnight Innovation',
            'effect': 'neural_glow'
        }
    }
    
    # Determine theme with smooth transitions
    if 5 <= hour < 8:
        theme = themes['dawn']
    elif 8 <= hour < 12:
        theme = themes['morning']
    elif 12 <= hour < 17:
        theme = themes['afternoon']
    elif 17 <= hour < 21:
        theme = themes['evening']
    else:
        theme = themes['night']
    
    # === ULTRA-SOPHISTICATED BACKGROUND ===
    # Multi-layered gradient with depth
    bg_gradient = dwg.defs.add(dwg.linearGradient(id="pinnacle_bg", x1="0%", y1="0%", x2="100%", y2="100%"))
    bg_gradient.add_stop_color(offset="0%", color=theme['bg'][0])
    bg_gradient.add_stop_color(offset="33%", color=theme['bg'][1])
    bg_gradient.add_stop_color(offset="66%", color=theme['bg'][2])
    bg_gradient.add_stop_color(offset="100%", color=theme['bg'][3])
    
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='url(#pinnacle_bg)'))
    
    # === QUANTUM PARTICLE FIELD ===
    # Dynamic particle system based on time
    particle_count = 80 + (day_of_year % 40)  # Changes throughout the year
    
    for i in range(particle_count):
        x = random.randint(0, 1400)
        y = random.randint(0, 200)
        size = random.uniform(0.5, 4)
        
        # Time-based color variation
        colors = [theme['accent'], theme['secondary'], theme['tertiary']]
        color = colors[i % 3]
        opacity = random.uniform(0.2, 0.9)
        
        # Particle with quantum glow
        glow_radius = size * random.uniform(2, 4)
        glow = dwg.circle(center=(x, y), r=glow_radius, fill=color, opacity=str(opacity * 0.1))
        particle = dwg.circle(center=(x, y), r=size, fill=color, opacity=str(opacity))
        
        dwg.add(glow)
        dwg.add(particle)
        
        # Quantum connections
        if i % 8 == 0 and i < particle_count - 1:
            next_x = random.randint(max(0, x-150), min(1400, x+150))
            next_y = random.randint(max(0, y-50), min(200, y+50))
            dwg.add(dwg.line(start=(x, y), end=(next_x, next_y), 
                           stroke=color, stroke_width='0.5', opacity=str(opacity * 0.3)))
    
    # === NEURAL ARCHITECTURE VISUALIZATION ===
    # Left side neural network
    neural_center_x, neural_center_y = 120, 100
    layers = [8, 12, 16, 12, 6, 3]  # Neural network architecture
    
    for layer_idx, nodes in enumerate(layers):
        layer_x = 50 + (layer_idx * 40)
        
        for node_idx in range(nodes):
            node_y = neural_center_y - (nodes * 8) + (node_idx * 16)
            
            # Neural node
            node_size = 3 + (16 - nodes) * 0.3  # Bigger nodes for smaller layers
            node_color = theme['tertiary'] if layer_idx in [0, len(layers)-1] else theme['secondary']
            
            dwg.add(dwg.circle(center=(layer_x, node_y), r=node_size, 
                             fill=node_color, opacity='0.8'))
            
            # Connections to next layer
            if layer_idx < len(layers) - 1:
                next_layer_nodes = layers[layer_idx + 1]
                for next_node_idx in range(next_layer_nodes):
                    next_node_y = neural_center_y - (next_layer_nodes * 8) + (next_node_idx * 16)
                    next_layer_x = layer_x + 40
                    
                    # Connection strength based on position
                    strength = random.uniform(0.1, 0.4)
                    dwg.add(dwg.line(start=(layer_x + node_size, node_y), 
                                   end=(next_layer_x - node_size, next_node_y),
                                   stroke=theme['accent'], stroke_width='1', 
                                   opacity=str(strength)))
    
    # === PINNACLE TITLE SECTION ===
    # Sophisticated glass morphism container
    title_container = dwg.rect(insert=(350, 30), size=('700px', '140px'), 
                              fill='#000000', opacity='0.15', rx=25, ry=25)
    dwg.add(title_container)
    
    # Elegant border
    title_border = dwg.rect(insert=(350, 30), size=('700px', '140px'), 
                           fill='none', stroke=theme['accent'], stroke_width='2', 
                           rx=25, ry=25, opacity='0.6')
    dwg.add(title_border)
    
    # Dynamic title based on theme
    main_title = dwg.text(theme['title'], insert=(380, 80), 
                         fill=theme['accent'], font_family='Segoe UI, Arial, sans-serif', 
                         font_size='32px', font_weight='700', letter_spacing='3px')
    dwg.add(main_title)
    
    # Sophisticated subtitle
    subtitle = dwg.text(theme['subtitle'], insert=(380, 110), 
                       fill=theme['secondary'], font_family='Segoe UI, Arial, sans-serif', 
                       font_size='16px', font_weight='300', letter_spacing='2px')
    dwg.add(subtitle)
    
    # Personal brand
    brand = dwg.text("SAURABH PAREEK", insert=(380, 140), 
                    fill=theme['tertiary'], font_family='Segoe UI, Arial, sans-serif', 
                    font_size='14px', font_weight='500', letter_spacing='4px', opacity='0.8')
    dwg.add(brand)
    
    # === ELITE STATUS DASHBOARD ===
    # Right side status panel
    status_panel = dwg.rect(insert=(1080, 30), size=('290px', '140px'), 
                           fill='#000000', opacity='0.2', rx=20, ry=20)
    dwg.add(status_panel)
    
    # Status indicators
    status_items = [
        ("🌐 SYSTEMS", "OPERATIONAL", theme['accent']),
        ("⚡ AI MODELS", "TRAINING", theme['secondary']),
        ("🚀 DEPLOYMENT", "ACTIVE", theme['tertiary']),
        ("💎 PERFORMANCE", "OPTIMAL", theme['accent']),
        ("🔮 INNOVATION", "CONTINUOUS", theme['secondary'])
    ]
    
    for i, (label, status, color) in enumerate(status_items):
        y_pos = 60 + (i * 20)
        
        # Status dot
        dot_x = 1100
        dwg.add(dwg.circle(center=(dot_x, y_pos), r=3, fill=color, opacity='0.9'))
        
        # Status text
        dwg.add(dwg.text(label, insert=(dot_x + 15, y_pos + 4), 
                        fill=color, font_family='Segoe UI, Arial, sans-serif', 
                        font_size='11px', font_weight='600'))
        
        dwg.add(dwg.text(status, insert=(dot_x + 120, y_pos + 4), 
                        fill=color, font_family='Segoe UI, Arial, sans-serif', 
                        font_size='11px', font_weight='300', opacity='0.8'))
    
    # Timestamp with elegant styling
    time_bg = dwg.rect(insert=(1090, 155), size=('270px', '25px'), 
                      fill=theme['accent'], opacity='0.1', rx=12, ry=12)
    dwg.add(time_bg)
    
    timestamp_text = dwg.text(f"Last Updated: {timestamp}", insert=(1100, 170), 
                             fill=theme['accent'], font_family='Segoe UI, Arial, sans-serif', 
                             font_size='10px', font_weight='400', opacity='0.9')
    dwg.add(timestamp_text)
    
    # === QUANTUM FIELD EFFECTS ===
    # Dynamic geometric patterns
    for i in range(5):
        center_x = 200 + (i * 200)
        center_y = 100
        
        # Rotating hexagon
        rotation = (day_of_year * 2 + i * 60) % 360
        hexagon_points = []
        
        for j in range(6):
            angle = math.radians(j * 60 + rotation)
            x = center_x + 30 * math.cos(angle)
            y = center_y + 30 * math.sin(angle)
            hexagon_points.append((x, y))
        
        dwg.add(dwg.polygon(points=hexagon_points, fill='none', 
                           stroke=theme['tertiary'], stroke_width='1', opacity='0.3'))
    
    # === PINNACLE BORDER SYSTEM ===
    # Outer elite border
    outer_border = dwg.rect(insert=(10, 10), size=('1380px', '180px'), 
                           fill='none', stroke=theme['accent'], stroke_width='3', 
                           rx=20, ry=20, opacity='0.8')
    dwg.add(outer_border)
    
    # Inner sophisticated border
    inner_border = dwg.rect(insert=(20, 20), size=('1360px', '160px'), 
                           fill='none', stroke=theme['secondary'], stroke_width='1', 
                           rx=15, ry=15, opacity='0.4')
    dwg.add(inner_border)
    
    dwg.save()
    print(f"🌟 PINNACLE ELITE {theme['title']} header generated! Ultra-sophisticated level achieved! 🚀")

if __name__ == "__main__":
    generate_pinnacle_elite_header()