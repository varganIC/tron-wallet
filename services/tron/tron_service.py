from tronpy import Tron
from tronpy.exceptions import AddressNotFound, BadAddress


class TronAccountService:
    def __init__(self, client: Tron):
        self.client = client
        self.trx = 1_000_000

    def get_balance(self, address: str) -> float:
        account = self.client.get_account(address)
        return account.get("balance", 0) / self.trx

    def get_bandwidth(self, address: str) -> int:
        return self.client.get_bandwidth(address)

    def get_energy(self, address: str) -> int:
        return (
            self.client.get_account_resource(address)
            .get("TotalEnergyLimit", 0)
        )

    def get_account_info(self, address: str) -> dict:
        try:
            return {
                "address": address,
                "balance": self.get_balance(address),
                "bandwidth": self.get_bandwidth(address),
                "energy": self.get_energy(address),
            }
        except (AddressNotFound, BadAddress) as e:
            return {'error': f'{e}'}


def get_tron_client() -> TronAccountService:
    client = Tron()
    service_tron = TronAccountService(client)
    return service_tron
