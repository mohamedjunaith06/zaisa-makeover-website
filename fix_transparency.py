from PIL import Image, ImageEnhance
import math

def fix_logo_transparency():
    # Load original cropped logo or current logo
    orig = Image.open('static/logo_cropped.png').convert('RGB')
    
    # Scale up with Lanczos for retina sharpness
    scale = 6
    w, h = orig.size
    hires = orig.resize((w * scale, h * scale), Image.Resampling.LANCZOS)
    
    pixels = hires.load()
    hw, hh = hires.size
    
    out_img = Image.new('RGBA', (hw, hh), (0, 0, 0, 0))
    out_pix = out_img.load()
    
    for y in range(hh):
        for x in range(hw):
            r, g, b = pixels[x, y]
            
            # The background in the original image is a light grayish/off-white tone where r,g,b are close to each other
            # Let's calculate:
            # 1. Darkness from white
            # 2. Chroma / Saturation: max(r,g,b) - min(r,g,b)
            # 3. Specific distance to Wine (#802038) or Gold (#b08850)
            
            # Wine target: (130, 45, 60), Gold target: (175, 135, 75)
            # Background is around (235, 230, 225) to (245, 245, 245)
            
            # Let's check how much saturation it has
            max_c = max(r, g, b)
            min_c = min(r, g, b)
            chroma = max_c - min_c
            brightness = (r + g + b) / 3.0
            
            # If brightness is high and chroma is low, it is 100% background:
            # Background has brightness > 210 and chroma < 30
            if brightness > 200 and chroma < 35:
                out_pix[x, y] = (0, 0, 0, 0)
                continue
            elif brightness > 220 and chroma < 45:
                out_pix[x, y] = (0, 0, 0, 0)
                continue
            elif brightness > 235:
                out_pix[x, y] = (0, 0, 0, 0)
                continue
                
            # Foreground check:
            # Gold: R > 110, G > 70, B < 120, R > B + 25
            # Wine: R > 80, G < 100, B < 110, R > G + 20
            is_gold = (r > 100 and g > 65 and r > b + 20 and g > b - 15)
            is_wine = (r > 70 and r > g + 15 and r > b + 10 and g < 130)
            
            if not is_gold and not is_wine and chroma < 25:
                out_pix[x, y] = (0, 0, 0, 0)
                continue
                
            # It is a foreground pixel!
            # Let's compute smooth alpha edge based on chroma and darkness
            # Wine darkness
            if is_wine:
                target_r, target_g, target_b = 125, 36, 60 # deep luxury wine
                # compute alpha
                alpha = min(255, int(max(0, (230 - brightness) / 100.0 * 255)))
                alpha = max(alpha, min(255, int(chroma / 60.0 * 255)))
                if alpha < 20:
                    out_pix[x, y] = (0, 0, 0, 0)
                else:
                    # Clean wine color
                    fr = 125
                    fg = 36
                    fb = 60
                    out_pix[x, y] = (fr, fg, fb, min(255, int(alpha * 1.2)))
            elif is_gold:
                target_r, target_g, target_b = 180, 140, 80 # radiant luxury gold
                alpha = min(255, int(max(0, (235 - brightness) / 90.0 * 255)))
                alpha = max(alpha, min(255, int(chroma / 40.0 * 255)))
                if alpha < 20:
                    out_pix[x, y] = (0, 0, 0, 0)
                else:
                    fr = 185
                    fg = 142
                    fb = 78
                    out_pix[x, y] = (fr, fg, fb, min(255, int(alpha * 1.2)))
            else:
                out_pix[x, y] = (0, 0, 0, 0)

    # Enhance sharpness
    enhancer = ImageEnhance.Sharpness(out_img)
    out_img = enhancer.enhance(1.2)
    
    out_img.save('static/logo.png', 'PNG')
    out_img.save('static/zaisa-logo.png', 'PNG')
    print('Successfully saved 100% transparent static/logo.png')

if __name__ == '__main__':
    fix_logo_transparency()
