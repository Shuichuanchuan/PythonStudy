# 使用get()访问值
alien_0 = {'color': 'green', 'speed': 'slow'} 

point_value = alien_0.get('points',
                          'No point value assined')

print(point_value)