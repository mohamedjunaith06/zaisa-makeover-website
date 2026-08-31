from PIL import Image

# HD image paths from brain
paths = {
    'look-muhurtham-hd.jpg': (r'C:\Users\acer\.gemini\antigravity-ide\brain\c7861512-d120-4713-8939-fb434f96dce9\look_muhurtham_hd_1788114313582.jpg', (120, 80, 780, 960)),
    'look-christian-hd.jpg': (r'C:\Users\acer\.gemini\antigravity-ide\brain\c7861512-d120-4713-8939-fb434f96dce9\look_christian_hd_1788114599183.jpg', (150, 60, 750, 860)),
    'look-traditional-hd.jpg': (r'C:\Users\acer\.gemini\antigravity-ide\brain\c7861512-d120-4713-8939-fb434f96dce9\look_traditional_hd_1788114678193.jpg', (160, 120, 780, 940)),
    'look-reception-hd.jpg': (r'C:\Users\acer\.gemini\antigravity-ide\brain\c7861512-d120-4713-8939-fb434f96dce9\look_reception_hd_1788114765415.jpg', (160, 100, 780, 920))
}

for name, (path, crop_box) in paths.items():
    img = Image.open(path)
    cropped = img.crop(crop_box)
    # Resize to standard 3:4 portrait (750x1000)
    resized = cropped.resize((750, 1000), Image.Resampling.LANCZOS)
    resized.save(f'static/{name}', quality=95)
    print(f'Saved static/{name}, size: {resized.size}')
