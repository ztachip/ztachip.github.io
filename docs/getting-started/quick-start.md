# Quick Start

## 1. Install Ubuntu packages

```bash
sudo apt-get update
sudo apt-get install autoconf automake autotools-dev curl python3 \
    libmpc-dev libmpfr-dev libgmp-dev gawk build-essential \
    bison flex texinfo gperf libtool patchutils bc \
    zlib1g-dev libexpat-dev python3-pip
pip3 install numpy
```

## 2. Install the RISC-V toolchain

A prebuilt toolchain is available from the ztachip GitHub releases. Install it
under `/opt/riscv`, then add it to your shell path:

```bash
export PATH=/opt/riscv/bin:$PATH
```

You may also build `riscv-gnu-toolchain` from source using the `rv32im`
architecture and `ilp32` ABI.

## 3. Clone and build ztachip

```bash
git clone https://github.com/ztachip/ztachip.git
cd ztachip

cd SW/compiler
make clean all

cd ../fs
python3 bin2c.py

cd ..
make clean all -f makefile.kernels
make clean all
```

## 4. Recommended: build the MicroPython port

```bash
git clone https://github.com/micropython/micropython.git
cd micropython/ports
cp -avr <ztachip-folder>/micropython/ztachip_port .
cd ztachip_port

export PATH=/opt/riscv/bin:$PATH
export ZTACHIP=<ztachip-folder>

make clean
make
```

## 5. Program and debug the board

ztachip uses OpenOCD plus RISC-V GDB for the reference JTAG flow. Start
OpenOCD in one terminal and GDB in another.

From GDB:

```text
set pagination off
target remote localhost:3333
set remotetimeout 60
set arch riscv:rv32
monitor reset halt
load
continue
```

```{note}
The first goal should be to run an existing example unchanged. Once the
hardware, serial console, JTAG link, and software image are known to work,
modify one component at a time.
```
