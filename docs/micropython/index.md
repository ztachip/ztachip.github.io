# MicroPython Integration

MicroPython is the recommended high-level environment for ztachip application
development when rapid iteration and scripting are more important than a
fully bare-metal C application.

The ztachip MicroPython port integrates the RISC-V firmware with accelerator
functions and makes it possible to build applications that combine:

- accelerator-backed AI and vision functions;
- local LLM inference;
- function calling;
- serial and device I/O;
- application logic written in Python.

## Build

```bash
git clone https://github.com/micropython/micropython.git
cd micropython/ports
cp -avr <ztachip-folder>/micropython/ztachip_port .
cd ztachip_port

export PATH=/opt/riscv/bin:$PATH
export ZTACHIP=<ztachip-folder>

make clean
make
```

## Examples

The main ztachip repository contains MicroPython examples under
`micropython/examples/`. Start with an existing example and verify it on the
reference hardware before adding your own functions or models.
