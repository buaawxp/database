# -*- coding: utf-8 -*-

from django.http import HttpResponse

from polls.models import User


# 数据库操作
def testdb(request):
    test1 = User(uid="qwe", upwd="123456", un="clearlove", up="sdads")
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")