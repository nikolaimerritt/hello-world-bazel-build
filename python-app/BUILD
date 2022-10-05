## Python 3 docker image
load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")

## Pushing docker image to docker hub
load("@io_bazel_rules_docker//container:container.bzl", "container_push")


## Python 3
py3_image(
    name = "python-server",
    srcs = ["server.py"],
    main = "server.py",
)

## Pushing docker image
container_push(
    name = "deploy",
    image = ":python-server",
    format = "Docker",
    registry = "index.docker.io",
    repository = "{}/{}".format(
        "nikolaivaticle",
	    "docker-test",
    ),
    tag_file = "//:VERSION",
)