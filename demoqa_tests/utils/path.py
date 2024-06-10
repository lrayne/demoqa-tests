import demoqa_tests
from pathlib import Path


def resource(path):
    return str(
        Path(demoqa_tests.__file__).parent.parent.joinpath(f'resources/{path}')
    )
