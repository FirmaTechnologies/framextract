import pytest, subprocess, os
from pathlib import Path

COMMAND = ['python', 'framextract', 'tests/FT.mp4']

def capture(command):
    proc = subprocess.run(command, capture_output=True)
    return proc.stdout, proc.stderr, proc.returncode

def test_framextract_no_param():
    _, err, exitcode = capture(COMMAND[:-1])
    assert exitcode != 0
    assert err.startswith(b'usage: framextract [-h] [--version]')

def test_framextract(tmp_path):
    pwd = Path.cwd()
    command = [COMMAND[0], pwd/COMMAND[1], pwd/COMMAND[-1]]
    os.chdir(tmp_path)
    out, _, exitcode = capture(command)
    os.chdir(pwd)
    assert exitcode == 0
    assert out.endswith(b'104 frames were extracted to "FT"\n')

def test_framextract_invalid_input_video():
    command = COMMAND[:-1] + ['FT.mp4']
    out, _, exitcode = capture(command)
    assert exitcode == 0
    assert out.endswith(b'Couldn\'t read video stream from file "FT.mp4"\n')

def test_framextract_output_framerate(tmp_path):
    command = COMMAND + ['-o', tmp_path/'FT', '-f', '4']
    out, _, exitcode = capture(command)
    assert exitcode == 0
    assert out.endswith(f'2 frames were extracted to "{tmp_path}/FT"\n'
                        .encode('utf-8'))

def test_framextract_get_info(tmp_path):
    command = COMMAND + ['--get-info-only']
    out, _, exitcode = capture(command)
    assert exitcode == 0
    assert out.endswith(b'Frame size: 960 X 540\n')

def test_framextract_small_framerate(tmp_path):
    command = COMMAND + ['-o', tmp_path/'FT', '-f', '.01']
    out, _, exitcode = capture(command)
    assert exitcode == 0
    assert out.endswith(f'104 frames were extracted to "{tmp_path}/FT"\n'
                        .encode('utf-8'))
