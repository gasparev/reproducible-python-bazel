import platform
import subprocess
import sys

from flask import Flask


def cmd(args):
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    out, _ = process.communicate()
    return out.decode('ascii').strip()


app = Flask(__name__)


@app.route('/')
def python_versions():
    bazel_python_path = f'Python executable used by Bazel is: {sys.executable} <br/><br/>'
    bazel_python_version = f'Python version used by Bazel is: {platform.python_version()} <br/><br/>'
    host_python_path = f'Python executable on the HOST machine is: {cmd(["which", "python3"])} <br/><br/>'
    host_python_version = f'Python version on the HOST machine is: {cmd(["python3", "-c", "import platform; print(platform.python_version())"])}'
    python_string = (
        bazel_python_path
        + bazel_python_version
        + host_python_path
        + host_python_version
    )
    return python_string


if __name__ == '__main__':
    app.run()
