# ztachip Documentation

<div class="zt-hero">
  <div class="zt-kicker">OPEN-SOURCE EDGE AI ACCELERATOR</div>
  <h2>ztachip Developer Documentation</h2>
  <p>
    Complete programmer-facing documentation for ztachip, presented on the web
    in the same order as the main ztachip project page.
  </p>
</div>

```{image} _static/images/ztachip_arch.png
:alt: ztachip architecture
:class: zt-main-image
:width: 100%
```

## Documentation

The documentation below mirrors the five guides listed on the
[ztachip project home page](https://github.com/ztachip/ztachip). The source
content is synchronized from the main repository during every documentation
build. Formatting, spelling, and grammar are cleaned up for the web, while the
technical content and examples are preserved.

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} 1. Technical Overview
:link: technical-overview
:link-type: doc

Why ztachip uses a domain-specific architecture, the problems it addresses,
and the design goals behind its tensor-oriented execution model.
:::

:::{grid-item-card} 2. Hardware Architecture
:link: hardware-architecture
:link-type: doc

The complete ztachip hardware architecture, including interfaces,
subcomponents, tensor dataplane, P-core array, FPU, and memory movement.
:::

:::{grid-item-card} 3. Programmer Guide
:link: programmer-guide/index
:link-type: doc

The complete ztachip programmer guide converted from the original document to
searchable, navigable web documentation with its figures and tables preserved.
:::

:::{grid-item-card} 4. Vision AI Stack Programmer Guide
:link: vision-ai-stack-programmer-guide/index
:link-type: doc

The complete Vision AI Stack programmer guide converted to web documentation,
including the original figures and examples.
:::

:::{grid-item-card} 5. MicroPython Programmer Guide
:link: micropython-programmer-guide
:link-type: doc

How to build and use the ztachip MicroPython port and its accelerator-facing
APIs and examples.
:::

::::

```{toctree}
:maxdepth: 3
:caption: ztachip Documentation

technical-overview
hardware-architecture
programmer-guide/index
vision-ai-stack-programmer-guide/index
micropython-programmer-guide
```
