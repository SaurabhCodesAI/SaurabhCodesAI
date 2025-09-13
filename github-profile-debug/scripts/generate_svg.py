#!/usr/bin/env python3
"""
Elite SVG Generator for GitHub Profile
Advanced animated graphics with comprehensive error handling and production-grade code quality.

Author: Saurabh Pareek (AI Engineer)
License: MIT
"""

import sys
import os
import traceback
import logging
from pathlib import Path
from typing import Tuple, Optional
from datetime import datetime, timezone, timedelta

# Configure logging for production monitoring (cross-platform)
import sys
import io

# Fix Windows console encoding issues while maintaining Linux compatibility
if sys.platform.startswith('win'):
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    except AttributeError:
        # Handle cases where stdout/stderr don't have buffer attribute
        pass

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('svg_generation.log', mode='a', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)

# Safe imports with comprehensive error handling
try:
    import svgwrite
    logger.info(f"✅ svgwrite imported successfully (version: {svgwrite.__version__})")
except ImportError as e:
    logger.error(f"❌ Failed to import svgwrite: {e}")
    logger.error("Install with: pip install svgwrite")
    sys.exit(1)

try:
    import random
    import math
    logger.info("✅ Standard libraries imported successfully")
except ImportError as e:
    logger.error(f"❌ Failed to import standard libraries: {e}")
    sys.exit(1)

# Global configuration with type hints
SVG_CONFIG = {
    'header': {'width': 1200, 'height': 300, 'filename': 'header.svg'},
    'analytics': {'width': 800, 'height': 200, 'filename': 'analytics.svg'}
}

def setup_environment() -> bool:
    """
    Setup and validate the execution environment.
    Returns True if environment is ready, False otherwise.
    """
    try:
        # Ensure we're in the correct directory
        script_dir = Path(__file__).parent.absolute()
        root_dir = script_dir.parent
        
        logger.info(f"Script directory: {script_dir}")
        logger.info(f"Root directory: {root_dir}")
        
        # Change to root directory for SVG output
        os.chdir(root_dir)
        logger.info(f"Changed working directory to: {os.getcwd()}")
        
        # Verify scripts directory exists
        if not script_dir.exists():
            logger.error(f"Scripts directory not found: {script_dir}")
            return False
        
        logger.info("✅ Environment setup completed successfully")
        return True
        
    except Exception as e:
        logger.error(f"❌ Environment setup failed: {e}")
        logger.error(traceback.format_exc())
        return False

