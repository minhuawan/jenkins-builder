import os
import sys

UNITY_EDITORS = {}
if sys.platform == 'win32':
    UNITY_EDITORS = {
        "2021.2.11f1": "E:\\Program Files\\Unity Editors\\2021.2.11f1\\Editor\\Unity.exe",
        "2020.3.30f1": "E:\\Program Files\\Unity Editors\\2020.3.30f1\\Editor\\Unity.exe",
    }

PROJECTS = {
    "ci-test": {
        "unity_version": "2020.3.30f1",
        "git_url": "git@git.bilibili.co:wanminhua/ci-test.git",
    },
    "galaxy-studio": {
        "unity_version": "2021.2.11f1",
        "git_url": "git@git.bilibili.co:live-unity/galaxy_studio.git",
    }
}


def get_workshop_project_root_path():
    if sys.platform == 'win32':
        return "E:\\ci-workshop\\projects"

    raise f'unsupported platform {sys.platform}'


def get_workshop_output_root_path():
    if sys.platform == 'win32':
        return "E:\\ci-workshop\\outputs"

    raise f'unsupported platform {sys.platform}'


def get_build_number():
    build_number = os.environ.get("BUILD_NUMBER")
    return build_number or "0000"


def get_job_name():
    job_name = os.environ.get("JOB_NAME")
    return job_name or "__TEMPORARY__"


def get_repo_git_url(project_name):
    assert project_name in PROJECTS, f"name not found in REPOS, project_name: {project_name}"
    git_url = PROJECTS[project_name]["git_url"]
    assert git_url, f"git url is None, project_name: {project_name}"
    return git_url


def get_unity_editor_path(project_name):
    assert project_name in PROJECTS, f"name not found in REPOS, project_name: {project_name}"
    unity_version = PROJECTS[project_name]['unity_version']
    assert unity_version, f"unity_version is None, project_name: {project_name}"
    assert unity_version in UNITY_EDITORS, f'unity version not in UNITY_EDITORS, version: {unity_version}'
    return UNITY_EDITORS[unity_version]
