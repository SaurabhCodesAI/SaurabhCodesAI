import svgwrite
import datetime
import random
import math

def generate_elite_combo_svg():
    # Get IST time
    ist_offset = datetime.timedelta(hours=5, minutes=30)
    now = datetime.datetime.now(datetime.timezone.utc) + ist_offset
    timestamp = now.strftime("%B %d, %Y %H:%M:%S IST")
    time_only = now.strftime("%H:%M:%S")
    
    # Elite dimensions - much larger and more impressive
    dwg = svgwrite.Drawing('header.svg', profile='full', size=('1000px', '200px'))
    
    # === BACKGROUND LAYERS ===
    # Gradient background (cyberpunk style)
    gradient = dwg.defs.add(dwg.linearGradient(id="cyber_bg", x1="0%", y1="0%", x2="100%", y2="100%"))
    gradient.add_stop_color(offset="0%", color="#0a0a0a")
    gradient.add_stop_color(offset="30%", color="#1a0033")
    gradient.add_stop_color(offset="70%", color="#000a1a")
    gradient.add_stop_color(offset="100%", color="#0D1117")
    
    # Main background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='url(#cyber_bg)'))
    
    # Matrix grid overlay
    for i in range(0, 1000, 100):
        dwg.add(dwg.line(start=(i, 0), end=(i, 200), 
                        stroke='#00FFFF', stroke_width='0.3', opacity='0.1'))
    for i in range(0, 200, 40):
        dwg.add(dwg.line(start=(0, i), end=(1000, i), 
                        stroke='#00FFFF', stroke_width='0.3', opacity='0.1'))
    
    # Animated particles (matrix rain effect)
    for i in range(25):
        x = random.randint(50, 950)
        y = random.randint(20, 180)
        size = random.uniform(0.5, 2)
        opacity = random.uniform(0.3, 0.8)
        dwg.add(dwg.circle(center=(x, y), r=size, 
                          fill='#00FFFF', opacity=str(opacity)))
    
    # === TERMINAL WINDOW DECORATION ===
    # Terminal header bar
    terminal_bar = dwg.rect(insert=(20, 20), size=('960px', '25px'), 
                           fill='#2d2d2d', rx=8, ry=8)
    dwg.add(terminal_bar)
    
    # Terminal buttons
    dwg.add(dwg.circle(center=(35, 32), r=4, fill='#FF5F56'))  # Close
    dwg.add(dwg.circle(center=(55, 32), r=4, fill='#FFBD2E'))  # Minimize
    dwg.add(dwg.circle(center=(75, 32), r=4, fill='#27CA3F'))  # Maximize
    
    # Terminal title
    terminal_title = dwg.text("elite_dev_terminal.sh", insert=(100, 37), 
                             fill='#ffffff', font_family='JetBrains Mono', 
                             font_size='11px', opacity='0.8')
    dwg.add(terminal_title)
    
    # Current time indicator (top right)
    time_display = dwg.text(f"⏰ {time_only} IST", insert=(850, 37), 
                           fill='#00FF88', font_family='JetBrains Mono', 
                           font_size='11px', font_weight='bold')
    dwg.add(time_display)
    
    # === MAIN CONTENT AREA ===
    # Terminal prompt line 1
    prompt1 = dwg.text("saurabh@elite-architect:~$ ", insert=(30, 70), 
                      fill='#00FF00', font_family='JetBrains Mono', 
                      font_size='16px', font_weight='bold')
    dwg.add(prompt1)
    
    # Command output line 1
    cmd1 = dwg.text("whoami", insert=(230, 70), 
                   fill='#FFD700', font_family='JetBrains Mono', 
                   font_size='16px')
    dwg.add(cmd1)
    
    # Output of whoami
    output1 = dwg.text("🚀 LLM Infrastructure Architect | AI Systems Designer", 
                      insert=(30, 95), fill='#00D4FF', 
                      font_family='JetBrains Mono', font_size='14px')
    dwg.add(output1)
    
    # Terminal prompt line 2
    prompt2 = dwg.text("saurabh@elite-architect:~$ ", insert=(30, 120), 
                      fill='#00FF00', font_family='JetBrains Mono', 
                      font_size='16px', font_weight='bold')
    dwg.add(prompt2)
    
    # Command output line 2
    cmd2 = dwg.text("git status --porcelain", insert=(230, 120), 
                   fill='#FFD700', font_family='JetBrains Mono', 
                   font_size='16px')
    dwg.add(cmd2)
    
    # Git status output
    status_text = f"🔥 ACTIVE • Building the future with AI • Last Sync: {timestamp}"
    output2 = dwg.text(status_text, insert=(30, 145), 
                      fill='#FF69B4', font_family='JetBrains Mono', 
                      font_size='12px')
    dwg.add(output2)
    
    # === ELITE STATUS INDICATORS ===
    # Status badges (right side)
    badge_y = 70
    
    # Online status
    dwg.add(dwg.rect(insert=(650, badge_y-10), size=('80px', '20px'), 
                    fill='#00FF88', rx=10, ry=10))
    dwg.add(dwg.text("🟢 ONLINE", insert=(658, badge_y+2), 
                    fill='#000000', font_family='JetBrains Mono', 
                    font_size='10px', font_weight='bold'))
    
    # Building status
    dwg.add(dwg.rect(insert=(740, badge_y-10), size=('85px', '20px'), 
                    fill='#FFD700', rx=10, ry=10))
    dwg.add(dwg.text("⚡ CODING", insert=(748, badge_y+2), 
                    fill='#000000', font_family='JetBrains Mono', 
                    font_size='10px', font_weight='bold'))
    
    # Elite level
    dwg.add(dwg.rect(insert=(835, badge_y-10), size=('90px', '20px'), 
                    fill='#FF1493', rx=10, ry=10))
    dwg.add(dwg.text("👑 ELITE LVL", insert=(843, badge_y+2), 
                    fill='#FFFFFF', font_family='JetBrains Mono', 
                    font_size='10px', font_weight='bold'))
    
    # === TECH STACK VISUAL ===
    tech_y = 100
    tech_items = ["🐍 Python", "⚛️ React", "🚀 FastAPI", "☁️ GCP", "🤖 AI/ML"]
    
    for i, tech in enumerate(tech_items):
        x_pos = 650 + (i * 70)
        # Tech bubble
        dwg.add(dwg.circle(center=(x_pos+15, tech_y+10), r=12, 
                          fill='#1a1a2e', stroke='#00FFFF', stroke_width='1'))
        dwg.add(dwg.text(tech.split()[0], insert=(x_pos+10, tech_y+15), 
                        fill='#00FFFF', font_family='JetBrains Mono', 
                        font_size='12px'))
    
    # === NEURAL NETWORK ANIMATION EFFECT ===
    # Connection lines between elements
    for i in range(5):
        start_x = 650 + (i * 70) + 15
        end_x = start_x + 70
        if i < 4:  # Don't draw beyond last element
            dwg.add(dwg.line(start=(start_x+12, tech_y+10), end=(end_x-12, tech_y+10), 
                            stroke='#00FFFF', stroke_width='1', opacity='0.5'))
    
    # === CURSOR BLINK EFFECT ===
    cursor = dwg.rect(insert=(30 + len(status_text) * 7, 135), size=('2px', '15px'), 
                     fill='#00FF00')
    dwg.add(cursor)
    
    # === BORDER GLOW EFFECT ===
    border = dwg.rect(insert=(10, 10), size=('980px', '180px'), 
                     fill='none', stroke='#00FFFF', stroke_width='2', 
                     rx=10, ry=10, opacity='0.3')
    dwg.add(border)
    
    dwg.save()
    print("🌟 ELITE COMBO HEADER GENERATED! The pinnacle of GitHub aesthetics! 🚀")

if __name__ == "__main__":
    generate_elite_combo_svg()