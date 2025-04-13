FROM humble_env
# ENV DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-c"]

RUN echo "source /ros2_ws/install/setup.bash" >> ~/.bashrc

# Setup colcon_cd
RUN echo "source /usr/share/colcon_cd/function/colcon_cd.sh" >> ~/.bashrc
RUN echo "export _colcon_cd_root=/opt/ros/humble/" >> ~/.bashrc

# Setup colcon tab completion
RUN echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc

# Install required ROS 2 Humble control packages for Deepmind control
RUN apt-get update && apt-get install -y \
    ros-humble-ros2-control \
    ros-humble-ros2-controllers \
    ros-humble-gazebo-ros2-control

COPY /ros2_ws/ /ros2_ws/
# Install ultralytics for YOLOv8
RUN pip3 install ultralytics
# Update rosdep database and install dependencies
RUN source /opt/ros/humble/setup.bash && \
    apt-get update --fix-missing && \
    cd /ros2_ws  && \
    # This installs dpdencies declared in package.xml from all pkgs in the src folder for ROS 2 Humble
    rosdep install -i --from-path src --rosdistro humble -y --skip-keys rviz && \
    # Build env_ws
    colcon build --symlink-install 

# Set Working directory
WORKDIR '/ros2_ws'
# ENTRYPOINT ["/ros_entrypoint.sh"]