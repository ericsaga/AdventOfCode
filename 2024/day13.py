from day_base import Day
from math import isclose

def calculate_A(da,db,t,B):
    return (t-db*B)/da

def calculate_B1(da1,db1,t1,da2,db2,t2):
    return (t2-(da2*t1/da1))/(db2-(db1*da2/da1))

def calculate_B2(da1,db1,t1,da2,db2,t2):
    return (t1-(da1*t2/da2))/(db1-(db2*da1/da2))
TOL = 0.01

class Day13(Day):

    def __init__(self):
        super().__init__(2024, 13, 'Claw Contraption', debug = False, expected_a=480)
        
    def part_a(self):
        a_lines,b_lines,total_lines = self.input[::4],self.input[1::4],self.input[2::4]
        a_buttons = [ (int(x.split('X+')[-1].split(', Y')[0]),int(x.split(', Y+')[-1])) for x in a_lines]
        b_buttons = [ (int(x.split('X+')[-1].split(', Y')[0]),int(x.split(', Y+')[-1])) for x in b_lines]
        totals = [ (int(x.split('X=')[-1].split(', Y')[0]),int(x.split(', Y=')[-1])) for x in total_lines]

        tokens = 0
        for a_group,b_group,total_values in zip(a_buttons,b_buttons,totals):
            da1,da2 = a_group
            db1,db2 = b_group
            t1,t2 = total_values
            B1 = calculate_B1(da1,db1,t1,da2,db2,t2)
            if isclose(B1, round(B1),abs_tol=TOL):
                B1 =round(B1)
                A1 = calculate_A(da1, db1, t1, B1)
                if isclose(A1, round(A1),abs_tol=TOL):
                    A1 = round(A1)
                    if A1*da1+B1*db1 == t1:
                        tokens += 3*A1+B1



        return tokens

    def part_b(self):
        a_lines, b_lines, total_lines = self.input[::4], self.input[1::4], self.input[2::4]
        a_buttons = [(int(x.split('X+')[-1].split(', Y')[0]), int(x.split(', Y+')[-1])) for x in a_lines]
        b_buttons = [(int(x.split('X+')[-1].split(', Y')[0]), int(x.split(', Y+')[-1])) for x in b_lines]
        totals = [(10000000000000+int(x.split('X=')[-1].split(', Y')[0]), 10000000000000+int(x.split(', Y=')[-1])) for x in total_lines]

        tokens = 0
        for a_group, b_group, total_values in zip(a_buttons, b_buttons, totals):
            da1, da2 = a_group
            db1, db2 = b_group
            t1, t2 = total_values
            B1 = calculate_B1(da1, db1, t1, da2, db2, t2)
            if isclose(B1, round(B1), abs_tol=TOL):
                B1 = round(B1)
                A1 = calculate_A(da1, db1, t1, B1)
                if isclose(A1, round(A1), abs_tol=TOL):
                    A1 = round(A1)
                    B2 = calculate_B2(da1, db1, t1, da2, db2, t2)
                    if isclose(B2, round(B2), abs_tol=TOL):
                        B2 = round(B2)
                        A2 = calculate_A(da2, db2, t2, B2)
                        if isclose(A2, round(A2), abs_tol=TOL):
                            A2 = round(A2)
                            if A1 * da1 + B1 * db1 == t1 and A2 * da2 + B2 * db2 == t2:
                                tokens += 3 * A1 + B1
        return tokens






if __name__ == '__main__':
    (Day13()).run()

