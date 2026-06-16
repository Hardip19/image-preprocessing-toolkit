import cv2
import os
import argparse

def process_image(path, out_dir):
    img = cv2.imread(path)
    if img is None:
        return

    resized = cv2.resize(img, (256, 256))
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    norm = gray / 255.0
    flipped = cv2.flip(gray, 1)

    base = os.path.basename(path).split('.')[0]

    cv2.imwrite(f"{out_dir}/{base}_gray.jpg", gray)
    cv2.imwrite(f"{out_dir}/{base}_flip.jpg", flipped)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    for file in os.listdir(args.input):
        if file.lower().endswith((".jpg", ".png")):
            process_image(os.path.join(args.input, file), args.output)

if __name__ == "__main__":
    main()
