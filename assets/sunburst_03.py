from bokeh_rocks import create_sunburst, save_plot

sales_data = {
    "name": "Global Sales",
    "children": [
        {
            "name": "Americas",
            "children": [
                {
                    "name": "North America",
                    "children": [
                        {"name": "USA", "value": 850},
                        {"name": "Canada", "value": 280},
                        {"name": "Mexico", "value": 190}
                    ]
                },
                {
                    "name": "South America",
                    "children": [
                        {"name": "Brazil", "value": 240},
                        {"name": "Argentina", "value": 120},
                        {"name": "Other", "value": 150}
                    ]
                }
            ]
        },
        {
            "name": "Europe",
            "children": [
                {
                    "name": "Western Europe",
                    "children": [
                        {"name": "Germany", "value": 420},
                        {"name": "France", "value": 380},
                        {"name": "UK", "value": 350},
                        {"name": "Spain", "value": 220}
                    ]
                },
                {
                    "name": "Eastern Europe",
                    "children": [
                        {"name": "Poland", "value": 180},
                        {"name": "Other", "value": 160}
                    ]
                }
            ]
        },
        {
            "name": "Asia Pacific",
            "children": [
                {
                    "name": "East Asia",
                    "children": [
                        {"name": "China", "value": 720},
                        {"name": "Japan", "value": 480},
                        {"name": "South Korea", "value": 320}
                    ]
                },
                {
                    "name": "Southeast Asia",
                    "children": [
                        {"name": "Singapore", "value": 250},
                        {"name": "Indonesia", "value": 200},
                        {"name": "Other", "value": 280}
                    ]
                },
                {"name": "India", "value": 520},
                {"name": "Australia", "value": 310}
            ]
        },
        {
            "name": "Middle East & Africa",
            "children": [
                {"name": "UAE", "value": 280},
                {"name": "Saudi Arabia", "value": 220},
                {"name": "South Africa", "value": 180},
                {"name": "Other", "value": 190}
            ]
        }
    ]
}
p3 = create_sunburst(
    sales_data,
    title="Global Sales by Region ($M)",
)
save_plot(p3, "output/sunburst_03")