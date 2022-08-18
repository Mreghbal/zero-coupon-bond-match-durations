######################################################################################################

import pandas as pd
import numpy as np

######################################################################################################

def zero_coupon_bond_match_durations(cash_flow_time, cash_flow_short, 
                                     cash_flow_long, discount_rate):
    """
    
    Returns the weight "W" for short bond cash flow and long bond cash flow:

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
######################################################################################################
    
    def discount(dates, rate_interest):
        """

        Compute the price of a pure discount bond that pays a dollar at time date:

        1- "t" as time is in years.
        
        """
        return (1 + rate_interest) ** (-dates)

    def macaulay_duration(cash_flows, discount_rate):
        """

        Computes the Macaulay Duration of a sequence of cash flows, given a per-period discount rate:
        
        """
        discounted_flows = discount(cash_flows.index, discount_rate) * cash_flows
        weights = discounted_flows / discounted_flows.sum()
        return np.average(cash_flows.index, weights = weights)

######################################################################################################

    d_t = macaulay_duration(cash_flow_time, discount_rate)
    d_s = macaulay_duration(cash_flow_short, discount_rate)
    d_l = macaulay_duration(cash_flow_long, discount_rate)
    return (d_l - d_t) / (d_l - d_s)
