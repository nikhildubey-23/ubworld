from PIL import Image
import os

# Directory containing images
img_dir = 'static/img/'

# Resize dimensions based on display sizes
resize_dims = {
    'img11.jpeg': (467, 250),
    'img12.jpeg': (410, 250),
    'img4.jpeg': (445, 250),
    'img13.jpeg': (544, 199),
    'img10.jpeg': (445, 250),
    'img3.jpeg': (445, 250),
    'img2.jpeg': (445, 250),
    'logo.jpeg': (62, 62),
    # Carousel images: keep original for cover, but convert to WebP
    'img8.jpeg': None,  # No resize
    'img5.jpeg': None,  # Assuming not used, but convert
    'img6.jpeg': None,
    'img7.jpeg': None,
    'img9.jpeg': None,
    'img1.jpeg': None,
}

def optimize_image(filename, resize_dim=None):
    filepath = os.path.join(img_dir, filename)
    if not os.path.exists(filepath):
        print(f"File {filename} not found.")
        return

    img = Image.open(filepath)

    # Resize if needed
    if resize_dim:
        img = img.resize(resize_dim, Image.Resampling.LANCZOS)

    # Convert to WebP
    webp_filename = filename.replace('.jpeg', '.webp').replace('.jpg', '.webp')
    webp_filepath = os.path.join(img_dir, webp_filename)
    img.save(webp_filepath, 'WEBP', quality=85)  # Adjust quality as needed

    print(f"Optimized {filename} to {webp_filename}")

# Process all images
for filename in os.listdir(img_dir):
    if filename.endswith(('.jpeg', '.jpg')):
        resize_dim = resize_dims.get(filename, None)
        optimize_image(filename, resize_dim)

print("Image optimization complete.")
