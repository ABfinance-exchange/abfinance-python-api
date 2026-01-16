from ._http_manager import _V5HTTPManager
from .asset import Asset


class AssetHTTP(_V5HTTPManager):
    def get_coin_exchange_records(self, **kwargs):
        """Query the coin exchange records.

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Asset.GET_COIN_EXCHANGE_RECORDS}",
            query=kwargs,
            auth=True,
        )

    def get_coins_balance(self, **kwargs):
        """You could get all coin balance of all account types under the master account, and sub account.

        Required args:
            memberId (string): User Id. It is required when you use master api key to check sub account coin balance
            accountType (string): Account type

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Asset.GET_ALL_COINS_BALANCE}",
            query=kwargs,
            auth=True,
        )

    def get_coin_balance(self, **kwargs):
        """Query the balance of a specific coin in a specific account type. Supports querying sub UID's balance.

        Required args:
            memberId (string): UID. Required when querying sub UID balance
            accountType (string): Account type

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Asset.GET_SINGLE_COIN_BALANCE}",
            query=kwargs,
            auth=True,
        )

    def get_transferable_coin(self, **kwargs):
        """Query the transferable coin list between each account type

        Required args:
            fromAccountType (string): From account type
            toAccountType (string): To account type

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Asset.GET_TRANSFERABLE_COIN}",
            query=kwargs,
            auth=True,
        )

    def create_internal_transfer(self, **kwargs):
        """Create the internal transfer between different account types under the same UID.

        Required args:
            transferId (string): UUID. Please manually generate a UUID
            coin (string): Coin
            amount (string): Amount
            fromAccountType (string): From account type
            toAccountType (string): To account type

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{Asset.CREATE_INTERNAL_TRANSFER}",
            query=kwargs,
            auth=True,
        )

    def get_internal_transfer_records(self, **kwargs):
        """Query the internal transfer records between different account types under the same UID.

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Asset.GET_INTERNAL_TRANSFER_RECORDS}",
            query=kwargs,
            auth=True,
        )

    def get_sub_uid(self, **kwargs):
        """Query the sub UIDs under a main UID

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Asset.GET_SUB_UID}",
            query=kwargs,
            auth=True,
        )

    def create_universal_transfer(self, **kwargs):
        """Transfer between sub-sub or main-sub. Please make sure you have enabled universal transfer on your sub UID in advance.

        Required args:
            transferId (string): UUID. Please manually generate a UUID
            coin (string): Coin
            amount (string): Amount
            fromMemberId (integer): From UID
            toMemberId (integer): To UID
            fromAccountType (string): From account type
            toAccountType (string): To account type

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{Asset.CREATE_UNIVERSAL_TRANSFER}",
            query=kwargs,
            auth=True,
        )

    def get_universal_transfer_records(self, **kwargs):
        """Query universal transfer records

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Asset.GET_UNIVERSAL_TRANSFER_RECORDS}",
            query=kwargs,
            auth=True,
        )

    def set_deposit_account(self, **kwargs):
        """Set auto transfer account after deposit. The same function as the setting for Deposit on web GUI

        Required args:
            accountType (string): Account type: UNIFIED,SPOT,OPTION,CONTRACT,FUND

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{Asset.SET_DEPOSIT_ACCOUNT}",
            query=kwargs,
            auth=True,
        )

    def get_deposit_records(self, **kwargs):
        """Query deposit records.

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Asset.GET_DEPOSIT_RECORDS}",
            query=kwargs,
            auth=True,
        )

    def get_sub_deposit_records(self, **kwargs):
        """Query subaccount's deposit records by MAIN UID's API key.

        Required args:
            subMemberId (string): Sub UID

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Asset.GET_SUB_ACCOUNT_DEPOSIT_RECORDS}",
            query=kwargs,
            auth=True,
        )

    def get_internal_deposit_records(self, **kwargs):
        """Query deposit records within the platform. These transactions are not on the blockchain.

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Asset.GET_INTERNAL_DEPOSIT_RECORDS}",
            query=kwargs,
            auth=True,
        )

    def get_master_deposit_address(self, **kwargs):
        """Query the deposit address information of MASTER account.

        Required args:
            coin (string): Coin

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Asset.GET_MASTER_DEPOSIT_ADDRESS}",
            query=kwargs,
            auth=True,
        )

    def get_sub_deposit_address(self, **kwargs):
        """Query the deposit address information of SUB account.

        Required args:
            coin (string): Coin
            chainType (string): Chain, e.g.,ETH

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Asset.GET_SUB_DEPOSIT_ADDRESS}",
            query=kwargs,
            auth=True,
        )

    def get_coin_info(self, **kwargs):
        """Query coin information, including chain information, withdraw and deposit status.

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Asset.GET_COIN_INFO}",
            query=kwargs,
            auth=True,
        )

    def get_withdrawal_address_list(self, **kwargs):
        """Query withdrawal address list.

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Asset.GET_WITHDRAWAL_ADDRESS_LIST}",
            query=kwargs,
            auth=True,
        )

    def get_withdrawal_records(self, **kwargs):
        """Query withdrawal records.

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Asset.GET_WITHDRAWAL_RECORDS}",
            query=kwargs,
            auth=True,
        )

    def get_withdrawable_amount(self, **kwargs):
        """Get withdrawable amount

        Required args:
            coin (string): Coin name

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Asset.GET_WITHDRAWABLE_AMOUNT}",
            query=kwargs,
            auth=True,
        )

    def withdraw(self, **kwargs):
        """Withdraw assets from your account. You can make an off-chain transfer if the target wallet address. This means that no blockchain fee will be charged.

        Required args:
            coin (string): Coin
            chain (string): Chain
            address (string): Wallet address
            tag (string): Tag. Required if tag exists in the wallet address list
            amount (string): Withdraw amount
            timestamp (integer): Current timestamp (ms). Used for preventing from withdraw replay

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{Asset.WITHDRAW}",
            query=kwargs,
            auth=True,
        )

    def cancel_withdrawal(self, **kwargs):
        """Cancel the withdrawal

        Required args:
            id (string): Withdrawal ID

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{Asset.CANCEL_WITHDRAWAL}",
            query=kwargs,
            auth=True,
        )
