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

@csrf_exempt
def regist_user(request):
    if request.method == "POST":
        data_json = json.loads(request.body)

        uid = data_json["uid"]
        upwd = data_json["upwd"]
        un = data_json["un"]
        up = data_json.get('up', '')  # 注册时输入头像可能为空

        if uid and upwd and un:  # 注册时头像为空并不影响进入注册函数
            if Administator.objects.filter(aid=uid).exists():  # 如果该id已由管理员使用，则无法注册
                return JsonResponse({"uid": uid, "un": un, "up": up, "result": 0, "message": "注册失败，该id已被管理员注册"})
            elif User.objects.filter(uid=uid).exists():  # 如果该id已经被其他用户使用，则无法注册
                return JsonResponse(
                    {"uid": uid, "un": un, "up": up, "result": 1, "message": "注册失败，该id已被其他用户注册"})
            else:  # 可以注册
                test1 = User(uid=uid, upwd=upwd, un=un, up=up)
                test1.save()
                return JsonResponse({"uid": uid, "un": un, "up": up, "result": 2, "message": "用户注册成功"})
        else:
            return JsonResponse({"uid": uid, "un": un, "up": up, "result": 3, "message": "注册失败，请输入完整的注册信息"})


@csrf_exempt
def regist_admin(request):
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
def login(request):
    if request.method == "POST":
        data_json = json.loads(request.body)

        id = data_json["uid"]
        pwd = data_json["upwd"]

        if id and pwd:
            if Administator.objects.filter(aid=id).exists():  # 如果该账号是管理员账号，则进入管理员登录判断
                test1 = Administator.objects.get(aid=id)
                an = test1.an
                if test1.apwd == pwd:
                    return JsonResponse({"uid": id, "un": an, "up": '', "result": 3, "message": "管理员登录成功"})  ## 如果是管理员的话，随便返回一个作为头像
                else:
                    return JsonResponse({"uid": id, "un": an, "up": '', "result": 2, "message": "管理员登陆失败，密码错误"})
            elif User.objects.filter(uid=id).exists():  # 如果该账号是用户账号，则进入用户登录判断
                test1 = User.objects.get(uid=id)
                up = test1.up
                un = test1.un
                if test1.upwd == pwd:
                    return JsonResponse({"uid": id, "un": un, "up": up, "result": 1, "message": "用户登录成功"})
                else:
                    return JsonResponse({"uid": id, "un": un, "up": up, "result": 0, "message": "用户登陆失败，密码错误"})
            else:
                return JsonResponse({"uid": id, "un": '', "up": '', "result": 4, "message": "您输入的账号和密码在系统中不存在"})
        else:
            return JsonResponse({"result": 5, "message": "登录失败，请输入完整的账号和密码信息"})  # 实际不处理输入有空的情况，不做修改

@csrf_exempt
def change_pwd_user(request):
    if request.method == "POST":
        data_json = json.loads(request.body)
        uid = data_json["uid"]
        oldpwd = data_json["oldpwd"]
        newpwd = data_json["newpwd"]  # 新密码
        if not User.objects.filter(uid=uid).exists():  # 如果要改密码的用户id并不存在
            return JsonResponse(
                {"uid": uid, "result": 0, "message": "修改失败，您输入的用户账号在系统中不存在"})
        else:
            user = User.objects.get(uid=uid)
            if user.upwd == oldpwd:
                user.update(upwd=newpwd)
                JsonResponse({"uid": uid, "result": 1, "message": "用户密码修改成功"})
            else:
                return JsonResponse(
                    {"uid": uid, "result": 2, "message": "修改失败，您输入的旧密码错误"})


@csrf_exempt
# 修改用户昵称
def change_n_user(request):
    if request.method == "POST":
        data_json = json.loads(request.body)
        uid = data_json["uid"]
        nun = data_json["nun"]  ## 新昵称
        if not User.objects.filter(uid=uid).exists():  # 如果要改昵称的用户id并不存在
            return JsonResponse(
                {"uid": uid, "result": 0, "message": "修改失败，您输入的用户账号在系统中不存在"})
        else:
            user = User.objects.get(uid=uid)
            user.update(un=nun)
            JsonResponse({"uid": uid, "result": 1, "message": "用户昵称修改成功"})


@csrf_exempt
def change_p_user(request):
    if request.method == "POST":
        data_json = json.loads(request.body)
        uid = data_json["uid"]
        nup = data_json["nup"]  # 新头像
        if not User.objects.filter(uid=uid).exists():  # 如果要改昵称的用户id并不存在
            return JsonResponse(
                {"uid": uid, "result": 0, "message": "修改失败，您输入的用户账号在系统中不存在"})
        else:
            user = User.objects.get(uid=uid)
            user.update(up=nup)
            JsonResponse({"uid": uid, "result": 1, "message": "用户头像修改成功"})



@csrf_exempt
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


@csrf_exempt
# 商品
def regist_clothing(request):
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


@csrf_exempt
# 订单
def regist_order(request):
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


@csrf_exempt
# 消息
def regist_message(request):
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


@csrf_exempt
# 分享
def regist_share(request):
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


@csrf_exempt
def del_clothing(request):
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


@csrf_exempt
def del_share(request):
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
