from butils import *

flows_music = [
    # 2015 -> 2017 (totals: iTunes=100, Pandora=55, Spotify=60, YouTube=20, Other=20)
    [
        ("iTunes", "iTunes", 45),
        ("iTunes", "Spotify", 30),
        ("iTunes", "Apple Music", 25),
        ("Pandora", "Pandora", 35),
        ("Pandora", "Spotify", 20),
        ("Spotify", "Spotify", 60),
        ("YouTube Music", "YouTube Music", 15),
        ("YouTube Music", "Spotify", 5),
        ("Other", "Other", 8),
        ("Other", "Spotify", 12),
    ],
    # 2017 -> 2019 (totals must match 2017 nodes)
    # iTunes=45, Spotify=127, Apple Music=25, Pandora=35, YouTube=15, Other=8
    [
        ("iTunes", "Apple Music", 30),
        ("iTunes", "Spotify", 15),
        ("Spotify", "Spotify", 115),
        ("Spotify", "Apple Music", 5),
        ("Spotify", "YouTube Music", 7),
        ("Apple Music", "Apple Music", 22),
        ("Apple Music", "Spotify", 3),
        ("Pandora", "Pandora", 28),
        ("Pandora", "Spotify", 7),
        ("YouTube Music", "YouTube Music", 13),
        ("YouTube Music", "Spotify", 2),
        ("Other", "Spotify", 5),
        ("Other", "Other", 3),
    ],
    # 2019 -> 2021 (totals must match 2019 nodes)
    # Spotify=147, Apple Music=57, Pandora=28, YouTube=20, Other=3
    [
        ("Spotify", "Spotify", 135),
        ("Spotify", "YouTube Music", 10),
        ("Spotify", "Apple Music", 2),
        ("Apple Music", "Apple Music", 52),
        ("Apple Music", "Spotify", 5),
        ("Pandora", "Pandora", 22),
        ("Pandora", "Spotify", 6),
        ("YouTube Music", "YouTube Music", 18),
        ("YouTube Music", "Spotify", 2),
        ("Other", "Spotify", 2),
        ("Other", "Other", 1),
    ],
    # 2021 -> 2024 (totals must match 2021 nodes)
    # Spotify=150, Apple Music=54, Pandora=22, YouTube=28, Other=1
    [
        ("Spotify", "Spotify", 140),
        ("Spotify", "YouTube Music", 8),
        ("Spotify", "Apple Music", 2),
        ("Apple Music", "Apple Music", 50),
        ("Apple Music", "Spotify", 4),
        ("Pandora", "Pandora", 18),
        ("Pandora", "Spotify", 4),
        ("YouTube Music", "YouTube Music", 26),
        ("YouTube Music", "Spotify", 2),
        ("Other", "Spotify", 1),
    ],
]

time_points_music = ["2015", "2017", "2019", "2021", "2024"]
categories_music = ["iTunes", "Spotify", "Apple Music", "Pandora", "YouTube Music", "Other"]
colors_music = {
    "iTunes": "#A2AAAD",
    "Spotify": "#1DB954",
    "Apple Music": "#FA243C",
    "Pandora": "#3668FF",
    "YouTube Music": "#FF0000",
    "Other": "#95A5A6"
}

diagram4 = create_alluvial(
    flows_music,
    time_points_music,
    categories_music,
    colors_music,
    title="Music Streaming Platform Migration (millions of users)",
    width=1400,
    height=650,
    gap=3
)
show(diagram4)
save_plot(diagram4, 'output/sankey_07')


