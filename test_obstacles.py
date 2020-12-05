import unittest
from io import StringIO
from test_base import captured_io
import world.obstacles as obstacles


class MyTestCase(unittest.TestCase):

    def test_get_obstacles(self):
        
        list_of_obstacles = obstacles.get_obstacles()
        self.assertTrue(0 <= len(list_of_obstacles) <= 10)

    
    def test_is_position_blocked(self):

        list_of_obstacles = obstacles.get_obstacles()
        for i in list_of_obstacles:
            for j in range(i[0], i[0]+4):
                for k in range(i[1], i[1]+4):
                    input_x, input_y = j, k
                    self.assertFalse(obstacles.is_position_blocked(input_x,input_y))
    
    
    def test_is_path_blocked(self):

        list_of_obstacles = obstacles.get_obstacles()
        for i in list_of_obstacles:
            for j in range(i[0], i[0]+4):
                for k in range(i[1], i[1]+4):
                    input_x, input_y = j, k
                    self.assertFalse(obstacles.is_path_blocked(input_x, input_y, input_x, input_y))


    def test_print_obstacles(self):
        
        with captured_io(StringIO()) as (out, err):
            obstacles.print_obstacles()
        
        output = out.getvalue().strip()
        self.assertEqual("", output[:26])