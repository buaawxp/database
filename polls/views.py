from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

global total_did  ##全局订单id
global total_mid
total_mid = 0
total_did = 0


# Create your views here.

def toLogin_view(request):
    return render(request, 'login.html')


def Login_view(request):
    u = request.POST.get("user", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    p = request.POST.get("pwd", '')

    if u and p:
        # c = StudentInfo.objects.filter(stu_name=u, stu_psw=p).count()

        # status = 1
        # res = JsonResponse(status, safe=False)
        #
        # return res
        return HttpResponse(f"登陆成功,学生姓名是,学生密码是,学生学号为")

    else:
        return HttpResponse("请输入正确的账号和密码")


def regist_user(request):
    # a = request.POST.get("id", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # b = request.POST.get("pwd", '')
    # c = request.POST.get("name", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # d = request.POST.get("head", '')
    # if a and b and c and d:
    #     test1 = User(uid=a, upwd=b, un=c, up=d)
    #     test1.save()
    #     return HttpResponse("<p>用户注册成功！</p>")
    # else:
    #     return HttpResponse("<p>测你的码</p>")
    if request.method == "POST":
        data_json = json.loads(request.body)

        uid = data_json["uid"]
        upwd = data_json["upwd"]
        un = data_json["un"]
        up = data_json["up"]

        if uid and upwd and un and up:
            test1 = User(uid=uid, upwd=upwd, un=un, up=up)
            test1.save()
            return JsonResponse({"result": 1, "message": "用户注册成功"})
        else:
            return JsonResponse({"result": 0, "message": "注册失败，请输入完整的注册信息"})


def regist_admin(request):
    # a = request.POST.get("id", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # b = request.POST.get("pwd", '')
    # c = request.POST.get("name", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # d = request.POST.get("head", '')
    # if a and b and c and d:
    #     test1 = User(uid=a, upwd=b, un=c, up=d)
    #     test1.save()
    #     return HttpResponse("<p>用户注册成功！</p>")
    # else:
    #     return HttpResponse("<p>测你的码</p>")
    if request.method == "POST":
        data_json = json.loads(request.body)

        aid = data_json["aid"]
        apwd = data_json["apwd"]
        an = data_json["an"]

        if aid and apwd and an:
            test1 = Administator(aid=aid, apwd=apwd, an=an)
            test1.save()
            return JsonResponse({"result": 1, "message": "管理员注册成功"})
        else:
            return JsonResponse({"result": 0, "message": "注册失败，请输入完整的注册信息"})


# 用户登录
@csrf_exempt
def login_user(request):
    # a = request.POST.get("id", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # b = request.POST.get("pwd", '')
    # if a and b:
    #     c = User.objects.filter(uid=a, upwd=b).count()
    #     if c:
    #         return HttpResponse("<p>用户登录成功！</p>")
    #     else:
    #         return HttpResponse("<p>用户登录失败！</p>")
    # else:
    #     return HttpResponse("<p>请输入正确的用户id和密码</p>")
    print("request")
    return JsonResponse({"result": 0, "message": "fuck u","rType":request.method})
    """
    if request.method == "POST":
        data_json = json.loads(request.body)

        id = data_json["id"]
        pwd = data_json["pwd"]

        if id and pwd:
            if User.objects.filter(uid=id).exists():  # 如果用户存在
                test1 = User.objects.get(uid=id)
                if test1.upwd == pwd:
                    return JsonResponse({"result": 1, "message": "用户登录成功"})
                else:
                    return JsonResponse({"result": 0, "message": "登陆失败，密码错误"})
            else:
                return JsonResponse({"result": 0, "message": "用户不存在"})
        else:
            return JsonResponse({"result": 0, "message": "登录失败，请输入完整的账号和密码信息"})"""


def change_pwd_user(request):
    # a = request.POST.get("id", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # b = request.POST.get("oldpwd", '')
    # c = request.POST.get("newpwd", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # if a and b and c:
    #     User.objects.filter(upwd=b).update(upwd=c)
    #     return HttpResponse("<p>用户密码更改成功！</p>")
    # else:
    #     return HttpResponse("<p>用户密码更改失败</p>")
    if request.method != "POST":
        return JsonResponse({"result": 0, "message": "Error"})
    data_json = json.loads(request.body)
    uid = request.session.get("id", 0)
    if uid == 0:
        return JsonResponse({"result": 0, "message": "尚未登录"})
    user = User.objects.get(uid=uid)
    oupwd = user.upwd
    nupwd = data_json["nupwd"]  ## 新昵称

    if uid and oupwd and nupwd:
        user.update(upwd=nupwd)
        JsonResponse({"result": 1, "message": "用户密码修改成功"})
    else:
        return JsonResponse({"result": 0, "message": "用户密码修改失败"})


# 修改用户昵称
def change_n_user(request):
    # a = request.POST.get("id", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # b = request.POST.get("oldn", '')
    # c = request.POST.get("newn", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # if a and b and c:
    #     User.objects.filter(un=b).update(un=c)
    #     return HttpResponse("<p>用户昵称更改成功！</p>")
    # else:
    #     return HttpResponse("<p>用户昵称更改失败</p>")
    if request.method != "POST":
        return JsonResponse({"result": 0, "message": "Error"})
    data_json = json.loads(request.body)
    uid = request.session.get("id", 0)
    if uid == 0:
        return JsonResponse({"result": 0, "message": "尚未登录"})
    user = User.objects.get(uid=uid)
    oun = user.uid
    nun = data_json["nun"]  ## 新昵称

    if uid and oun and nun:
        user.update(un=nun)
        JsonResponse({"result": 1, "message": "昵称修改成功"})
    else:
        return JsonResponse({"result": 0, "message": "昵称修改失败"})


# ????????????????? 只有一个新头像怎么操作
def change_p_user(request):
    # a = request.POST.get("id", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # b = request.POST.get("oldp", '')
    # c = request.POST.get("newp", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # if a and b and c:
    #     User.objects.filter(up=b).update(up=c)
    #     return HttpResponse("<p>用户头像更改成功！</p>")
    # else:
    #     return HttpResponse("<p>用户头像更改失败</p>")
    if request.method != "POST":
        return JsonResponse({"result": 0, "message": "Error"})
    data_json = json.loads(request.body)
    uid = request.session.get("id", 0)
    if uid == 0:
        return JsonResponse({"result": 0, "message": "尚未登录"})
    user = User.objects.get(uid=uid)
    oup = user.up
    nup = data_json["nup"]  ## 新昵称

    if uid and oup and nup:
        user.update(up=nup)
        JsonResponse({"result": 1, "message": "用户头像修改成功"})
    else:
        return JsonResponse({"result": 0, "message": "用户头像修改失败"})


# 管理员登录
def login_admin(request):
    # a = request.POST.get("id", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # b = request.POST.get("pwd", '')
    # if a and b:
    #     c = Administator.objects.filter(aid=a, apwd=b).count()
    #     if c:
    #         return HttpResponse("<p>管理员登录成功！</p>")
    #     else:
    #         return HttpResponse("<p>管理员登录失败！</p>")
    # else:
    #     return HttpResponse("<p>请输入正确的管理员id和密码</p>")
    if request.method == "POST":
        data_json = json.loads(request.body)

        aid = data_json["aid"]
        apwd = data_json["apwd"]

        if aid and apwd:
            if Administator.objects.filter(aid=aid).exists():  # 如果用户存在
                test1 = Administator.objects.get(aid=aid)
                if test1.apwd == apwd:
                    return JsonResponse({"result": 1, "message": "管理员登录成功"})
                else:
                    return JsonResponse({"result": 0, "message": "登陆失败，密码错误"})
            else:
                return JsonResponse({"result": 0, "message": "管理员不存在"})
        else:
            return JsonResponse({"result": 0, "message": "登录失败，请输入完整的账号和密码信息"})


def change_pwd_admin(request):
    # a = request.POST.get("id", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # b = request.POST.get("oldpwd", '')
    # c = request.POST.get("newpwd", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # if a and b and c:
    #     Administator.objects.filter(apwd=b).update(apwd=c)
    #     return HttpResponse("<p>管理员密码更改成功！</p>")
    # else:
    #     return HttpResponse("<p>管理员密码更改失败</p>")
    if request.method != "POST":
        return JsonResponse({"result": 0, "message": "Error"})
    data_json = json.loads(request.body)
    aid = request.session.get("id", 0)
    if aid == 0:
        return JsonResponse({"result": 0, "message": "尚未登录"})
    administator = Administator.objects.get(aid=aid)
    oapwd = administator.apwd
    napwd = data_json["napwd"]  ## 新昵称

    if aid and oapwd and napwd:
        administator.update(apwd=napwd)
        JsonResponse({"result": 1, "message": "管理员密码修改成功"})
    else:
        return JsonResponse({"result": 0, "message": "管理员密码修改失败"})


# 商品
def regist_clothing(request):
    # a = request.POST.get("id", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # b = request.POST.get("pid", '')
    # c = request.POST.get("pi", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # d = request.POST.get("pr", '')
    # e = request.POST.get("n", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # f = request.POST.get("num", '')
    # g = request.POST.get("de", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # h = request.POST.get("co", '')
    # if a and b and c and d and e and f and h and g:
    #     c = Clothing.objects.filter(cid=a,cpid=b,cpi=c,cpr=d,cn=e).count()
    #     if c:#如果这件衣服已经有了，数量++
    #         tmp = Clothing.objects.get(cid=a,cpid=b,cpi=c,cpr=d,cn=e).cnum
    #         Clothing.objects.filter(cid=a,cpid=b,cpi=c,cpr=d,cn=e).update(cnum=tmp+1)
    #     else:#这件衣服无库存，添加
    #         test1 = Clothing(cid=a, cpid=b,cpi=c,cpr=d,cn=e,cnum=f,cde=g,cco=h)
    #         test1.save()
    #     return HttpResponse("<p>商品上架成功！</p>")
    # else:
    #     return HttpResponse("<p>商品上架失败</p>")
    if request.method == "POST":
        data_json = json.loads(request.body)

        cid = data_json["cid"]
        cpid = data_json["cpid"]
        cpi = data_json["cpi"]
        cpr = data_json["cpr"]
        cn = data_json["cn"]
        if Clothing.objects.filter(cid=cid).exists():  # 如果此件衣服已经存在，当前数量为之前数量，否则为0
            cloth1 = Clothing.objects.get(cid=cid)
            cnum = cloth1.cnum
        else:
            cnum = 0
        cde = data_json["cde"]
        cco = data_json["cco"]

        if cid and cpid and cpi and cpr and cn and cnum and cde and cco:
            test1 = Clothing(cid=cid, cpid=cpid, cpi=cpi, cpr=cpr, cn=cn, cnum=cnum + 1, cde=cde, cco=cco)
            test1.save()
            return JsonResponse({"result": 1, "message": "衣物添加成功"})
        else:
            return JsonResponse({"result": 0, "message": "衣物添加失败，请输入完整的衣物信息"})


# 订单
def regist_order(request):
    # a = request.POST.get("id", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # b = request.POST.get("bid", '')
    # c = request.POST.get("sid", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # d = request.POST.get("cid", '')
    # e = request.POST.get("pri", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # f = request.POST.get("st", '')
    # g = request.POST.get("ti", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # h = request.POST.get("num", '')
    # if a and b and c and d and e and f and h and g:
    #     # c = Order.objects.filter(cid=a,cpid=b,cpi=c,cpr=d,cn=e).count()
    #     # if c:#如果这件衣服已经有了，数量++
    #     #     tmp = Clothing.objects.get(cid=a,cpid=b,cpi=c,cpr=d,cn=e).cnum
    #     #     Clothing.objects.filter(cid=a,cpid=b,cpi=c,cpr=d,cn=e).update(cnum=tmp+1)
    #     # else:#这件衣服无库存，添加
    #     test1 = Order(did=a, dbid=b,dsid=c,dcid=d,dpri=e,dst=f,dti=g,dnum=h)
    #     test1.save()
    #     return HttpResponse("<p>订单生成成功！</p>")
    # else:
    #     return HttpResponse("<p>订单生成失败</p>")
    if request.method == "POST":

        dbid = request.session.get("id", 0)  # 生成订单的主体id是当前登录了的用户
        if dbid == 0:
            return JsonResponse({"result": 0, "message": "尚未登录"})

        data_json = json.loads(request.body)
        global total_did
        did = total_did
        dsid = data_json["dsid"]
        dcid = data_json["dcid"]
        dst = data_json["dst"]
        dti = datetime.now()  # 时间是人为规定还是系统生成
        dnum = data_json["dnum"]
        if Clothing.objects.filter(cid=dcid).exists():  # 如果商品存在
            cloth1 = Clothing.objects.get(cid=dcid)
            dpri = cloth1.cpr * dnum  ##订单价格应该由商品价格生成
        else:
            return JsonResponse({"result": 1, "message": "要购买的商品不存在"})

        if did and dbid and dsid and dcid and dpri and dst and dti and dnum:
            test1 = Order(did=did, dbid=dbid, dsid=dsid, dcid=dcid, dpri=dpri, dst=dst, dti=dti, dnum=dnum)
            test1.save()
            total_did = total_did + 1  # 订单序号++
            return JsonResponse({"result": 1, "message": "订单生成成功"})
        else:
            return JsonResponse({"result": 0, "message": "订单生成失败，请检查订单内容是否填写完整"})
    else:
        return JsonResponse({"result": 0, "message": "Error"})


# 消息
def regist_message(request):
    # a = request.POST.get("id", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # b = request.POST.get("bid", '')
    # c = request.POST.get("sid", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # d = request.POST.get("cid", '')
    # e = request.POST.get("pri", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # f = request.POST.get("st", '')
    # if a and b and c and d and e and f:
    #     # c = Order.objects.filter(cid=a,cpid=b,cpi=c,cpr=d,cn=e).count()
    #     # if c:#如果这件衣服已经有了，数量++
    #     #     tmp = Clothing.objects.get(cid=a,cpid=b,cpi=c,cpr=d,cn=e).cnum
    #     #     Clothing.objects.filter(cid=a,cpid=b,cpi=c,cpr=d,cn=e).update(cnum=tmp+1)
    #     # else:#这件衣服无库存，添加
    #     test1 = Message(mid=a, mt=b, mr=c, ms=d, mc=e, mst=f)
    #     test1.save()
    #     return HttpResponse("<p>消息存储成功！</p>")
    # else:
    #     return HttpResponse("<p>消息存储失败</p>")
    if request.method == "POST":
        data_json = json.loads(request.body)
        global total_mid
        mid = total_mid
        mt = datetime.now()
        mr = data_json["mr"]
        ms = data_json["ms"]
        mc = data_json["mc"]
        mst = data_json["mst"]

        if mid and mt and mr and ms and mc and mst:
            test1 = Message(mid=mid, mt=mt, mr=mr, ms=ms, mc=mc, mst=mst)
            test1.save()
            return JsonResponse({"result": 1, "message": "信息发送成功"})
        else:
            return JsonResponse({"result": 0, "message": "信息失败，请确认信息是否填写完整"})


# 分享
def regist_share(request):
    # a = request.POST.get("sid", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # b = request.POST.get("spid", '')
    # c = request.POST.get("spi", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # d = request.POST.get("scid", '')
    # e = request.POST.get("sst", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # f = request.POST.get("she", '')
    # g = request.POST.get("sde", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # h = request.POST.get("sti", '')
    # i = request.POST.get("sco", '')
    # if a and b and c and d and e and f and h and g and i:
    #     # c = Order.objects.filter(cid=a,cpid=b,cpi=c,cpr=d,cn=e).count()
    #     # if c:#如果这件衣服已经有了，数量++
    #     #     tmp = Clothing.objects.get(cid=a,cpid=b,cpi=c,cpr=d,cn=e).cnum
    #     #     Clothing.objects.filter(cid=a,cpid=b,cpi=c,cpr=d,cn=e).update(cnum=tmp+1)
    #     # else:#这件衣服无库存，添加
    #     test1 = Share(sid=a, spid=b, spi=c, scid=d, sst=e, she=f, sde=g, sti=h, sco=i)
    #     test1.save()
    #     return HttpResponse("<p>分享存储成功！</p>")
    # else:
    #     return HttpResponse("<p>分享存储失败</p>")
    if request.method == "POST":

        sid = request.session.get("id", 0)  # 发布分享的主体id是当前登录了的用户
        if sid == 0:
            return JsonResponse({"result": 0, "message": "尚未登录"})

        data_json = json.loads(request.body)
        spid = data_json["spid"]
        spi = data_json["spi"]
        scid = data_json["scid"]
        sst = data_json["sst"]
        she = data_json["she"]
        sde = data_json["sde"]
        sti = datetime.now()  # 时间是人为规定还是系统生成
        sco = data_json["sco"]

        if sid and spid and spi and scid and sst and she and sde and sti and sco:
            test1 = Share(sid=sid, spid=spid, spi=spi, scid=scid, sst=sst, she=she, sde=sde, sti=sti, sco=sco)
            test1.save()
            return JsonResponse({"result": 1, "message": "发布分享成功"})
        else:
            return JsonResponse({"result": 0, "message": "发布分享失败，请检查分享内容是否填写完整"})
    else:
        return JsonResponse({"result": 0, "message": "Error"})


def del_clothing(request):
    # a = request.POST.get("id", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # b = request.POST.get("cid", '')
    # if a and b:
    #     test1 = Clothing.objects.get(cid=b)
    #     test1.delete()
    #     return HttpResponse("<p>衣物删除成功！</p>")
    # else:
    #     return HttpResponse("<p>衣物删除失败</p>")
    if request.method != "POST":
        return JsonResponse({"result": 0, "message": "Error"})
    data_json = json.loads(request.body)
    id = data_json["id"]
    cid = data_json["cid"]

    if Clothing.objects.filter(cid=cid).exists():
        cloth1 = Clothing.objects.get(cid=cid)
        cloth1.delete()
        JsonResponse({"result": 1, "message": "衣物删除成功"})
    else:
        return JsonResponse({"result": 0, "message": "要删除的衣物不存在"})


def del_share(request):
    # a = request.POST.get("id", '')  # 后面那个是默认值，如果前面为空，该处变量为后面的默认值
    # b = request.POST.get("sid", '')
    # if a and b:
    #     test1 = Share.objects.get(sid=b)
    #     test1.delete()
    #     return HttpResponse("<p>分享删除成功！</p>")
    # else:
    #     return HttpResponse("<p>分享删除失败</p>")
    if request.method != "POST":
        return JsonResponse({"result": 0, "message": "Error"})
    data_json = json.loads(request.body)
    id = data_json["id"]
    sid = data_json["cid"]

    if Share.objects.filter(sid=sid).exists():
        share1 = Share.objects.get(sid=sid)
        share1.delete()
        JsonResponse({"result": 1, "message": "分享删除成功"})
    else:
        return JsonResponse({"result": 0, "message": "要删除的分享不存在"})
