# VisionAI Software Stack

The VisionAI layer provides reusable building blocks so programmers do not
need to write every tensor operator from scratch.

A typical camera pipeline can be divided into:

1. **Input and formatting** - capture pixels and convert them to the required
   color/layout representation.
2. **Preprocessing** - resize, normalize, filter, or otherwise prepare data.
3. **Inference or vision processing** - run a neural-network model or a
   traditional vision algorithm.
4. **Post-processing** - decode detections, thresholds, geometry, or motion
   information.
5. **Output** - display, communicate, or use the result to control an
   application.

ztachip is intended to accelerate multiple parts of this pipeline rather than
only the neural-network stage.
