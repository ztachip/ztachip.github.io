# P-core Kernel Programming

P-core kernels implement the tensor operators launched by tensor programs.

## Execution model

Each P-core is a lightweight VLIW vector processor. The architecture combines:

- vector arithmetic;
- scalar integer operations for indexing and loop control;
- control operations;
- local memory;
- hardware multithreading.

P-cores execute the same instruction stream in lockstep. Within each P-core,
hardware threads are interleaved through the pipeline.

## Kernel example

```cpp
_NT16_ class matrix;

_kernel_ void matrix::add(float8 x, float8 y, float8 z)
{
    z = x + y;
}
```

This compact expression describes vector work that is distributed across the
accelerator's P-cores and threads.

## Memory scope

P-core data may be:

- **private** - one instance for each hardware thread;
- **shared** - one instance shared by the threads in a P-core;
- **global** - read-only scalar parameters supplied by the tensor program.

## Vector masking

`_VMASK` selects which vector lanes are written. Comparison helpers such as
`GE`, `GT`, `LE`, `LT`, `EQ`, and `NE` can produce masks for conditional
vector execution without requiring divergent thread branches.

For the full language description, see the
[P-core Language Reference](pcore_language_reference.md).
