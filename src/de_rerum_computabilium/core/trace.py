"""
Core tracing module to record the steps of historical algorithms.
"""
from typing import Any, List, Optional
from pydantic import BaseModel
import json

class TraceStep(BaseModel):
    step_index: int
    operation: str
    operands: list[Any]
    result: Any
    precision: Optional[str] = None
    annotation: Optional[str] = None
    cost: Optional[int] = 1  # basic unit of work, e.g. 1 manual addition

class Trace(BaseModel):
    method_name: str
    historical_era: str
    steps: List[TraceStep] = []
    
    def add_step(self, operation: str, operands: list[Any], result: Any, precision: str = None, annotation: str = None, cost: int = 1):
        step = TraceStep(
            step_index=len(self.steps) + 1,
            operation=operation,
            operands=operands,
            result=result,
            precision=precision,
            annotation=annotation,
            cost=cost
        )
        self.steps.append(step)
        
    def total_cost(self) -> int:
        return sum(step.cost for step in self.steps if step.cost)

    def __str__(self) -> str:
        out = [f"Trace for: {self.method_name} ({self.historical_era})"]
        for step in self.steps:
            ops = ", ".join(str(o) for o in step.operands)
            s = f"[{step.step_index}] {step.operation}({ops}) -> {step.result}"
            if step.annotation:
                s += f"  # {step.annotation}"
            out.append(s)
        out.append(f"Total historical operations: {self.total_cost()}")
        return "\n".join(out)