def get_ist_time() -> datetime:
    """
    Get current time in IST with error handling.
    Returns current IST time or UTC time as fallback.
    """
    try:
        ist = timezone(timedelta(hours=5, minutes=30))
        current_time = datetime.now(ist)
        logger.info(f"Current IST time: {current_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
        return current_time
    except Exception as e:
        logger.warning(f"Failed to get IST time, using UTC: {e}")
        return datetime.now(timezone.utc)

def get_dynamic_status() -> Tuple[str, str]:
    """
    Get dynamic status based on current time with comprehensive error handling.
    Returns (status_message, theme_color) tuple.
    """
    try:
        current_time = get_ist_time()
        hour = current_time.hour
        
        # Define status mapping with fallback
        status_map = {
            (5, 12): ("Optimizing Vector Memory Systems ⚡", "#00B4D8"),
            (12, 17): ("Developing Tool Selection Logic 🧠", "#FF5722"),
            (17, 21): ("Training LLM Agent Workflows 🔧", "#FFB703"),
            (21, 5): ("AI Research Mode Active 🌙", "#8338EC")
        }
        
        for (start, end), (status, color) in status_map.items():
            if start <= end:  # Normal range
                if start <= hour < end:
                    logger.info(f"Status: {status} (hour: {hour})")
                    return status, color
            else:  # Overnight range (21-5)
                if hour >= start or hour < end:
                    logger.info(f"Status: {status} (hour: {hour})")
                    return status, color
        
        # Fallback status
        logger.warning(f"No status found for hour {hour}, using fallback")
        return "AI Development Active 🤖", "#64FFDA"
        
    except Exception as e:
        logger.error(f"Failed to get dynamic status: {e}")
        return "AI Engineer Available 🚀", "#00B4D8"

def create_safe_gradient(dwg: svgwrite.Drawing, gradient_id: str, stops: list) -> bool:
    """
    Create SVG gradient with error handling.
    Returns True if successful, False otherwise.
    """
    try:
        gradient = dwg.defs.add(dwg.linearGradient(
            id=gradient_id, 
            x1="0%", y1="0%", 
            x2="100%", y2="100%"
        ))
        
        for i, (color, opacity) in enumerate(stops):
            position = i / (len(stops) - 1) if len(stops) > 1 else 0
            gradient.add_stop_color(position, color, opacity=opacity)
        
        logger.debug(f"Created gradient: {gradient_id}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to create gradient {gradient_id}: {e}")
        return False

def create_header_svg() -> Optional[svgwrite.Drawing]:
    """
    Create advanced animated header for GitHub profile with comprehensive error handling.
    Returns SVG Drawing object or None if failed.
    """
    try:
        logger.info("🎨 Starting header SVG generation...")
        
        # SVG dimensions from config
        config = SVG_CONFIG['header']
        width, height = config['width'], config['height']
        
        # Create drawing with error handling
        try:
            dwg = svgwrite.Drawing(config['filename'], size=(width, height))
            logger.info(f"Created SVG canvas: {width}x{height}")
        except Exception as e:
            logger.error(f"Failed to create SVG drawing: {e}")
            return None
        
        # Define gradients with comprehensive error handling
        gradients = [
            ("mainGradient", [("#0B0B14", 1.0), ("#16213E", 1.0), ("#0F3460", 1.0), ("#0D1B2A", 1.0)]),
            ("neuralGradient", [("#00B4D8", 0.8), ("#0077B6", 0.6), ("#023E8A", 0.4)])
        ]
        
        for gradient_id, stops in gradients:
            if not create_safe_gradient(dwg, gradient_id, stops):
                logger.warning(f"Failed to create {gradient_id}, using fallback")
        
        # Main background with animation and error handling
        try:
            bg_rect = dwg.rect(insert=(0, 0), size=(width, height), fill="url(#mainGradient)")
            bg_rect.add(dwg.animate(
                attributeName="fill-opacity", 
                values="0.9;1;0.9", 
                dur="8s", 
                repeatCount="indefinite"
            ))
            dwg.add(bg_rect)
            logger.debug("Added animated background")
        except Exception as e:
            logger.warning(f"Failed to add animated background: {e}")
            # Fallback: solid background
            dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill="#0D1B2A"))
        
        # Create neural network with error handling
        if not create_neural_network(dwg, width, height):
            logger.warning("Neural network creation failed, continuing without it")
        
        # Get dynamic status
        status, theme_color = get_dynamic_status()
        
        # Main title with comprehensive error handling
        try:
            title_group = dwg.g()
            
            # Shadow effect
            title_shadow = dwg.text(
                "SAURABH PAREEK", 
                insert=(80, 85), 
                style=f"font-family: 'JetBrains Mono', monospace; font-size: 48px; font-weight: 900; fill: #000000; opacity: 0.3;"
            )
            title_group.add(title_shadow)
            
            # Main title with animation
            main_title = dwg.text(
                "SAURABH PAREEK", 
                insert=(78, 83), 
                style=f"font-family: 'JetBrains Mono', monospace; font-size: 48px; font-weight: 900; fill: {theme_color}; filter: drop-shadow(0 0 8px {theme_color});"
            )
            main_title.add(dwg.animate(
                attributeName="fill", 
                values=f"{theme_color};#FFFFFF;{theme_color}", 
                dur="5s", 
                repeatCount="indefinite"
            ))
            title_group.add(main_title)
            
            # Subtitle
            subtitle = dwg.text(
                "Autonomous AI Agent Engineer • Vector Memory Systems", 
                insert=(80, 115), 
                style="font-family: 'Source Code Pro', monospace; font-size: 20px; fill: #E8F4FD; font-weight: 600;"
            )
            title_group.add(subtitle)
            
            dwg.add(title_group)
            logger.debug("Added title section")
            
        except Exception as e:
            logger.error(f"Failed to create title section: {e}")
            # Fallback: simple title
            try:
                dwg.add(dwg.text(
                    "SAURABH PAREEK - AI Engineer", 
                    insert=(80, 83), 
                    style="font-family: monospace; font-size: 36px; fill: #64FFDA;"
                ))
            except Exception as fallback_e:
                logger.error(f"Even fallback title failed: {fallback_e}")
        
        # Status dashboard with error handling
        if not create_status_dashboard(dwg, status, theme_color, width, height):
            logger.warning("Status dashboard creation failed")
        
        # Data particles with error handling
        if not create_data_particles(dwg, width, height):
            logger.warning("Data particles creation failed")
        
        logger.info("✅ Header SVG generation completed successfully")
        return dwg
        
    except Exception as e:
        logger.error(f"❌ Critical error in header SVG generation: {e}")
        logger.error(traceback.format_exc())
        return None

