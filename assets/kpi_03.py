from bokeh.models import Div
from bokeh.plotting import show
from bokeh_rocks import save_plot
from bokeh.layouts import row
progress = 83  # percent

kpi_progress_hover = Div(text=f"""
<style>
.kpi-card-hover {{
  transition: transform 0.22s cubic-bezier(.4,1.4,.5,1), box-shadow 0.22s;
  box-shadow: 0 3px 14px #44337a13;
}}
.kpi-card-hover:hover {{
  transform: translateY(-13px) scale(1.032) rotateZ(-0.5deg);
  box-shadow: 0 14px 40px #38b00044, 0 1px 6px #a2e8dd11;
  z-index: 3;
}}
</style>
<div class="kpi-card-hover" style="
    background: #fff;
    border-radius: 1.4em;
    padding: 2em 1.4em 1.25em 1.4em;
    min-width: 230px;
    text-align: center;
    margin: 1em auto;
    cursor: pointer;
">
    <div style="font-size:2.15em; color:#009688; font-weight:800;">
        {progress}%
    </div>
    <div style="font-size:1.08em; color:#49757e; margin-top:0.1em;">
        Project Completion
    </div>
    <div style="margin-top:1.1em; margin-bottom:0.5em;">
        <div style="height:14px; width:85%; margin:0 auto; background:#e0f2f1; border-radius:9px; overflow:hidden;">
            <div style="
                height:100%; width:{progress}%; background:linear-gradient(90deg, #5ee7df 0%, #b490ca 100%);
                border-radius:9px 0 0 9px; transition: width 1s;">
            </div>
        </div>
    </div>
    <div style="font-size:0.98em; color:#009688;">
        Keep it up!
    </div>
</div>
""")
show(kpi_progress_hover)
save_plot(kpi_progress_hover, "output/kpi_03")