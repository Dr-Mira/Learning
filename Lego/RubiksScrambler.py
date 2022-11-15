# --------------------------------------------------------------------------------------------------
# MindCuber-Scrambler
#
# information on https://github.com/Dr-Mira/Learning/tree/main/Lego
# ---------------------------------------------------------------------------------------------------

from mindstorms import Motor, MSHub, MotorPair, ColorSensor, DistanceSensor
from mindstorms.control import wait_for_seconds
from random import choice
import gc

gc.collect()

hub = MSHub()
mot_l = Motor('F')
mot_m = Motor('D')
mot_r = Motor('B')
mot_cam = Motor('E')
color_sensor = ColorSensor('C')
distance_sensor = DistanceSensor('A')
color_sensor.light_up_all(0)

no_of_scrambles = 20


def arms_open():
    mot_l.start(70)
    mot_r.start(-70)
    wait_for_seconds(0.2)


def rotate_cube(direction):
    if direction == -1:
        mot_m.run_for_degrees(320, 80)
        mot_m.run_for_degrees(-50, 80)
    elif direction == 1:
        mot_m.run_for_degrees(-320, 80)
        mot_m.run_for_degrees(50, 80)
    wait_for_seconds(0.2)
    arms_open()


def rotate_bottom(direction):
    mot_l.start(-50)
    mot_r.start(50)
    wait_for_seconds(0.5)
    if direction == -1:
        mot_m.run_for_degrees(320, 80)
        mot_m.run_for_degrees(-51, 80)
    elif direction == 1:
        mot_m.run_for_degrees(-320, 80)
        mot_m.run_for_degrees(51, 80)
    wait_for_seconds(0.1)
    arms_open()


def cube_flip(direction):
    if direction == 1:
        mot_r.start(80)
        wait_for_seconds(0.5)
        mot_l.start(-80)
        wait_for_seconds(0.1)
        mot_r.start(-50)
    elif direction == -1:
        mot_l.start(-80)
        wait_for_seconds(0.5)
        mot_r.start(80)
        wait_for_seconds(0.1)
        mot_l.start(50)
    wait_for_seconds(0.2)
    arms_open()


def U():
    hub.light_matrix.show('00000:00000:99999:00009:99999')
    cube_flip(1)
    cube_flip(1)
    rotate_bottom(-1)


def D():
    hub.light_matrix.show('00000:00000:09990:90009:99999')
    rotate_bottom(-1)


def R():
    hub.light_matrix.show('00000:00009:09090:90900:99999')
    cube_flip(-1)
    rotate_bottom(-1)


def L():
    hub.light_matrix.show('00000:00000:00009:00009:99999')
    cube_flip(1)
    rotate_bottom(-1)


def F():
    hub.light_matrix.show('00000:00000:90000:90900:99999')
    rotate_cube(1)
    cube_flip(1)
    rotate_bottom(-1)


def B():
    hub.light_matrix.show('00000:00000:09090:90909:99999')
    rotate_cube(-1)
    cube_flip(1)
    rotate_bottom(-1)


def U_prime():
    hub.light_matrix.show('00000:55000:99999:00009:99999')
    cube_flip(1)
    cube_flip(1)
    rotate_bottom(1)


def D_prime():
    hub.light_matrix.show('00000:55000:09990:90009:99999')
    rotate_bottom(1)


def R_prime():
    hub.light_matrix.show('00000:55009:09090:90900:99999')
    cube_flip(-1)
    rotate_bottom(1)


def L_prime():
    hub.light_matrix.show('00000:55000:00009:00009:99999')
    cube_flip(1)
    rotate_bottom(1)


def F_prime():
    hub.light_matrix.show('00000:55000:90000:90900:99999')
    rotate_cube(1)
    cube_flip(1)
    rotate_bottom(1)


def B_prime():
    hub.light_matrix.show('00000:55000:09090:90909:99999')
    rotate_cube(-1)
    cube_flip(1)
    rotate_bottom(1)


def U2():
    hub.light_matrix.show('55000:55000:09090:90909:99999')
    cube_flip(1)
    cube_flip(1)
    rotate_bottom(1)
    rotate_bottom(1)


def D2():
    hub.light_matrix.show('55000:55000:09990:90009:99999')
    rotate_bottom(1)
    rotate_bottom(1)


def R2():
    hub.light_matrix.show('55000:55009:09090:90900:99999')
    cube_flip(-1)
    rotate_bottom(1)
    rotate_bottom(1)


def L2():
    hub.light_matrix.show('55000:55000:00009:00009:99999')
    cube_flip(1)
    rotate_bottom(1)
    rotate_bottom(1)


def F2():
    hub.light_matrix.show('55000:55000:90000:90900:99999')
    rotate_cube(1)
    cube_flip(1)
    rotate_bottom(1)
    rotate_bottom(1)


def B2():
    hub.light_matrix.show('55000:55000:09090:90909:99999')
    rotate_cube(-1)
    cube_flip(1)
    rotate_bottom(1)
    rotate_bottom(1)


def main():
    arms_open()
    moves = [U, D, R, L, F, B, U_prime, D_prime, R_prime, L_prime, F_prime, B_prime, U2, D2, R2, L2, F2, B2]
    sequence = list()
    for i in range(no_of_scrambles):
        a = choice(moves)
        b = a.__name__
        if b.endswith('prime'):
            b = b.strip('_prime')
            b = b + "'"
        sequence.append(b)
        print(i+1, b)
        a()
    print(', '.join(map(str, sequence)))


main()

