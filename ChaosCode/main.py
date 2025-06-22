from sculptor import Simulation
from chaos import *
from pathlib import Path
import os


def make_static_lorenz(out_file):
    sim = Simulation("Lorenz", lorenz, (10, 8 / 3, 28),
                     30, 2700, color="inferno", num_trajectories=200, velocity=3)
    sim.set_start_frame(1000)
    sim.set_limits((-17, 17), (-17, 17), (13, 38))
    sim.set_perspective("xz")
    sim.generate_animation()
    Path(os.path.dirname(out_file)).mkdir(parents=True, exist_ok=True)
    sim.save_video(out_file.replace(".gif", ".mp4"))


def make_rotating_lorenz(out_file):
    sim = Simulation("Lorenz", lorenz, (10, 8 / 3, 28),
                     30, 2700, color="inferno", num_trajectories=200, period=360, velocity=3)
    sim.set_start_frame(1000)
    sim.set_limits((-23, 23), (-23, 23), (11, 40))
    sim.set_perspective("xz")
    sim.set_rotation(azim_rotation="dynamic")
    sim.generate_animation()
    Path(os.path.dirname(out_file)).mkdir(parents=True, exist_ok=True)
    sim.save_video(out_file.replace(".gif", ".mp4"))


def make_static_halvorsen(out_file):
    sim = Simulation("Halvorsen", halvorsen, (1.4,), 30, 2700,
                     color="viridis", num_trajectories=200, velocity=3)
    sim.set_perspective((-30, -135))
    sim.set_limits((-9, 9), (-9, 9), (-6, 9))
    sim.generate_animation()
    Path(os.path.dirname(out_file)).mkdir(parents=True, exist_ok=True)
    sim.save_video(out_file.replace(".gif", ".mp4"))


def make_rotating_halvorsen(out_file):
    sim = Simulation("Halvorsen", halvorsen, (1.4,), 30, 2700,
                     color="viridis", num_trajectories=200, period=360, velocity=3)
    sim.set_perspective((-30, -135))
    sim.set_rotation(alt_rotation="partial", azim_rotation="dynamic")
    sim.set_limits((-11, 11), (-11, 11), (-6, 9))
    sim.generate_animation()
    Path(os.path.dirname(out_file)).mkdir(parents=True, exist_ok=True)
    sim.save_video(out_file.replace(".gif", ".mp4"))


def make_static_aizawa(out_file):
    sim = Simulation("Aizawa", aizawa, (0.95, 0.7, 0.65, 3.5, 0.25, 0.1),
                     30, 2700, color="magma", num_trajectories=200, tail_length=70, velocity=3)
    sim.set_perspective("xz")
    sim.set_limits((-1.06, 1), (-1, 1), (0, 1.5))
    sim.generate_animation()
    Path(os.path.dirname(out_file)).mkdir(parents=True, exist_ok=True)
    sim.save_video(out_file.replace(".gif", ".mp4"))


def make_rotating_aizawa(out_file):
    sim = Simulation("Aizawa", aizawa, (0.95, 0.7, 0.65, 3.5, 0.25, 0.1),
                     30, 2700, color="magma", num_trajectories=200, period=360, velocity=3)
    sim.set_perspective("xz")
    sim.set_rotation(azim_rotation="dynamic")
    sim.set_limits((-1.2, 1.2), (-1.2, 1.2), (-0.5, 1.8))
    sim.generate_animation()
    Path(os.path.dirname(out_file)).mkdir(parents=True, exist_ok=True)
    sim.save_video(out_file.replace(".gif", ".mp4"))


def make_static_thomas(out_file):
    sim = Simulation("Thomas", thomas, (0.1, 0.1, 0.1, 0.18), 30, 10000,
                     color="magma", num_trajectories=400, velocity=3)
    sim.set_perspective("xyz")
    sim.set_limits((-10, 10), (-10, 10), (-10, 10))
    sim.generate_animation()
    Path(os.path.dirname(out_file)).mkdir(parents=True, exist_ok=True)
    sim.save_video(out_file.replace(".gif", ".mp4"))


