import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_organized_architecture():
    fig, ax = plt.subplots(figsize=(14, 8))

    # Define positions for each component
    positions = {
        'MainActivity': (0.1, 0.7),
        'JourneyViewModel': (0.3, 0.7),
        'CarbonFootprintCalculator': (0.5, 0.7),
        'LocationService': (0.7, 0.7),
        'External APIs': (0.5, 0.4),
    }

    # Define rectangles for each layer/component
    for component, pos in positions.items():
        rect = patches.FancyBboxPatch(
            (pos[0] - 0.1, pos[1] - 0.1), 0.2, 0.2,
            boxstyle="round,pad=0.05", edgecolor='black', facecolor='lightblue',
            linewidth=2
        )
        ax.add_patch(rect)
        ax.text(pos[0], pos[1], component, ha='center', va='center', fontsize=12, weight='bold')

    # Define arrows to show the flow of data and interaction
    arrows = [
        ((0.1, 0.65), (0.3, 0.65)),  # MainActivity to JourneyViewModel
        ((0.3, 0.65), (0.5, 0.65)),  # JourneyViewModel to CarbonFootprintCalculator
        ((0.5, 0.65), (0.7, 0.65)),  # CarbonFootprintCalculator to LocationService
        ((0.7, 0.65), (0.5, 0.4)),   # LocationService to External APIs
        ((0.5, 0.35), (0.5, 0.4)),   # External APIs to CarbonFootprintCalculator
    ]

    for start, end in arrows:
        ax.annotate('', xy=end, xytext=start,
                    arrowprops=dict(facecolor='black', shrink=0.05, lw=2))

    # Set limits, hide axes, and add title
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('Organized Architecture for Carbon Footprint Journey Planner Android App', fontsize=16, weight='bold')

    # Show plot
    plt.show()

# Call the function to draw the organized diagram
draw_organized_architecture()
