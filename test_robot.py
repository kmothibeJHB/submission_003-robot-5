import sys
import robot
import unittest
import robot
from io import StringIO
from world.text import world
from unittest.mock import patch
from test_base import captured_io

class MyTestCase(unittest.TestCase):

    def test_get_robot_name(self):
        with captured_io(StringIO('HAL\njump\n')) as (out, err):
            robot.get_robot_name()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot?""", output)
    

    def test_get_command(self):
        with captured_io(StringIO('jump\noff\n')) as (out, err):
            robot.get_command("HAL")

        output = out.getvalue().strip()
        self.assertEqual("""HAL: What must I do next? HAL: Sorry, I did not understand 'jump'.\nHAL: What must I do next?""", output)

    
    def test_spit_command_input(self):
        
        self.assertEqual('forward', robot.split_command_input("forward 10")[0])
        self.assertEqual('back', robot.split_command_input("back 10")[0])
        self.assertEqual('right', robot.split_command_input("right")[0])
        self.assertEqual('left', robot.split_command_input("left")[0])
        self.assertEqual('sprint', robot.split_command_input("sprint 10")[0])


    def test_is_int(self):
        lst_true = ['5', '42', '1', '90', '100']
        lst_false = ['5 time', 'is it the answer 42', 'one 1', 'nineteen 90', 'two 100']
        for i in lst_true:
            self.assertTrue(robot.is_int(i))
        for j in lst_false:
            self.assertFalse(robot.is_int(j))

    
    def test_valid_command(self):
        input_commands = ["forward 10", "back 2", "right", "off", "help", "sprint 10", "replay reversed"]
        invalid_input_commands = ["go 10", "bacck 2", "rights", "offs", "helping", "sprinting 10", "replaying reversed"]
                
        for command in input_commands:
            self.assertTrue(robot.valid_command(command))

        for command in invalid_input_commands:
            self.assertFalse(robot.valid_command(command))


    def test_output(self):
        with captured_io(StringIO()) as (out, err):
            name = "HAL"
            message = "message received"
            robot.output(name,message)

        output = out.getvalue().strip()
        self.assertEqual("HAL: message received", output)

    
    def test_do_help(self):

        self.assertTrue(robot.do_help()[0])
        self.assertEqual("""I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
""", robot.do_help()[1])


    def test_get_commands_history(self):
        robot.commands_to_replay = ["forward 10", "right", "forward 5", "sprint 5" ]
        self.assertEqual([], robot.get_commands_history(False, 0, -1))
    
    def test_update_position(self):
        self.assertTrue(robot.update_position(0))


    def test_do_replay(self):
        with captured_io(StringIO()) as (out, err):
            name = "HAL"
            arguments = 'reversed'
            robot.do_replay(name, arguments)

        output = out.getvalue().strip()

        self.assertEqual("", output)
        self.assertTrue(robot.do_replay("HAL", "reversed"))


    def test_call_command_help(self):
        self.assertTrue(robot.call_command('help', '', 'HAL')[0])
        self.assertEqual("""I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
""",
robot.call_command('help', '', 'HAL')[1])

    def test_do_call_command_do_forward(self):

        self.assertTrue(robot.call_command('forward', 10, 'HAL'))
        self.assertEqual(' > HAL moved forward by 10 steps.',robot.call_command('forward', 10, 'HAL')[1])
    

    def test_do_call_command_do_forward(self):

        self.assertTrue(robot.call_command('forward', 10, 'HAL'))
        self.assertEqual(' > HAL moved forward by 10 steps.',robot.call_command('forward', 10, 'HAL')[1])
    

    def test_do_call_command_do_back(self):

        self.assertTrue(robot.call_command('back', 10, 'HAL'))
        self.assertEqual(' > HAL moved back by 10 steps.',robot.call_command('back', 10, 'HAL')[1])
    

    def test_do_call_command_do_right(self):

        self.assertTrue(robot.call_command('right', '', 'HAL'))
        self.assertEqual(' > HAL turned right.',robot.call_command('right', '', 'HAL')[1])
    

    def test_do_call_command_do_left(self):

        self.assertTrue(robot.call_command('left', '', 'HAL'))
        self.assertEqual(' > HAL turned left.',robot.call_command('left', '', 'HAL')[1])
    

    def test_do_call_command_do_sprint(self):
        with captured_io(StringIO()) as (out, err):
            name = "HAL"
            argument1 = "sprint"
            argument2 = 5
            robot.call_command(argument1, argument2, name)

        output = out.getvalue().strip()
        self.assertTrue(robot.call_command('spirnt', 5, 'HAL'))
        self.assertEqual("""> HAL moved forward by 5 steps.
 > HAL moved forward by 4 steps.
 > HAL moved forward by 3 steps.
 > HAL moved forward by 2 steps.""", output)
    

    def test_do_call_command_do_replay(self):

        self.assertTrue(robot.call_command('replay', '', 'HAL'))
        self.assertEqual(' > HAL replayed 0 commands.',robot.call_command('replay', '', 'HAL')[1])
    

    def test_handle_command_off(self):
        self.assertFalse(robot.handle_command('HAL', 'off'))

    def test_handle_command_False(self):
        self.assertFalse(robot.handle_command('HAL', ''))
    
    
    def test_add_to_history(self):
        self.assertEqual(None,robot.add_to_history('replay'))
        
    