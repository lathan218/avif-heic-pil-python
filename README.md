# avif-heic-pil-python

Easily convert AVIF and HEIF/HEIC images using Python and Pillow (PIL) with the help of `pillow-avif-plugin` and `pillow-heif`.

## Features

- Read and write AVIF and HEIF/HEIC images in Python
- Simple command-line conversion utility
- Automatic handling of EXIF orientation

## Requirements

- Python 3.7+
- [Pillow](https://pypi.org/project/Pillow/)
- [pillow-avif-plugin](https://pypi.org/project/pillow-avif-plugin/)
- [pillow-heif](https://pypi.org/project/pillow-heif/)

Install dependencies with:

```sh
pip install -r requirements.txt
```

## Usage

Convert images to AVIF format from the command line:

python converter.py image2.heic example.png

- Output files will be saved in the same directory as the input, with .avif extension.
- If a file with the same name exists, a numeric suffix will be added.
