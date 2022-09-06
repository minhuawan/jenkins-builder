import sys
from datetime import datetime as dt

from builders.galaxy_studio_win64 import GalaxyStudioWin64Builder
from configs.build_config import BuildConfig


def log(msg):
    print(f"{dt.now().strftime('%H:%M:%S')}: {msg}", flush=True)


argv = sys.argv[1:]

BUILDERS = {
    "galaxy-studio-win64": GalaxyStudioWin64Builder
}


def parse_config():
    repo_name = get_arg_index(argv, '--repo')
    branch = get_arg_index(argv, '--branch')
    return BuildConfig(
        repo_name=repo_name,
        branch=branch,
        ext_args=argv,
    )


def get_arg_index(args, arg_name):
    assert arg_name in args, f'launch argv missing: {arg_name}'
    return args[args.index(arg_name) + 1]


if __name__ == "__main__":
    log(f'enter args {argv}')
    config = parse_config()
    builder = get_arg_index(argv, '--builder')
    assert builder in BUILDERS, f'builder not found in builders, name: {builder}'
    BUILDERS[builder](config).start_build()
