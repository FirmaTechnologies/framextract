import pytest, subprocess, os
from pathlib import Path

COMMAND = ['python', 'framextract']

def capture(command):
    proc = subprocess.run(command, capture_output=True)
    return proc.stdout, proc.stderr, proc.returncode

def test_framextract_no_param():
    out, err, exitcode = capture(COMMAND)
    assert exitcode != 0
    assert err.startswith(b'usage: framextract [-h] [--version]')

def test_framextract(tmp_path):
    pwd = Path().absolute()
    command = ['python', pwd/'framextract', pwd/'tests/FT.mp4']
    os.chdir(tmp_path)
    out, err, exitcode = capture(command)
    os.chdir(pwd)
    assert exitcode == 0
    assert out.endswith(b'104 frames were extracted to FT/\n')

def test_framextract_output(tmp_path):
    command = COMMAND + ['tests/FT.mp4', '-o', tmp_path/'FT']
    out, _, exitcode = capture(command)
    assert exitcode == 0
    assert out.endswith(f'frames were extracted to {tmp_path}/FT/\n'
                        .encode('utf-8'))

def test_framextract_framerate(tmp_path):
    command = COMMAND + ['tests/FT.mp4', '-f', '4',
                         '-o', tmp_path/'FT']
    out, _, exitcode = capture(command)
    assert exitcode == 0
    assert out.endswith(f'2 frames were extracted to {tmp_path}/FT/\n'
                        .encode('utf-8'))

def test_framextract_get_info(tmp_path):
    command = COMMAND + ['tests/FT.mp4', '--get-info']
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert out.endswith(b'Frame size: 960 X 540\n')
