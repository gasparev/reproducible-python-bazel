load("@rules_python//python:defs.bzl", "py_binary")
load("@py_deps//:requirements.bzl", "requirement")

py_binary(
    name = "flask_app",
    srcs = ["flask_app.py"],
    python_version = "PY3",
    deps = [
        requirement("flask"),
        requirement("jinja2"),
        requirement("werkzeug"),
        requirement("itsdangerous"),
        requirement("click"),
    ],
)
