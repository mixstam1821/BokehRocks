from bokeh_rocks import create_sunburst, save_plot

revenue_data = {
    "name": "Annual Revenue",
    "children": [
        {
            "name": "Products",
            "children": [
                {
                    "name": "Software",
                    "children": [
                        {"name": "Enterprise", "value": 450},
                        {"name": "SMB", "value": 280},
                        {"name": "Individual", "value": 120}
                    ]
                },
                {
                    "name": "Hardware",
                    "children": [
                        {"name": "Servers", "value": 320},
                        {"name": "Devices", "value": 180}
                    ]
                }
            ]
        },
        {
            "name": "Services",
            "children": [
                {
                    "name": "Consulting",
                    "children": [
                        {"name": "Strategy", "value": 200},
                        {"name": "Implementation", "value": 350},
                        {"name": "Training", "value": 150}
                    ]
                },
                {
                    "name": "Support",
                    "children": [
                        {"name": "Premium", "value": 240},
                        {"name": "Standard", "value": 160}
                    ]
                }
            ]
        },
        {
            "name": "Subscriptions",
            "children": [
                {"name": "Cloud Platform", "value": 400},
                {"name": "Analytics", "value": 280},
                {"name": "Security", "value": 220}
            ]
        }
    ]
}
p2 = create_sunburst(
        revenue_data,
        title="Annual Revenue Breakdown ($M)",
    )
save_plot(p2, "output/sunburst_02")