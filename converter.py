import sys
from pathlib import Path
import traceback

import pillow_avif
from PIL import Image, ImageOps
from pillow_heif import register_heif_opener

register_heif_opener()

def generate_output(image_path: Path, start_at=1) -> Path:
    """Find a good, not used, filename to use for the output file name"""
    if (output := image_path.parent / f"{image_path.stem}.avif").exists():
        if (output := image_path.parent / f"{image_path.stem}_{start_at}.avif").exists():
            return generate_output(image_path=image_path, start_at=start_at+1)
    return output


def convert(image_path: Path):
    image = Image.open(image_path)

    # Make sure the image is turned the right way
    if image.format != "GIF":
        image = ImageOps.exif_transpose(image)

    # Make sure it's not in a weird mode we need to change it from
    if image.format not in ("GIF", "AVIF") and image.mode not in ("RBG", "RBGA"):
            image.convert("RGBA")

    image.save(generate_output(image_path=image_path), quality=81, save_all=True)


if __name__ == '__main__':
    errors = 0
    for img_file in sys.argv[1:]:
        try:
            convert(Path(img_file))
        except Exception as err:
            traceback.print_exc()
        else:
            print(f"Converted {img_file} successfully")

    if errors:
        input(f"There were {errors} errors while converting, press enter to exit...")