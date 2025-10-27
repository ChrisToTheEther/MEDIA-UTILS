from PIL import Image
import argparse
import os


def convert_to_bitmap(input_path, output_path=None):
    """
    Converts an image to 256-color BMP format.

    Args:
        input_path (str): Path to the input image (any supported format).
        output_path (str, optional): Path to save the converted BMP image.
                                     If not provided, creates one automatically.
    """
    try:
        img = Image.open(input_path)

        # Convert  256-color 
        bmp_img = img.convert("P", palette=Image.ADAPTIVE, colors=256)

        # output path if not given
        if not output_path:
            base_name = os.path.splitext(input_path)[0]
            output_path = f"{base_name}_converted.bmp"

        #Save BMP
        bmp_img.save(output_path, format="BMP")

        print(f"Image successfully converted to 256-color BMP: {output_path}")

    except FileNotFoundError:
        print(f"Error: File not found — {input_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert images to 256-color BMP format.")
    parser.add_argument("input_path", help="Path to the input image file")
    parser.add_argument("--output_path", help="Optional path to save the BMP output")

    args = parser.parse_args()

    convert_to_bitmap(args.input_path, args.output_path)
