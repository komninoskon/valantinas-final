import qrcode

# Αν το site είναι τοπικό:
# url = "http://127.0.0.1:5000"

# Αν έχεις domain (π.χ. online site στο render.com ή άλλο):
url = "https://www.valantinasrestaurant.gr"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")
img.save("restaurant_qr.png")