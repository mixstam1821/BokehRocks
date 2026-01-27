import pandas as pd, numpy as np
import bokeh_rocks as br
np.random.seed(42)
df1 = pd.DataFrame(
    {
        "subject": np.repeat(["Math", "Science", "English", "History"], 50),
        "score": np.concatenate(
            [
                np.random.normal(75, 10, 50),  # Math
                np.random.normal(80, 8, 50),  # Science
                np.random.normal(70, 12, 50),  # English
                np.random.normal(78, 9, 50),  # History
            ]
        ),
    }
)

p1 = br.boxplot(
    df1,
    xcol="subject",
    ycol="score",
    title="Student Test Scores by Subject",
    ylabel="Score (%)",
    theme="light",
    width=1000,
    height=600,
)
p1.min_border_bottom = 140
br.save_plot(p1, 'output/box_01')