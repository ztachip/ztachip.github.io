# Vivado FPGA Build

The reference FPGA target uses Xilinx Vivado and the Digilent Arty A7.

## Recommended build sequence

1. Install the Vivado edition that supports the target Artix-7 device.
2. Clone the ztachip repository.
3. Open or create the project using the scripts and project files supplied
   under the hardware/platform directories.
4. Generate required vendor IP, including the memory subsystem.
5. Synthesize and implement the design.
6. Generate the bitstream.
7. Program the FPGA and, when desired, the configuration flash.
8. Confirm the FPGA configuration LED is active before starting OpenOCD.

```{note}
Treat the FPGA build and software build as separate milestones. First verify
that the bitstream configures correctly; then verify JTAG/OpenOCD; then load
the software image.
```

The original repository's `Documentation/Vivado.md` remains the source of
target-specific project details and screenshots.
