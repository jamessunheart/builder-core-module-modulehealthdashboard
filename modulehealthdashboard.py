from typing import Dict, List
import time

class ModuleHealthDashboard:
    def __init__(self):
        self.module_scores: Dict[str, Dict[str, float]] = {}
        self.last_updated: Dict[str, float] = {}

    def update_scores(self, module_name: str, scores: Dict[str, float]):
        self.module_scores[module_name] = scores
        self.last_updated[module_name] = time.time()

    def get_status(self) -> List[str]:
        return [
            f"{module}: Score={info['total']} (Last Updated: {time.ctime(self.last_updated[module])})"
            for module, info in self.module_scores.items()
        ]

    def get_flagged_modules(self, threshold: float = 35.0) -> List[str]:
        return [m for m, s in self.module_scores.items() if s['total'] < threshold]

    def trigger_evaluation(self, module_name: str, evaluator) -> None:
        code = evaluator.get_module_code(module_name)
        scores = evaluator.evaluate(code)
        self.update_scores(module_name, scores)