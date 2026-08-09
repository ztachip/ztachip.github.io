# Introduction

ztachip is a **domain-specific accelerator architecture** for workloads that
can be expressed as a sequence of tensor data operations and tensor compute
operations. The project combines open RTL, a RISC-V host processor, a tensor
engine, an array of lightweight P-core processors, software libraries, a
compiler, and MicroPython integration.

## Why the architecture is different

Many accelerators are optimized primarily for a single operation such as
matrix multiplication or convolution. That approach can deliver very high
throughput, but it often leaves image preprocessing, data movement, control
logic, and non-neural-network workloads to a separate CPU or GPU.

ztachip instead separates the problem into two coordinated activities:

1. **Data movement** - tensor instructions move, reshape, transpose, resize,
   and remap data between external memory and on-chip memory.
2. **Computation** - tensor operators execute from local memory across many
   P-cores and hardware threads.

This separation makes data access predictable and allows memory transfers to
overlap with computation. It also lets the programming model describe
parallelism explicitly without exposing most of the low-level RTL details.

## Complete stack

ztachip provides:

- synthesizable hardware source for FPGA and ASIC targets;
- a RISC-V host and hardware control path;
- a tensor-program compiler and P-core kernel compiler;
- reusable vision and AI software;
- TensorFlow-oriented inference support;
- an FPU path used by transformer and LLM workloads;
- MicroPython integration for scripting and edge-agent applications.

```{image} _static/images/ztachip_ai_agent.png
:alt: AI harness using ztachip to run LLM, CNN, vision, and system tasks concurrently
:width: 100%
```

## Recommended learning path

A programmer does **not** need to understand the entire RTL before using
ztachip. The recommended sequence is:

1. Build and run an existing example.
2. Learn how tensors are represented and moved.
3. Learn how a tensor operator is dispatched.
4. Modify or write a P-core kernel.
5. Move to the detailed hardware documentation only when optimizing,
   debugging, or porting the accelerator.
