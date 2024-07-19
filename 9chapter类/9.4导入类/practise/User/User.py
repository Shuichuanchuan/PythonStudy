class User:
    """模拟用户信息"""

    def __init__(self, first_name, last_name, age, email):
        """初始化用户信息"""
        self.firstname = first_name
        self.lastname = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        full_name = self.firstname + self.lastname
        print("用户信息：")
        print(f"name: {full_name}")
        print(f"age: {self.age}")
        print(f"e-mail: {self.email}")

    def greet_user(self):
        full_name = self.firstname + self.lastname
        print(f"Hello, {full_name}")

    def increment_login_attempts(self):
        """将属性login_attempts 的值加 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """将属性login_attempts 的值重置为 0"""
        self.login_attempts = 0

    def show_login_attempts(self):
        """打印等登录次数"""
        print("登录次数是:")
        print(self.login_attempts)


class Admin(User):
    """管理员类"""

    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges()


class Privileges:

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """打印管理员的权限"""
        for privilege in self.privileges:
            print(privilege)