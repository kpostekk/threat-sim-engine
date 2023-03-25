from pydantic import BaseModel
from .networking.device import NetworkDevice
from .threats.vulnerability import Vulnerability
from .traits import NetworkEntityType, EntityCurrentOS, EntityTraits


class NetworkEntity(BaseModel):
    entity_type: NetworkEntityType
    os: EntityCurrentOS
    traits: list[EntityTraits]
    network_cards: list[NetworkDevice]
    vulnerabilities: list[Vulnerability]

    def default_card(self) -> NetworkDevice | None:
        if len(self.network_cards) == 0:
            return None

        return self.network_cards[0]
