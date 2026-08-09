# Repository Layout

The main ztachip repository is divided into hardware, software, MicroPython,
documentation, and development-tool areas.

| Path | Purpose |
|---|---|
| `HW/` | Synthesizable RTL, platform wrappers, simulation hardware, and configuration |
| `SW/` | RISC-V software, compiler, runtime, kernels, applications, and filesystem |
| `micropython/` | ztachip MicroPython port, bindings, and examples |
| `tools/` | OpenOCD and other development support files |
| `Documentation/` | Original project documentation and diagrams |

For application development, most programmers spend their time under `SW/`
and `micropython/`. Hardware developers and porting work primarily under
`HW/`.
