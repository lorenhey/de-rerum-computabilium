"""
Generates a printable worksheet from an execution trace.
"""
from de_rerum_computabilium.core.trace import Trace

def generate_worksheet(trace: Trace, filename: str):
    """
    Exports a Trace to a Markdown format that can be printed and filled out.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Historical Worksheet: {trace.method_name}\n\n")
        f.write(f"**Historical Era:** {trace.historical_era}\n\n")
        f.write("> *Try computing this value using only the tools available in that era.*\n\n")
        
        f.write("## Calculation Trace\n\n")
        f.write("| Step | Operation | Operands | Your Calculation | Reference Result |\n")
        f.write("|---|---|---|---|---|\n")
        
        for step in trace.steps:
            ops_str = ", ".join(str(o) for o in step.operands)
            f.write(f"| {step.step_index} | `{step.operation}` | `{ops_str}` |  | `{step.result}` |\n")
            
        f.write(f"\n**Total Historical Operations:** {trace.total_cost()}\n")
        
if __name__ == "__main__":
    # Test worksheet generation
    from de_rerum_computabilium.reconstructions.babbage_difference_engine.algorithm import babbage_engine
    t = babbage_engine(5, 41, 2, 2)
    generate_worksheet(t, "babbage_worksheet.md")
