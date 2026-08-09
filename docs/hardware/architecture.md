# Hardware Architecture

The accelerator is organized around a RISC-V host, tensor-engine control
logic, memory-movement engines, scratch memory, an FPU path, and an array of
P-core processors.

```{image} ../_static/images/ztachip_arch.png
:alt: High-level ztachip architecture
:width: 100%
```

## Major blocks

**RISC-V host**
: Runs application and tensor-program control code.

**Tensor engine / dataplane**
: Receives tensor instructions, coordinates memory movement, and dispatches
  operators to the P-core array.

**P-core array**
: Executes parallel VLIW vector kernels from local memory.

**Scratch-pad SRAM**
: Provides temporary high-bandwidth storage and feeds the FPU path.

**FPU**
: Handles floating-point vector and reduction-oriented operations used by
  transformer/LLM workloads.

**DDR interfaces**
: Stream data between external memory and accelerator-local memory.

The detailed RTL block-by-block description is available in
[Hardware Detail](../reference/hardware_detail.md).
