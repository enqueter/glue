<br>

## Remote Development Environment

The remote environment's image is built via

```shell
docker build . --file .devcontainer/Dockerfile --tag glue
```

It names the image `glue`.  Subsequently, a container/instance of the image `glue` is launched via:


> docker run [--rm](https://docs.docker.com/engine/reference/commandline/run/#:~:text=a%20container%20exits-,%2D%2Drm,-Automatically%20remove%20the) [-i](https://docs.docker.com/engine/reference/commandline/run/#:~:text=and%20reaps%20processes-,%2D%2Dinteractive,-%2C%20%2Di) [-t](https://docs.docker.com/get-started/02_our_app/#:~:text=Finally%2C%20the-,%2Dt,-flag%20tags%20your) [-p](https://docs.docker.com/engine/reference/commandline/run/#:~:text=%2D%2Dpublish%20%2C-,%2Dp,-Publish%20a%20container%E2%80%99s) 127.0.0.1:10000:8888 -w /app --mount \
> &nbsp; &nbsp; type=bind,src="$(pwd)",target=/app -v ~/.aws:/root/.aws glue

wherein   `-p 10000:8888` maps the host port `10000` to container port `8888`.  Note, the container's working environment,
i.e., `-w`, must be inline with this project's parent directory.  Never deploy a root container.

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
