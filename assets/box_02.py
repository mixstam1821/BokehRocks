import pandas as pd, numpy as np
import bokeh_rocks as br
df2 = pd.DataFrame(
    {
        "city": np.repeat(["New York", "Los Angeles", "Chicago", "Miami"], 100),
        "season": np.tile(np.repeat(["Winter", "Spring", "Summer", "Fall"], 25), 4),
        "temperature": np.concatenate(
            [
                # New York
                np.random.normal(0, 5, 25),  # Winter
                np.random.normal(15, 4, 25),  # Spring
                np.random.normal(28, 3, 25),  # Summer
                np.random.normal(12, 4, 25),  # Fall
                # Los Angeles
                np.random.normal(15, 3, 25),  # Winter
                np.random.normal(18, 3, 25),  # Spring
                np.random.normal(24, 2, 25),  # Summer
                np.random.normal(20, 3, 25),  # Fall
                # Chicago
                np.random.normal(-5, 6, 25),  # Winter
                np.random.normal(10, 5, 25),  # Spring
                np.random.normal(25, 4, 25),  # Summer
                np.random.normal(8, 5, 25),  # Fall
                # Miami
                np.random.normal(20, 2, 25),  # Winter
                np.random.normal(24, 2, 25),  # Spring
                np.random.normal(30, 2, 25),  # Summer
                np.random.normal(26, 2, 25),  # Fall
            ]
        ),
    }
)

season_palette = {
    "Winter": "#4db4fd",
    "Spring": "#63ff8d",
    "Summer": "#ffc562",
    "Fall": "#ff8bff",
}

p2 = br.boxplot(
    df2,
    xcol="city",
    ycol="temperature",
    group_col="season",
    title="Average Temperature by City and Season",
    ylabel="Temperature (°C)",
    palette=season_palette,
    theme="dark",
    legend_outside=True,
    width=1400,
    height=700,
)
p2.min_border_bottom = 220
br.save_plot(p2, 'output/box_02')