def create_status_dashboard(dwg: svgwrite.Drawing, status: str, theme_color: str, width: int, height: int) -> bool:
    """
    Create status dashboard with comprehensive error handling.
    Returns True if successful, False otherwise.
    """
    try:
        current_time = get_ist_time()
        
        status_group = dwg.g()
        
        # Status background
        status_bg = dwg.rect(
            insert=(720, 35), 
            size=(450, 220), 
            rx=15, ry=15, 
            fill="#131526", 
            stroke=theme_color, 
            stroke_width=2, 
            opacity=0.95
        )
        status_bg.add(dwg.animate(
            attributeName="stroke", 
            values=f"{theme_color};#FFFFFF;{theme_color}", 
            dur="6s", 
            repeatCount="indefinite"
        ))
        status_group.add(status_bg)
        
        # Dashboard title
        dashboard_title = dwg.text(
            "🤖 AI Engineer Dashboard", 
            insert=(740, 65), 
            style=f"font-family: 'Fira Code', monospace; font-size: 18px; fill: {theme_color}; font-weight: 700;"
        )
        status_group.add(dashboard_title)
        
        # Status items with error handling
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
            try:
                status_text = dwg.text(
                    item, 
                    insert=(740, 100 + (i * 22)), 
                    style="font-family: 'Fira Code', monospace; font-size: 14px; fill: #E8F4FD; font-weight: 500;"
                )
                status_group.add(status_text)
            except Exception as e:
                logger.warning(f"Failed to add status item {i}: {e}")
                continue
        
        dwg.add(status_group)
        logger.debug("Status dashboard created successfully")
        return True
        
    except Exception as e:
        logger.error(f"Failed to create status dashboard: {e}")
        return False

