from PIL import Image, ImageDraw, ImageFont
import random

def generate_random_color():
    return tuple(random.randint(0, 255) for _ in range(3))

def generate_logo(width, height, text):
    # Create a blank image
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Draw random shapes
    for _ in range(5):
        shape_type = random.choice(["rectangle", "ellipse"])
        top_left = (random.randint(0, width // 2), random.randint(0, height // 2))
        bottom_right = (random.randint(width // 2, width), random.randint(height // 2, height))
        color = generate_random_color()

        if shape_type == "rectangle":
            draw.rectangle([top_left, bottom_right], fill=color)
        elif shape_type == "ellipse":
            draw.ellipse([top_left, bottom_right], fill=color)

    # Add text to the logo
    try:
        font = ImageFont.truetype("arial.ttf", size=40)
    except IOError:
        font = ImageFont.load_default()

    # Calculate text size and position
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_position = ((width - text_width) // 2, (height - text_height) // 2)

    draw.text(text_position, text, fill="black", font=font)

    # Save the logo
    image.save("innovative_logo.png")
    print("Logo generated and saved as innovative_logo.png")

# Parameters for the logo
logo_width = 400
logo_height = 200
logo_text = "samskruti college"
# Generate the logo
generate_logo(logo_width, logo_height, logo_text)
