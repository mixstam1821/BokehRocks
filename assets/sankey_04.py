from butils import *
budget_flows = [
    {"source": "Revenue", "target": "Engineering", "value": 400},
    {"source": "Revenue", "target": "Marketing", "value": 250},
    {"source": "Revenue", "target": "Sales", "value": 200},
    {"source": "Revenue", "target": "Operations", "value": 150},
    {"source": "Investment", "target": "Engineering", "value": 100},
    {"source": "Investment", "target": "Marketing", "value": 50},
]

budget_source_colors = {"Revenue": "#2ECC71", "Investment": "#3498DB"}
budget_target_colors = {
    "Engineering": "#E74C3C",
    "Marketing": "#F39C12",
    "Sales": "#9B59B6",
    "Operations": "#1ABC9C"
}

diagram3 = create_sankey(
    budget_flows, 
    source_colors=budget_source_colors,
    target_colors=budget_target_colors,
    title="Company Budget Allocation ($M) - Static",
    flow_alpha=0.6,
    interactive=False  # No hover effects
)
show(diagram3)
save_plot(diagram3, 'output/sankey_04')