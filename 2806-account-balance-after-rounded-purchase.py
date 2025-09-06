# https://leetcode.com/problems/account-balance-after-rounded-purchase

class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        r = purchaseAmount % 10
        if r <= 4:
            purchaseAmount = 10 * int(purchaseAmount/10)
        else:
            purchaseAmount = 10 * int(purchaseAmount/10) + 10
        
        return 100 - purchaseAmount