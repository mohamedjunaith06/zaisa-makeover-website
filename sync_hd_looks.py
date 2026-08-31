import shutil

# Copy the HD closeups to the standard look filenames
files = ['look-muhurtham', 'look-christian', 'look-traditional', 'look-reception']

for f in files:
    shutil.copy(f'static/{f}-hd.jpg', f'static/{f}.jpg')
    shutil.copy(f'static/{f}-hd.jpg', f'static/{f}.png')
    print(f'Updated static/{f}.jpg and static/{f}.png with 4K HD quality')
