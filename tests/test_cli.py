import pytest, subprocess

COMMAND = ['python', 'framextract']

def capture(command):
    proc = subprocess.run(command, capture_output=True)
    return proc.stdout, proc.stderr, proc.returncode

def test_framextract_no_param():
    out, err, exitcode = capture(COMMAND)
    assert exitcode != 0
    assert out == b''
    assert err.startswith(b'usage: framextract [-h] [--version]')

def test_framextract():
    command = COMMAND + ['tests/FT.mp4']
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert out.endswith(b'104 frames were extracted to FT/\n')
    assert err == b''

def test_framextract_invalid_video():
    command = COMMAND + ['FT.mp4']
    out, err, exitcode = capture(command)
    assert exitcode != 0
    assert out.startswith(b'FT.mp4')
    assert b"OpenCV: Couldn't read video stream" in err

def test_framextract_output():
    command = COMMAND + ['tests/FT.mp4', '-o', 'tests/FT']
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert out.endswith(b'frames were extracted to tests/FT/\n')
    assert err == b''

def test_framextract_framerate():
    command = COMMAND + ['tests/FT.mp4', '-f', '4']
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert out.endswith(b'2 frames were extracted to FT/\n')
    assert err == b''
