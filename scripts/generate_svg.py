import svgwrite
import datetime
import random
import math

def generate_legendary_header():
    # Get IST time
    ist_offset = datetime.timedelta(hours=5, minutes=30)
    now = datetime.datetime.now(datetime.timezone.utc) + ist_offset
    timestamp = now.strftime("%B %d, %Y %H:%M:%S IST")
    time_only = now.strftime("%H:%M:%S")
    
    # LEGENDARY CANVAS - 1200x300px
    dwg = svgwrite.Drawing('header.svg', profile='full', size=('1200px', '300px'))
    
    # === HOLOGRAPHIC BACKGROUND ===
    # Multiple gradient layers for depth
    bg_gradient = dwg.defs.add(dwg.radialGradient(id="holo_bg", cx="50%", cy="50%"))
    bg_gradient.add_stop_color(offset="0%", color="#000011")
    bg_gradient.add_stop_color(offset="30%", color="#001122")
    bg_gradient.add_stop_color(offset="60%", color="#000033")
    bg_gradient.add_stop_color(offset="100%", color="#0D1117")
    
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='url(#holo_bg)'))
    
    # NEURAL NETWORK BACKGROUND
    for i in range(50):
        x1, y1 = random.randint(0, 1200), random.randint(0, 300)
        x2, y2 = x1 + random.randint(-100, 100), y1 + random.randint(-50, 50)
        dwg.add(dwg.line(start=(x1, y1), end=(x2, y2), 
                        stroke='#00FFFF', stroke_width='0.5', opacity='0.1'))
    
    # FLOATING PARTICLES WITH GLOW
    for i in range(100):
        x = random.randint(0, 1200)
        y = random.randint(0, 300)
        size = random.uniform(0.5, 3)
        color = random.choice(['#00FFFF', '#FF00FF', '#FFD700', '#00FF88'])
        
        # Glow effect
        glow = dwg.circle(center=(x, y), r=size*2, fill=color, opacity='0.1')
        particle = dwg.circle(center=(x, y), r=size, fill=color, opacity='0.8')
        dwg.add(glow)
        dwg.add(particle)
    
    # === FUTURISTIC HUD OVERLAY ===
    # Main HUD border with corner brackets
    hud_corners = [
        # Top-left
        dwg.path(d="M 20 20 L 60 20 M 20 20 L 20 60", 
                stroke='#00FFFF', stroke_width='3'),
        # Top-right  
        dwg.path(d="M 1140 20 L 1180 20 M 1180 20 L 1180 60", 
                stroke='#00FFFF', stroke_width='3'),
        # Bottom-left
        dwg.path(d="M 20 240 L 20 280 M 20 280 L 60 280", 
                stroke='#00FFFF', stroke_width='3'),
        # Bottom-right
        dwg.path(d="M 1140 280 L 1180 280 M 1180 280 L 1180 240", 
                stroke='#00FFFF', stroke_width='3')
    ]
    
    for corner in hud_corners:
        dwg.add(corner)
    
    # === ELITE STATUS PANEL ===
    # Main title with MASSIVE impact
    title_bg = dwg.rect(insert=(50, 40), size=('600px', '50px'), 
                       fill='#000000', opacity='0.7', rx=10)
    dwg.add(title_bg)
    
    main_title = dwg.text("⚡ SAURABH PAREEK ⚡", insert=(60, 75), 
                         fill='#FFD700', font_family='JetBrains Mono', 
                         font_size='36px', font_weight='bold')
    dwg.add(main_title)
    
    # Glitch effect on title
    glitch_title = dwg.text("⚡ SAURABH PAREEK ⚡", insert=(62, 73), 
                           fill='#FF00FF', font_family='JetBrains Mono', 
                           font_size='36px', font_weight='bold', opacity='0.3')
    dwg.add(glitch_title)
    
    # === AI SYSTEM STATUS ===
    ai_panel = dwg.rect(insert=(700, 40), size=('450px', '200px'), 
                       fill='#001122', opacity='0.8', rx=15)
    dwg.add(ai_panel)
    
    # AI System header
    ai_header = dwg.text("🤖 AI NEURAL MATRIX STATUS", insert=(720, 70), 
                        fill='#00FF88', font_family='JetBrains Mono', 
                        font_size='16px', font_weight='bold')
    dwg.add(ai_header)
    
    # Real-time metrics
    metrics = [
        "🧠 Neural Networks: ONLINE",
        "🔥 GPU Clusters: 98% Efficiency", 
        "⚡ Model Training: ACTIVE",
        "🚀 Deployment Pipeline: READY",
        "💎 Code Quality: ELITE LEVEL",
        f"⏰ Last Sync: {timestamp}"
    ]
    
    for i, metric in enumerate(metrics):
        y_pos = 95 + (i * 25)
        color = random.choice(['#00FFFF', '#FFD700', '#00FF88', '#FF69B4'])
        dwg.add(dwg.text(metric, insert=(720, y_pos), 
                        fill=color, font_family='JetBrains Mono', 
                        font_size='12px'))
    
    # === 3D TECH STACK VISUALIZATION ===
    tech_stack = [
        ("🐍", "Python", "#FFD43B"),
        ("⚛️", "React", "#61DAFB"), 
        ("🚀", "FastAPI", "#009688"),
        ("☁️", "GCP", "#4285F4"),
        ("🤖", "AI/ML", "#FF6B6B"),
        ("🔥", "LangChain", "#FFD700"),
        ("⚡", "Vector DB", "#00FFFF"),
        ("💎", "MLOps", "#FF69B4")
    ]
    
    # Circular tech orbit
    center_x, center_y = 400, 180
    radius = 80
    
    # Central core
    core_glow = dwg.circle(center=(center_x, center_y), r=30, fill='#FFD700', opacity='0.2')
    core = dwg.circle(center=(center_x, center_y), r=15, fill='#FFD700', opacity='0.9')
    core_text = dwg.text("AI", insert=(center_x-10, center_y+5), 
                        fill='#000000', font_family='JetBrains Mono', 
                        font_size='14px', font_weight='bold')
    dwg.add(core_glow)
    dwg.add(core)
    dwg.add(core_text)
    
    for i, (icon, name, color) in enumerate(tech_stack):
        angle = (2 * math.pi * i) / len(tech_stack)
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        
        # Tech node with glow
        glow = dwg.circle(center=(x, y), r=25, fill=color, opacity='0.2')
        node = dwg.circle(center=(x, y), r=15, fill=color, opacity='0.8')
        icon_text = dwg.text(icon, insert=(x-8, y+5), 
                           fill='#FFFFFF', font_family='JetBrains Mono', 
                           font_size='16px', font_weight='bold')
        
        # Tech name label
        label_y = y + 35 if y > center_y else y - 25
        label = dwg.text(name, insert=(x-len(name)*3, label_y), 
                        fill=color, font_family='JetBrains Mono', 
                        font_size='10px', font_weight='bold')
        
        dwg.add(glow)
        dwg.add(node)
        dwg.add(icon_text)
        dwg.add(label)
        
        # Connection lines to center with pulse effect
        dwg.add(dwg.line(start=(center_x, center_y), end=(x, y), 
                        stroke=color, stroke_width='2', opacity='0.5'))
        
        # Orbital rings
        if i % 2 == 0:
            ring = dwg.circle(center=(center_x, center_y), r=radius, 
                            fill='none', stroke=color, stroke_width='1', opacity='0.2')
            dwg.add(ring)
    
    # === QUANTUM TERMINAL ===
    terminal_bg = dwg.rect(insert=(50, 100), size=('600px', '140px'), 
                          fill='#000000', opacity='0.9', rx=10)
    dwg.add(terminal_bg)
    
    # Terminal header
    term_header = dwg.rect(insert=(50, 100), size=('600px', '25px'), 
                          fill='#2d2d2d', rx=10)
    dwg.add(term_header)
    
    # Terminal buttons
    dwg.add(dwg.circle(center=(65, 112), r=4, fill='#FF5F56'))  # Close
    dwg.add(dwg.circle(center=(85, 112), r=4, fill='#FFBD2E'))  # Minimize
    dwg.add(dwg.circle(center=(105, 112), r=4, fill='#27CA3F'))  # Maximize
    
    # Terminal title
    term_title = dwg.text("quantum_neural_terminal.sh", insert=(130, 117), 
                         fill='#ffffff', font_family='JetBrains Mono', 
                         font_size='11px', opacity='0.8')
    dwg.add(term_title)
    
    # Time display
    time_display = dwg.text(f"⏰ {time_only} IST", insert=(550, 117), 
                           fill='#00FF88', font_family='JetBrains Mono', 
                           font_size='11px', font_weight='bold')
    dwg.add(time_display)
    
    # Terminal commands with epic output
    commands = [
        ("root@quantum-dev:~# ", "initialize_ai_dominance()", "#00FF00"),
        (">>> ", "Neural networks: FULLY OPERATIONAL", "#FFD700"),
        (">>> ", "Scaling to infinity... ∞", "#00FFFF"),
        (">>> ", "Elite mode: PERMANENTLY ACTIVATED", "#FF69B4"),
        (">>> ", f"Last sync: {timestamp}", "#00FF88")
    ]
    
    for i, (prompt, cmd, color) in enumerate(commands):
        y_pos = 150 + (i * 22)
        
        # Prompt
        dwg.add(dwg.text(prompt, insert=(60, y_pos), 
                        fill='#00FF00', font_family='JetBrains Mono', 
                        font_size='14px', font_weight='bold'))
        
        # Command/Output
        cmd_x = 60 + len(prompt) * 8
        dwg.add(dwg.text(cmd, insert=(cmd_x, y_pos), 
                        fill=color, font_family='JetBrains Mono', 
                        font_size='14px'))
    
    # Cursor blink effect
    cursor_x = 60 + len(">>> ") * 8 + len(f"Last sync: {timestamp}") * 8
    cursor = dwg.rect(insert=(cursor_x, 215-10), size=('2px', '15px'), 
                     fill='#00FF00')
    dwg.add(cursor)
    
    # === ELITE STATUS BADGES ===
    badges = [
        ("🟢 ONLINE", "#00FF88"),
        ("⚡ CODING", "#FFD700"), 
        ("🚀 DEPLOYING", "#00FFFF"),
        ("👑 ELITE", "#FF1493")
    ]
    
    for i, (badge_text, badge_color) in enumerate(badges):
        x_pos = 50 + (i * 140)
        
        # Badge background
        badge_bg = dwg.rect(insert=(x_pos, 250), size=('120px', '25px'), 
                           fill=badge_color, rx=12, ry=12, opacity='0.8')
        dwg.add(badge_bg)
        
        # Badge text
        badge_label = dwg.text(badge_text, insert=(x_pos+8, 267), 
                              fill='#000000', font_family='JetBrains Mono', 
                              font_size='12px', font_weight='bold')
        dwg.add(badge_label)
    
    # === FINAL ELITE BORDER ===
    elite_border = dwg.rect(insert=(10, 10), size=('1180px', '280px'), 
                           fill='none', stroke='#FFD700', stroke_width='3', 
                           rx=15, ry=15, opacity='0.6')
    dwg.add(elite_border)
    
    dwg.save()
    print("🌟 LEGENDARY LEVEL 4 HEADER GENERATED! Ultimate holographic tech stack deployed! 🚀")

if __name__ == "__main__":
    generate_legendary_header()