"""
模拟注册，登录
"""
# 登录
import pymysql


class LoginRegister:

    def __init__(self):
        self.db = pymysql.connect(user='root',
                                  password='123456',
                                  database='stu',
                                  charset='utf8')
        self.cur = self.db.cursor()

    def login(self, user, password):
        sql = "select user,passsword from user where user = %s and passsword = %s;"
        self.cur.execute(sql, [user, password])
        one_row = self.cur.fetchone()
        if one_row:
            print('登录成功')
            return
        print('你还没有注册，正在帮你注册！')
        self.register(user, password)

    def register(self, user, password):
        sql = "select user from user where user = %s;"
        self.cur.execute(sql, [user])
        r = self.cur.fetchone()
        if r:
            return
        sql = "insert into user values (%s, %s);"
        try:
            self.cur.execute(sql, [user, password])
            self.db.commit()
        except:
            self.db.rollback()
            print('注册失败')
            return
        self.cur.close()
        self.db.close()
        print('注册成功，请登录')


if __name__ == '__main__':
    user = input('请输入用户名：')
    password = input('请输入密码：')
    login = LoginRegister()
    login.login(user, password)
    # login.register(user, password)















