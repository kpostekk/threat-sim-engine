from pydantic import BaseModel

from threat_sim.engine.entity import NetworkEntity


class ScenarioEntity(NetworkEntity):
    allow_mutations: bool = True
    allow_patches: bool = True
    allow_replacements: bool = True


class Scenario(BaseModel):
    name: str
    description: str
    entities: list[NetworkEntity]
