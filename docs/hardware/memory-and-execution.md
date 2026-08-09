# Memory and Execution

The central performance idea in ztachip is that **external-memory traffic and
operator execution are separate operations**.

P-core compute operates from internal memory. Tensor instructions move the
working set between DDR, scratch memory, and P-core memory.

## Double-context operation

The tensor engine provides two contexts. P-core memory is correspondingly
partitioned so one context can be used for compute while the other is being
filled or drained.

Conceptually:

```text
Context A: [transfer input] -> [execute] -> [transfer output]
Context B:          [transfer input] -> [execute] -> [transfer output]
```

Staggering the two contexts lets memory traffic overlap useful computation.

## Why this matters

A conventional processor often discovers a missing cache line only after an
instruction requests it. ztachip's tensor program describes the required data
movement explicitly, enabling streaming and prefetch behavior with fewer
round-trip stalls.
