import qrcode
from PIL import Image
import datetime
import random

# BADGE QR GENERATOR


def new_qr_code(qrcode_data):
    qr = qrcode.QRCode(
                      version=2,
                      error_correction=qrcode.constants.ERROR_CORRECT_H,
                      box_size=4,
                      border=4,
                      )
    qr.add_data(qrcode_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    cur_size = img.size
    new_size = (cur_size[0]+10, cur_size[1]+10)
    new_im = Image.new("RGB", new_size)
    new_im.paste(img, (5, 5))
    return new_im


repeats = [12, 18]
offset = [0, 0]
off = 0
padding = 10
probe_size_img = new_qr_code("123")
size = probe_size_img.size

complete_img = Image.new(
                        "RGB",
                        (
                         (size[0]+padding)*repeats[0],
                         (size[0]+padding)*repeats[1]
                        ),
                        (255, 255, 255)
                        )

# rows and columns
for i in range(repeats[1]):
    for j in range(repeats[0]):
        now = datetime.datetime.now()
        rand = random.randint(1, 999)
        milli = now.strftime("%f").zfill(6)[0:2]
        qrdata = now.strftime("%M%S") + str(milli) + str(rand).zfill(3)
        newqr = new_qr_code(qrdata)
        print(qrdata)
        complete_img.paste(newqr, (offset[0], offset[1]))
        offset[0] = offset[0] + padding + size[0]
    offset[0] = 0
    offset[1] = offset[1] + padding + size[1]

complete_img.save('ninja_badge.png', dpi=(300, 300))
