from bokeh_rocks import create_alluvial, save_plot
from bokeh.io import show
from bokeh.io import curdoc
curdoc().theme = "light_minimal"
flows_customer = [
    # Awareness -> Consideration (Awareness totals: Social Media=1200, Search=1100, Referral=300)
    [
        ("Social Media", "Website", 800),
        ("Social Media", "Comparison", 400),
        ("Search", "Website", 600),
        ("Search", "Comparison", 500),
        ("Referral", "Website", 200),
        ("Referral", "Comparison", 100),
    ],
    # Consideration -> Intent (Consideration totals: Website=1600, Comparison=1000)
    [
        ("Website", "Free Trial", 800),
        ("Website", "Demo Request", 500),
        ("Website", "Exit", 300),
        ("Comparison", "Free Trial", 300),
        ("Comparison", "Demo Request", 200),
        ("Comparison", "Exit", 500),
    ],
    # Intent -> Purchase (Intent totals: Free Trial=1100, Demo Request=700, Exit=800)
    [
        ("Free Trial", "Purchase", 600),
        ("Free Trial", "Exit", 500),
        ("Demo Request", "Purchase", 400),
        ("Demo Request", "Exit", 300),
        ("Exit", "Exit", 800),
    ],
    # Purchase -> Loyalty (Purchase totals: Purchase=1000, Exit=1600)
    [
        ("Purchase", "Active User", 850),
        ("Purchase", "Churned", 150),
        ("Exit", "Churned", 1600),
    ],
]

time_points_customer = ["Awareness", "Consideration", "Intent", "Purchase", "Loyalty"]
categories_customer = ["Social Media", "Search", "Referral", "Website", "Comparison", 
                       "Free Trial", "Demo Request", "Exit", "Purchase", "Active User", "Churned"]
colors_customer = {
    "Social Media": "#3498DB",
    "Search": "#2ECC71",
    "Referral": "#F39C12",
    "Website": "#9B59B6",
    "Comparison": "#E74C3C",
    "Free Trial": "#1ABC9C",
    "Demo Request": "#E67E22",
    "Exit": "#95A5A6",
    "Purchase": "#27AE60",
    "Active User": "#16A085",
    "Churned": "#C0392B",
}

diagram2 = create_alluvial(
    flows_customer,
    time_points_customer,
    categories_customer,
    colors_customer,
    title="Customer Journey Funnel",
    width=1400,
    height=650
)
show(diagram2)

save_plot(diagram2, 'output/sankey_01')
