import os
import shutil

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    dst = os.path.join(output_dir, "entry.png")

    if not os.path.isfile(src):
        raise FileNotFoundError(f"Source entry image not found: {src}")

    shutil.copyfile(src, dst)
    print(f"Successfully copied {src} -> {dst}")

if __name__ == "__main__":
    main()
