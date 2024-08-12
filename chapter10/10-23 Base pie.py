'''
PyEcharts的使用可以分四个步骤实现：
1. 导入pyecharts包
2. 找到相应图形模板
3. 准备相应数据
4. 对图表进行个性化修饰
'''


# 导入
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

lst = [['温博',1000],['王倩',5111],['温如水',562]]


c = (
    Pie()
    #.add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    .add("",lst)
    .set_global_opts(title_opts=opts.TitleOpts(title="459家庭"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("my_family.html")
)

