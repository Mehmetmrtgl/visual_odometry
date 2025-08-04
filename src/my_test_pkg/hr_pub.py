#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3Stamped, Vector3

class hr_data(Node):
    def __init__(self):
        super().__init__('hr_data')
        self.gyro_vector3 = Vector3()
        self.accel_vector3 = Vector3()

        self.gyro_subscription = self.create_subscription(
            Vector3Stamped,
            "/imu/angular_velocity_hr",
            self.gyro_callback,
            10)

        self.accel_subscription = self.create_subscription(
            Vector3Stamped,
            "/imu/acceleration_hr",
            self.accel_callback,
            10)

        self.publisher_ = self.create_publisher(
            Imu,
            "/imu/data",
            10)

        timer_period = 0.01
        self.timer = self.create_timer(timer_period, self.publish_imu_data)

    def gyro_callback(self, msg):
        # self.get_logger().info(f'Gyro data received: {msg.vector.x}, {msg.vector.y}, {msg.vector.z}')
        self.gyro_vector3.x = msg.vector.x
        self.gyro_vector3.y = msg.vector.y
        self.gyro_vector3.z = msg.vector.z

    def accel_callback(self, msg):
        # self.get_logger().info(f'Accel data received: {msg.vector.x}, {msg.vector.y}, {msg.vector.z}')
        self.accel_vector3.x = msg.vector.x
        self.accel_vector3.y = msg.vector.y
        self.accel_vector3.z = msg.vector.z

    def publish_imu_data(self):
        imu_msg = Imu()
        imu_msg.header.stamp = self.get_clock().now().to_msg()
        imu_msg.header.frame_id = "imu_frame"

        imu_msg.angular_velocity.x = self.gyro_vector3.x
        imu_msg.angular_velocity.y = self.gyro_vector3.y
        imu_msg.angular_velocity.z = self.gyro_vector3.z

        imu_msg.linear_acceleration.x = self.accel_vector3.x
        imu_msg.linear_acceleration.y = self.accel_vector3.y
        imu_msg.linear_acceleration.z = self.accel_vector3.z

        self.publisher_.publish(imu_msg)
        self.get_logger().info('IMU data published')

def main(args=None):
    rclpy.init(args=args)
    imu_node = hr_data()
    rclpy.spin(imu_node)
    imu_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

