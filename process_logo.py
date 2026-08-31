from PIL import Image, ImageEnhance

def clean_and_sharpen_logo():
    # Load original logo
    orig = Image.open('static/logo.png').convert('RGB')

    # The actual logo content is in the center, free from the square border artifacts
    crop_box = (93, 116, 331, 283)
    cropped = orig.crop(crop_box)

    # Upscale 6x with Lanczos resampling for high-DPI retina sharpness
    scale = 6
    w, h = cropped.size
    hires = cropped.resize((w * scale, h * scale), Image.Resampling.LANCZOS)

    pixels = hires.load()
    hires_w, hires_h = hires.size

    out_img = Image.new('RGBA', (hires_w, hires_h), (0, 0, 0, 0))
    out_pix = out_img.load()

    for y in range(hires_h):
        for x in range(hires_w):
            r, g, b = pixels[x, y]
            min_c = min(r, g, b)
            
            # Remove white/off-white background and eliminate edge lines
            if min_c >= 246:
                out_pix[x, y] = (0, 0, 0, 0)
            else:
                darkness = 255.0 - min_c
                if darkness < 8:
                    alpha = 0
                elif darkness < 40:
                    alpha = int(((darkness - 8) / 32.0) * 190)
                else:
                    alpha = min(255, int(190 + ((darkness - 40) / 100.0) * 65))
                
                if alpha > 0:
                    a_norm = alpha / 255.0
                    fr = max(0, min(255, int((r - (1.0 - a_norm) * 255) / a_norm)))
                    fg = max(0, min(255, int((g - (1.0 - a_norm) * 255) / a_norm)))
                    fb = max(0, min(255, int((b - (1.0 - a_norm) * 255) / a_norm)))
                    
                    # Enhance richness and vibrancy
                    if fr > 110 and fg > 80 and fb < 100: # Gold
                        fr = min(255, int(fr * 1.08))
                        fg = min(255, int(fg * 1.03))
                    elif fr > 100 and fg < 70: # Wine
                        fr = max(0, int(fr * 0.95))
                        fg = max(0, int(fg * 0.90))
                        fb = max(0, int(fb * 0.92))
                    
                    out_pix[x, y] = (fr, fg, fb, alpha)

    # Enhance sharpness for crisp typography and contours
    enhancer = ImageEnhance.Sharpness(out_img)
    out_img = enhancer.enhance(1.3)

    out_img.save('static/logo.png', 'PNG')
    print('Cleaned static/logo.png created successfully')

    # Also make a crisp logo-icon.png
    woman_crop = out_img.crop((int(90 * scale), 0, int(160 * scale), int(60 * scale)))
    woman_crop.save('static/logo-icon.png', 'PNG')
    print('Cleaned static/logo-icon.png created successfully')

if __name__ == '__main__':
    clean_and_sharpen_logo()
