# Troubleshooting

## GDB cannot connect

Verify that OpenOCD is still running and listening on port `3333`. Confirm the
USB/JTAG device permissions and that the FPGA is already configured.

## FPGA configures but software does not run

Check, in this order:

1. FPGA configuration LED;
2. OpenOCD connection;
3. GDB target connection;
4. successful `load`;
5. serial-port device and baud/configuration;
6. board reset sequence.

## Build cannot find RISC-V tools

```bash
export PATH=/opt/riscv/bin:$PATH
which riscv32-unknown-elf-gcc
```

If the second command returns nothing, fix the toolchain installation before
debugging the ztachip build.

## Accelerator output is incorrect

Start with the smallest deterministic kernel. Verify tensor dimensions,
strides, memory space, data type, and active tensor context. Then verify the
P-core kernel and `_VMASK` behavior.

## Performance is lower than expected

Measure memory movement and compute separately. Check whether transfers overlap
execution and whether the application is repeatedly moving data that could
remain in accelerator-local memory.
