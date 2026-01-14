from PIL import Image

def image_to_c_bitmap(
    image_path,
    out_width,
    out_height,
    array_name="bitmap"
):

    img = Image.open(image_path).convert("L")

    # resize 
    img = img.resize((out_width, out_height), Image.LANCZOS)

    # convert to 1-bit black & white
    img = img.convert("1",dither=Image.FLOYDSTEINBERG)

    pixels = img.load()

    bytes_per_row = (out_width + 7) // 8
    data = []

    for y in range(out_height):
        for x_byte in range(bytes_per_row):
            byte = 0
            for bit in range(8):
                x = x_byte * 8 + bit
                if x < out_width:
                    # In PIL "1" mode: 0 = black, 255 = white
                    if pixels[x, y] == 0:
                        byte |= (1 << (7 - bit))
            data.append(byte)

    # print C array
    print(f"const uint8_t {array_name}[] PROGMEM = {{")
    for i, b in enumerate(data):
        if i % 12 == 0:
            print("    ", end="")
        print(f"0x{b:02x}", end="")
        if i < len(data) - 1:
            print(", ", end="")
        if i % 12 == 11:
            print()
    print("\n};")

    print(f"\n// Size: {out_width}x{out_height}")
    print(f"// Bytes: {len(data)}")

# example usage
image_to_c_bitmap(
    "anime-eyes.jpg",
    out_width=64,
    out_height=32,
    array_name="eyes_idle"
)
