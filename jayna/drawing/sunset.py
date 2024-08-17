import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.colors import LinearSegmentedColormap

def draw_classic_sunset(ax):
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, y)
    sunset_colors = plt.cm.magma(Y)
    ax.imshow(sunset_colors, extent=[0, 1, 0, 1], aspect='auto')
    sun = plt.Circle((0.5, 0.3), 0.1, color='yellow', alpha=0.8)
    ax.add_artist(sun)
    ax.fill_between(x, 0, 0.3 + 0.1 * np.sin(10 * x), color='#2c3e50')
    ax.axhline(y=0.3, color='white', linestyle='--', alpha=0.5)
    ax.fill_between(x, 0, 0.3, color='#3498db', alpha=0.3)

def draw_palm_beach_sunset(ax):
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, y)
    
    # Create a custom colormap for a pink-orange sunset
    colors = ['#FF9AA2', '#FFB7B2', '#FFDAC1', '#E2F0CB']  # pink to light green
    n_bins = 100
    cmap = LinearSegmentedColormap.from_list('custom', colors, N=n_bins)
    sunset_colors = cmap(Y)
    ax.imshow(sunset_colors, extent=[0, 1, 0, 1], aspect='auto')
    
    # Sun - higher in the sky
    sun = plt.Circle((0.5, 0.6), 0.1, color='#FF6347', alpha=0.6)
    ax.add_artist(sun)
    
    # Ocean - increased size
    ax.fill_between(x, 0, 0.6 + 0.02 * np.sin(10 * x), color='#4169E1', alpha=0.6)
    
    # Beach - reduced size
    ax.fill_between(x, 0, 0.2 + 0.01 * np.sin(5 * x), color='#F4A460')
    
    def draw_palm_tree(x, height):
        # Trunk
        trunk_width = 0.02
        trunk_height = height * 0.8
        trunk = plt.Rectangle((x - trunk_width/2, 0.2), trunk_width, trunk_height, 
                              facecolor='#8B4513', edgecolor='none')
        ax.add_artist(trunk)
        
        # Leaves
        leaf_color = '#228B22'
        leaf_cluster = plt.Circle((x, 0.2 + trunk_height), 0.05, 
                                  facecolor=leaf_color, edgecolor='none')
        ax.add_artist(leaf_cluster)
        
        for angle in [-60, -30, 0, 30, 60]:
            leaf = plt.Polygon([(x, 0.2 + trunk_height), 
                                (x + 0.1 * np.cos(np.deg2rad(angle)), 
                                 0.2 + trunk_height + 0.1 * np.sin(np.deg2rad(angle)))],
                               facecolor=leaf_color, edgecolor='none')
            ax.add_artist(leaf)
    
    # Draw multiple palm trees
    draw_palm_tree(0.2, 0.3)
    draw_palm_tree(0.5, 0.35)
    draw_palm_tree(0.8, 0.32)

def draw_mountain_lake_sunset(ax):
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, y)
    sunset_colors = plt.cm.coolwarm(Y)
    ax.imshow(sunset_colors, extent=[0, 1, 0, 1], aspect='auto')
    sun = plt.Circle((0.5, 0.6), 0.08, color='#FFD700', alpha=0.8)
    ax.add_artist(sun)
    
    def mountain(peak_height):
        return peak_height + 0.2 * np.random.random(100) - 0.1
    
    ax.fill_between(x, 0, mountain(0.5), color='#2F4F4F')
    ax.fill_between(x, 0, mountain(0.3), color='#3D5A5A')
    ax.fill_between(x, 0, 0.2, color='#4682B4', alpha=0.6)
    reflection = plt.Circle((0.5, 0.1), 0.06, color='#FFD700', alpha=0.4)
    ax.add_artist(reflection)

