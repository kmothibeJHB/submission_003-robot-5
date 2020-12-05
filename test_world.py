import unittest
from io import StringIO
from test_base import captured_io
import world.text.world as w


class MyTestCase(unittest.TestCase):
    
    def test_is_position_allowed(self):
        for i in range(-100,100):
            for j in range(-200,200):
                self.assertTrue(w.is_position_allowed(i, j))
                
    def test_update_position(self):
        self.assertTrue(w.update_position(100))
        self.assertTrue(w.update_position(-100))
        self.assertTrue(w.update_position(0))
        # self.assertFalse(w.update_position(1000))
        self.assertFalse(w.update_position(-1000))
        
    def test_show_position(self):
        with captured_io(StringIO()) as (out, err):
            w.position_y = 0
            w.position_x = 0
            robot_name = "HAL"
            w.show_position(robot_name)

        output = out.getvalue().strip()
        self.assertEqual('> '+robot_name+' now at position (0,0).', output)
        
    
    def test_do_forward(self):
    
        self.assertTrue(w.do_forward('HAL', 10))
        self.assertEqual(' > HAL moved forward by 10 steps.',w.do_forward('HAL',10)[1])
    

    def test_do_back(self):

        self.assertTrue(w.do_back('HAL', 10))
        self.assertEqual(' > HAL moved back by 10 steps.',w.do_back('HAL', 10)[1])
    

    def test_do_right_turn(self):

        self.assertTrue(w.do_right_turn('HAL'))
        self.assertEqual(' > HAL turned right.',w.do_right_turn('HAL')[1])
    

    def test_do_left_turn(self):

        self.assertTrue(w.do_left_turn('HAL'))
        self.assertEqual(' > HAL turned left.',w.do_left_turn('HAL')[1])
    

    def test_do_sprint(self):
        with captured_io(StringIO()) as (out, err):
            name = "HAL"
            argument = 5
            w.do_sprint(name, argument)

        output = out.getvalue().strip()
        self.assertTrue(w.do_sprint('HAL', 5))
        self.assertEqual("""> HAL moved forward by 5 steps.
 > HAL moved forward by 4 steps.
 > HAL moved forward by 3 steps.
 > HAL moved forward by 2 steps.""", output)
    

    def test_do_call_command_do_replay(self):

        self.assertTrue(w.do_sprint('HAL', 5)[0])
        self.assertEqual(' > HAL moved forward by 1 steps.',w.do_sprint('HAL', 5)[1])
    