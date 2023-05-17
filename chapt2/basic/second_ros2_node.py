import rclpy
from rclpy.node import Node

# 调用rclcpp的初始化函数
rclpy.init()
# 调用rclcpp的循环运行我们创建的second_node节点
rclpy.spin(Node("second_node"))

