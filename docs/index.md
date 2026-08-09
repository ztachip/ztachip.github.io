# ztachip Documentation

<div class="zt-hero">

**ztachip** is an open-source, multicore, data-aware RISC-V accelerator for
edge AI, computer vision, and other tensor-oriented workloads. It is designed
to run on cost-sensitive FPGA devices and can also be implemented as a custom
ASIC.

This documentation is organized around the tasks a developer performs:
understand the architecture, build the toolchain, run the first application,
learn the tensor programming model, write P-core kernels, integrate AI and
vision workloads, and finally port the design to a new FPGA or ASIC.

</div>

```{image} _static/images/ztachip_arch.png
:alt: ztachip architecture showing the RISC-V host, tensor engine, P-core array, memory hierarchy, and processing threads
:width: 100%
```

## Where should I start?

::::{grid} 2
:gutter: 3

:::{grid-item-card} New to ztachip?
Read **Introduction** and then follow **Quick Start** to build and run the
reference platform.
:link: getting-started/quick-start
:link-type: doc
:::

:::{grid-item-card} Writing accelerated code?
Start with the **Programming Model**, then continue with the Tensor Language
and P-core Kernel guides.
:link: programming/model
:link-type: doc
:::

:::{grid-item-card} Building AI or vision applications?
Use the **Vision & AI** section for the software stack, model flow, examples,
and quantization process.
:link: vision-ai/index
:link-type: doc
:::

:::{grid-item-card} Porting the hardware?
Read **Hardware Architecture**, **Vivado Build**, and **Porting Guide**.
:link: hardware/architecture
:link-type: doc
:::

::::

```{toctree}
:maxdepth: 2
:caption: Start Here

introduction
getting-started/index
getting-started/quick-start
getting-started/repository-layout
```

```{toctree}
:maxdepth: 3
:caption: Programming

programming/model
programming/tensor-programming
programming/pcore-programming
programming/software-architecture
programming/tensor_language_reference
programming/pcore_language_reference
programming/software_architecture_detail
```

```{toctree}
:maxdepth: 3
:caption: Vision, AI & Agents

vision-ai/index
vision-ai/vision-stack
vision-ai/llm-agents
vision-ai/model-quantization
micropython/index
```

```{toctree}
:maxdepth: 3
:caption: Hardware & FPGA

hardware/architecture
hardware/memory-and-execution
hardware/vivado
hardware/porting
hardware/simulation
reference/hardware_detail
```

```{toctree}
:maxdepth: 2
:caption: Reference

reference/glossary
reference/troubleshooting
reference/source-map
```
