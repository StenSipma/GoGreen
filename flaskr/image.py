"""
File for creating images
"""

import os
from PIL import Image, ImageDraw, ImageFont


def draw_cirle(app, color, ranking):
    # Some sizes & values
    image_size = 600
    outline = 50
    antialias = 4
    transparant_background = (255, 255, 255, 0)
    percent_msg = str(ranking)+"%"

    # Create image (large version) + draw object
    img = Image.new(
        'RGBA',
        [size * antialias for size
         in [image_size]*2],
        transparant_background
    )
    img_draw = ImageDraw.Draw(img)

    # Draw pie
    start = 0
    end = ranking*3.6

    img_draw.pieslice(
        [dim*antialias for dim in [0, 0, image_size, image_size]],
        start=start-90,
        end=end-90,
        fill=color
    )

    # Draw the transparant inner cirle
    img_draw.ellipse(
        [(dim + outline)*antialias for dim in [0, 0]]
        + [(dim - outline)*antialias for dim in [image_size, image_size]],
        fill=(255, 255, 255, 0)
    )

    # Add Text
    text_font = ImageFont.truetype(
        font="/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf",
        size=(image_size*antialias)//5
    )
    w, h = img_draw.textsize(percent_msg, font=text_font)
    img_draw.text((((image_size*antialias-w))/2, ((image_size*antialias-h))/2),
                  percent_msg,
                  fill=color,
                  font=text_font)

    # Resize for anti aliasing
    img = img.resize((image_size, image_size), Image.LANCZOS)

    # Save image
#    location = os.path.join(app.instance_path, 'generated')
    location = os.path.join('./flaskr', 'static/images')
    location = os.path.join(location, 'generated')
    im_name = "custom_circle_image.png"
    img.save(os.path.join(location, im_name), format='png')