def create_neural_network(dwg: svgwrite.Drawing, width: int, height: int) -> bool:
    """
    Create animated neural network visualization with comprehensive error handling.
    Returns True if successful, False otherwise.
    """
    try:
        logger.debug("Creating neural network visualization...")
        
        # Set random seed for reproducible results in CI
        random.seed(42)
        
        # Generate nodes with error handling
        nodes = []
        for _ in range(25):
            try:
                x = random.uniform(50, width-100)
                y = random.uniform(50, height-80)
                radius = random.uniform(3, 6)
                nodes.append((x, y, radius))
            except Exception as e:
                logger.warning(f"Failed to generate node: {e}")
                continue
        
        if not nodes:
            logger.error("No nodes generated for neural network")
            return False
        
        # Create connections between nodes
        connections_created = 0
        for i, (x1, y1, _) in enumerate(nodes):
            for j, (x2, y2, _) in enumerate(nodes):
                if i != j and math.sqrt((x2-x1)**2 + (y2-y1)**2) < 150:
                    try:
                        line = dwg.line(
                            start=(x1, y1), 
                            end=(x2, y2), 
                            stroke="url(#neuralGradient)", 
                            stroke_width=1, 
                            opacity=0.6
                        )
                        
                        # Add animations with error handling
                        try:
                            line.add(dwg.animate(
                                attributeName="opacity", 
                                values="0.2;0.6;0.2", 
                                dur=f"{random.uniform(3, 7)}s", 
                                repeatCount="indefinite"
                            ))
                            line.add(dwg.animate(
                                attributeName="stroke-width", 
                                values="1;1.5;1", 
                                dur=f"{random.uniform(2, 4)}s", 
                                repeatCount="indefinite"
                            ))
                        except Exception as e:
                            logger.warning(f"Failed to add line animation: {e}")
                        
                        dwg.add(line)
                        connections_created += 1
                        
                    except Exception as e:
                        logger.warning(f"Failed to create connection: {e}")
                        continue
        
        # Create node circles
        nodes_created = 0
        for x, y, size in nodes:
            try:
                node = dwg.circle(center=(x, y), r=size, fill="#00B4D8", opacity=0.8)
                
                # Add animation with error handling
                try:
                    node.add(dwg.animate(
                        attributeName="r", 
                        values=f"{size-1};{size+2};{size-1}", 
                        dur=f"{random.uniform(2, 5)}s", 
                        repeatCount="indefinite"
                    ))
                except Exception as e:
                    logger.warning(f"Failed to add node animation: {e}")
                
                dwg.add(node)
                nodes_created += 1
                
            except Exception as e:
                logger.warning(f"Failed to create node: {e}")
                continue
        
        logger.info(f"Neural network created: {nodes_created} nodes, {connections_created} connections")
        return True
        
    except Exception as e:
        logger.error(f"Failed to create neural network: {e}")
        return False

def create_data_particles(dwg: svgwrite.Drawing, width: int, height: int) -> bool:
    """
    Create animated data processing particles with comprehensive error handling.
    Returns True if successful, False otherwise.
    """
    try:
        logger.debug("Creating data particles...")
        
        particles_created = 0
        for i in range(15):
            try:
                x = random.uniform(100, width - 100)
                y = random.uniform(140, height - 80)
                color = "#FF5722" if i % 3 == 0 else "#00B4D8"
                
                particle = dwg.circle(center=(x, y), r=2, fill=color, opacity=0.7)
                
                # Movement parameters
                move_x = random.randint(50, 150) * random.choice([1, -1])
                move_y = random.randint(-30, 30)
                
                # Add transform animation with error handling
                try:
                    transform_anim = dwg.animateTransform(
                        "translate",
                        values=f"0,0;{move_x},{move_y};0,0",
                        dur=f"{random.uniform(5, 12)}s",
                        repeatCount="indefinite"
                    )
                    particle.add(transform_anim)
                except Exception as e:
                    logger.warning(f"Failed to add particle transform animation: {e}")
                
                # Add opacity animation with error handling
                try:
                    particle.add(dwg.animate(
                        attributeName="opacity",
                        values="0.3;1;0.3",
                        dur=f"{random.uniform(2, 5)}s",
                        repeatCount="indefinite"
                    ))
                except Exception as e:
                    logger.warning(f"Failed to add particle opacity animation: {e}")
                
                dwg.add(particle)
                particles_created += 1
                
            except Exception as e:
                logger.warning(f"Failed to create particle {i}: {e}")
                continue
        
        logger.info(f"Created {particles_created} data particles")
        return True
        
    except Exception as e:
        logger.error(f"Failed to create data particles: {e}")
        return False

