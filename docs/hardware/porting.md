# Porting ztachip

ztachip is structured so the accelerator core can be moved to another FPGA
family, SoC, or ASIC while keeping the programming model intact.

## Porting checklist

A new platform typically requires work in these areas:

1. **Clock and reset** - provide stable accelerator and peripheral clocks.
2. **External memory** - replace the platform-specific DDR controller and
   validate the AXI path and achievable bandwidth.
3. **Interconnect** - connect the RISC-V host, ztachip control interface,
   external memory, and required peripherals.
4. **JTAG/debug** - provide a working RISC-V debug path for GDB/OpenOCD.
5. **Board I/O** - adapt camera, video, UART, Ethernet, or other peripherals.
6. **Configuration constants** - scale P-core count, local memories, FPU width,
   and related hardware parameters to the target device.
7. **Timing closure** - pipeline or floorplan platform-specific bottlenecks.
8. **Validation** - start with simulation, then a small deterministic kernel,
   then full AI/vision applications.

The most important portability boundary is the external-memory and platform
wrapper. Keep algorithm code independent of vendor-specific FPGA IP whenever
possible.
