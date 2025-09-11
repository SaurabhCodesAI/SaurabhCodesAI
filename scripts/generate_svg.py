# SVG Generator for GitHub Profile
import svgwrite
from datetime import datetime, timezone, timedelta
import random
import math
import os

def get_ist_time():
    """Get current time in IST"""
    ist = timezone(timedelta(hours=5, minutes=30))
    return datetime.now(ist)

def create_header_svg():
    """Create advanced animated header for GitHub profile"""
    
    # SVG dimensions
    width, height = 1200, 300
    
    # Create SVG with animation capabilities
    dwg = svgwrite.Drawing('header.svg', size=(width, height))
    
    # Define gradients
    main_gradient = dwg.defs.add(dwg.linearGradient(id="mainGradient", x1="0%", y1="0%", x2="100%", y2="100%"))
    main_gradient.add_stop_color(0, "#0B0B14")
    main_gradient.add_stop_color(0.3, "#16213E")
    main_gradient.add_stop_color(0.6, "#0F3460")
    main_gradient.add_stop_color(1, "#0D1B2A")
    
    # Neural network gradient
    neural_gradient = dwg.defs.add(dwg.linearGradient(id="neuralGradient", x1="0%", y1="0%", x2="100%", y2="0%"))
    neural_gradient.add_stop_color(0, "#00B4D8", opacity=0.8)
    neural_gradient.add_stop_color(0.5, "#0077B6", opacity=0.6)
    neural_gradient.add_stop_color(1, "#023E8A", opacity=0.4)
    
    # Main background with animation
    bg_rect = dwg.rect(insert=(0, 0), size=(width, height), fill="url(#mainGradient)")
    bg_rect.add(dwg.animate("fill-opacity", values="0.9;1;0.9", dur="8s", repeatCount="indefinite"))
    dwg.add(bg_rect)
    
    # Create neural network visualization
    create_neural_network(dwg, width, height)
    
    # Get current time for dynamic elements
    current_time = get_ist_time()
    hour = current_time.hour
    
    # Dynamic status based on time of day
    if 5 <= hour < 12:
        status = "Optimizing Vector Memory Systems ⚡"
        theme_color = "#00B4D8"
    elif 12 <= hour < 17:
        status = "Developing Tool Selection Logic 🧠"
        theme_color = "#FF5722"
    elif 17 <= hour < 21:
        status = "Training LLM Agent Workflows 🔧"
        theme_color = "#FFB703"
    else:
        status = "AI Research Mode Active 🌙"
        theme_color = "#8338EC"
    
    # Main title section
    title_group = dwg.g()
    
    # Shadow effect for title
    title_shadow = dwg.text("SAURABH PAREEK", insert=(80, 85), 
                            style="font-family: 'JetBrains Mono', monospace; font-size: 48px; font-weight: 900; fill: #000000; opacity: 0.3;")
    title_group.add(title_shadow)
    
    # Main title with glow effect
    main_title = dwg.text("SAURABH PAREEK", insert=(78, 83), 
                          style=f"font-family: 'JetBrains Mono', monospace; font-size: 48px; font-weight: 900; fill: {theme_color}; filter: drop-shadow(0 0 8px {theme_color});")
    main_title.add(dwg.animate("fill", values=f"{theme_color};#FFFFFF;{theme_color}", dur="5s", repeatCount="indefinite"))
    title_group.add(main_title)
    
    # Professional subtitle
    subtitle = dwg.text("Autonomous AI Agent Engineer • Vector Memory Systems", insert=(80, 115),
                        style="font-family: 'Source Code Pro', monospace; font-size: 20px; fill: #E8F4FD; font-weight: 600;")
    title_group.add(subtitle)
    dwg.add(title_group)
    
    # Status dashboard
    status_group = dwg.g()
    
    # Status panel background
    status_bg = dwg.rect(insert=(720, 35), size=(450, 220), rx=15, ry=15,
                         fill="#131526", stroke=theme_color, stroke_width=2, opacity=0.95)
    status_bg.add(dwg.animate("stroke", values=f"{theme_color};#FFFFFF;{theme_color}", dur="6s", repeatCount="indefinite"))
    status_group.add(status_bg)
    
    # Dashboard header
    dashboard_title = dwg.text("🤖 AI Engineer Dashboard", insert=(740, 65),
                               style=f"font-family: 'Fira Code', monospace; font-size: 18px; fill: {theme_color}; font-weight: 700;")
    status_group.add(dashboard_title)
    
    # Status items
    status_items = [
        f"⚡ {status}",
        f"🧠 Projects Delivered: 7+",
        f"🔍 Experience: 1.5+ Years",
        f"☁️  Availability: Ready for Opportunities",
        f"🐳 Tech Stack: Python, LangChain, FAISS",
        f"📊 Specialization: Autonomous AI Agents",
        f"⏰ {current_time.strftime('%H:%M IST')} • Activity: High"
    ]
    
    for i, item in enumerate(status_items):
        y_pos = 100 + (i * 22)
        status_text = dwg.text(item, insert=(740, y_pos),
                               style="font-family: 'Fira Code', monospace; font-size: 14px; fill: #E8F4FD; font-weight: 500;")
        status_group.add(status_text)
    
    dwg.add(status_group)
    
    # Add data processing particles
    create_data_particles(dwg, width, height)
    
    return dwg

