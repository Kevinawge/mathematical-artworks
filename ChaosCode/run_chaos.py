from main import (
    make_static_lorenz,
    make_rotating_lorenz,
    make_static_halvorsen,
    make_rotating_halvorsen,
    make_static_aizawa,
    make_rotating_aizawa,
    make_static_rossler,
    make_rotating_rossler,
    make_static_thomas,
    make_rotating_thomas,
    make_static_chen,
    make_rotating_chen,
    make_static_dadras,
    make_rotating_dadras
)

from pathlib import Path
import os


def run():
    Path("attractor_videos").mkdir(exist_ok=True)

    options = {
        "1": ("static_lorenz.mp4", make_static_lorenz),
        "2": ("rotating_lorenz.mp4", make_rotating_lorenz),
        "3": ("static_halvorsen.mp4", make_static_halvorsen),
        "4": ("rotating_halvorsen.mp4", make_rotating_halvorsen),
        "5": ("static_aizawa.mp4", make_static_aizawa),
        "6": ("rotating_aizawa.mp4", make_rotating_aizawa),
        "7": ("static_rossler.mp4", make_static_rossler),
        "8": ("rotating_rossler.mp4", make_rotating_rossler),
        "9": ("static_thomas.mp4", make_static_thomas),
        "10": ("rotating_thomas.mp4", make_rotating_thomas),
        "11": ("static_chen.mp4", make_static_chen),
        "12": ("rotating_chen.mp4", make_rotating_chen),
        "13": ("static_dadras.mp4", make_static_dadras),
        "14": ("rotating_dadras.mp4", make_rotating_dadras),
    }

    print("\nChoose an Attractor to Render:\n")
    for key, (filename, _) in options.items():
        print(f"[{key}] {filename}")

    choice = input("\nEnter number: ").strip()

    if choice in options:
        filename, func = options[choice]
        full_path = f"attractor_videos/{filename}"
        print(f"\nRendering {filename} ...")
        func(full_path)
        print(f"\nSaved to {full_path}")
    else:
        print("Invalid choice. Try again.")


if __name__ == "__main__":
    run()
