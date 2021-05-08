from PIL import Image, ImageDraw, ImageFont
import glob


def draw_text(img: str, text: str, font_size: int, x: int, y: int):
    draw = ImageDraw.Draw(img)
    font_name = 'font/NotoSansJP-Regular.otf'
    font = ImageFont.truetype(font_name, font_size)
    draw.text((x, y), text, font=font, fill=(0, 0, 0, 255))


def create_Layout(title_text: str, number: int,):
    X = 100
    Y = 120
    HEIGHT = 180
    LEFT_TOP = 180 * number + Y

    croped_img = img.crop((X, LEFT_TOP, 400, LEFT_TOP+HEIGHT))
    resized_img = croped_img.resize((croped_img.width*6, croped_img.height*6))
    copied_back_img = back_img.copy()
    copied_back_img.paste(resized_img, (100, 300))

    return copied_back_img


back_img = Image.open("back_image/back.jpg")
title_text = "アニメタイトル"

files = glob.glob("images/*.png")

def main():
    for index, file in enumerate(files):
        print(index,file)
        img = Image.open(file).convert('RGBA')

        for i in range(5):

            number_text = 5*index+(i+1)

            img = create_Layout(title_text, i)
            draw_text(img, title_text, 40, 500, 130)
            draw_text(img, str(number_text), 40, 1350, 130)
            img.save(f'result/{title_text}_{number_text}.png', quality=95)
