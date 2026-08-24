import os
import shutil
from PIL import Image

src_dir = 'hinh goc'
dest_dir = 'assets/image'

images = [f for f in os.listdir(src_dir) if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg')]
images.sort()

landscape = []
portrait = []

for img in images:
    img_path = os.path.join(src_dir, img)
    try:
        with Image.open(img_path) as im:
            width, height = im.size
            if width > height:
                landscape.append(img_path)
            else:
                portrait.append(img_path)
    except Exception as e:
        print(f"Error reading {img}: {e}")

print(f"Found {len(landscape)} landscape and {len(portrait)} portrait images.")

# Assignments
assignments = {}

def assign(dest_name, source_list):
    if source_list:
        assignments[dest_name] = source_list.pop(0)

# Landscape placements
assign('anh_bia_1.jpg', landscape)
assign('anh_nen_co_dau_chu_re.png', landscape)
assign('anh_su_kien_thanh_hon.jpeg', landscape)
assign('anh_su_kien_moi_tiec.jpeg', landscape)
assign('anh_chia_se_link.jpeg', landscape)
assign('anh_chuyen_tinh_yeu.jpeg', landscape)

# Portrait placements
assign('anh_chu_re.jpeg', portrait)
assign('anh_co_dau.jpeg', portrait)
assign('anh_loi_ngo.jpg', portrait)

# Gallery
gallery_sources = landscape + portrait
for i in range(1, 11):
    if gallery_sources:
        src = gallery_sources.pop(0)
        assignments[f'anh_album_day_du_{i}.jpg'] = src
        assignments[f'anh_album_thu_nho_{i}.jpg'] = src

# Execute assignments
for dest, src in assignments.items():
    dest_path = os.path.join(dest_dir, dest)
    shutil.copy(src, dest_path)
    print(f"Copied {os.path.basename(src)} -> {dest}")

print("Done assigning photos.")
