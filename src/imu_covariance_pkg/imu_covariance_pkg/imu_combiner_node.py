#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3
from std_msgs.msg import Header

class ImuCombinerNode(Node):
    def __init__(self):
        super().__init__('imu_combiner_node')

        self.acceleration = None
        self.angular_velocity = None
        self.last_header = None

        self.sub_acc = self.create_subscription(
            Imu,
            '/imu/acceleration',
            self.acc_callback,
            10
        )
        self.sub_gyro = self.create_subscription(
            Imu,
            '/imu/angular_velocity',
            self.gyro_callback,
            10
        )

        self.pub = self.create_publisher(Imu, '/imu/data_combined', 10)
        self.timer = self.create_timer(0.01, self.publish_combined_imu)  # 100 Hz

    def acc_callback(self, msg):
        self.acceleration = msg.linear_acceleration
        self.last_header = msg.header

    def gyro_callback(self, msg):
        self.angular_velocity = msg.angular_velocity
        self.last_header = msg.header

    def publish_combined_imu(self):
        if self.acceleration is not None and self.angular_velocity is not None:
            imu_msg = Imu()
            imu_msg.header = self.last_header if self.last_header else Header()
            imu_msg.linear_acceleration = self.acceleration
            imu_msg.angular_velocity = self.angular_velocity

            # İsteğe bağlı: sabit quaternion ve kovaryanslar
            imu_msg.orientation_covariance[0] = -1  # orientation bilinmiyor
            imu_msg.angular_velocity_covariance = [
                0.0001, 0, 0,
                0, 0.0001, 0,
                0, 0, 0.0001
            ]
            imu_msg.linear_acceleration_covariance = [
                0.0004, 0, 0,
                0, 0.0004, 0,
                0, 0, 0.0004
            ]

            self.pub.publish(imu_msg)

def main(args=None):
    rclpy.init(args=args)
    node = ImuCombinerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

