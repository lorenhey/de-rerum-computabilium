# Methodology

How do we build an "executable history"?

## Levels of Reconstruction

Historical sources vary wildly in their level of operational detail. A published table might not explicitly state the interpolation method used. An ancient text might give an example without a generalized formula. 

We classify our reconstructions according to the following evidence levels:

*   **A — Direct Reconstruction**: The procedure is documented step-by-step in a primary source and can be executed almost literally.
*   **B — Reconstructed Procedure**: The mathematical method is clear, but specific operational details (like intermediate rounding or exact table layout) must be inferred from context or practice of the era.
*   **C — Mathematical Reconstruction**: The underlying mathematics is known, but the historical workflow is lost or undocumented. We reconstruct a *plausible* operational sequence.
*   **D — Experimental Implementation**: A highly speculative reconstruction based on partial evidence, designed to test a hypothesis about how a calculation *might* have been performed.

## The Trace Engine

The core of our methodology is the `Trace` engine. 
Rather than simply returning a result, every reconstruction logs its operations. 

```python
trace = Trace(method_name="Babylonian Square Root")
trace.add_step(operation="divide", operands=[S, x], result=div, cost=2)
```

This allows us to audit the **Material Complexity** of an algorithm. We can count the exact number of additions, multiplications, and table lookups required.

## Validation

Every numerical procedure is validated against a modern, high-precision reference. We record:
- The historical printed/published result (when available).
- The result of our simulated historical procedure.
- The modern reference result.

Discrepancies are investigated: Are they due to our misinterpretation, a different rounding convention, or an original printing error in the historical source? We never silently "fix" documented historical errors; we expose them.
