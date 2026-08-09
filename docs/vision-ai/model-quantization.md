# Model Quantization

Large neural-network and language-model weights generally need to be
quantized before they are practical on a small FPGA platform.

The ztachip repository includes model-conversion tooling and release artifacts
for supported demos. The exact conversion command depends on the model family
and the runtime format used by the current software release.

## Recommended workflow

1. Start from a model already known to work in the ztachip examples.
2. Reproduce the reference conversion unchanged.
3. Verify numerical behavior on the host.
4. Quantize one dimension at a time: weight format, activation format, then
   model-specific options.
5. Compare accuracy and throughput after every change.
6. Keep the original model metadata, tokenizer files, and configuration under
   version control with your conversion script.

```{warning}
Quantization is model-specific. Do not assume that a conversion setting that
works for a CNN is appropriate for an LLM, or that metadata omitted by one
conversion tool is safely optional for another runtime.
```
