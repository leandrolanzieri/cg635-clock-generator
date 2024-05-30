import pytest
from cg635_clock_generator_mocker import CG635ClockGeneratorMocker
from pyvisa import ResourceManager
from pyvisa_mock.base.register import register_resource

from cg635_clock_generator import CG635ClockGenerator, CG635Communication

RESOURCE_PATH = "MOCK0::mock1::INSTR"


def pytest_addoption(parser):
    parser.addoption(
        "--hil", action="store_true", help="Run test on hardware-in-the-loop"
    )


@pytest.fixture(scope="module")
def mock_cg635_clock_generator():
    mock_cg635_clock_generator = CG635ClockGeneratorMocker()
    register_resource(RESOURCE_PATH, mock_cg635_clock_generator)
    return mock_cg635_clock_generator


@pytest.fixture(scope="session")
def hil(request):
    return request.config.option.hil is not None and request.config.option.hil


@pytest.fixture(scope="module")
def cg635_clock_generator(mock_cg635_clock_generator, hil):
    if hil:
        clock_generator = CG635ClockGenerator(
            communication_type=CG635Communication.RS232,
            serial_device="/dev/ttyUSB0",
        )
    else:
        resource_manager = ResourceManager(visa_library="@mock")
        clock_generator = CG635ClockGenerator(
            communication_type=CG635Communication.OTHER,
            resource_path=RESOURCE_PATH,
            resource_manager=resource_manager,
        )
    return clock_generator
