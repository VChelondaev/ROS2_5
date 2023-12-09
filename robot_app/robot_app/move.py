import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist



class TextToCmdVelNode(Node):
    def __init__(self):
        super().__init__('cmd_vel')
        self.publisher = self.create_publisher(Twist, '/robot/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.text_command_callback)
        

    def text_command_callback(self):
        cmd_vel_msg = Twist()
        cmd_vel_msg.angular.z = -1.5
        cmd_vel_msg.linear.x = -1.0

        self.publisher.publish(cmd_vel_msg)
        self.get_logger().info(f'Published cmd_vel: linear.x={cmd_vel_msg.linear.x}, '
                               f'angular.z={cmd_vel_msg.angular.z}')


def main():
    rclpy.init()

    cmd_vel_node = TextToCmdVelNode()
    rclpy.spin(cmd_vel_node)

    cmd_vel_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()