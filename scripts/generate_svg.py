import svgwrite
import datetime
import random
import math

def generate_vc_grade_header():
    ist_offset = datetime.timedelta(hours=5, minutes=30)
    now = datetime.datetime.now(datetime.timezone.utc) + ist_offset
    timestamp = now.strftime("%B %d, %Y %H:%M:%S IST")
    hour = now.hour
    
    # PINNACLE DIMENSIONS - Ultra-professional
    dwg = svgwrite.Drawing('header.svg', profile='full', size=('1400px', '220px'))
    
    # === EXECUTIVE-LEVEL THEMES ===
    executive_themes = {
        'morning': {  # 6-12
            'bg': ['#1a237e', '#283593', '#3949ab', '#5c6bc0'],
            'primary': '#64B5F6',
            'secondary': '#FFD54F', 
            'accent': '#81C784',
            'status': 'OPTIMIZING SYSTEMS',
            'mode': '⚡ HIGH PERFORMANCE'
        },
        'afternoon': {  # 12-18
            'bg': ['#0d47a1', '#1565c0', '#1976d2', '#42a5f5'],
            'primary': '#00E676',
            'secondary': '#FF7043',
            'accent': '#FFB74D',
            'status': 'SCALING INFRASTRUCTURE', 
            'mode': '🚀 PEAK PRODUCTIVITY'
        },
        'evening': {  # 18-22
            'bg': ['#4a148c', '#6a1b9a', '#8e24aa', '#ab47bc'],
            'primary': '#E91E63',
            'secondary': '#00BCD4',
            'accent': '#FFC107',
            'status': 'ARCHITECTING SOLUTIONS',
            'mode': '🎯 STRATEGIC FOCUS'
        },
        'night': {  # 22-6
            'bg': ['#263238', '#37474f', '#455a64', '#546e7a'],
            'primary': '#00E5FF',
            'secondary': '#FF6EC7',
            'accent': '#FFAB40',
            'status': 'DEEP CODE SESSIONS',
            'mode': '🌙 INNOVATION MODE'
        }
    }
    
    # Select theme
    if 6 <= hour < 12:
        theme = executive_themes['morning']
    elif 12 <= hour < 18:
        theme = executive_themes['afternoon'] 
    elif 18 <= hour < 22:
        theme = executive_themes['evening']
    else:
        theme = executive_themes['night']
    
    # === EXECUTIVE GRADIENT SYSTEM ===
    bg_gradient = dwg.defs.add(dwg.linearGradient(id="executive_bg", x1="0%", y1="0%", x2="100%", y2="100%"))
    bg_gradient.add_stop_color(offset="0%", color=theme['bg'][0])
    bg_gradient.add_stop_color(offset="30%", color=theme['bg'][1])
    bg_gradient.add_stop_color(offset="70%", color=theme['bg'][2])
    bg_gradient.add_stop_color(offset="100%", color=theme['bg'][3])
    
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='url(#executive_bg)'))
    
    # === SOPHISTICATED TECH VISUALIZATION ===
    # Neural network architecture (left side)
    network_x = 80
    network_y = 110
    
    # Industry-standard neural layers
    layers = [
        {"nodes": 8, "label": "INPUT", "color": theme['primary']},
        {"nodes": 16, "label": "HIDDEN-1", "color": theme['secondary']},
        {"nodes": 32, "label": "ATTENTION", "color": theme['accent']},
        {"nodes": 16, "label": "HIDDEN-2", "color": theme['secondary']},
        {"nodes": 4, "label": "OUTPUT", "color": theme['primary']}
    ]
    
    for layer_idx, layer in enumerate(layers):
        layer_x = network_x + (layer_idx * 60)
        nodes = layer["nodes"]
        
        # Calculate node positions
        node_spacing = min(140 / max(nodes, 1), 12)
        start_y = network_y - (nodes * node_spacing / 2)
        
        for node_idx in range(min(nodes, 12)):  # Limit visual nodes
            node_y = start_y + (node_idx * node_spacing)
            node_size = 3 if nodes > 16 else 4
            
            # Professional nodes
            dwg.add(dwg.circle(center=(layer_x, node_y), r=node_size, 
                             fill=layer["color"], opacity='0.8'))
            
            # Connections to next layer
            if layer_idx < len(layers) - 1:
                next_layer = layers[layer_idx + 1]
                next_nodes = min(next_layer["nodes"], 12)
                next_spacing = min(140 / max(next_nodes, 1), 12)
                next_start_y = network_y - (next_nodes * next_spacing / 2)
                
                # Connect to subset of next layer nodes
                connections = min(3, next_nodes)
                for conn_idx in range(connections):
                    next_y = next_start_y + (conn_idx * next_spacing * (next_nodes / connections))
                    dwg.add(dwg.line(start=(layer_x + node_size, node_y), 
                                   end=(layer_x + 60 - node_size, next_y),
                                   stroke=layer["color"], stroke_width='0.8', 
                                   opacity='0.3'))
        
        # Layer labels
        dwg.add(dwg.text(layer["label"], insert=(layer_x - 15, network_y + 80), 
                        fill=layer["color"], font_family='SF Pro Display, system-ui', 
                        font_size='9px', font_weight='600', opacity='0.7'))
    
    # === EXECUTIVE TITLE SECTION ===
    title_x = 420
    title_y = 40
    title_width = 700
    title_height = 80
    
    # Glass morphism panel
    title_bg = dwg.rect(insert=(title_x, title_y), size=(f'{title_width}px', f'{title_height}px'), 
                       fill='#000000', opacity='0.12', rx=20, ry=20)
    dwg.add(title_bg)
    
    # Executive border
    title_border = dwg.rect(insert=(title_x, title_y), size=(f'{title_width}px', f'{title_height}px'), 
                           fill='none', stroke=theme['primary'], stroke_width='2', 
                           rx=20, ry=20, opacity='0.6')
    dwg.add(title_border)
    
    # Executive title
    main_title = dwg.text("SAURABH PAREEK", insert=(title_x + 30, title_y + 35), 
                         fill=theme['primary'], font_family='SF Pro Display, Arial, sans-serif', 
                         font_size='32px', font_weight='700', letter_spacing='3px')
    dwg.add(main_title)
    
    # Professional subtitle
    subtitle = dwg.text("Full-Stack Developer • AI/ML Engineer", insert=(title_x + 30, title_y + 60), 
                       fill=theme['secondary'], font_family='SF Pro Display, Arial, sans-serif', 
                       font_size='16px', font_weight='500', letter_spacing='1px')
    dwg.add(subtitle)
    
    # === EXECUTIVE STATUS DASHBOARD ===
    status_x = 420
    status_y = 140
    status_width = 700
    status_height = 60
    
    # Status panel
    status_bg = dwg.rect(insert=(status_x, status_y), size=(f'{status_width}px', f'{status_height}px'), 
                        fill='#000000', opacity='0.08', rx=15, ry=15)
    dwg.add(status_bg)
    
    # Live metrics
    metrics = [
        ("🔥", "ACTIVE DEVELOPMENT", theme['accent']),
        ("⚡", theme['status'], theme['primary']),
        ("🎯", theme['mode'], theme['secondary'])
    ]
    
    for i, (icon, label, color) in enumerate(metrics):
        metric_x = status_x + 30 + (i * 220)
        
        # Metric icon
        dwg.add(dwg.text(icon, insert=(metric_x, status_y + 25), 
                        fill=color, font_family='Apple Color Emoji, sans-serif', 
                        font_size='16px'))
        
        # Metric label
        dwg.add(dwg.text(label, insert=(metric_x + 25, status_y + 25), 
                        fill=color, font_family='SF Pro Display, system-ui', 
                        font_size='11px', font_weight='600'))
        
        # Pulse indicator
        pulse = dwg.circle(center=(metric_x + 8, status_y + 40), r=3, 
                          fill=color, opacity='0.8')
        dwg.add(pulse)
    
    # Executive timestamp
    timestamp_text = dwg.text(f"Last Deployed: {timestamp}", 
                             insert=(status_x + 30, status_y + 50), 
                             fill=theme['primary'], font_family='SF Mono, monospace', 
                             font_size='10px', font_weight='400', opacity='0.8')
    dwg.add(timestamp_text)
    
    # === PERFORMANCE INDICATORS ===
    perf_y = 200
    
    # System metrics bars
    metrics_data = [
        ("API Latency", 0.95, theme['primary']),
        ("Code Quality", 0.88, theme['secondary']),
        ("Test Coverage", 0.82, theme['accent'])
    ]
    
    for i, (label, value, color) in enumerate(metrics_data):
        bar_x = 80 + (i * 120)
        bar_width = 100
        fill_width = bar_width * value
        
        # Background bar
        dwg.add(dwg.rect(insert=(bar_x, perf_y), size=(f'{bar_width}px', '4px'), 
                        fill='#333333', rx=2, ry=2))
        
        # Progress bar
        dwg.add(dwg.rect(insert=(bar_x, perf_y), size=(f'{fill_width}px', '4px'), 
                        fill=color, rx=2, ry=2))
        
        # Label
        dwg.add(dwg.text(f"{label}: {value:.0%}", insert=(bar_x, perf_y - 5), 
                        fill=color, font_family='SF Pro Display, system-ui', 
                        font_size='9px', font_weight='500'))
    
    # === EXECUTIVE BORDER SYSTEM ===
    # Outer border
    dwg.add(dwg.rect(insert=(15, 15), size=('1370px', '190px'), 
                    fill='none', stroke=theme['primary'], stroke_width='2', 
                    rx=15, ry=15, opacity='0.4'))
    
    # Corner accents
    corner_size = 25
    corners = [(15, 15), (1370, 15), (15, 190), (1370, 190)]
    
    for i, (x, y) in enumerate(corners):
        if i % 2 == 0:  # Top-left, bottom-left
            dwg.add(dwg.path(d=f"M {x} {y + corner_size} L {x} {y} L {x + corner_size} {y}", 
                           stroke=theme['accent'], stroke_width='3', fill='none'))
        else:  # Top-right, bottom-right  
            dwg.add(dwg.path(d=f"M {x - corner_size} {y} L {x} {y} L {x} {y + corner_size}", 
                           stroke=theme['accent'], stroke_width='3', fill='none'))
    
    dwg.save()
    print(f"🌟 VC-GRADE EXECUTIVE header deployed! Status: {theme['status']} 🚀")

if __name__ == "__main__":
    generate_vc_grade_header()