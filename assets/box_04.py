import pandas as pd, numpy as np
import bokeh_rocks as br
df4 = pd.DataFrame(
    {
        "department": np.repeat(
            ["Engineering", "Sales", "Marketing", "Operations"], 120
        ),
        "experience": np.tile(np.repeat(["Junior", "Mid", "Senior"], 40), 4),
        "satisfaction": np.concatenate(
            [
                # Engineering
                np.random.normal(7.2, 1.2, 40),  # Junior
                np.random.normal(7.8, 1.0, 40),  # Mid
                np.random.normal(8.2, 0.9, 40),  # Senior
                # Sales
                np.random.normal(6.8, 1.5, 40),  # Junior
                np.random.normal(7.5, 1.2, 40),  # Mid
                np.random.normal(8.0, 1.0, 40),  # Senior
                # Marketing
                np.random.normal(7.5, 1.1, 40),  # Junior
                np.random.normal(8.0, 0.9, 40),  # Mid
                np.random.normal(8.5, 0.8, 40),  # Senior
                # Operations
                np.random.normal(7.0, 1.3, 40),  # Junior
                np.random.normal(7.6, 1.1, 40),  # Mid
                np.random.normal(8.1, 0.9, 40),  # Senior
            ]
        ),
    }
)

experience_palette = {"Junior": "#ff6464", "Mid": "#ffc562", "Senior": "#63ff8d"}

p4 = br.boxplot(
    df4,
    xcol="department",
    ycol="satisfaction",
    group_col="experience",
    title="Employee Satisfaction by Department and Experience Level",
    ylabel="Satisfaction Score (1-10)", 
    palette=experience_palette,
    theme="light",
    legend_outside=True,
    width=1400,
    height=700,

)
p4.min_border_bottom = 200
br.save_plot(p4, 'output/box_04')