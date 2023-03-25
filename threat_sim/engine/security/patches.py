from pydantic import BaseModel

from threat_sim.engine.threats.vulnerability import Vulnerability


class Patch(BaseModel):
    applies_to: list[Vulnerability]
