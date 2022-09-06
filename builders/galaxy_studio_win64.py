import os
import subprocess as sp

from configs.build_config import BuildConfig
from start import log


class GalaxyStudioWin64Builder:
    config: BuildConfig

    def __init__(self, config: BuildConfig):
        self.config = config
        pass

    def start_build(self):
        self.config.check_local_repo()
        output_path = os.path.join(self.config.output_path, 'galaxy_studio', 'galaxy_studio.exe')
        self.config.set_output_path(output_path)
        args = self.config.get_build_command_args('Builder.BuildFromCI')
        log(f'build args: {args}')
        # code = sp.call(args)
        # if code == 0:
        #     if '--showlog' in self.config.ext_args:
        #         self.config.print_log()
        # else:
        #     self.config.print_log()
        #     exit(code)

        self.after_build()

    def after_build(self):
        if not os.path.exists(self.config.output_path):
            log(f'output path not exist! {self.config.output_path}')
            exit(1)

        # abspath = os.path.abspath(self.config.output_path)
        # dir_name = os.path.dirname(abspath)
        # zippath = shutil.make_archive(
        #     'galaxy_studio',
        #     "zip",
        #     jp(dir_name, os.path.pardir)
        # )
        # full_path = jp(self.config.output_path, 'galaxy_studio.zip')
        # # if os.path.exists(full_path):
        # #     print('remove ', full_path)
        # #     os.remove(full_path)
        # # shutil.move(zippath, self.zip_store_path)
        # print('zip_store_path', full_path)
