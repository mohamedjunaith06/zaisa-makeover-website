from PIL import Image

src_path = r'C:\Users\acer\.gemini\antigravity-ide\brain\c7861512-d120-4713-8939-fb434f96dce9\service_makeup_close_1788121463084.jpg'
img = Image.open(src_path)
orig_w, orig_h = img.size

# 16:10 crop inside 1376x768
target_ratio = 16.0 / 10.0
crop_w = int(orig_h * target_ratio) # 1228
crop_h = orig_h

start_x = (orig_w - crop_w) // 2
start_y = 0
crop_box = (start_x, start_y, start_x + crop_w, start_y + crop_h)

cropped = img.crop(crop_box)
resized = cropped.resize((960, 600), Image.Resampling.LANCZOS)
resized.save('static/service-makeup.jpg', quality=95)
print(f'Successfully updated static/service-makeup.jpg to {resized.size} without any black borders or extra person!')
