from packaging import version
import importlib.metadata

def test_python_version():
    flask_version = importlib.metadata.version("flask")
    print(f'Flask version is {flask_version}')
    assert version.parse(flask_version) >= version.parse("3.0.0")
    print(f'Version parsed is {version.parse(flask_version)}')
