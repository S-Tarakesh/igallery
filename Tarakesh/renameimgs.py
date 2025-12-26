import os

folder = 'galleryapp/static/figure'

images = sorted(
    [f for f in os.listdir(folder) if f.lower().endswith('.png')]
)

for i, filename in enumerate(images):
    new_name = f"{i}.png"
    old_path = os.path.join(folder, filename)
    new_path = os.path.join(folder, new_name)

    if filename != new_name:
        os.rename(old_path, new_path)

print("Renaming complete.")
