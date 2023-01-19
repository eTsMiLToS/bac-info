import qrcode
from PIL import Image
import turtle
import time

def create_qr_with_logo(data, logo_path):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    logo = Image.open("imgik1.jpg")
    img_w, img_h = img.size
    factor = 3
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)

    logo_w, logo_h = logo.size
    logo = logo.resize((size_w, size_h))
    logo_w, logo_h = logo.size

    img.paste(logo, (int((img_w - logo_w) / 2), int((img_h - logo_h) / 2)))
    img.save("imgik1.jpg")
    animation()
    
def animation():
    t = turtle.Turtle()
    t.speed(10)
    turtle.bgcolor("white")
    t.color("red")
    t.pensize(5)
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    text = " <3 ADMIS(e) Bac 2023k <3 "
    for i in range(len(text)):
        t.write(text[i], font=("Arial", 24, "bold"))
        t.forward(30)
        time.sleep(0.1)
        t.clear()
    t.penup()
    t.goto(-200, -50)
    t.pendown()
    t.color("red")
    t.write("<3 ADMIS(e) Bac 2023k <3", font=("Arial", 24, "bold"))
    turtle.mainloop()
    
data = "https://www.example.com"
logo_path = "imgik1.jpg"
create_qr_with_logo(data, logo_path)