def draw_cityscape_sunset(ax):
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, y)
    sunset_colors = plt.cm.plasma(Y)
    ax.imshow(sunset_colors, extent=[0, 1, 0, 1], aspect='auto')
    sun = plt.Circle((0.5, 0.4), 0.12, color='#FFA500', alpha=0.7)
    ax.add_artist(sun)
    
    for i in range(20):
        height = np.random.uniform(0.2, 0.6)
        width = np.random.uniform(0.03, 0.08)
        x_pos = np.random.uniform(0, 1)
        ax.add_artist(plt.Rectangle((x_pos, 0), width, height, color='black'))
        
    ax.fill_between(x, 0, 0.05, color='#696969')  # Road

def draw_desert_sunset(ax):
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, y)
    sunset_colors = plt.cm.YlOrRd(Y)
    ax.imshow(sunset_colors, extent=[0, 1, 0, 1], aspect='auto')
    sun = plt.Circle((0.5, 0.2), 0.15, color='#FF6347', alpha=0.8)
    ax.add_artist(sun)
    
    # Sand dunes
    ax.fill_between(x, 0, 0.3 + 0.1 * np.sin(5 * x), color='#D2691E')
    ax.fill_between(x, 0, 0.2 + 0.05 * np.sin(8 * x), color='#8B4513')
    
    # Cactus
    ax.add_artist(plt.Rectangle((0.7, 0.2), 0.02, 0.2, color='#006400'))
    ax.add_artist(plt.Rectangle((0.68, 0.3), 0.06, 0.02, color='#006400'))

def draw_snowy_mountain_sunset(ax):
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, y)
    sunset_colors = plt.cm.winter(Y)
    ax.imshow(sunset_colors, extent=[0, 1, 0, 1], aspect='auto')
    sun = plt.Circle((0.5, 0.7), 0.08, color='#FF69B4', alpha=0.6)
    ax.add_artist(sun)
    
    def snowy_mountain(peak_height):
        return peak_height + 0.2 * np.random.random(100) - 0.1
    
    ax.fill_between(x, 0, snowy_mountain(0.6), color='#F0F8FF')
    ax.fill_between(x, 0, snowy_mountain(0.4), color='#E6E6FA')
    ax.fill_between(x, 0, snowy_mountain(0.2), color='#B0E0E6')

def draw_stormy_sunset(ax):
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, y)
    storm_colors = plt.cm.gist_gray(Y)
    ax.imshow(storm_colors, extent=[0, 1, 0, 1], aspect='auto')
    
    # Sun peeking through clouds
    sun = plt.Circle((0.2, 0.6), 0.1, color='#FFA07A', alpha=0.4)
    ax.add_artist(sun)
    
    # Lightning
    for _ in range(3):
        start = np.random.uniform(0.4, 0.8)
        ax.plot([start, start + np.random.uniform(-0.1, 0.1)], 
                [1, np.random.uniform(0.4, 0.8)], color='yellow', linewidth=2, alpha=0.7)
    
    # Stormy sea
    ax.fill_between(x, 0, 0.3 + 0.05 * np.sin(20 * x), color='#4682B4', alpha=0.7)


