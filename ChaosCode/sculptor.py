import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib import cm
from chaos import *


class Simulation:
    FPS = 30

    VIEWS = {
        "xy": (-90, 90),
        "xz": (0, 90),
        "yz": (0, 0)
    }

    def __init__(self, name, ode, args, t_final, num_t_values,
                 num_trajectories=100, tail_length=50, t_initial=0,
                 velocity=3, period=360, color="plasma", seed=1):

        np.random.seed(seed)
        self.num_trajectories = num_trajectories
        self.tail_length = tail_length
        self.t_values = np.linspace(t_initial, t_final, num_t_values)
        self.velocity = velocity
        self.period = period
        self.color_map = cm.get_cmap(color)
        self.start_frame = 0

        self.rotate_alt = lambda x: 0
        self.rotate_azim = lambda x: 0

        initial_values = -0.005 + 0.01 * \
            np.random.random((num_trajectories, 3))
        self.trajectories = np.asarray([
            odeint(ode, point, self.t_values, args=args)
            for point in initial_values
        ])

        self.fig = plt.figure(name, figsize=(5, 5))
        self.ax = self.fig.add_axes([0, 0, 1, 1], projection='3d')
        self.fig.subplots_adjust(left=0, bottom=0, right=1, top=1)
        self.ax.axis("off")
        self.ax.set_facecolor("black")

        # ONE tail layer per trajectory
        self.tails = []
        for _ in range(num_trajectories):
            line = Line3DCollection(
                [], linewidths=1.0, alpha=0.9, cmap=self.color_map)
            self.ax.add_collection3d(line)
            self.tails.append(line)

        self.heads = sum([
            self.ax.plot([], [], [], '.', markersize=0.15, c="white")
            for _ in range(num_trajectories)
        ], [])

    def set_start_frame(self, start_frame):
        self.start_frame = start_frame

    def set_limits(self, x_limits, y_limits, z_limits):
        self.ax.set_xlim(x_limits)
        self.ax.set_ylim(y_limits)
        self.ax.set_zlim(z_limits)

    def set_perspective(self, perspective):
        if perspective in Simulation.VIEWS:
            alt, azim = Simulation.VIEWS[perspective]
        else:
            alt, azim = perspective
        self.ax.view_init(alt, azim)
        self.rotate_alt = lambda x: alt
        self.rotate_azim = lambda x: azim

    def get_rotation_function(self, rotation_type, initial):
        if rotation_type == "linear":
            return lambda x: initial + x * 360 / self.period
        elif rotation_type == "dynamic":
            return lambda x: initial + 360 / self.period * x - 90 / np.pi * np.sin(4 * np.pi * x / self.period)
        elif rotation_type == "partial":
            return lambda x: initial * np.cos(2 * np.pi * x / self.period)
        else:
            return lambda x: initial

    def set_rotation(self, alt_rotation="static", azim_rotation="static"):
        self.rotate_alt = self.get_rotation_function(
            alt_rotation, self.ax.elev)
        self.rotate_azim = self.get_rotation_function(
            azim_rotation, self.ax.azim)

    def get_animation_function(self):
        def animate(i):
            self.ax.view_init(self.rotate_alt(i), self.rotate_azim(i))

            i += self.start_frame
            i = int(self.velocity * i) % self.trajectories.shape[1]

            for idx, (tail, head, traj) in enumerate(zip(self.tails, self.heads, self.trajectories)):
                tail_start = max(0, i - self.tail_length)
                segment = traj[tail_start:i]
                if len(segment) < 2:
                    continue

                points = segment.reshape(-1, 1, 3)
                segments = np.concatenate([points[:-1], points[1:]], axis=1)

                velocity_vec = np.diff(segment, axis=0)
                speed = np.linalg.norm(velocity_vec, axis=1)
                norm_speed = (speed - speed.min()) / (speed.ptp() + 1e-9)
                colors = self.color_map(norm_speed)

                tail.set_segments(segments)
                tail.set_color(colors)

                x, y, z = segment[-1]
                head.set_data([x], [y])
                head.set_3d_properties([z])

            return self.tails + self.heads

        return animate

    def generate_animation(self):
        animate = self.get_animation_function()
        frames = len(self.t_values) // self.velocity
        interval = 1000 // Simulation.FPS
        self.anim = animation.FuncAnimation(
            self.fig, animate, frames=frames, interval=interval, blit=False)

    def show_animation(self):
        plt.show()

    def save_video(self, file_name):
        self.anim.save(file_name, writer="ffmpeg", dpi=400, fps=Simulation.FPS)
