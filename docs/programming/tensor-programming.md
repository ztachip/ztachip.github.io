# Tensor Programming

Tensor programs run on the host RISC-V processor and emit commands to the
tensor engine.

## Memory spaces

A tensor can reside in:

- external DDR memory;
- scratch-pad SRAM;
- P-core private memory;
- P-core shared memory.

P-core memory is split into independent process pages so tensor-engine memory
operations can use one page while the P-core array executes from the other.

## Tensor slicing

A DDR tensor reference describes both shape and a selected range:

```text
DDR(pointer, dim0, dim1, ...)[begin:stride:end][begin:stride:end]...
```

For example:

```text
DDR(p,100,200)[0:1:19][20:1:29]
```

When stride is omitted, it defaults to one. Omitting the beginning selects
from index zero; omitting the end selects through the end of that dimension.

## Typical application sequence

A simple accelerated operator generally follows this pattern:

```text
> move input tensor A from DDR to P-core memory
> move input tensor B from DDR to P-core memory
> execute operator on the P-core array
> move result tensor back to DDR
```

Real applications can overlap the transfers for one tensor context with the
execution of another.

For complete syntax, data types, memory spaces, execution forms, FPU
operations, and examples, see the
[Tensor Language Reference](tensor_language_reference.md).
