import asyncio
from PIL import Image, ImageDraw, ImageFont


def write_text_on_image(photo: str, text: str) -> None:
    image = Image.open(photo)

    left = (image.width - 200) / 2
    top = (image.height - 250)

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(font='font.ttf',size=100)

    draw.text((left,top), text ,font=font, fill=(255,255,255))

    image.save('profile.jpg')



async def delete_message(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()
