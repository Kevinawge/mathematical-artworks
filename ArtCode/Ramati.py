from PIL import Image, ImageDraw
import torch
import numpy as np
import random
import os

canvas_width = 1500
canvas_height = 1000
canvas_size = (canvas_width, canvas_height)
frame_count = 20
line_count_range = (30, 55)
output_filename = "generative_art.gif"
circle_prob = 0.7
square_prob = 0.5


def get_distributions():
    y_start_distribution = torch.distributions.Normal(
        canvas_height / 2, canvas_height / 4)
    y_end_distribution = torch.distributions.Normal(
        canvas_height / 2, canvas_height / 4)
    x_distribution = torch.distributions.Normal(
        canvas_width / 2, canvas_width / 4)
    return y_start_distribution, y_end_distribution, x_distribution


def sample_halfnormal_radius(line_length):
    mean = np.sqrt(line_length * 2)
    scale = mean / np.sqrt(2 / np.pi)
    radius_dist = torch.distributions.HalfNormal(scale / 3)
    return max(1, int(radius_dist.sample()))


def draw_circle(draw, center_x, center_y, radius):
    left = center_x - radius
    right = center_x + radius
    top = center_y - radius
    bottom = center_y + radius
    fill_color = "black" if random.random() < 0.5 else "white"
    draw.ellipse([left, top, right, bottom], outline="black", fill=fill_color)


def draw_square(draw, base_x, base_y, size):
    x0 = base_x
    y0 = base_y
    x1 = base_x + size
    y1 = base_y + size
    draw.rectangle([x0, y0, x1, y1], fill="black")


def draw_lines_with_shapes():
    image = Image.new("RGB", canvas_size, "white")
    draw = ImageDraw.Draw(image)

    y_start_dist, y_end_dist, x_dist = get_distributions()
    line_count = random.randint(*line_count_range)

    for _ in range(line_count):
        x = int(x_dist.sample().item())
        y_start = int(y_start_dist.sample().item())
        y_end = int(y_end_dist.sample().item())
        draw.line([(x, y_start), (x, y_end)], fill="black", width=1)

        if random.random() < circle_prob:
            length = abs(y_end - y_start)
            radius = sample_halfnormal_radius(length)
            cx = x + random.choice([-radius, 0, radius])
            cy = y_end
            draw_circle(draw, cx, cy, radius)

        if random.random() < square_prob:
            mean_size = 30
            std_dev = 10
            size_distribution = torch.distributions.Normal(mean_size, std_dev)
            size = max(2, int(size_distribution.sample().item()))
            offset_x = x + random.randint(-size, size)
            offset_y = y_start + random.randint(-size, size)
            draw_square(draw, offset_x, offset_y, size)

    return image


frames = []
for _ in range(frame_count):
    frame = draw_lines_with_shapes()
    frames.append(frame)

frames[0].save(
    output_filename,
    save_all=True,
    append_images=frames[1:],
    duration=350,
    loop=0
)
