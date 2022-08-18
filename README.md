# zero-coupon-bond-match-durations
Returns the weights for short bond cash flow and long bond cash flow to match a liability

"""
    
    Returns the weight "W" for short bond cash flow and "1 - W" for long bond cash flow:

    1- Try to match a liability if we had a zero coupon bond that had the
       exact maturity as the liability, in which case, assuming we had enough
       funds available, we could do perfect cash flow matching.
    
    2- Use a portfolio of standard, non-coupon bonds to try and achieve the same
       behaviour as a zero coupon bond.

    3- Use "bond_cash_flows" function to generate cash flows for long and short bonds.
         
    4- Computes "W" that is the weight for short bond cash flow.
    
    5- (1-W) is the weight for long bond cash flow.
    
    6- The weights for short and long bonds cash flows have effective duration
       that matches the cash flow time of liability.

    """
