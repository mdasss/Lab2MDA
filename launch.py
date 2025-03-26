from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    config = os.path.join( 
        get_package_share_directory('pid_controller_pkg'),'config','parameters.yaml'
    ) # added cuz of task 3


    return LaunchDescription([Node(package = 'pid_controller_pkg', executable =         'pid_controller_node', name = 'pid_controller', output = 'screen'), 
    Node(package = 'joint_simulator', executable = 'joint_simulator_node', name = 'joint_simulator', output = 'screen', parameters = [config]), 
    Node(package = 'pid_controller', executable = 'reference_input_node', name = 'reference_input', output = 'screen')])
