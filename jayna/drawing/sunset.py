import matplotlib.pyplot as plt
import numpy as np
import random

def draw_classic_sunset(ax):
    # Create gradient background
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, y)
    sunset_colors = plt.cm.magma(Y)
    ax.imshow(sunset_colors, extent=[0, 1, 0, 1], aspect='auto')
    
    # Draw sun
    sun = plt.Circle((0.5, 0.3), 0.1, color='yellow', alpha=0.8)
    ax.add_artist(sun)
    
    # Draw mountains
    mountain_color = '#2c3e50'
    ax.fill_between(x, 0, 0.3 + 0.1 * np.sin(10 * x), color=mountain_color)
    
    # Draw water reflection
    water_level = 0.3
    ax.axhline(y=water_level, color='white', linestyle='--', alpha=0.5)
    ax.fill_between(x, 0, water_level, color='#3498db', alpha=0.3)

def draw_palm_beach_sunset(ax):
    # Sky gradient
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, y)
    sunset_colors = plt.cm.RdYlOr_r(Y)
    ax.imshow(sunset_colors, extent=[0, 1, 0, 1], aspect='auto')
    
    # Sun
    sun = plt.Circle((0.5, 0.2), 0.15, color='#FF4500', alpha=0.6)
    ax.add_artist(sun)
    
    # Palm tree silhouettes
    def draw_palm(x, height):
        trunk = plt.Rectangle((x, 0), 0.02, height, color='black')
        ax.add_artist(trunk)
        for angle in [-50, -25, 0, 25, 50]:
            leaf = plt.Polygon([(x, height), (x + 0.1 * np.cos(np.deg2rad(angle)), height + 0.1 * np.sin(np.deg2rad(angle)))], closed=False, color='black')
            ax.add_artist(leaf)
    
    draw_palm(0.2, 0.4)
    draw_palm(0.8, 0.5)
    
    # Ocean
    ax.fill_between(x, 0, 0.1 + 0.02 * np.sin(20 * x), color='#4169E1', alpha=0.6)

def draw_mountain_lake_sunset(ax):
    # Sky gradient
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, y)
    sunset_colors = plt.cm.coolwarm(Y)
    ax.imshow(sunset_colors, extent=[0, 1, 0, 1], aspect='auto')
    
    # Sun
    sun = plt.Circle((0.5, 0.6), 0.08, color='#FFD700', alpha=0.8)
    ax.add_artist(sun)
    
    # Mountains
    def mountain(peak_height):
        return peak_height + 0.2 * np.random.random(100) - 0.1
    
    ax.fill_between(x, 0, mountain(0.5), color='#2F4F4F')
    ax.fill_between(x, 0, mountain(0.3), color='#3D5A5A')
    
    # Lake
    ax.fill_between(x, 0, 0.2, color='#4682B4', alpha=0.6)
    
    # Lake reflection
    reflection = plt.Circle((0.5, 0.1), 0.06, color='#FFD700', alpha=0.4)
    ax.add_artist(reflection)

def draw_sunset():
    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # List of available sunset drawing functions
    sunset_functions = [draw_classic_sunset, draw_palm_beach_sunset, draw_mountain_lake_sunset]
    
    # Randomly select and call one of the sunset drawing functions
    random.choice(sunset_functions)(ax)
    
    # Remove axes
    ax.axis('off')
    
    # Show the plot
    plt.show()
