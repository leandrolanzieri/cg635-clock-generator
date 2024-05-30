# cg635-clock-generator - Stanford Research Systems CG635 Synthesized Clock Generator Interface

Interface with a Stanford Research Systems CG635 Synthesized Clock Generator.

## Installation

```bash
$ pip install git+https://gitlab.desy.de/leandro.lanzieri/cg635-clock-generator.git
```

## Usage

```python
from cg635_clock_generator import CG635ClockGenerator, CG635Communication

clock_generator = CG635ClockGenerator(
        communication_type=CG635Communication.RS232,
        serial_device='/dev/ttyUSB0',
)

print(clock_generator.get_identification())

FREQ = 10e6
PHASE = 90.0

clock_generator.set_frequency(FREQ)

frequency = clock_generator.get_frequency()
print(f"Frequency is {frequency} Hz")

clock_generator.set_phase(PHASE)

phase = clock_generator.get_phase()
print(f"Phase is {phase} degrees")

```

## Status

Currently only the RS232 communication has been tested on the device.

## Documentation

For more details of the module API, check the
[online documentation](http://cg635-clock-generator-leandro-lanzieri-c9d5fa14e6af42e02aa27f45.pages.desy.de/).

## Feeling like contributing?

Great! Check the [Contributing Guide](CONTRIBUTING.md) to get started.
