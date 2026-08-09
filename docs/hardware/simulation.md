# RTL Simulation

Build the simulation software image first:

```bash
export PATH=/opt/riscv/bin:$PATH
cd ztachip

cd SW/compiler
make clean all

cd ..
make clean all -f makefile.kernels
make clean all -f makefile.sim
```

The generated memory image is:

```text
SW/build/ztachip_sim.hex
```

Compile RTL from the project simulation and hardware source directories. The
top-level simulation component is:

```text
HW/simulation/main.vhd
```

Drive `main:clk`. The `main:led_out` output toggles as tests pass.

Simulation is the preferred place to validate a new platform wrapper, tensor
instruction sequence, or RTL modification before debugging the same problem
through FPGA JTAG.
