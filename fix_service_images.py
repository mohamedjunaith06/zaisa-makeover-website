from PIL import Image

services = {
    'service-saree.jpg': r'C:\Users\acer\.gemini\antigravity-ide\brain\c7861512-d120-4713-8939-fb434f96dce9\service_saree_1788116318245.jpg',
    'service-hairstyle.jpg': r'C:\Users\acer\.gemini\antigravity-ide\brain\c7861512-d120-4713-8939-fb434f96dce9\service_hairstyle_1788116378137.jpg',
    'service-makeup.jpg': r'C:\Users\acer\.gemini\antigravity-ide\brain\c7861512-d120-4713-8939-fb434f96dce9\service_makeup_1788116444185.jpg'
}

for name, path in services.items():
    img = Image.open(path)
    orig_w, orig_h = img.size
    print(f'{name} original dimensions: {orig_w}x{orig_h}')
    
    # Proper 16:10 crop inside the 1376x768 bounds
    target_ratio = 16.0 / 10.0
    crop_w = int(orig_h * target_ratio) # 768 * 1.6 = 1228
    crop_h = orig_h
    
    start_x = (orig_w - crop_w) // 2
    start_y = 0
    crop_box = (start_x, start_y, start_x + crop_w, start_y + crop_h)
    
    print(f'Cropping with box: {crop_box}')
    cropped = img.crop(crop_box)
    
    # Save high quality without any black pixels
    resized = cropped.resize((960, 600), Image.Resampling.LANCZOS)
    resized.save(f'static/{name}', quality=95)
    print(f'Saved static/{name}, size: {resized.size}')

print("All service images successfully regenerated without any black padding!")
