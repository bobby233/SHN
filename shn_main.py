# This line includes 79 characters because PEP8 says,"Limit ... 79 characters"

# 作者：bobby233 <mczsjzsjz@outlook.com>
# 版本：v0.0.1
# 更新时间：2020/10/1

"""SHN社工库的主要操作

这个文件提供了SHN社工库所需要的主要和简单操作，这些操作是组成SHN社工库的根本，
有了这些操作，SHN社工库才可以正常运转。

作为一个社工库，一定需要有大致分为三方面的操作：读取、添加和修改。一个社工库的
运转需要如下的步骤：在现实生活中获取信息->添加人物画像中的信息->在之后读取
人物的信息->及时修改信息。在第二步中，需要提供指定的项目信息，每个项目都在程序
本身的函数中有所体现；在第四步中，程序可以在某些情况下自动更新有需要的信息，
比如距离生日的天数等。

推荐使用Python 3.8运行以获取完整的、更好的体验，需要全套内置标准库。

"""

class Person:
    """人物画像类

    在这个类中，拥有添加、读取和修改的函数以提供社工库的基本操作，也拥有基本的
    信息模板

    """

    # 基本信息模板
    basics = {
        "shnid": None,
        "name": None,
        "sex": None,
        "birth": None,
        "grade": None,
        "height": None,
        "weight": None,
        "hair": None,
        "glasses": None,
        "phone": None,
        "qq_no": None,
        "qq_ps": None,
        "uid_no": None,
        "uid_ps": None
    }
    # 高级信息模板
    things = []

    def __init__(self, fromf=True, **kwargs):
        """初始化一个人物画像类
        
        可以从文件内导入或者新建画像。如果想从文件导入，fromf应为True，反之则为
        False。
        当fromf为True时，需要提供人物画像的shnid唯一编号；当fromf为False时，需要
        提供一系列的基本信息（具体参照上方基本信息模板）。
        
        """
        if fromf:
            # 读取文件信息
            with open("people.json") as p:
                from json import loads
                p = p.read()
                self.basics = loads(p)[kwargs["shnid"]]["basics"]
                self.things = loads(p)[kwargs["shnid"]]["things"]
        else:
            # 添加所有信息
            lkwargs = []
            for i in range(len(kwargs.keys())):
                if isinstance(list(kwargs.values())[i], str):
                    lkwargs.append(list(kwargs.keys())[i] + '=' + '"' +\
                        str(list(kwargs.values())[i]) + '"')
                else:
                    lkwargs.append(list(kwargs.keys())[i] + '=' +\
                        str(list(kwargs.values())[i]))
            exec("self.add_basics(" + ','.join(lkwargs) + ')')

    # 添加信息的函数由此开始

    def add_basics(self, **kwargs):
        """添加（或修改）所有的基本信息"""
        for i in range(len(kwargs.keys())):
            if list(kwargs.keys())[i] in list(self.basics.keys()):
                self.basics[list(kwargs.keys())[i]] =\
                    kwargs[list(kwargs.keys())[i]]
            else:
                print(list(kwargs.keys())[i] + "不在基本信息模板中。")
    def add_things(self, *args):
        """添加（或修改）所有的事件信息"""
        for i in args:
            self.things.append(args[i])

    # 读取信息操作由此开始

    def show_basics(self):
        """以特定格式读取基本信息，并显示完成度"""
        print("BASICS:")
        comp = 0
        for i in range(len(self.basics)):
            print("\t- " + list(self.basics.keys())[i] + ": " +\
                str(self.basics[list(self.basics.keys())[i]]))
            if self.basics[list(self.basics.keys())[i]] != None:
                comp += 1
        print("完成度：" + ("%.1f%%")%(comp/len(self.basics)*100))

def read_db(file="people.json"):
    """读取整个数据库"""
    with open(file) as f:
        from json import load
        return load(f)
def init_db(file="people.json"):
    """使用普通模板初始化数据库"""
    temp = {"T000": None}
    with open(file, 'w') as f:
        from json import dump
        dump(temp, f)
    print("初始化完成，文件为" + file)
def write_db(people: list, file="people.json"):
    """更改社工库的信息，需要提供人物画像列表"""
    db = {}
    print("整合人物画像为整个社工库……", end='')
    for i in range(len(people)):
        db[people[i].basics["shnid"]] = {
            "basics": people[i].basics,
            "things": people[i].things,
        }
    print("完成")
    print("写入文件……", end='')
    with open(file, 'w') as f:
        from json import dump
        dump(db, f)
    print("完成")
def modify_db(person: Person, file="people.json"):
    """更简单和精确的更改"""
    with open(file, 'r') as f:
        from json import load, dump
        db = load(f)
    with open(file, 'w') as f:
        db[person.basics["shnid"]]["basics"] = person.basics
        db[person.basics["shnid"]]["things"] = person.things
        dump(db, f)
def search_basic(file="people.json", **kwargs):
    """在数据库中查找基本信息，需要提供一系列的关键词"""
    with open(file) as f:
        from json import load
        db: dict = load(f)
    # 仅提取指定项非None的人物
    people = {}
    kwk = list(kwargs.keys())
    for i in range(len(db)):
        dbv = list(db.values())[i]["basics"]
        for j in range(len(kwk)):
            # 生日、号码专用搜索（使用正则）
            if kwk[j] in ("birth", "phone", "qq_no", "qq_ps", "uid_no", "uid_ps"):
                from re import fullmatch
                if fullmatch(kwargs[kwk[j]], str(dbv[kwk[j]])):
                    if dbv["shnid"] not in people.keys():
                        people[dbv["shnid"]] = 1
                    else:
                        people[dbv["shnid"]] += 1
            else:
                if dbv[kwk[j]] == kwargs[kwk[j]]:
                    if dbv["shnid"] not in people.keys():
                        people[dbv["shnid"]] = 1
                    else:
                        people[dbv["shnid"]] += 1
    # 排序后总结输出结果
    people = sorted(people.items(), key=lambda x:x[1], reverse=True)
    if people != []:
        print("以下人物符合搜索标准：")
        for i in range(len(people)):
            for j in range(len(db[people[i][0]]["basics"])):
                print("- " + list(db[people[i][0]]["basics"].keys())[j] + ": " +\
                    str(list(db[people[i][0]]["basics"].values())[j]))
            print("匹配度：%0.1f%%"%(people[i][1]/len(kwargs)*100) + '\n')
    else:
        print("没有人物符合搜索标准。")

####################### TEST AREA ###########################
