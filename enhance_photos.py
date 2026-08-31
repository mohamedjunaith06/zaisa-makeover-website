from PIL import Image, ImageFilter, ImageEnhance, ImageOps

banner = Image.open(r'C:\Users\acer\.gemini\antigravity-ide\brain\c7861512-d120-4713-8939-fb434f96dce9\.user_uploaded\media_1788113280732.png')

crops = {
    'look-muhurtham.png': (27, 4, 252, 250),
    'look-christian.png': (275, 4, 502, 250),
    'look-traditional.png': (523, 4, 748, 250),
    'look-reception.png': (769, 4, 994, 250)
}

for filename, box in crops.items():
    cropped = banner.crop(box)
    
    # 4x high-DPI scaling with Lanczos
    w, h = cropped.size
    hires = cropped.resize((w * 4, h * 4), Image.Resampling.LANCZOS)
    
    # Multi-pass sharpening
    # 1. Unsharp mask with radius 2, percent 180, threshold 2
    unsharp = hires.filter(ImageFilter.UnsharpMask(radius=2.2, percent=190, threshold=2))
    
    # 2. Subtle contrast & color enhancement for rich luxury look
    enhancer_con = ImageEnhance.Contrast(unsharp)
    boosted = enhancer_con.enhance(1.08)
    
    enhancer_col = ImageEnhance.Color(boosted)
    boosted = enhancer_col.enhance(1.06)
    
    enhancer_sharp = ImageEnhance.Sharpness(boosted)
    final_img = enhancer_sharp.enhance(1.35)
    
    final_img.save(f'static/{filename}', 'PNG')
    print(f'Successfully saved ultra-sharp static/{filename}, size: {final_img.size}')
