from PIL import Image
import argparse
import os


def scale_bitmap(input_path, size, output_path=None):
    """
    Scales to the specified size, saves as a 256-color BMP.

    If the aspect ratio does not match the target size, the image is centered with
    black padding 

    python reScale.py file.bmp 320x240

    Args:
        input_path (str): Path to the input image.
        size (str): Target resolution in the format 'WIDTHxHEIGHT'
        output_path (str, optional): Path to save the scaled image. If not provided,
                                     the output will be named automatically.
    """
    try:
  
        if "x" not in size.lower():
            raise ValueError("Size must be in the format WIDTHxHEIGHT (e.g. 320x240)")
        width, height = map(int, size.lower().split("x"))

        # Load image
        img = Image.open(input_path).convert("RGBA")

        # Compute aspect ratios
        orig_width, orig_height = img.size
        orig_aspect = orig_width / orig_height
        target_aspect = width / height

        if orig_aspect > target_aspect:
            # Image is wider — fit to width
            new_width = width
            new_height = int(width / orig_aspect)
        else:
            # Image is taller — fit to height
            new_height = height
            new_width = int(height * orig_aspect)

        # Resize 
        resized = img.resize((new_width, new_height), Image.NEAREST)

        #  new image with black background 
        result = Image.new("RGBA", (width, height), (0, 0, 0, 255))
        paste_x = (width - new_width) // 2
        paste_y = (height - new_height) // 2
        result.paste(resized, (paste_x, paste_y))

        #  256-color BMP
        bmp_img = result.convert("P", palette=Image.ADAPTIVE, colors=256)

        if not output_path:
            base_name = os.path.splitext(input_path)[0]
            output_path = f"{base_name}_{width}x{height}_scaled.bmp"

        bmp_img.save(output_path, format="BMP")
        print(f"Image scaled to {width}x{height} (aspect preserved) and saved as: {output_path}")

    except FileNotFoundError:
        print(f"Error: File not found — {input_path}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scale images to 256-color BMPs with aspect-ratio preservation.")
    parser.add_argument("input_path", help="Path to the input image file")
    parser.add_argument("size", help="Target size, e.g. '320x240'")
    parser.add_argument("--output_path", help="Optional path to save the scaled BMP")

    args = parser.parse_args()
    scale_bitmap(args.input_path, args.size, args.output_path)
