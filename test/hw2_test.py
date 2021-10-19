import unittest
import homework2.trajectory_calcs
import sympy as sym
from numpy import pi

W = 1
H = 1
T = 10
traj = homework2.trajectory_calcs.trajectory(W,H,T)

class GettingTesty(unittest.TestCase):
    
    def test_x(self):
        global traj
        self.assertEquals(traj.x_test(), 0)

    def test_y(self):
        global traj
        self.assertEquals(traj.y_test(), 0)
    
    def test_xdot(self):
        global traj
        self.assertEquals(traj.xdot_test(), pi/10)
    
    def test_ydot(self):
        global traj
        self.assertEquals(traj.ydot_test(), pi/5)

    def test_xddot(self):
        global traj
        self.assertEquals(traj.xddot_test(), 0)

    def test_yddot(self):
        global traj
        self.assertEquals(traj.yddot_test(), 0)

    def test_v(self):
        global traj
        self.assertEquals(traj.v_test(), 0)

    def test_w(self):
        global traj
        self.assertEquals(traj.w_test(), 0)

if __name__ == "__main__":
    import rosunit
    rosunit.unitrun(homework2, 'test_class_name', GettingTesty)
