from PIL import Image, ImageDraw, ImageFont


def draw_text(img: str, text: str, font_size: int, x: int, y: int):
    draw = ImageDraw.Draw(img)
    font_name = 'font/NotoSansJP-Regular.otf'
    font = ImageFont.truetype(font_name, font_size)
    draw.text((x, y), text, font=font, fill=(0, 0, 0, 255))


title_text = "アニメタイトル"
number_text = "100"


def create_Layout(title_text: str, number: int,):
    croped_img = img.crop((100, 120, 400, 300))
    resized_img = croped_img.resize((croped_img.width*6, croped_img.height*6))
    copied_back_img = back_img.copy()
    copied_back_img.paste(resized_img, (100, 300))

    draw_text(copied_back_img, title_text, 40, 500, 130)
    draw_text(copied_back_img, str(number_text), 40, 1350, 130)

    copied_back_img.save(f'result/result_{number}.png', quality=95)


img = Image.open("images/test.png").convert('RGBA')
back_img = Image.open("images/back.jpg")
title_text = "アニメタイトル"
for i in range(5):
    create_Layout(title_text, i)
