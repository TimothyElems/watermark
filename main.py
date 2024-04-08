from PIL import Image, ImageDraw, ImageFont


def add_watermark_over_image(input_image_path, output_image_path, watermark_text):
    input_image = Image.open(input_image_path)
    input_image = input_image.convert('RGBA')
    width, height = input_image.size

    # Image.new(mode), was switched from
    overlay = Image.new(mode: 'RGBA', size=input_image.size, color: (225, 225, 225, 0))

    draw = ImageDraw.Draw(overlay)

    watermark_color_pattern = (225, 225, 225, 30)

    for i in range(0, width + height, 50):
        draw.line([(0, height - i), (i, height)],
                  fill=watermark_color_pattern, width=5)

    font_size = 80
    font = ImageFont.truetype('arial.ttf', font_size)

    text_width, text_height = draw.textsize(watermark_text, font)

    x = (width - text_width) // 2
    y = (height - text_height) // 2

    watermark_text_color = (225, 225, 225, 80)

    draw.text(xy: (x, y), watermark_text, fill=watermark_text_color, font=font)

    watermaked_image = Image.alpha_composite(input_image, overlay)

    watermaked_image.save(output_image_path)


input_image_path = 'timmity.jpg'
output_image_path = 'tim.jpg'
watermark_text = 'insideoutaerials.com'

add_watermark_over_image(input_image_path, output_image_path, watermark_text)
