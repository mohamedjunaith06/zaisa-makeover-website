from PIL import Image

# Load the exact authentic cleaned logo
img = Image.open('static/logo.png').convert('RGBA')
w, h = img.size
pix = img.load()

# Create light version with exact same dimensions, exact same font, exact same curves
out = Image.new('RGBA', (w, h), (0, 0, 0, 0))
out_pix = out.load()

for y in range(h):
    for x in range(w):
        r, g, b, a = pix[x, y]
        if a > 0:
            # Check if this pixel is part of gold silhouette/crown vs wine typography
            # In logo.png:
            # Gold: R is high (~185), G is med (~142), B is low (~78)
            # Wine: R is (~125), G is low (~36), B is low (~60)
            is_gold = (g > 70 and r > 130)
            
            if is_gold:
                # Radiant champagne gold: #e6cd9b -> (230, 205, 155)
                out_pix[x, y] = (230, 205, 155, a)
            else:
                # Pure elegant cream/white for wine letters: #fbf3ea -> (251, 243, 234)
                out_pix[x, y] = (251, 243, 234, a)

out.save('static/logo-light.png', 'PNG')
print("Successfully generated exact static/logo-light.png from authentic logo.png")
