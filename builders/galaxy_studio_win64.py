import os
import shutil
import subprocess as sp

from configs.build_config import BuildConfig
from globals import log, execute_command


class GalaxyStudioWin64Builder:
    config: BuildConfig
    raw_output_path: str

    def __init__(self, config: BuildConfig):
        self.config = config
        pass

    def before_build(self):
        self.config.check_local_repo()
        self.raw_output_path = self.config.output_path
        output_path = os.path.join(self.config.output_path, 'galaxy_studio', 'galaxy_studio.exe')
        self.config.set_output_path(output_path)
        args = self.config.get_build_command_args('EditorBuild.EditorBuildHelper.BuildFromCI')
        return args

    def start_build(self):
        args = self.before_build()
        log(f'build args: {args}')
        code = sp.call(args)
        if code == 0:
            if '--showlog' in self.config.ext_args:
                self.config.print_log()
        else:
            self.config.print_log()
            exit(code)

        self.after_build()

    def after_build(self):
        if not os.path.exists(self.config.output_path):
            log(f'output path not exist! {self.config.output_path}')
            exit(1)

        log(f'change dir to output path: {self.raw_output_path}')
        os.chdir(self.raw_output_path)
        execute_command(['python', '-m', 'zipfile', '-c', 'galaxy_studio.zip', './galaxy_studio'])
        shutil.rmtree('./galaxy_studio')  # remove build file after zip file
