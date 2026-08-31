from PIL import Image

services = {
    'service-saree.jpg': (r'C:\Users\acer\.gemini\antigravity-ide\brain\c7861512-d120-4713-8939-fb434f96dce9\service_saree_1788116318245.jpg', (100, 50, 1600, 1000)),
    'service-hairstyle.jpg': (r'C:\Users\acer\.gemini\antigravity-ide\brain\c7861512-d120-4713-8939-fb434f96dce9\service_hairstyle_1788116378137.jpg', (120, 50, 1620, 1000)),
    'service-makeup.jpg': (r'C:\Users\acer\.gemini\antigravity-ide\brain\c7861512-d120-4713-8939-fb434f96dce9\service_makeup_1788116444185.jpg', (100, 50, 1600, 1000))
}

for name, (path, crop_box) in services.items():
    img = Image.open(path)
    cropped = img.crop(crop_box)
    resized = cropped.resize((800, 500), Image.Resampling.LANCZOS)
    resized.save(f'static/{name}', quality=95)
    print(f'Successfully saved static/{name}, size: {resized.size}')
