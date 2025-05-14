"""
Vehicle Insurance Agent Tools

This package contains tools for a vehicle insurance agent to assist clients
with insurance policies, quotes, and commission calculations.
"""

from .policy_tools import (
    get_vehicle_insurance_quotes,
    get_policy_details,
    calculate_premium,
    check_claim_status,
    get_agent_commission
)

from .customer_tools import (
    get_customer_profile,
    update_customer_details,
    get_customer_policies
)

from .vehicle_tools import (
    get_vehicle_details,
    validate_vehicle_registration
)

__all__ = [
    'get_vehicle_insurance_quotes',
    'get_policy_details',
    'calculate_premium',
    'check_claim_status',
    'get_agent_commission',
    'get_customer_profile',
    'update_customer_details',
    'get_customer_policies',
    'get_vehicle_details',
    'validate_vehicle_registration'
]
