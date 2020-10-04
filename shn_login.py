# This line includes 79 characters because PEP8 says,"Limit ... 79 characters"

# 作者：bobby233 <mczsjzsjz@outlook.com>
# 版本：v0.0.1
# 更新时间：2020/9/30

"""SHN社工库的登录操作

这个文件提供了一系列的登录操作，这些操作需要使用其他文件（例如SHN.py）调用才可以使用。这些
函数不使用少量模块，大多为自己编写的代码，此文件完全开源，允许其他开发者进行调用、改进和重写。
如果时间和技术允许，本文件将会持续优化算法和代码规范性，使得文件具有更强的可读性和更高的性能。

"""

class User:
    """只要和程序交互的，都是用户(User)，在这个文件中必须铭记

    一个用户，顾名思义，当然是需要使用这个程序的，而这个程序十分讲究权限的使用，就分为了
    管理员(Admin)、参与者(Joiner)和游客(Guest)。这样可以更简单地管理用户的不同操作。
    所有关于管理员、参与者和游客的信息，请参见各个类，如class Admin(User)。

    用户必须要拥有密码才可以管理自己的权限，包括游客亦是如此，因为社工库十分讲究隐私的重要性。
    想要创建一个合格的用户类，需要三个参数，一个必须提供，两个可选。其一是密码，这是一定需要的
    参数，有了密码，才可以保证自己的访问记录和隐私的安全；其二是账号，这是可选的参数，可以
    使用自己的账号，也可以使用自动生成的账号，但这是不可以更改的；其三是昵称，这也是可选的，
    如果不填入的话，将会由电脑自动生成一个形如"Guest000"的昵称，如果认为自己的昵称不是很好，
    可以自行更改。

    有了以上的参数，一个合格的用户类就创建了，可以随时调用里面的数据和函数，函数文档参见各个
    函数的文档。

    """

    # 临时存放用户的信息
    info = {}
    # 临时存放数据库信息
    db = {}

    def __init__(self, password, username=None, nickname=None):
        """见类文档正文第三段"""
        # 检查是否有已经存储的用户文件
        try:
            with open("user_info.json") as i:
                from json import load
                self.info = load(i)
        except FileNotFoundError:
            while True:
                if username:
                    self.info["username"] = username
                    if nickname:
                        self.info["nickname"] = nickname
                    else:
                        self.info["nickname"] = self.rand_nickname()
                else:
                    self.info["username"] = self.rand_username()
                # 检查是否重名
                if not self.check():
                    print("用户名或昵称重复，请更改！")
                    continue
                self.info["password"] = password
                break

    def rand_nickname(self, type_="rnick"):
        """如果没有提供昵称时，随机返回昵称"""
        # 打开用户信息文件查看
        try:
            with open("user_info.json") as i:
                from json import load
                self.db = load(i)
        except FileNotFoundError:
            return "shnid000"
        else:
            return "shnid" + str(self.db["const"][type_]+1)
    
    def rand_username(self):
        """如果没有提供用户名时，随机返回用户名"""
        # rand_nickname的衍生版
        self.rand_nickname("ruser")