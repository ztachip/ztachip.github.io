# Glossary

**DDR**
: External dynamic memory used to hold application data and model weights.

**DSA**
: Domain-Specific Architecture. Hardware optimized for a defined class of
  applications rather than arbitrary general-purpose workloads.

**FPU**
: Floating-Point Unit. In ztachip, a vector/dataflow path used for FP32,
  BFLOAT, and aggregate operations.

**P-core**
: Lightweight VLIW vector processor used in the parallel accelerator array.

**RISC-V host**
: Embedded processor that runs control software and tensor programs.

**Scratch-pad**
: Explicitly managed on-chip SRAM used for temporary data and FPU operations.

**Tensor engine**
: Hardware controller that decodes tensor instructions, performs data
  operations, and dispatches tensor operators.

**Tensor operator**
: Compute operation implemented by a P-core program and launched by a tensor
  program.

**VLIW**
: Very Long Instruction Word; an instruction format that encodes multiple
  operations that can execute together.
