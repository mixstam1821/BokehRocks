
from bokeh_rocks import create_radar_chart, show, save_plot
categories7 = [
    'Strength',
    'Dexterity',
    'Intelligence',
    'Wisdom',
    'Constitution',
    'Charisma',
    'Speed',
    'Defense',
    'Magic'
]

character_data = [
    [0.95, 0.60, 0.40, 0.45, 0.85, 0.50, 0.70, 0.90, 0.35],  # Warrior
    [0.50, 0.95, 0.70, 0.65, 0.60, 0.60, 0.90, 0.65, 0.55],  # Rogue
    [0.30, 0.50, 0.95, 0.90, 0.50, 0.70, 0.60, 0.40, 0.95],  # Mage
    [0.70, 0.65, 0.75, 0.85, 0.75, 0.80, 0.70, 0.70, 0.70],  # Paladin
]

character_names = ['⚔️ Warrior', '🗡️ Rogue', '🔮 Mage', '🛡️ Paladin']
character_colors = ['#c0392b', '#8e44ad', '#2980b9', '#f39c12']

chart7 = create_radar_chart(
    categories=categories7,
    series_data=character_data,
    series_names=character_names,
    colors=character_colors,
    title="🎮 RPG Character Class Comparison",
    width=850,
    height=850,
    fill_alpha=0.2,
    line_width=4,
    marker_size=13,
    grid_levels=5,
    theme="dark",
    background_gradient="radial-gradient(circle at center, #232526 0%, #414345 100%)"
)

show(chart7)
save_plot(chart7, "output/radar_07")

