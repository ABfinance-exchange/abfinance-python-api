from ._http_manager import _V5HTTPManager
from .account import Account


class AccountHTTP(_V5HTTPManager):
    def get_wallet_balance(self, **kwargs):
        """Obtain wallet balance, query asset information of each currency, and account risk rate information under unified margin mode.
        By default, currency information with assets or liabilities of 0 is not returned.

        Required args:
            accountType (string): Account type
                Unified account: UNIFIED
                Normal account: CONTRACT

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Account.GET_WALLET_BALANCE}",
            query=kwargs,
            auth=True,
        )

    def get_transferable_amount(self, **kwargs):
        """Query the available amount to transfer of a specific coin in the Unified wallet.

        Required args:
            coinName (string): Coin name, uppercase only

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Account.GET_TRANSFERABLE_AMOUNT}",
            query=kwargs,
            auth=True,
        )

    def get_borrow_history(self, **kwargs):
        """Get interest records, sorted in reverse order of creation time.

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Account.GET_BORROW_HISTORY}",
            query=kwargs,
            auth=True,
        )

    def get_collateral_info(self, **kwargs):
        """Get the collateral information of the current unified margin account, including loan interest rate, loanable amount, collateral conversion rate, whether it can be mortgaged as margin, etc.

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Account.GET_COLLATERAL_INFO}",
            query=kwargs,
            auth=True,
        )

    def set_collateral_coin(self, **kwargs):
        """You can decide whether the assets in the Unified account needs to be collateral coins.

        Required args:
            coin (string): Coin name
            collateralSwitch (string): ON: switch on collateral, OFF: switch off collateral

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{Account.SET_COLLATERAL_COIN}",
            query=kwargs,
            auth=True,
        )

    def batch_set_collateral_coin(self, **kwargs):
        """You can decide whether the assets in the Unified account needs to be collateral coins.

        Required args:
            request (array): Object
            > coin (string): Coin name
            > collateralSwitch (string): ON: switch on collateral, OFF: switch off collateral

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{Account.BATCH_SET_COLLATERAL_COIN}",
            query=kwargs,
            auth=True,
        )

    def get_fee_rates(self, **kwargs):
        """Get the trading fee rate of derivatives.

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Account.GET_FEE_RATE}",
            query=kwargs,
            auth=True,
        )

    def get_account_info(self, **kwargs):
        """Query the margin mode configuration of the account.

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Account.GET_ACCOUNT_INFO}",
            query=kwargs,
            auth=True,
        )

    def get_transaction_log(self, **kwargs):
        """Query transaction logs in Unified account.

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Account.GET_TRANSACTION_LOG}",
            query=kwargs,
            auth=True,
        )

    def get_mmp_state(self, **kwargs):
        """Get MMP state

        Required args:
            baseCoin (string): Base coin

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Account.GET_MMP_STATE}",
            query=kwargs,
            auth=True,
        )

    def get_instruments_info(self, **kwargs):
        """Get available instruments info for unified account.

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Account.GET_INSTRUMENTS_INFO}",
            query=kwargs,
            auth=True,
        )

    def query_dcp_info(self, **kwargs):
        """Query the DCP configuration of the account.

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Account.QUERY_DCP_INFO}",
            query=kwargs,
            auth=True,
        )

    def get_smp_group(self, **kwargs):
        """Get the SMP group ID of the account.

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Account.GET_SMP_GROUP}",
            query=kwargs,
            auth=True,
        )

    def set_limit_price_action(self, **kwargs):
        """Set the limit price action behavior.

        Required args:
            limitPxAction (string): "ForceAdjust" or "RejectOrder"

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{Account.SET_LIMIT_PRICE_ACTION}",
            query=kwargs,
            auth=True,
        )