def create_analytics_svg() -> Optional[svgwrite.Drawing]:
    """
    Create analytics dashboard SVG with comprehensive error handling.
    Returns SVG Drawing object or None if failed.
    """
    try:
        logger.info("📊 Starting analytics SVG generation...")
        
        # SVG dimensions from config
        config = SVG_CONFIG['analytics']
        width, height = config['width'], config['height']
        
        # Create drawing with error handling
        try:
            dwg = svgwrite.Drawing(config['filename'], size=(width, height))
            logger.info(f"Created analytics SVG canvas: {width}x{height}")
        except Exception as e:
            logger.error(f"Failed to create analytics SVG drawing: {e}")
            return None
        
        # Background with error handling
        try:
            bg = dwg.rect(
                insert=(0, 0), 
                size=(width, height), 
                fill="#0D1117", 
                stroke="#21262D", 
                stroke_width=1
            )
            dwg.add(bg)
            logger.debug("Added analytics background")
        except Exception as e:
            logger.warning(f"Failed to add background: {e}")
        
        # Title with error handling
        try:
            title = dwg.text(
                "AI Engineering Metrics", 
                insert=(20, 40),
                style="font-family: 'Fira Code', monospace; font-size: 24px; fill: #58A6FF; font-weight: 700;"
            )
            dwg.add(title)
            logger.debug("Added analytics title")
        except Exception as e:
            logger.warning(f"Failed to add title: {e}")
        
        # Metrics with comprehensive error handling
        metrics = [
            ("Vector Memory Ops", "2.3M+", "#FF6B6B"),
            ("Tool Selection Accuracy", "92%", "#4ECDC4"),
            ("Cost Optimization", "85%", "#45B7D1"),
            ("Active Projects", "7+", "#96CEB4")
        ]
        
        metrics_created = 0
        for i, (label, value, color) in enumerate(metrics):
            try:
                x_pos = 50 + (i * 180)
                
                # Metric box with error handling
                try:
                    box = dwg.rect(
                        insert=(x_pos-30, 70), 
                        size=(160, 80), 
                        rx=8, ry=8,
                        fill="#161B22", 
                        stroke=color, 
                        stroke_width=2, 
                        opacity=0.9
                    )
                    dwg.add(box)
                except Exception as e:
                    logger.warning(f"Failed to create metric box {i}: {e}")
                    continue
                
                # Value text with error handling
                try:
                    val_text = dwg.text(
                        value, 
                        insert=(x_pos, 110),
                        style=f"font-family: 'JetBrains Mono', monospace; font-size: 20px; fill: {color}; font-weight: 900; text-anchor: middle;"
                    )
                    dwg.add(val_text)
                except Exception as e:
                    logger.warning(f"Failed to create value text {i}: {e}")
                
                # Label text with error handling
                try:
                    label_text = dwg.text(
                        label, 
                        insert=(x_pos, 130),
                        style="font-family: 'Fira Code', monospace; font-size: 12px; fill: #C9D1D9; text-anchor: middle;"
                    )
                    dwg.add(label_text)
                except Exception as e:
                    logger.warning(f"Failed to create label text {i}: {e}")
                
                metrics_created += 1
                
            except Exception as e:
                logger.warning(f"Failed to create metric {i} ({label}): {e}")
                continue
        
        logger.info(f"Analytics SVG created with {metrics_created} metrics")
        return dwg
        
    except Exception as e:
        logger.error(f"❌ Critical error in analytics SVG generation: {e}")
        logger.error(traceback.format_exc())
        return None

