# Programming Model

ztachip uses a two-level programming model.

## Tensor program

A **tensor program** runs on the RISC-V host. It describes the application as
a sequence of high-level tensor operations:

- move tensors between DDR, scratch memory, and P-core memory;
- reshape, resize, transpose, or remap data;
- launch a tensor operator on the P-core array;
- coordinate two tensor-engine contexts so data transfer can overlap compute.

Tensor-program source uses C with ztachip extensions. Tensor-extension
statements begin with `>`.

## P-core program

A **P-core program** defines the implementation of tensor operators. P-core
source uses a C-like language compiled into the accelerator's VLIW
instruction stream.

P-cores execute in parallel and use hardware multithreading to keep the deep
execution pipeline occupied.

## Key design principle: separate movement from compute

On a conventional processor, loads and arithmetic are interleaved. When data
is not in cache, the processor can stall while waiting for memory.

ztachip moves the required working set into local accelerator memory first.
The tensor operator then runs against that local memory. A second tensor
context can prepare the next working set while the first one is executing.

This explicit separation is central to both ztachip performance and its
programming model.
