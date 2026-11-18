import os
import shutil
import sys

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    dst = os.path.join(output_dir, "entry.png")

    if not os.path.isfile(src):
        sys.stderr.write(f"Error: source entry image not found: {src}\n")
        sys.exit(1)

    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    print(f"Copied entry image to {dst} ({size} bytes)")

if __name__ == "__main__":
    main()
