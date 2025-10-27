from PIL import Image
import argparse


def pixelate_image(input_path, output_path, pixel_size=16):
    """
    Pixelates a JPEG image using Pillow.

    Args:
        input_path (str): The path to the input JPEG image.
        output_path (str): The path to save the pixelated image.
        pixel_size (int): The size of the "pixel blocks" in the output image.
                          A higher value results in more pixelation.
    """
    try:
        img = Image.open(input_path)
        if img.format == "JPEG":
            output_path = input_path.rsplit(".", 1)[0] + ".png"

        output_path = input_path.rsplit(".", 1)[0] + "_converted.png"

        # Calc new dimensions for downscaling
        original_width, original_height = img.size
        small_width = max(1, original_width // pixel_size)
        small_height = max(1, original_height // pixel_size)

        # Downscale
        img_small = img.resize((small_width, small_height), Image.NEAREST)

        # Upscale to original size using NEAREST resampling
        pixelated_img = img_small.resize(
            (original_width, original_height), Image.NEAREST
        )

        # reduce colors 256 8-bit
        pixelated_img = pixelated_img.convert("P", palette=Image.ADAPTIVE, colors=256)

        pixelated_img.show()

        # Save img
        pixelated_img.save(output_path)
        print(f"Image successfully pixelated and saved to {output_path}")

    except FileNotFoundError:
        print(f"Error: Image not found at {input_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Test Program For Pillow Wrapper")
    parser.add_argument("input_path", help="Path to the input JPEG image")
    parser.add_argument("--output_path", help="Path to save the pixelated output image")

    args = parser.parse_args()

    input_path = args.input_path
    output_path = args.output_path

    pixelate_image(input_path, output_path, pixel_size=6)
