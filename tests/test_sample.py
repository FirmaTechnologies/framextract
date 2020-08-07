import pytest, subprocess

def capture(command):
    proc = subprocess.run(command, capture_output=True)
    return proc.stdout, proc.stderr, proc.returncode

def test_framextract_no_param():
    command = ['python', 'framextract']
    out, err, exitcode = capture(command)
    assert exitcode != 0
    assert out == b''
    assert err.startswith(b'usage: framextract [-h] [--version]')

# def test_framextract(arg):
#     command = ['python', 'framextract', arg]
#     out, err, exitcode = capture(command)
#     assert exitcode == 0
#     assert out == b''
#     assert err == b''