def make_rotating_thomas(out_file):
    sim = Simulation("Thomas", thomas, (0.1, 0.1, 0.1, 0.18), 30, 10000,
                     color="magma", num_trajectories=400, period=360, velocity=3)
    sim.set_perspective("xyz")
    sim.set_rotation(azim_rotation="dynamic")
    sim.set_limits((-10, 10), (-10, 10), (-10, 10))
    sim.generate_animation()
    Path(os.path.dirname(out_file)).mkdir(parents=True, exist_ok=True)
    sim.save_video(out_file.replace(".gif", ".mp4"))


def make_static_rossler(out_file):
    sim = Simulation("Rossler", rossler, (0.1, 0.0, 0.0, 0.2, 0.2, 10), 30, 10000,
                     color="plasma", num_trajectories=400, velocity=3)
    sim.set_perspective("xyz")
    sim.set_limits((-20, 20), (-20, 20), (0, 40))
    sim.generate_animation()
    Path(os.path.dirname(out_file)).mkdir(parents=True, exist_ok=True)
    sim.save_video(out_file.replace(".gif", ".mp4"))


def make_rotating_rossler(out_file):
    sim = Simulation("Rossler", rossler, (0.1, 0.0, 0.0, 0.2, 0.2, 10), 30, 10000,
                     color="plasma", num_trajectories=400, period=360, velocity=3)
    sim.set_perspective("xyz")
    sim.set_rotation(azim_rotation="dynamic")
    sim.set_limits((-20, 20), (-20, 20), (0, 40))
    sim.generate_animation()
    Path(os.path.dirname(out_file)).mkdir(parents=True, exist_ok=True)
    sim.save_video(out_file.replace(".gif", ".mp4"))


def make_static_chen(out_file):
    sim = Simulation("Chen", chen, (35, 28, 3), 30, 2700,
                     color="plasma", num_trajectories=200, velocity=3)
    sim.set_perspective("yz")
    sim.set_limits((-30, 30), (-30, 30), (-10, 60))
    sim.generate_animation()
    Path(os.path.dirname(out_file)).mkdir(parents=True, exist_ok=True)
    sim.save_video(out_file.replace(".gif", ".mp4"))


def make_rotating_chen(out_file):
    sim = Simulation("Chen", chen, (35, 28, 3), 30, 2700,
                     color="plasma", num_trajectories=200, period=360, velocity=3)
    sim.set_perspective("yz")
    sim.set_rotation(azim_rotation="dynamic")
    sim.set_limits((-35, 35), (-35, 35), (-10, 60))
    sim.generate_animation()
    Path(os.path.dirname(out_file)).mkdir(parents=True, exist_ok=True)
    sim.save_video(out_file.replace(".gif", ".mp4"))


def make_static_dadras(out_file):
    sim = Simulation("Dadras", dadras, (3, 2.7, 1.7, 2, 9), 30, 2700,
                     color="turbo", num_trajectories=200, velocity=3)
    sim.set_perspective((-20, 110))
    sim.set_limits((-2.5, 2.5), (-2.5, 2.5), (-2.5, 2.5))
    sim.generate_animation()
    Path(os.path.dirname(out_file)).mkdir(parents=True, exist_ok=True)
    sim.save_video(out_file.replace(".gif", ".mp4"))


def make_rotating_dadras(out_file):
    sim = Simulation("Dadras", dadras, (3, 2.7, 1.7, 2, 9), 30, 2700,
                     color="turbo", num_trajectories=200, period=360, velocity=3)
    sim.set_perspective((-20, 110))
    sim.set_rotation(azim_rotation="dynamic")
    sim.set_limits((-3, 3), (-3, 3), (-3, 3))
    sim.generate_animation()
    Path(os.path.dirname(out_file)).mkdir(parents=True, exist_ok=True)
    sim.save_video(out_file.replace(".gif", ".mp4"))
