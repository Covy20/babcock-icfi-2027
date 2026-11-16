import os
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
os.makedirs(OUT, exist_ok=True)

# name: (source, (w, h), vertical centering)
JOBS = {
    "logo_icfi.jpg":   ("logo.jpeg",                 (200, 200),  0.5),
    "logo_bu.jpg":     ("img/bu logo.jpg",           None,        0.5),
    "hero_main.jpg":   ("images2/IMGL0050.JPG",      (1200, 900), 0.5),
    "hero_sub.jpg":    ("images2/principal2.JPG",    (800, 520),  0.38),
    "welcome.jpg":     ("img/nwosu.JPG",             (920, 1040), 0.28),
    "host_vc.jpg":     ("New ICFI pic 2027/Chief Host.png", (760, 640),  0.42),
    "host_amanze.jpg": ("New ICFI pic 2027/Host SVP.png",   (760, 640),  0.42),
    "host_nwosu.jpg":  ("img/nwosu.JPG",             (760, 640),  0.25),
    "past_taylor.jpg": ("img/taylor.jpg",            (320, 320),  0.25),
    "past_balisasa.jpg": ("img/balisasa.jpg",        (320, 320),  0.25),
    "past_fisher.jpg": ("img/barbara.jpg",           (320, 320),  0.25),
    "past_oyedeji.jpg": ("img/oyedeji.jpg",          (320, 320),  0.25),
    "submit.jpg":      ("images2/img9.JPG",          (1040, 800), 0.35),
    "journal.jpg":     ("images2/IMGL0051.JPG",      (900, 620),  0.5),
    "gal_big.jpg":     ("images2/img13.JPG",         (1200, 780), 0.4),
    "gal_1.jpg":       ("images2/whites.JPG",        (640, 420),  0.4),
    "gal_2.jpg":       ("images2/Svp.JPG",           (640, 420),  0.35),
    "gal_3.jpg":       ("images2/IMGL0030.JPG",      (640, 420),  0.4),
    "gal_4.jpg":       ("images2/IMGL0140.JPG",      (640, 420),  0.45),
}

for name, (src, size, cy) in JOBS.items():
    im = Image.open(os.path.join(ROOT, src))
    im = ImageOps.exif_transpose(im).convert("RGB")
    if size:
        im = ImageOps.fit(im, size, Image.LANCZOS, centering=(0.5, cy))
    im.save(os.path.join(OUT, name), "JPEG", quality=86, optimize=True)
    print(name, im.size, os.path.getsize(os.path.join(OUT, name)))
