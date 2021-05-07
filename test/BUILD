load("@rules_python//python:defs.bzl", "py_test")
load("@py_deps//:requirements.bzl", "requirement")

py_test(
    name = "compiler_version_test",
    srcs = ["compiler_version_test.py"],
    deps = [
        requirement("attrs"),
	requirement("chardet"),
	requirement("idna"),
        requirement("more-itertools"),
        requirement("packaging"),
        requirement("pluggy"),
        requirement("py"),
        requirement("pytest"),
        requirement("wcwidth"),
    ],
)
