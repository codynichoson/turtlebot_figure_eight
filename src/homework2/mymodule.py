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