def create_neural_network(dwg, width, height):
    """Create animated neural network visualization"""
    nodes = []
    for i in range(25):
        x = random.uniform(50, width-100)
        y = random.uniform(50, height-80)
        size = random.uniform(3, 6)
        nodes.append((x, y, size))
    
    for i in range(len(nodes)):
        connections = random.randint(2, 4)
        connected = 0
        for j in range(len(nodes)):
            if i != j and connected < connections:
                x1, y1, _ = nodes[i]
                x2, y2, _ = nodes[j]
                dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
                if dist < 150:
                    line = dwg.line(start=(x1, y1), end=(x2, y2),
                                    stroke="url(#neuralGradient)", stroke_width=1, opacity=0.6)
                    line.add(dwg.animate("opacity", values="0.2;0.6;0.2", 
                                         dur=f"{random.uniform(3, 7)}s", repeatCount="indefinite"))
                    line.add(dwg.animate("stroke-width", values="1;1.5;1", 
                                         dur=f"{random.uniform(2, 4)}s", repeatCount="indefinite"))
                    dwg.add(line)
                    connected += 1
    
    for x, y, size in nodes:
        node = dwg.circle(center=(x, y), r=size, fill="#00B4D8", opacity=0.8)
        node.add(dwg.animate("r", values=f"{size-1};{size+2};{size-1}", 
                             dur=f"{random.uniform(2, 5)}s", repeatCount="indefinite"))
        node.add(dwg.animate("opacity", values="0.6;1;0.6", 
                             dur=f"{random.uniform(3, 6)}s", repeatCount="indefinite"))
        dwg.add(node)

def create_data_particles(dwg, width, height):
    """Create animated data processing particles"""
    for i in range(15):
        x = random.uniform(100, width-100)
        y = random.uniform(140, height-80)
        particle = dwg.circle(center=(x, y), r=2, fill="#FF5722" if i % 3 == 0 else "#00B4D8", opacity=0.7)
        move_x = random.randint(50, 150) * (1 if random.random() > 0.5 else -1)
        move_y = random.randint(-30, 30)
        
        # Flow animation
        particle.add(dwg.animateTransform("transform", type="translate",
                                          # FIXED: Changed the value from a single string to a list of strings,
                                          # which is what the svgwrite library validator expects.
                                          values=[f"0 0", f"{move_x} {move_y}", f"0 0"],
                                          dur=f"{random.uniform(5, 12)}s", 
                                          repeatCount="indefinite"))
        
        # Opacity pulsing
        particle.add(dwg.animate("opacity", values="0.3;1;0.3", 
                                 dur=f"{random.uniform(2, 5)}s", 
                                 repeatCount="indefinite"))
        dwg.add(particle)

def main():
    """Main function to generate all SVGs"""
    print("🎨 Generating GitHub Profile Visuals...")
    
    # Create the header SVG
    print("🔧 Creating header SVG...")
    header_svg = create_header_svg()
    header_path = os.path.join('header.svg')
    header_svg.saveas(header_path)
    print(f"✅ Header SVG created: {header_path}")
    
    print("🚀 All SVGs generated successfully!")

if __name__ == "__main__":
    main()
