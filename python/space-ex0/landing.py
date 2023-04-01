import math

from pid import PID
from moon import Moon
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from scipy.optimize import LinearConstraint
from scipy import optimize

class Landing(object):
    WEIGHT_EMP = 165.0
    WEIGHT_FULE = 420.0
    WEIGHT_FULL = WEIGHT_EMP + WEIGHT_FULE
    MAIN_ENG_F = 430.0
    SECOND_ENG_F = 25.0
    MAIN_BURN = 0.15
    SECOND_BURN = 0.009
    ALL_BURN = MAIN_BURN + 8 * SECOND_BURN

    @classmethod
    def accMax(cls, weight):
        return cls.acc(weight, True, 8)

    @classmethod
    def acc(cls, weight, main, seconds):
        t = 0
        if main:
            t += cls.MAIN_ENG_F
        t += seconds * cls.SECOND_ENG_F
        ans = t / weight
        return ans

    def land(self, a):  # TARGET_VS = 23.0, MAX_ANG = 70.0, MIN_ANG = 50.0):

        TARGET_VS = a[0]
        MIN_ANG = a[1]
        MAX_ANG = a[2]
        FINAL_ALT = a[3]
        INTEGRAL_VS = 0.35
        INTEGRAL_HS = 0.35
        LANDING_TARGET_VS = a[4]

        dist = 181 * 1000.0

        time = 0.0
        dt = 1
        acc = 0.0
        fuel = 121.0
        weight = self.WEIGHT_EMP + fuel
        NN = 0.7

        # FINAL_ALT = 2000.0
        TARGET_HS_FINAL_ALT = 100.0

        vs = 24.8
        hs = 932.0
        alt = 13748.0
        ang = 58.3

        VS_PID = PID(0.7, INTEGRAL_VS, 0.05, 300)
        HS_PID = PID(0.7, INTEGRAL_HS, 0.05, 300)

        ANG_PID = PID(1, 0.1, 0.01, 10)

        data_vs = []
        data_hs = []
        data_alt = []
        data_ang = []
        data_fuel = []

        need_plot = True

        print("alt,time,vs,hs,dist,ang,weight,acc,fuel")
        while True:

            if time % 1 == 0:
               print("{},{},{},{},{},{},{},{},{}".format(alt, time, vs, hs, dist, ang, weight, acc, fuel))

            data_vs.append(vs)
            data_hs.append(hs)
            data_alt.append(alt)
            data_ang.append(ang)
            data_fuel.append(fuel)

            landed_ok = hs <= 0.5 and hs >= -0.5 and alt < 0.8 and alt > -0.8 and vs < 2 and vs > -2
            #
            if alt < -2:
                return np.inf
            #
            # if hs <= 0:
            #     con = alt>=0 and hs >= -0.5  and alt>350 and fuel > 28 and alt < 1000
            #     if con:
            #         print((fuel, alt, vs, hs, a))
            #         return -alt
            #     return np.inf

            if landed_ok:
                if need_plot:
                    fig = plt.figure(1)
                    fig.suptitle("ALT")
                    plt.plot(data_alt, label='alt')
                    fig = plt.figure(2)
                    fig.suptitle("VS")

                    plt.plot(data_vs, label='vs')
                    fig = plt.figure(3)
                    fig.suptitle("HS")

                    plt.plot(data_hs, label='hs')
                    fig = plt.figure(4)
                    fig.suptitle("ANG")

                    plt.plot(data_ang, label='ang')

                    fig = plt.figure(5)
                    fig.suptitle("FUEL")
                    plt.plot(data_fuel, label='ang')

                    plt.show()
                if fuel > 26:
                    print((fuel, alt, vs, hs, a))
                return -(fuel)

            if hs <= 0:
                if alt < 100:
                    TARGET_VS = PID.constrain(alt / 5 * 1 / 10, 0, 3)
                else:
                    TARGET_VS = LANDING_TARGET_VS

            target_hs = alt * TARGET_HS_FINAL_ALT / FINAL_ALT
            error_hs = hs - target_hs
            error_vs = vs - TARGET_VS
            out_pid_vs = VS_PID.update(error_vs, dt)
            out_pid_hs = HS_PID.update(error_hs, dt)

            diff_percent_pid_vs = PID.normalize(-5, 20, out_pid_vs, 0, 2)
            diff_percent_pid_hs = PID.normalize(-200, 400, out_pid_hs, 0, 1)

            final_ang_hs = (MAX_ANG - MIN_ANG) * diff_percent_pid_hs + MIN_ANG
            final_ang_vs = (MAX_ANG - MIN_ANG) * (1 - diff_percent_pid_vs) + MIN_ANG

            angle_change_per_sec = 3

            if hs <= 0:
                wanted_ang = PID.constrain(ang - angle_change_per_sec * dt, 0, MAX_ANG)
                MIN_ANG = 0
            else:
                wanted_ang = (final_ang_hs + final_ang_vs) / 2

            error_wanted_ang = ang - wanted_ang
            pid_error_ang = ANG_PID.update(error_wanted_ang, dt)
            ang = PID.constrain(ang - pid_error_ang, MIN_ANG, MAX_ANG)

            landing_position = False
            if hs <= 0 and ang >= 0.5:
                NN = 0
            elif hs <= 0:
                NN = diff_percent_pid_vs
                if not landing_position:
                    landing_position = True
                    ANG_PID.reset()
                    VS_PID.reset()
            else:
                NN = (diff_percent_pid_hs + diff_percent_pid_vs) / 2

            ang_rad = math.radians(ang)
            h_acc = math.sin(ang_rad) * acc
            v_acc = math.cos(ang_rad) * acc
            vacc = Moon.getAcc(hs)
            time += dt

            dw = dt * self.ALL_BURN * NN
            if fuel > 0:
                fuel -= dw
                weight = self.WEIGHT_EMP + fuel
                acc = NN * self.accMax(weight)
            else:
                acc = 0
                return np.inf

            v_acc -= vacc;
            if hs > 0:
                hs -= h_acc * dt;  # TODO: return to oroginal
            dist -= hs * dt;
            vs -= v_acc * dt;
            alt -= dt * vs;


if __name__ == "__main__":
    from scipy.optimize import Bounds

    bounds = Bounds([20, 45, 70, 3000, 5], [30, 60, 80, 4000, 40])

    l = Landing()
    #x0 = np.array([25, 4.575e+01, 7.885e+01, 2.000e+03, 5])
    # res = minimize(l.land, x0, method='trust-constr', jac=None, hess=None,
    #               constraints=None,
    #           options={'verbose': 1}, bounds=bounds)
    #results = dict()
    # results['shgo'] = optimize.shgo(l.land, bounds, iters=4)
    # print(results['shgo'])

    print(Landing().land([30., 45., 80., 3500., 22.5]))
