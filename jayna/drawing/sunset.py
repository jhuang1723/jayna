# sunset for androo
import matplotlib.pyplot as plt
import numpy as np

def draw_sunset():
    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create gradient background
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, y)
    
    # Create sunset colors
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
    
    # Remove axes
    ax.axis('off')
    
    # Show the plot
    plt.show()

# Call the function to display the sunset
draw_sunset()