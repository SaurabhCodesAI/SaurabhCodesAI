import svgwrite
import datetime

def generate_svg():
    # Get the current time for India (IST is 5.5 hours ahead of UTC)
    ist_offset = datetime.timedelta(hours=5, minutes=30)
    now = datetime.datetime.now(datetime.timezone.utc) + ist_offset
    timestamp = now.strftime("%B %d, %Y %H:%M:%S IST")

    # Setup the SVG canvas (the drawing area)
    # Dimensions are 450 pixels wide by 50 pixels tall
    dwg = svgwrite.Drawing('header.svg', profile='tiny', size=('450px', '50px'))
    
    # Draw a dark background rectangle that fills the entire canvas
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='#0D1117'))
    
    # Prepare the text we want to display on the image
    text = f"Last Profile Sync: {timestamp}"
    
    # Add the text to our canvas with specific styling
    dwg.add(dwg.text(
        text,
        insert=(10, 30),  # Position: 10px from left, 30px from top
        fill='#FFD700',   # Text color: A gold-yellow
        font_family='JetBrains Mono, monospace',
        font_size='16px',
        font_weight='bold'
    ))
    
    # Save the final drawing to the 'header.svg' file
    dwg.save()
    print("Successfully generated header.svg")

if __name__ == "__main__":
    generate_svg()