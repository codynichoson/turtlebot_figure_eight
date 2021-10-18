#!/usr/bin/env python

import numpy as np
import sympy as sym


class trajectory():
    def __init__(self, W, H, T):
        self.t = sym.symbols('t')

        self.x = (W/2)*sym.sin(2*sym.pi*self.t/T)
        self.xdot = self.x.diff(self.t)
        self.xddot = self.xdot.diff(self.t)

        self.y = (H/2)*sym.sin(4*sym.pi*self.t/T)
        self.ydot = self.y.diff(self.t)
        self.yddot = self.ydot.diff(self.t)

    def lin_vel(self, time):
        v = sym.sqrt(self.xdot**2 + self.ydot**2)
        lin_vel_func = sym.lambdify(self.t,v)
        return lin_vel_func(time)

    def ang_vel(self, time):
        theta = sym.atan(self.ydot/self.xdot)
        thetadot = theta.diff(self.t)
        ang_vel_func = sym.lambdify(self.t,thetadot)
        return ang_vel_func(time)

    def theta0(self, time):
        theta = sym.atan(self.ydot/self.xdot)
        ang_func = sym.lambdify(self.t, theta)
        theta0 = ang_func(0)
        return theta0

    def x_test(self):
        x_func = sym.lambdify(self.t, self.x)
        return x_func(0)

    def y_test(self):
        y_func = sym.lambdify(self.t, self.y)
        return y_func(0)

    def xdot_test(self):
        xdot_func = sym.lambdify(self.t, self.xdot)
        return xdot_func(0)

    def ydot_test(self):
        ydot_func = sym.lambdify(self.t, self.ydot)
        return ydot_func(0)

    def xddot_test(self):
        xddot_func = sym.lambdify(self.t, self.xddot)
        return xddot_func(0)

    def yddot_test(self):
        yddot_func = sym.lambdify(self.t, self.yddot)
        return yddot_func(0)

if __name__ == "__main__":
    traj = trajectory(1,1,10)
    print(traj.x_test())