from bokeh_rocks import create_sunburst, save_plot

tech_data = {
    "name": "Tech Stack",
    "children": [
        {
            "name": "Frontend",
            "children": [
                {
                    "name": "React",
                    "children": [
                        {"name": "Next.js", "value": 45},
                        {"name": "Remix", "value": 30},
                        {"name": "Gatsby", "value": 25}
                    ]
                },
                {
                    "name": "Vue",
                    "children": [
                        {"name": "Nuxt", "value": 40},
                        {"name": "Quasar", "value": 20}
                    ]
                },
                {"name": "Svelte", "value": 35},
                {"name": "Angular", "value": 50}
            ]
        },
        {
            "name": "Backend",
            "children": [
                {
                    "name": "Python",
                    "children": [
                        {"name": "Django", "value": 55},
                        {"name": "FastAPI", "value": 60},
                        {"name": "Flask", "value": 40}
                    ]
                },
                {
                    "name": "Node.js",
                    "children": [
                        {"name": "Express", "value": 50},
                        {"name": "NestJS", "value": 45}
                    ]
                },
                {"name": "Go", "value": 65},
                {"name": "Rust", "value": 35}
            ]
        },
        {
            "name": "Database",
            "children": [
                {
                    "name": "SQL",
                    "children": [
                        {"name": "PostgreSQL", "value": 70},
                        {"name": "MySQL", "value": 55}
                    ]
                },
                {
                    "name": "NoSQL",
                    "children": [
                        {"name": "MongoDB", "value": 60},
                        {"name": "Redis", "value": 45},
                        {"name": "Cassandra", "value": 30}
                    ]
                }
            ]
        },
        {
            "name": "DevOps",
            "children": [
                {"name": "Docker", "value": 80},
                {"name": "Kubernetes", "value": 70},
                {"name": "Terraform", "value": 50},
                {"name": "GitHub Actions", "value": 60}
            ]
        }
    ]
}

p1 = create_sunburst(
    tech_data,
    title="Technology Stack Distribution", 
)

save_plot(p1, "output/sunburst_01")