import qrcode
import qrcode.image.svg

ig_url = "https://www.instagram.com/zaisa__makeover_?utm_source=ig_web_button_share_sheet&igsi=ZDNlZDc0MzIxNw=="

# 1. Generate crisp vector SVG QR code
factory = qrcode.image.svg.SvgPathImage
qr_svg = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=2,
    image_factory=factory
)
qr_svg.add_data(ig_url)
qr_svg.make(fit=True)
svg_img = qr_svg.make_image(attrib={'class': 'qr-code-svg'})
svg_img.save('static/instagram-qr.svg')
print("Successfully generated static/instagram-qr.svg")

# 2. Generate high-resolution PNG QR code
qr_png = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=16,
    border=2,
)
qr_png.add_data(ig_url)
qr_png.make(fit=True)
# Fill color deep wine (#4a1330), background white
png_img = qr_png.make_image(fill_color="#4a1330", back_color="white")
png_img.save('static/instagram-qr.png')
print("Successfully generated static/instagram-qr.png")
