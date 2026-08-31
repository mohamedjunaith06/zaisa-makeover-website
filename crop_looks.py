from PIL import Image, ImageEnhance

banner = Image.open(r'C:\Users\acer\.gemini\antigravity-ide\brain\c7861512-d120-4713-8939-fb434f96dce9\.user_uploaded\media_1788113280732.png')

# Precise inner bounding boxes for pure photo content
crops = {
    'look-muhurtham.png': (27, 3, 253, 252),
    'look-christian.png': (275, 3, 503, 252),
    'look-traditional.png': (523, 3, 749, 252),
    'look-reception.png': (769, 3, 995, 252)
}

for filename, box in crops.items():
    cropped = banner.crop(box)
    
    # 3x high-DPI scaling with Lanczos
    w, h = cropped.size
    hires = cropped.resize((w * 3, h * 3), Image.Resampling.LANCZOS)
    
    # Enhance sharpness and contrast slightly for crisp web presentation
    enhancer = ImageEnhance.Sharpness(hires)
    hires = enhancer.enhance(1.15)
    
    contrast = ImageEnhance.Contrast(hires)
    hires = contrast.enhance(1.03)
    
    hires.save(f'static/{filename}', 'PNG')
    print(f'Successfully saved static/{filename}, size: {hires.size}')
