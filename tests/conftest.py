import pytest
from cg635_clock_generator_mocker import CG635ClockGeneratorMocker
from pyvisa import ResourceManager
from pyvisa_mock.base.register import register_resource

from cg635_clock_generator import CG635ClockGenerator, CG635Communication

RESOURCE_PATH = "MOCK0::mock1::INSTR"


@pytest.fixture(scope="module")
def mock_cg635_clock_generator():
    mock_cg635_clock_generator = CG635ClockGeneratorMocker()
    register_resource(RESOURCE_PATH, mock_cg635_clock_generator)
    return mock_cg635_clock_generator


@pytest.fixture(scope="module")
def cg635_clock_generator(mock_cg635_clock_generator):
    resource_manager = ResourceManager(visa_library="@mock")

    clock_generator = CG635ClockGenerator(
        communication_type=CG635Communication.OTHER,
        resource_path=RESOURCE_PATH,
        resource_manager=resource_manager,
    )
    return clock_generator
