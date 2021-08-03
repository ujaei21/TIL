exit_angle = int(input('발사각도(1~90) : '))
exit_vel = int(input('발사속도 : '))
# 중력가속도
g=9.8
from math import sin, radians


if exit_angle > 0:
    # 호도법으로 변환
    trans_angle = radians(exit_angle)
    # 초속으로 변환
    trans_vel = exit_vel / 3.6
    # 최대고도
    max_attitude = trans_vel ** 2 * sin(trans_angle) ** 2 / (2 * g)
    # 비거리
    r = trans_vel ** 2 / g * sin(trans_angle)

else:
    pass




print('발사각도: {0: 2d} 도 \n출구속도: {1:3d} km\n 비거리 : {2: 3.0f} m '.format(exit_angle,exit_vel,r))
print('최대고도 : {0:3.2f} m'.format(max_attitude))