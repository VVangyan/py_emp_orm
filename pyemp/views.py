from django.shortcuts import render, HttpResponse

# Create your views here.
import datetime, time

from pyemp.models import *


# 查看执行sql 需要引入

def show_time(req):
    t = datetime.datetime.now()
    # return HttpResponse("<html><body>it is now  %s.</body></html>" % t)
    time = {"time": t}  # 字典，也成为map
    return render(req, "showtime.html", time)


class Animal():
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex


def query(req):
    l = ["张三", "李四", "王五"]
    d = {"name": "张三", "age": 18, "city": "wuhan"}
    c = Animal("Tom", "公")

    testfilter = "hello world!"

    num = 8
    a = "<a href='#'>如果想把标签渲染成html标签，需要 添加一个safe</a>"
    return render(req, "query.html", locals())


def gotopost(req):
    return render(req, "testpost.html")


def testpost(req):
    print(req)
    return HttpResponse("ok")


def index(request):
    return render(request, "index.html")


def addbook(request):
    # 方式一：
    # b=Book(name="python 基础",price=99,author="yan",pub_date="2018-7-22")
    # b.save()

    # 方式二：
    Book.objects.create(name="java 基础", price=99, author="yan", pub_date="2018-7-22")
    return HttpResponse("添加成功！")


# 注意：

# <1> 第二种方式修改不能用get的原因是：update是QuerySet对象的方法，
# get返回的是一个model对象，它没有update方法，而filter返回的是一个
# QuerySet对象(filter里面的条件可能有多个条件符合，比如name＝'alvin',
# 可能有两个name＝'alvin'的行数据)。
# <2>在“插入和更新数据”小节中，我们有提到模型的save()方法，这个方
# 法会更新一行里的所有列。 而某些情况下，我们只需要更新行里的某几列。
def updatebook(req):
    ######################## 方式一 ，推荐用方式一#######################
    # 查询id=1 ，其实是吧所有的值都查出来了
    # Book.objects.filter(id=1).update(price=80)
    # print(b.values())

    ####################### 方式二 ########################
    b = Book.objects.get(id=2)
    b.price = 133
    b.save()
    # print(b.query.__str__())#显示sql
    return HttpResponse("修改成功！")


def delbook(req):
    Book.objects.filter(id=1).delete()
    return HttpResponse("删除成功！")


# 查询相关API：
###  <1>filter(**kwargs):      它包含了与所给筛选条件相匹配的对象
###  <2>all():                 查询所有结果
#  <3>get(**kwargs):         返回与所给筛选条件相匹配的对象，返回结果有且只有一个，如果符合筛选条件的对象超过一个或者没有都会抛出错误。
# -----------下面的方法都是对查询的结果再进行处理:比如 objects.filter.values()--------
###  <4>values(*field):        返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列 model的实例化对象，而是一个可迭代的字典序列
#  <5>exclude(**kwargs):     它包含了与所给筛选条件不匹配的对象
#  <6>order_by(*field):      对查询结果排序
#  <7>reverse():             对查询结果反向排序
#  <8>distinct():            从返回结果中剔除重复纪录
#  <9>values_list(*field):   它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列
#  <10>count():              返回数据库中匹配查询(QuerySet)的对象数量。
# <11>first():               返回第一条记录
# <12>last():                返回最后一条记录
#  <13>exists():             如果QuerySet包含数据，就返回True，否则返回False。
def selectbook(req):
    bList = Book.objects.all()[:3]  # 切片
    print(bList[0].__str__())
    resultList = {"bList": bList}
    return render(req, "index.html", resultList)
