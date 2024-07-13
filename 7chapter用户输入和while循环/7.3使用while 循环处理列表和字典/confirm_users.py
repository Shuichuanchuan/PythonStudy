# ⾸先，创建⼀个待验证⽤户列表
# 和⼀个⽤于存储已验证⽤户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个⽤户，直到没有未验证⽤户为⽌
# 将每个经过验证的⽤户都移到已验证⽤户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# 显⽰所有的已验证⽤户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())