from bokeh.models import Div

kpi_glass = Div(text="""
<div style="
    backdrop-filter: blur(8px);
    background: rgba(255,255,255,0.33);
    border-radius: 2em;
    box-shadow: 0 8px 32px 0 rgba(31,38,135,0.18);
    border: 1.5px solid rgba(31,38,135,0.14);
    padding: 2em 2.1em 1.6em 2.1em;
    min-width: 220px;
    text-align: center;
    margin: 1.5em auto;
">
    <div style="font-size: 2.2em; font-weight: 900; color: #161a30; margin-bottom:0.28em;">1023</div>
    <div style="font-size: 1.02em; color: #2c365c; letter-spacing:1.2px;">Active Users</div>
</div>
""")
kpi_neon = Div(text="""
<div style="
    background: linear-gradient(120deg,#272e6a 0%,#0a1829 100%);
    border-radius: 1.4em;
    box-shadow: 0 2px 14px 0 #0005;
    padding: 2em 2em 1.6em 2em;
    min-width: 210px;
    text-align: center;
    margin: 1.2em auto;
">
    <div style="font-size:2.1em; font-weight:800; color:#18f0b8;
                text-shadow: 0 0 14px #18f0b8, 0 0 2px #18f0b8;">
        $9,150
    </div>
    <div style="font-size:1em; color:#8dc1ff; margin-top:0.15em;">
        Monthly Revenue
    </div>
    <div style="margin-top:0.4em; font-size:0.95em; color:#44e462;">
        ▲ +5.2% this month
    </div>
</div>
""")
kpi_leftbar = Div(text="""
<div style="
    display: flex;
    align-items: center;
    background: #f9fafe;
    border-left: 7px solid #845EC2;
    border-radius: 1.1em;
    box-shadow: 0 2px 10px #dad6ff33;
    padding: 1.7em 1.4em;
    min-width: 220px;
    margin: 1em auto;
">
    <div style="flex:1; text-align: left;">
        <div style="font-size: 1.4em; color: #845EC2; font-weight: 900;">
            72%
        </div>
        <div style="font-size: 1.02em; color: #262348;">
            System Health
        </div>
    </div>
    <div style="font-size: 1.4em; color: #e980fc; margin-left: 0.6em;">
        ❤
    </div>
</div>
""")
kpi_icon = Div(text="""
<div style="
    background: #fff;
    border-radius: 1.7em;
    box-shadow: 0 3px 14px #44337a13;
    padding: 2em 1.6em 1.4em 1.6em;
    min-width: 220px;
    text-align: center;
    margin: 1em auto;
">
    <div style="font-size: 2.4em; color: #0096c7; margin-bottom: 0.15em;">📈</div>
    <div style="font-size: 2.05em; color: #003459; font-weight:800;">
        438
    </div>
    <div style="font-size: 1.06em; color: #2b3a67; margin-top:0.13em;">
        Sales Today
    </div>
    <div style="margin-top: 0.29em; font-size: 0.98em; color: #38b000;">
        ▲ +16% vs yesterday
    </div>
</div>
""")

kpi_animated_icon = Div(text="""
<style>
@keyframes upWiggle {
  0% { transform: translateY(0) scale(1);}
  25% { transform: translateY(-5px) scale(1.18);}
  50% { transform: translateY(-2px) scale(1);}
  75% { transform: translateY(-7px) scale(1.1);}
  100% { transform: translateY(0) scale(1);}
}
.kpi-arrow {
  display:inline-block;
  color: #33c463;
  font-size: 1.3em;
  font-weight: bold;
  margin-left:0.4em;
  animation: upWiggle 1.4s infinite;
}
</style>
<div style="
    background: linear-gradient(120deg,#fafcfc 0%,#e8f7ee 100%);
    border-radius: 1.5em;
    box-shadow: 0 6px 22px #33c46311;
    padding: 2.2em 2.2em 1.7em 2.2em;
    min-width: 210px;
    text-align: center;
    margin: 1.2em auto;
">
    <div style="font-size:2.7em; font-weight:900; color:#1f6136;">
        41,230 <span class="kpi-arrow">▲</span>
    </div>
    <div style="font-size:1em; color:#417153; margin-top:0.23em;">
        Page Views
    </div>
    <div style="margin-top:0.41em; font-size:1.02em; color:#33c463;">
        +7.1% this week
    </div>
</div>
""")

kpi_animated_bg = Div(text="""
<style>
@keyframes gradientMove {
  0% {background-position: 0% 50%;}
  50% {background-position: 100% 50%;}
  100% {background-position: 0% 50%;}
}
.kpi-animated-bg {
  background: linear-gradient(270deg, #d9afd9, #97d9e1, #c3cfe2, #f6d365);
  background-size: 800% 800%;
  animation: gradientMove 4s ease-in-out infinite;
}
</style>
<div class="kpi-animated-bg" style="
    border-radius: 1.4em;
    box-shadow: 0 4px 16px #44337a18;
    padding: 2.3em 2em 1.7em 2em;
    min-width: 210px;
    text-align: center;
    margin: 1.2em auto;
">
    <div style="font-size:2.2em; font-weight:800; color:#233053;">5,620</div>
    <div style="font-size:1em; color:#41346b; margin-top:0.14em;">
        App Downloads
    </div>
    <div style="font-size:0.97em; color:#28648a; margin-top:0.37em;">
        ▲ +12% this month
    </div>
</div>
""")
from bokeh.layouts import row, column
from bokeh.plotting import show
from bokeh_rocks import save_plot
layout = column(row(kpi_glass, kpi_neon, kpi_leftbar),
row(kpi_icon,kpi_animated_icon,kpi_animated_bg))
show(layout)
save_plot(layout, "output/kpi_01")