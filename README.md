# DE RERUM COMPUTABILIUM
> An executable history of calculation.

Every numerical result has a history of work behind it. Most modern software is very good at hiding that work. A logarithm table is easy to call obsolete once somebody else has already computed it, checked it, printed it, and bound it in leather. 

**DE RERUM COMPUTABILIUM** is a project dedicated to reconstructing the material, algorithmic, and human cost of historical computation. We don't just present the modern mathematical formula; we rebuild the exact procedural steps, the numerical constraints, and the immense labor required to compute things before the advent of the electronic computer.

## What is an Executable History?

We treat computation not as an abstract mathematical truth, but as a physical procedure.
When you run a reconstruction in this project, you are seeing:
1.  **The Algorithm**: The specific steps historically used (e.g. Horner's method on a counting board, or repeated subtractions for early logarithms).
2.  **The Medium**: The constraints of the tools (base-60 clay tablets, fixed-precision printed tables, finite difference engines).
3.  **The Labor**: Every intermediate addition, multiplication, and table lookup is recorded and counted.

## The Corpus
The project contains dozens of reconstructions across multiple eras, cultures, and disciplines.

*   **Ancient Arithmetic**: Babylonian sexagesimal approximations, Euclidean algorithms as geometric procedures, ancient Chinese root extractions on counting boards.
*   **Early Modern Astronomy**: The grueling construction of the first logarithm tables, prosthaphaeresis, and orbital approximations.
*   **Engineering and Ballistics**: Historical numerical integration, early Runge-Kutta procedures, and graphical statics.
*   **The Table Era**: Babbage difference engine simulations, actuarial tables, and the industrialization of human computing.

## How to Explore

Use the command line interface to explore the corpus:

```bash
# List all available reconstructions
drc list

# Show details about a specific reconstruction
drc show jiuzhang-cuberoot

# Run a reconstruction and trace the historical steps
drc run babylonian-sqrt --mode trace
```

## Methodology

We reconstruct algorithms based on primary sources and verified historical studies. 
Each reconstruction implements two "clocks":
1.  **The Historical Clock**: A step-by-step trace respecting the historical base, precision, and tool limitations.
2.  **The Modern Clock**: A high-precision modern equivalent to validate the historical result and measure the error.

We do not project modern concepts (like $e$, limits, or floating-point arithmetic) backwards unless the historical actors used an equivalent concept.

## Contributing
We are always looking for new procedures, especially those from non-Western traditions or obscure engineering fields that have been overshadowed by modern computational methods. See the documentation for adding a new reconstruction.
