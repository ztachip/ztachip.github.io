# Software Architecture

The ztachip software stack hides most hardware-specific scheduling details
behind a domain-specific programming model.

At a high level:

1. application code runs on the RISC-V host;
2. tensor extensions describe memory movement and operator launches;
3. the ztachip compiler translates those extensions into tensor-engine
   commands;
4. P-core source implements the operators;
5. the P-core compiler produces the VLIW program loaded into the accelerator;
6. vision, AI, and MicroPython libraries build on top of these layers.

This arrangement allows an application to remain largely independent of the
number of P-cores or the exact FPGA implementation. Porting to a device with a
different accelerator capacity should therefore require much less application
rewriting than a design in which scheduling and hardware topology are embedded
directly into the algorithm.
