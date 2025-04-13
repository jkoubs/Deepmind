# Deepmind



# Install

We will build 2 images:
- <strong>humble_env</strong>: Allows to ROS 2 Humble from a linux computer.
- <strong>deepmind</strong>: Built on top of <strong>humble_env</strong> image to set up the ros2_ws for developing the Deepmind project.

First, let's create two folders to store the following repositories. The `ros2_humble` folder will store the ROS 2 Humble repository and the `Deepmind` will store the project repository.

```bash
mkdir $HOME/Projects/ros2_humble
mkdir $HOME/Projects/Deepmind
```


Open a new terminal and git clone the following repositories:
```bash
cd $HOME/Projects/ros2_humble
git clone https://github.com/jkoubs/ros2_humble.git
cd $HOME/Projects/Deepmind
git clone https://github.com/jkoubs/Deepmind.git
```
Then build the images:
```bash
cd $HOME/Projects/ros2_humble/docker
docker build -f Dockerfile -t humble_env .
cd $HOME/Projects/Deepmind/docker
docker build -f Dockerfile -t deepmind ../
```
<strong><em>Note</em></strong>: <strong>../</strong> represents the PATH context which sets the target context one level above to the <strong>Deepmind</strong> directory in order to successfully execute the COPY command from the Dockerfile which will copy the <strong>ros2_ws</strong> inside the container.


Next we will create the container:

<strong><em>Requirement</em></strong>: To run GUI applications in Docker on Linux hosts, you have to run <strong>"xhost +local:root"</strong>. To disallow, <strong>"xhost -local:root"</strong>. For Windows and Mac hosts please check : [Running GUI applications in Docker on Windows, Linux and Mac hosts](https://cuneyt.aliustaoglu.biz/en/running-gui-applications-in-docker-on-windows-linux-mac-hosts/). Can also found some more information about [Using GUI's with Docker](http://wiki.ros.org/docker/Tutorials/GUI).

```bash
xhost +local:root
```

**IMPORTANT NOTE:** Before running the container be sure to **edit the docker-compose.yml file and rename the path according to your local environment to properly mount your host directory into the container. Thus, you need to edit `$HOME/Projects/Deepmind/ros2_ws/src` to your own local path.**

<div align="center">
  <img src="doc/setup_project_path.png" alt="base"/>
</div>

We can now run the image as a container named <strong>deepmind_container</strong> using docker-compose :

```bash
docker-compose up
```

We are now <strong>inside the container</strong> and ready for executing our codes.

<u><strong><em>Note:</em></strong></u> For the next tasks we will consider that we are working from inside our container, in the <strong>ros2_ws</strong> workspace.
