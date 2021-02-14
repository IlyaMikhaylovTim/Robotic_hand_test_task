from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    ld = LaunchDescription()
    
    turtle_node = Node(
        package='turtlesim',
        namespace='turtlesim1',
        executable='turtlesim_node',
        name='red_screen_turtle',
	parameters=[
	{"background_b": 0},
	{"background_g": 0},
	{"background_r": 127}
	]
    )
    
    ld.add_action(turtle_node)
    return ld
    

