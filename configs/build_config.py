import os
import sys

from configs import static_config


class BuildConfig:
    project_name: str
    branch: str
    ext_args: [str]
    output_path: str
    log_path: str

    def __init__(self, repo_name, branch, ext_args):
        self.project_name = repo_name
        self.branch = branch
        self.ext_args = ext_args

        job_name = static_config.get_job_name()
        build_number = static_config.get_build_number()
        output_root_path = static_config.get_workshop_output_root_path()
        project_root_path = static_config.get_workshop_project_root_path()
        # E://ci-repos//test//master
        self.project_path = os.path.join(project_root_path, self.project_name, self.branch)
        self.log_path = os.path.join(self.project_path, 'build.log')
        self.output_path = os.path.join(output_root_path, job_name, build_number)

        print(f'repo path: {self.project_path}')
        print(f'log path: {self.log_path}')
        print(f'preset output path: {self.output_path}')

    def get_project_path(self):
        return self.project_path

    def get_output_path(self):
        return self.output_path

    def set_output_path(self, output_path):
        self.output_path = output_path
        print(f'set output path: {self.output_path}')

    def get_log_path(self):
        return self.log_path

    def check_local_repo(self):
        if not os.path.exists(self.project_path):
            git_url = static_config.get_repo_git_url(self.project_name)
            assert git_url, f'git url is None, repo name: {self.project_name}'
            assert self.branch, 'branch is None'
            command = f'git clone {git_url} -b {self.branch} {self.project_path}'
            print(f'target repo not existed, start clone with command: {command}')
            os.system(command)

        os.chdir(self.project_path)
        os.system(f'git clean -df')
        os.system(f'git fetch')
        os.system(f'git reset --hard origin/{self.branch}')

    def get_build_command_args(self, execute_method):
        assert execute_method, 'no execute method'
        editor_path = static_config.get_unity_editor_path(self.project_name)
        build_args = [
            editor_path,
            f'-logfile',
            f'{self.log_path}',
            f'-ProjectPath',
            f'{self.project_path}',
            f'-quit',
            f'-batchmode',
            f'-executeMethod',
            f'{execute_method}',
            f'-outputPath',
            f'{self.output_path}'
        ]
        build_args.extend(self.ext_args)
        return build_args

    def print_log(self):
        if not os.path.exists(self.log_path):
            print(f'log file at {self.log_path} not exist .. return')
        else:
            with open(self.log_path, 'r', encoding='utf-8') as f:
                n = 1
                line = f.readline()
                while line:
                    sys.stdout.write(f'[Unity-Log-File-Output]:{n} {line}')
                    n += 1
                    line = f.readline()
            print("\nprint log file finished\n")