# LLMs and Edge Agents

Recent ztachip software extends the platform beyond vision pipelines to
small-LLM inference and edge-agent workloads.

The architecture can schedule LLM, CNN/vision, and system tasks concurrently.
MicroPython provides the high-level control environment, while the accelerator
handles compute-intensive tensor work.

```{image} ../_static/images/ztachip_ai_agent.png
:alt: ztachip agent harness architecture
:width: 100%
```

## Typical agent flow

An embedded agent can:

1. receive a user command or sensor event;
2. run a local language model;
3. select or call a local function;
4. execute the function from MicroPython;
5. continue running vision or sensor tasks in parallel.

This is useful for demonstrations such as local function calling, device
control, robotics, and low-power multimodal edge systems.
