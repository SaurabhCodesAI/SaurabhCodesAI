# SVG Generator for GitHub Profile
import svgwrite
from datetime import datetime, timezone, timedelta
import random
import math

def get_ist_time():
    """Get current time in IST"""
    ist = timezone(timedelta(hours=5, minutes=30))
    return datetime.now(ist)

def create_header_svg():
    """Create advanced animated header for GitHub profile"""
    
    # SVG dimensions
    width, height = 1200, 300
    dwg = svgwrite.Drawing('header.svg', size=(width, height))
    
    # Define gradients
    main_gradient = dwg.defs.add(dwg.linearGradient(id="mainGradient", x1="0%", y1="0%", x2="100%", y2="100%"))
    main_gradient.add_stop_color(0, "#0B0B14")
    main_gradient.add_stop_color(0.3, "#16213E")
    main_gradient.add_stop_color(0.6, "#0F3460")
    main_gradient.add_stop_color(1, "#0D1B2A")
    
    neural_gradient = dwg.defs.add(dwg.linearGradient(id="neuralGradient", x1="0%", y1="0%", x2="100%", y2="0%"))
    neural_gradient.add_stop_color(0, "#00B4D8", opacity=0.8)
    neural_gradient.add_stop_color(0.5, "#0077B6", opacity=0.6)
    neural_gradient.add_stop_color(1, "#023E8A", opacity=0.4)
    
    # Main background with animation
    bg_rect = dwg.rect(insert=(0, 0), size=(width, height), fill="url(#mainGradient)")
    bg_rect.add(dwg.animate(attributeName="fill-opacity", values="0.9;1;0.9", dur="8s", repeatCount="indefinite"))
    dwg.add(bg_rect)
    
    create_neural_network(dwg, width, height)
    
    current_time = get_ist_time()
    hour = current_time.hour
    
    if 5 <= hour < 12:
        status, theme_color = "Optimizing Vector Memory Systems ⚡", "#00B4D8"
    elif 12 <= hour < 17:
        status, theme_color = "Developing Tool Selection Logic 🧠", "#FF5722"
    elif 17 <= hour < 21:
        status, theme_color = "Training LLM Agent Workflows 🔧", "#FFB703"
    else:
        status, theme_color = "AI Research Mode Active 🌙", "#8338EC"
    
    # Main title
    title_group = dwg.g()
    title_shadow = dwg.text("SAURABH PAREEK", insert=(80, 85), style="font-family: 'JetBrains Mono', monospace; font-size: 48px; font-weight: 900; fill: #000000; opacity: 0.3;")
    title_group.add(title_shadow)
    
    main_title = dwg.text("SAURABH PAREEK", insert=(78, 83), style=f"font-family: 'JetBrains Mono', monospace; font-size: 48px; font-weight: 900; fill: {theme_color}; filter: drop-shadow(0 0 8px {theme_color});")
    main_title.add(dwg.animate(attributeName="fill", values=f"{theme_color};#FFFFFF;{theme_color}", dur="5s", repeatCount="indefinite"))
    title_group.add(main_title)
    
    subtitle = dwg.text("Autonomous AI Agent Engineer • Vector Memory Systems", insert=(80, 115), style="font-family: 'Source Code Pro', monospace; font-size: 20px; fill: #E8F4FD; font-weight: 600;")
    title_group.add(subtitle)
    dwg.add(title_group)
    
    # Status dashboard
    status_group = dwg.g()
    status_bg = dwg.rect(insert=(720, 35), size=(450, 220), rx=15, ry=15, fill="#131526", stroke=theme_color, stroke_width=2, opacity=0.95)
    status_bg.add(dwg.animate(attributeName="stroke", values=f"{theme_color};#FFFFFF;{theme_color}", dur="6s", repeatCount="indefinite"))
    status_group.add(status_bg)
    
    dashboard_title = dwg.text("🤖 AI Engineer Dashboard", insert=(740, 65), style=f"font-family: 'Fira Code', monospace; font-size: 18px; fill: {theme_color}; font-weight: 700;")
    status_group.add(dashboard_title)
    
    status_items = [
        f"⚡ {status}", f"🧠 Projects Delivered: 7+", f"🔍 Experience: 1.5+ Years",
        f"☁️  Availability: Ready for Opportunities", f"🐳 Tech Stack: Python, LangChain, FAISS",
        f"📊 Specialization: Autonomous AI Agents", f"⏰ {current_time.strftime('%H:%M IST')} • Activity: High"
    ]
    
    for i, item in enumerate(status_items):
        status_text = dwg.text(item, insert=(740, 100 + (i * 22)), style="font-family: 'Fira Code', monospace; font-size: 14px; fill: #E8F4FD; font-weight: 500;")
        status_group.add(status_text)
    
    dwg.add(status_group)
    create_data_particles(dwg, width, height)
    return dwg

def create_neural_network(dwg, width, height):
    """Create animated neural network visualization"""
    nodes = [(random.uniform(50, width-100), random.uniform(50, height-80), random.uniform(3, 6)) for _ in range(25)]
    
    for i, (x1, y1, _) in enumerate(nodes):
        for j, (x2, y2, _) in enumerate(nodes):
            if i != j and math.sqrt((x2-x1)**2 + (y2-y1)**2) < 150:
                line = dwg.line(start=(x1, y1), end=(x2, y2), stroke="url(#neuralGradient)", stroke_width=1, opacity=0.6)
                line.add(dwg.animate(attributeName="opacity", values="0.2;0.6;0.2", dur=f"{random.uniform(3, 7)}s", repeatCount="indefinite"))
                line.add(dwg.animate(attributeName="stroke-width", values="1;1.5;1", dur=f"{random.uniform(2, 4)}s", repeatCount="indefinite"))
                dwg.add(line)
    
    for x, y, size in nodes:
        node = dwg.circle(center=(x, y), r=size, fill="#00B4D8", opacity=0.8)
        node.add(dwg.animate(attributeName="r", values=f"{size-1};{size+2};{size-1}", dur=f"{random.uniform(2, 5)}s", repeatCount="indefinite"))
        dwg.add(node)

def create_data_particles(dwg, width, height):
    """Create animated data processing particles"""
    for i in range(15):
        x = random.uniform(100, width - 100)
        y = random.uniform(140, height - 80)
        particle = dwg.circle(center=(x, y), r=2, fill="#FF5722" if i % 3 == 0 else "#00B4D8", opacity=0.7)
        
        move_x = random.randint(50, 150) * random.choice([1, -1])
        move_y = random.randint(-30, 30)
        
        # ✅ Fixed animateTransform usage
        particle.add(dwg.animateTransform(
            transform="translate",
            from_="0 0",
            to=f"{move_x} {move_y}",
            dur=f"{random.uniform(5, 12)}s",
            repeatCount="indefinite"
        ))
        
        particle.add(dwg.animate(
            attributeName="opacity",
            values="0.3;1;0.3",
            dur=f"{random.uniform(2, 5)}s",
            repeatCount="indefinite"
        ))
        
        dwg.add(particle)

def main():
    """Main function to generate the SVG"""
    print("🎨 Generating GitHub Profile Visuals...")
    header_svg = create_header_svg()
    header_svg.saveas('header.svg', pretty=True)
    print("✅ Header SVG created: header.svg")
    print("🚀 SVG generation successful!")

if __name__ == "__main__":
    main()
