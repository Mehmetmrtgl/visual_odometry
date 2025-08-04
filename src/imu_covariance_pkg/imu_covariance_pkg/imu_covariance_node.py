#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu

class ImuCovarianceNode(Node):
    def __init__(self):
        super().__init__('imu_covariance_node')

        self.get_logger().info("IMU Covariance Node başlatıldı.")  # ← BAŞLANGIÇ LOGU

        self.subscription = self.create_subscription(
            Imu,
            '/imu/data',
            self.imu_callback,
            10)

        self.publisher = self.create_publisher(Imu, '/imu/data_cov', 10)

    def imu_callback(self, msg):
        self.get_logger().info("IMU verisi alındı, covariance eklendi ve yayınlandı.")  # ← CALLBACK LOGU

        new_msg = Imu()
        new_msg.header = msg.header
        new_msg.orientation = msg.orientation
        new_msg.angular_velocity = msg.angular_velocity
        new_msg.linear_acceleration = msg.linear_acceleration

        new_msg.orientation_covariance = [
            0.001, 0.0,   0.0,
            0.0,   0.001, 0.0,
            0.0,   0.0,   0.001
        ]
        new_msg.angular_velocity_covariance = [
            0.0001, 0.0,    0.0,
            0.0,    0.0001, 0.0,
            0.0,    0.0,    0.0001
        ]
        new_msg.linear_acceleration_covariance = [
            0.0004, 0.0,    0.0,
            0.0,    0.0004, 0.0,
            0.0,    0.0,    0.0004
        ]

        self.publisher.publish(new_msg)

def main(args=None):
    rclpy.init(args=args)
    node = ImuCovarianceNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

