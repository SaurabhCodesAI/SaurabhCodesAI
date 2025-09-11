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
    main_gradient.add_stop_color(0, "#0B0B14")  # Dark blue-black
    main_gradient.add_stop_color(0.3, "#16213E") # Dark blue
    main_gradient.add_stop_color(0.6, "#0F3460") # Medium blue
    main_gradient.add_stop_color(1, "#0D1B2A")   # Deep blue
    
    # Neural network gradient
    neural_gradient = dwg.defs.add(dwg.linearGradient(id="neuralGradient", x1="0%", y1="0%", x2="100%", y2="0%"))
    neural_gradient.add_stop_color(0, "#00B4D8", opacity=0.8)  # Bright blue
    neural_gradient.add_stop_color(0.5, "#0077B6", opacity=0.6) # Medium blue
    neural_gradient.add_stop_color(1, "#023E8A", opacity=0.4)   # Dark blue
    
    # Activity gradient
    activity_gradient = dwg.defs.add(dwg.linearGradient(id="activityGradient", x1="0%", y1="0%", x2="100%", y2="0%"))
    activity_gradient.add_stop_color(0, "#FF5722", opacity=0.8)  # Orange
    activity_gradient.add_stop_color(0.5, "#FF9E80", opacity=0.6) # Light orange
    activity_gradient.add_stop_color(1, "#BF360C", opacity=0.4)  # Dark orange
    
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
    title_shadow.add(dwg.animate("opacity", values="0.1;0.4;0.1", dur="4s", repeatCount="indefinite"))
    title_group.add(title_shadow)
    
    # Main title with glow effect
    main_title = dwg.text("SAURABH PAREEK", insert=(78, 83), 
                          style=f"font-family: 'JetBrains Mono', monospace; font-size: 48px; font-weight: 900; fill: {theme_color}; filter: drop-shadow(0 0 8px {theme_color});")
    main_title.add(dwg.animate("fill", values=f"{theme_color};#FFFFFF;{theme_color}", dur="5s", repeatCount="indefinite"))
    title_group.add(main_title)
    
    # Professional subtitle
    subtitle = dwg.text("Autonomous AI Agent Engineer • Vector Memory Systems", insert=(80, 115),
                        style="font-family: 'Source Code Pro', monospace; font-size: 20px; fill: #E8F4FD; font-weight: 600;")
    subtitle.add(dwg.animate("opacity", values="0.7;1;0.7", dur="3s", repeatCount="indefinite"))
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
    dashboard_title.add(dwg.animate("fill", values=f"{theme_color};#FFFFFF;{theme_color}", dur="4s", repeatCount="indefinite"))
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
        y_pos = 100 + (i * 22) # Adjusted spacing
        status_text = dwg.text(item, insert=(740, y_pos),
                               style="font-family: 'Fira Code', monospace; font-size: 14px; fill: #E8F4FD; font-weight: 500;")
        # Progressive animation delay
        status_text.add(dwg.animate("opacity", values="0.6;1;0.6", dur="4s", 
                                    begin=f"{i*0.3}s", repeatCount="indefinite"))
        status_group.add(status_text)
    
    dwg.add(status_group)
    
    # Add data processing particles
    create_data_particles(dwg, width, height)
    
    # Footer section
    footer_group = dwg.g()
    
    footer_bg = dwg.rect(insert=(0, height-45), size=(width, 45), fill="#0D1117", opacity=0.9)
    footer_group.add(footer_bg)
    
    footer_text = dwg.text("🔬 VertexAutoGPT • Autonomous Research Agents • Vector Memory Systems • Dynamic Tool Selection • Cost-Efficient AI Infrastructure", 
                           insert=(width//2, height-18),
                           style="font-family: 'Inter', sans-serif; font-size: 14px; fill: #94A3B8; text-anchor: middle; font-weight: 600;")
    footer_text.add(dwg.animate("fill", values="#94A3B8;#E8F4FD;#94A3B8", dur="7s", repeatCount="indefinite"))
    footer_group.add(footer_text)
    
    dwg.add(footer_group)
    
    return dwg

def create_neural_network(dwg, width, height):
    """Create animated neural network visualization"""
    
    # Neural network nodes (representing AI agent components)
    nodes = []
    
    # Create neural network nodes
    for i in range(25):
        x = random.uniform(50, width-100)
        y = random.uniform(50, height-80)
        size = random.uniform(3, 6)
        nodes.append((x, y, size))
    
    # Create connections between nodes
    for i in range(len(nodes)):
        # Each node connects to 2-4 other nodes
        connections = random.randint(2, 4)
        connected = 0
        
        for j in range(len(nodes)):
            if i != j and connected < connections:
                # Calculate distance between nodes
                x1, y1, _ = nodes[i]
                x2, y2, _ = nodes[j]
                dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
                
                # Only connect if within reasonable distance
                if dist < 150:
                    # Data flow lines with gradient
                    line = dwg.line(start=(x1, y1), end=(x2, y2),
                                    stroke="url(#neuralGradient)", stroke_width=1, opacity=0.6)
                    
                    # Animate line opacity for data flow effect
                    line.add(dwg.animate("opacity", values="0.2;0.6;0.2", 
                                         dur=f"{random.uniform(3, 7)}s", repeatCount="indefinite"))
                    
                    # Add pulsing animation
                    line.add(dwg.animate("stroke-width", values="1;1.5;1", 
                                         dur=f"{random.uniform(2, 4)}s", repeatCount="indefinite"))
                    
                    dwg.add(line)
                    connected += 1
    
    # Draw neural nodes
    for x, y, size in nodes:
        # Node circle with glowing effect
        node = dwg.circle(center=(x, y), r=size, fill="#00B4D8", opacity=0.8)
        
        # Add subtle pulsing animation
        node.add(dwg.animate("r", values=f"{size-1};{size+2};{size-1}", 
                             dur=f"{random.uniform(2, 5)}s", repeatCount="indefinite"))
        
        node.add(dwg.animate("opacity", values="0.6;1;0.6", 
                             dur=f"{random.uniform(3, 6)}s", repeatCount="indefinite"))
        
        dwg.add(node)

def create_data_particles(dwg, width, height):
    """Create animated data processing particles"""
    
    # Data flow particles
    for i in range(15):
        x = random.uniform(100, width-100)
        y = random.uniform(140, height-80)
        
        # Create particle
        particle = dwg.circle(center=(x, y), r=2, fill="#FF5722" if i % 3 == 0 else "#00B4D8", opacity=0.7)
        
        # Animation path
        move_x = random.randint(50, 150) * (1 if random.random() > 0.5 else -1)
        move_y = random.randint(-30, 30)
        
        # Flow animation
        particle.add(dwg.animateTransform("transform", type="translate",
                                          # FIXED: Changed commas to spaces for correct SVG coordinate syntax
                                          values=f"0 0; {move_x} {move_y}; 0 0",
                                          dur=f"{random.uniform(5, 12)}s", 
                                          repeatCount="indefinite"))
        
        # Opacity pulsing
        particle.add(dwg.animate("opacity", values="0.3;1;0.3", 
                                 dur=f"{random.uniform(2, 5)}s", 
                                 repeatCount="indefinite"))
        
        dwg.add(particle)

def create_analytics_svg():
    """Create GitHub analytics visualization"""
    
    # SVG dimensions
    width, height = 800, 400
    
    # Create SVG
    dwg = svgwrite.Drawing('analytics.svg', size=(width, height))
    
    # Add background gradient
    bg_gradient = dwg.defs.add(dwg.linearGradient(id="bgGradient", x1="0%", y1="0%", x2="0%", y2="100%"))
    bg_gradient.add_stop_color(0, "#0D1117")
    bg_gradient.add_stop_color(1, "#161B22")
    
    # Add background
    bg = dwg.rect(insert=(0, 0), size=(width, height), fill="url(#bgGradient)", rx=10, ry=10)
    dwg.add(bg)
    
    # Add title
    title = dwg.text("AI Engineering Metrics", insert=(width//2, 40), 
                     style="font-family: 'Inter', sans-serif; font-size: 24px; font-weight: 600; fill: #E8F4FD; text-anchor: middle;")
    dwg.add(title)
    
    # Fake metrics data - make this look like GitHub contribution data
    projects = ["VertexAutoGPT", "Vector Memory", "Tool Router", "Snap2Slides", "Core Dev", "Unicode Map", "GitHub Flow"]
    values = [80, 65, 72, 85, 60, 45, 55]
    colors = ["#FF5722", "#00B4D8", "#FFB703", "#8338EC", "#00CC99", "#FB5607", "#3A86FF"]
    
    # Chart area
    chart_x = 100
    chart_y = 80
    chart_width = width - 200
    chart_height = 200
    bar_width = chart_width // len(projects) - 10
    
    # Draw bars
    for i, (project, value, color) in enumerate(zip(projects, values, colors)):
        # Calculate bar height
        bar_height = (value / 100) * chart_height
        
        # Bar x position
        bar_x = chart_x + (i * (bar_width + 10))
        
        # Create bar gradient
        bar_gradient_id = f"barGradient{i}"
        bar_gradient = dwg.defs.add(dwg.linearGradient(id=bar_gradient_id, x1="0%", y1="0%", x2="0%", y2="100%"))
        bar_gradient.add_stop_color(0, color)
        bar_gradient.add_stop_color(1, darken_color(color))
        
        # Draw bar
        bar = dwg.rect(insert=(bar_x, chart_y + chart_height - bar_height), 
                       size=(bar_width, bar_height), 
                       fill=f"url(#{bar_gradient_id})", 
                       rx=5, ry=5)
        
        # Add animation
        bar.add(dwg.animate("height", values="0;"+str(bar_height), dur="1s", begin=f"{i*0.1}s", fill="freeze"))
        bar.add(dwg.animate("y", values=f"{chart_y + chart_height};{chart_y + chart_height - bar_height}", dur="1s", begin=f"{i*0.1}s", fill="freeze"))
        
        dwg.add(bar)
        
        # Add project name
        project_text = dwg.text(project, insert=(bar_x + bar_width//2, chart_y + chart_height + 25),
                                style="font-family: 'Inter', sans-serif; font-size: 12px; fill: #94A3B8; text-anchor: middle; font-weight: 500;")
        project_text.add(dwg.animate("opacity", values="0;1", dur="0.5s", begin=f"{i*0.1 + 0.5}s", fill="freeze"))
        dwg.add(project_text)
        
        # Add value text
        value_text = dwg.text(str(value), insert=(bar_x + bar_width//2, chart_y + chart_height - bar_height - 10),
                              style="font-family: 'Inter', sans-serif; font-size: 14px; fill: #E8F4FD; text-anchor: middle; font-weight: 600;")
        value_text.add(dwg.animate("opacity", values="0;1", dur="0.5s", begin=f"{i*0.1 + 0.5}s", fill="freeze"))
        dwg.add(value_text)
    
    # Add horizontal line
    h_line = dwg.line(start=(chart_x - 10, chart_y + chart_height), end=(chart_x + chart_width + 10, chart_y + chart_height),
                      stroke="#2D333B", stroke_width=2)
    dwg.add(h_line)
    
    # Add vertical line
    v_line = dwg.line(start=(chart_x, chart_y - 10), end=(chart_x, chart_y + chart_height + 10),
                      stroke="#2D333B", stroke_width=2)
    dwg.add(v_line)
    
    return dwg

def darken_color(hex_color):
    """Darken a hex color by 30%"""
    # Remove the # if present
    hex_color = hex_color.lstrip('#')
    
    # Convert to RGB
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    
    # Darken by 30%
    factor = 0.7
    r = int(r * factor)
    g = int(g * factor)
    b = int(b * factor)
    
    # Convert back to hex
    return f"#{r:02x}{g:02x}{b:02x}"

def main():
    """Main function to generate all SVGs"""
    print("🎨 Generating GitHub Profile Visuals...")
    
    # Create the header SVG
    print("🔧 Creating header SVG...")
    header_svg = create_header_svg()
    # Use os.path.join for better path handling, especially in actions
    header_path = os.path.join('header.svg')
    header_svg.saveas(header_path)
    print(f"✅ Header SVG created: {header_path}")
    
    # Create analytics SVG
    print("📊 Creating analytics SVG...")
    analytics_svg = create_analytics_svg()
    analytics_path = os.path.join('analytics.svg')
    analytics_svg.saveas(analytics_path)
    print(f"✅ Analytics SVG created: {analytics_path}")
    
    print("🚀 All SVGs generated successfully!")

if __name__ == "__main__":
    main()
