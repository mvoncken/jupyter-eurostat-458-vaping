"""
can this work?
Just from mysetup import * ?
"""
%matplotlib inline
import pandas
A2PATH = "./SP458 Tobacco Volume A_v2.xls"
# Full width display for text fields.
pandas.set_option('display.max_colwidth', -1)

def style_eu_bar(ax,headers):
    ax.axes.get_yaxis().set_visible(False) #it's not a percentage ; but a ratio, hide

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    for (p,label) in zip(ax.patches,headers):
        width, height = p.get_width(), p.get_height()
        x, y = p.get_xy() 
        ax.annotate('{:.0%}'.format(height), (p.get_x()+.15*width, p.get_y() + height + 0.01))
        if (label.startswith("UE")):
            p.set_facecolor("red")
    return ax

class toggleDisplay(object):
    def __init__(self, title, obj):
        self.title = title
        self.obj = obj

    toggle = """<script>
    function toggle(el){
        console.log(el)
        var content = el.nextElementSibling;
        if (content.style.display === "block") {
          content.style.display = "none";
          el.childNodes[1].textContent = " (+)"
        } else {
          content.style.display = "block";
          el.childNodes[1].textContent = " (-)"
        }
    }    
    </script>
    
    <button class="collapsible" onclick="toggle(this)">%s<span> (+)</span></button>
    <div class="content" style="display:none">
      %s
    </div>
    """
    
    
    def _repr_html_(self):
        return self.toggle % (self.title,self.obj._repr_html_());
    
#toggleDisplay("my data",data)    


            