import sys
import getopt
import requests

print('''
 __  __  ___                   _       _____           _ 
|  \/  |/ _ \ _   _ _ __ _ __ ( )___  |_   _|__   ___ | |
| |\/| | | | | | | | '__| '_ \|// __|   | |/ _ \ / _ \| |
| |  | | |_| | |_| | |  | | | | \__ \   | | (_) | (_) | |
|_|  |_|\___/ \__,_|_|  |_| |_| |___/   |_|\___/ \___/|_|
''')
print("[=v=]随便写的QQ和微博id查绑定手机号的小工具，数据来自于公开的api接口，不保证准确性，仅作为参考。")
print("=======================================================================================")
url = "https://zy.xywlapi.cc/"
headers = {
    'User-Agent': 'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36(KHTML, like Gecko) Chrome/52 .0.2743. 116 Safari/537.36'
}


def qq2phone(qq):
    # qq = input("请输入想查询的QQ号：")
    print("\n[-]QQ数据查询中...")
    res = requests.post(url=url + "qqapi", headers=headers, data="qq=" + qq)
    # print(res.text)
    raw = res.json()
    if raw['status'] == 200:
        print("\n=============================")
        print("[!]QQ数据查询成功！")
        print("[+]QQ号：" + raw['qq'])
        print("[+]手机号：" + raw['phone'])
        print("[+]归属地：" + raw['phonediqu'])
        print("=============================")
    else:
        print("[×]暂无该qq号对应数据！")


def weibo2phone(weiboid):
    # qq = input("请输入想查询的weiboid：")
    print("\n[-]微博数据查询中...")
    res = requests.post(url=url + "wbapi", headers=headers, data="id=" + weiboid)
    # print(res.text)
    raw = res.json()
    if raw['status'] == 200:
        print("\n=============================")
        print("[!]微博数据查询成功！")
        print("[+]微博id：" + raw['id'])
        print("[+]手机号：" + raw['phone'])
        print("[+]归属地：" + raw['phonediqu'])
        print("=============================")
    else:
        print("[×]暂无该微博id对应数据！")


def help_msg():
    print('''示例：
                python ./old_version.py -q [qq号] -w [微博id]
                或
                python ./old_version.py --qq [qq号] --weibo [微博id]
                ''')


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hq:w:", ["help", "qq=", "weibo="])
    except getopt.GetoptError:
        print("[×]参数错误！")
        help_msg()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            help_msg()
        elif opt in ("-q", "--qq"):
            qq = arg
            qq2phone(qq)
        elif opt in ("-w", "--weibo"):
            weiboid = arg
            weibo2phone(weiboid)
        else:
            print("[×]参数错误！")
            help_msg()


if __name__ == '__main__':
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。
    main(sys.argv[1:])