def validate_svg_output(filename: str) -> bool:
    """
    Validate SVG file output with comprehensive checks.
    Returns True if valid, False otherwise.
    """
    try:
        filepath = Path(filename)
        
        # Check if file exists
        if not filepath.exists():
            logger.error(f"SVG file not found: {filename}")
            return False
        
        # Check file size
        file_size = filepath.stat().st_size
        if file_size == 0:
            logger.error(f"SVG file is empty: {filename}")
            return False
        elif file_size < 100:
            logger.warning(f"SVG file suspiciously small: {filename} ({file_size} bytes)")
            return False
        
        # Basic content validation
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if not content.strip().startswith('<?xml') and not content.strip().startswith('<svg'):
                logger.error(f"SVG file doesn't start with proper XML/SVG tag: {filename}")
                return False
                
            if '</svg>' not in content:
                logger.error(f"SVG file doesn't have closing tag: {filename}")
                return False
            
            logger.info(f"✅ SVG validation passed: {filename} ({file_size} bytes)")
            return True
            
        except Exception as e:
            logger.error(f"Failed to read SVG file {filename}: {e}")
            return False
        
    except Exception as e:
        logger.error(f"SVG validation failed for {filename}: {e}")
        return False

def main() -> int:
    """
    Main function with elite-level error handling and comprehensive logging.
    Returns 0 for success, 1 for failure.
    """
    try:
        logger.info("🚀 Starting Elite SVG Generator...")
        logger.info(f"Python version: {sys.version}")
        logger.info(f"Working directory: {os.getcwd()}")
        
        # GitHub Actions specific debugging
        if os.getenv('GITHUB_ACTIONS'):
            logger.info("🔧 Running in GitHub Actions environment")
            logger.info(f"GITHUB_WORKSPACE: {os.getenv('GITHUB_WORKSPACE', 'not set')}")
            logger.info(f"RUNNER_OS: {os.getenv('RUNNER_OS', 'not set')}")
        
        # Setup environment
        if not setup_environment():
            logger.error("Environment setup failed")
            return 1
        
        success_count = 0
        total_count = 2
        
        # Generate header SVG
        logger.info("=" * 60)
        header_svg = create_header_svg()
        if header_svg:
            try:
                header_svg.saveas(SVG_CONFIG['header']['filename'], pretty=True)
                if validate_svg_output(SVG_CONFIG['header']['filename']):
                    logger.info(f"✅ Header SVG created successfully: {SVG_CONFIG['header']['filename']}")
                    success_count += 1
                else:
                    logger.error(f"❌ Header SVG validation failed")
            except Exception as e:
                logger.error(f"❌ Failed to save header SVG: {e}")
        else:
            logger.error("❌ Header SVG creation failed")
        
        # Generate analytics SVG
        logger.info("=" * 60)
        analytics_svg = create_analytics_svg()
        if analytics_svg:
            try:
                analytics_svg.saveas(SVG_CONFIG['analytics']['filename'], pretty=True)
                if validate_svg_output(SVG_CONFIG['analytics']['filename']):
                    logger.info(f"✅ Analytics SVG created successfully: {SVG_CONFIG['analytics']['filename']}")
                    success_count += 1
                else:
                    logger.error(f"❌ Analytics SVG validation failed")
            except Exception as e:
                logger.error(f"❌ Failed to save analytics SVG: {e}")
        else:
            logger.error("❌ Analytics SVG creation failed")
        
        # Final status report
        logger.info("=" * 60)
        if success_count == total_count:
            logger.info(f"🎉 All {total_count} SVG files generated successfully!")
            logger.info("🤖 Elite SVG Generator completed with full success!")
            return 0
        elif success_count > 0:
            logger.warning(f"⚠️  Partial success: {success_count}/{total_count} SVG files generated")
            return 1
        else:
            logger.error(f"❌ Complete failure: 0/{total_count} SVG files generated")
            return 1
        
    except KeyboardInterrupt:
        logger.warning("⚠️  Process interrupted by user")
        return 1
    except Exception as e:
        logger.error(f"❌ Critical error in main function: {e}")
        logger.error(traceback.format_exc())
        return 1
    finally:
        logger.info("🏁 Elite SVG Generator execution completed")

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
