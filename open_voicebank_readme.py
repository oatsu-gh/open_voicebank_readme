#!/usr/bin/env python3
# Copyright (c) 2021 oatsu
"""
UTAU音源のreadme.txtを開くプラグイン
"""
import subprocess

import utaupy


def main(plugin):
    path_readme_txt = f'{plugin.voicedir}/readme.txt'
    subprocess.run(['@start', path_readme_txt], shell=True)


if __name__ == '__main__':
    utaupy.utauplugin.run(main)
