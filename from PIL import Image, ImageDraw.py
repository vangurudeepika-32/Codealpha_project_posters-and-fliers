from PIL import Image, ImageDraw, ImageFont

# Create a blank white poster
width, height = 800, 1200  # dimensions of the flyer
poster = Image.new('RGB', (width, height), (255, 255, 255))  # white background
draw = ImageDraw.Draw(poster)

# Define colors and fonts
background_color = (0, 153, 255)  # Blue
text_color = (255, 255, 255)  # White
accent_color = (255, 223, 0)  # Yellow
title_font = ImageFont.load_default()
sub_title_font = ImageFont.truetype("arial.ttf", 50)
body_font = ImageFont.truetype("arial.ttf", 30)

# Add background color (a top banner)
draw.rectangle([0, 0, width, 200], fill=background_color)

# Add Title Text
title_text = "Big Sale - Up to 50% Off!"
# Use textbbox instead of textsize to get the width and height
title_bbox = draw.textbbox((0, 0), title_text, font=sub_title_font)
title_width = title_bbox[2] - title_bbox[0]
title_height = title_bbox[3] - title_bbox[1]
draw.text(((width - title_width) / 2, 50), title_text, font=sub_title_font, fill=text_color)

# Add Subtitle Text
sub_title_text = "Don't miss out on the biggest deals of the year."
# Use textbbox instead of textsize to get the width and height
sub_title_bbox = draw.textbbox((0, 0), sub_title_text, font=body_font)
sub_title_width = sub_title_bbox[2] - sub_title_bbox[0]
sub_title_height = sub_title_bbox[3] - sub_title_bbox[1]
draw.text(((width - sub_title_width) / 2, 200), sub_title_text, font=body_font, fill=text_color)

# Add Details (body text)
details_text = "Visit our store and enjoy discounts on selected items.\nDate: January 10th - 20th, 2025\nLocation: ABC Mall"
draw.text((50, 300), details_text, font=body_font, fill=(0, 0, 0))

# Add a call-to-action (CTA)
cta_text = "Hurry! Limited time offer!"
# Use textbbox instead of textsize to get the width and height
cta_bbox = draw.textbbox((0, 0), cta_text, font=sub_title_font)
cta_width = cta_bbox[2] - cta_bbox[0]
cta_height = cta_bbox[3] - cta_bbox[1]
draw.text(((width - cta_width) / 2, 1000), cta_text, font=sub_title_font, fill=accent_color)

# Add decorative elements (for example, a simple rectangle or circle for emphasis)
draw.rectangle([100, 950, 700, 1000], outline=accent_color, width=5)

# Save the poster
poster.save('digital_flyer_example.png')

# Show the image (optional)
poster.show()