def draw_tropical_island_sunset(ax):
    x = np.linspace(0, 1, 200)
    y = np.linspace(0, 1, 200)
    X, Y = np.meshgrid(x, y)
    
    # Create custom sunset colormap
    colors = ['#FF4500', '#FF6347', '#FFD700', '#87CEEB', '#4682B4']
    n_bins = 100
    cmap = LinearSegmentedColormap.from_list('custom_sunset', colors, N=n_bins)
    sunset_colors = cmap(Y)
    ax.imshow(sunset_colors, extent=[0, 1, 0, 1], aspect='auto')
    
    # Sun with gradient
    sun_radius = 0.12
    sun_center = (0.5, 0.35)
    sun_gradient = np.sqrt((X - sun_center[0])**2 + (Y - sun_center[1])**2)
    sun_mask = sun_gradient < sun_radius
    sunset_colors[sun_mask] = plt.cm.YlOrRd(1 - sun_gradient[sun_mask] / sun_radius)
    ax.imshow(sunset_colors, extent=[0, 1, 0, 1], aspect='auto')
    
    # Island with perspective
    island_points = np.array([(0.2, 0), (0.8, 0), (0.65, 0.25), (0.35, 0.25)])
    ax.add_artist(plt.Polygon(island_points, color='#228B22', zorder=2))
    
    # Beach
    beach_points = np.array([(0.25, 0), (0.75, 0), (0.7, 0.1), (0.3, 0.1)])
    ax.add_artist(plt.Polygon(beach_points, color='#F4A460', zorder=3))
    
    # Palm trees with perspective
    def draw_palm(x, height, width, leaf_size):
        trunk_color = '#8B4513'
        leaf_color = '#228B22'
        ax.add_artist(plt.Polygon([(x, 0.25), (x + width, 0.25), (x + width/2, 0.25 + height)], color=trunk_color, zorder=4))
        for angle in [-60, -30, 0, 30, 60]:
            leaf_end = (x + width/2 + leaf_size * np.cos(np.deg2rad(angle)), 
                        0.25 + height + leaf_size * np.sin(np.deg2rad(angle)))
            ax.add_artist(plt.Polygon([(x + width/2, 0.25 + height), leaf_end], closed=False, color=leaf_color, linewidth=2, zorder=5))
    
    draw_palm(0.4, 0.15, 0.02, 0.1)
    draw_palm(0.55, 0.18, 0.025, 0.12)
    draw_palm(0.3, 0.1, 0.015, 0.08)
    
    # Ocean with waves
    ocean_level = 0.25
    wave_height = 0.02
    wave_freq = 20
    ocean_surface = ocean_level + wave_height * np.sin(wave_freq * x) * np.exp(-10 * (y[:, np.newaxis] - ocean_level))
    ax.fill_between(x, 0, ocean_surface[0], color='#4169E1', alpha=0.6, zorder=1)
    
    # Reflections
    reflection_strength = 0.3
    reflection_height = 0.1
    ocean_mask = Y < ocean_level
    reflection_mask = (Y < ocean_level) & (Y > ocean_level - reflection_height)
    
    # Create a separate array for reflections
    reflection_colors = np.copy(sunset_colors)
    reflection_slice = sunset_colors[ocean_mask]
    reflection_slice = np.flipud(reflection_slice)
    reflection_colors[ocean_mask] = reflection_slice
    
    # Apply reflections
    blended_colors = np.where(reflection_mask[:,:,np.newaxis],
                              sunset_colors * (1 - reflection_strength) + reflection_colors * reflection_strength,
                              sunset_colors)
    
    ax.imshow(blended_colors, extent=[0, 1, 0, 1], aspect='auto')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

def draw_arctic_sunset(ax):
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, y)
    sunset_colors = plt.cm.cool(Y)
    ax.imshow(sunset_colors, extent=[0, 1, 0, 1], aspect='auto')
    sun = plt.Circle((0.5, 0.8), 0.07, color='#FFB6C1', alpha=0.6)
    ax.add_artist(sun)
    
    # Ice
    ax.fill_between(x, 0, 0.4 + 0.05 * np.sin(8 * x), color='white')
    ax.fill_between(x, 0, 0.3 + 0.03 * np.sin(12 * x), color='#F0FFFF')
    
    # Polar bear silhouette
    bear = plt.Polygon([(0.6, 0.4), (0.7, 0.4), (0.75, 0.45), (0.7, 0.5), (0.65, 0.5), (0.6, 0.45)], color='black')
    ax.add_artist(bear)

def draw_sunset():
    fig, ax = plt.subplots(figsize=(10, 6))
    sunset_functions = [
        draw_classic_sunset,
        draw_palm_beach_sunset,
        draw_mountain_lake_sunset,
        draw_cityscape_sunset,
        draw_desert_sunset,
        draw_snowy_mountain_sunset,
        draw_stormy_sunset,
        draw_tropical_island_sunset,
        draw_arctic_sunset
    ]
    random.choice(sunset_functions)(ax)
    ax.axis('off')
    plt.show()
