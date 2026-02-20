
from PIL import Image
import os

input_path = "icon_Fourward.png"
output_path = "icon_Fourward.png"

try:
    with Image.open(input_path) as img:
        img = img.resize((512, 512), Image.Resampling.LANCZOS)
        img.save(output_path, "PNG", optimize=True)
        print(f"Successfully resized {input_path} to 512x512.")
except Exception as e:
    print(f"Error resizing image: {e}")
