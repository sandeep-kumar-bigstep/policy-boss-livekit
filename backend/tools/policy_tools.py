"""
Policy Tools for Vehicle Insurance Agent

This module contains tools related to insurance policies, quotes, and commission calculations.
"""

from livekit.agents import function_tool, RunContext, ToolError
from typing import Dict, List, Any, Optional


@function_tool()
async def get_vehicle_insurance_quotes(
    context: RunContext,
    vehicle_type: str,
    vehicle_model: str,
    vehicle_age: int,
    coverage_type: str,
    city: str
) -> Dict[str, Any]:
    """
    Get insurance quotes for a vehicle from multiple insurance companies.
    
    Args:
        vehicle_type: Type of vehicle (two_wheeler, four_wheeler, commercial)
        vehicle_model: Model of the vehicle (e.g., "Honda Activa", "Maruti Swift")
        vehicle_age: Age of the vehicle in years
        coverage_type: Type of coverage (third_party, comprehensive, zero_dep)
        city: City where the vehicle is registered
    
    Returns:
        A dictionary containing quotes from different insurance companies
    """
    # Dummy data for different vehicle types and coverage options
    quotes = {
        "quotes": []
    }
    
    if vehicle_type == "two_wheeler":
        quotes["quotes"] = [
            {
                "company": "Bajaj Allianz",
                "premium": 2500,
                "coverage": 150000,
                "features": ["Roadside Assistance", "Personal Accident Cover"],
                "discount": "10% for online purchase"
            },
            {
                "company": "ICICI Lombard",
                "premium": 2200,
                "coverage": 140000,
                "features": ["Zero Depreciation", "Engine Protection"],
                "discount": "No Claim Bonus up to 50%"
            },
            {
                "company": "HDFC ERGO",
                "premium": 2350,
                "coverage": 145000,
                "features": ["Cashless Claims", "24x7 Assistance"],
                "discount": "5% for HDFC Bank customers"
            }
        ]
    elif vehicle_type == "four_wheeler":
        quotes["quotes"] = [
            {
                "company": "Tata AIG",
                "premium": 8500,
                "coverage": 500000,
                "features": ["Zero Depreciation", "Engine Protection", "Key Replacement"],
                "discount": "NCB up to 50% for claim-free years"
            },
            {
                "company": "Reliance General",
                "premium": 7800,
                "coverage": 480000,
                "features": ["Roadside Assistance", "Return to Invoice"],
                "discount": "15% for online purchase"
            },
            {
                "company": "Kotak General Insurance",
                "premium": 8200,
                "coverage": 490000,
                "features": ["Cashless Claims", "Hydrostatic Lock Cover"],
                "discount": "10% for existing customers"
            }
        ]
    elif vehicle_type == "commercial":
        quotes["quotes"] = [
            {
                "company": "New India Assurance",
                "premium": 15000,
                "coverage": 1000000,
                "features": ["Comprehensive Coverage", "Third-party Liability"],
                "discount": "Fleet discount available"
            },
            {
                "company": "Oriental Insurance",
                "premium": 14500,
                "coverage": 950000,
                "features": ["Passenger Cover", "Driver Cover"],
                "discount": "5% for renewal"
            },
            {
                "company": "United India Insurance",
                "premium": 14800,
                "coverage": 980000,
                "features": ["Goods in Transit", "Legal Liability"],
                "discount": "No Claim Bonus up to 40%"
            }
        ]
    
    # Adjust quotes based on vehicle age
    for quote in quotes["quotes"]:
        if vehicle_age > 5:
            quote["premium"] = int(quote["premium"] * 1.2)  # 20% increase for older vehicles
        elif vehicle_age < 2:
            quote["premium"] = int(quote["premium"] * 0.9)  # 10% discount for newer vehicles
    
    # Adjust quotes based on coverage type
    for quote in quotes["quotes"]:
        if coverage_type == "third_party":
            quote["premium"] = int(quote["premium"] * 0.6)  # 40% cheaper for third-party only
            quote["coverage"] = int(quote["coverage"] * 0.5)
        elif coverage_type == "zero_dep":
            quote["premium"] = int(quote["premium"] * 1.3)  # 30% more expensive for zero depreciation
            quote["coverage"] = int(quote["coverage"] * 1.2)
    
    return quotes


@function_tool()
async def get_policy_details(
    context: RunContext,
    policy_id: str
) -> Dict[str, Any]:
    """
    Get detailed information about a specific insurance policy.
    
    Args:
        policy_id: The unique identifier for the policy
    
    Returns:
        A dictionary containing policy details
    """
    # Dummy policy details based on policy ID with 4-digit numeric IDs
    policies = {
        "2001": {
            "policy_number": "2001",
            "customer_id": "1001",
            "customer_name": "Rahul Sharma",
            "vehicle_details": {
                "type": "four_wheeler",
                "model": "Maruti Swift",
                "registration": "3001",
                "year": 2020
            },
            "coverage": {
                "type": "comprehensive",
                "amount": 500000,
                "start_date": "2023-01-15",
                "end_date": "2024-01-14",
                "add_ons": ["Zero Depreciation", "Engine Protection"]
            },
            "premium": 8500,
            "status": "active"
        },
        "2003": {
            "policy_number": "2003",
            "customer_id": "1002",
            "customer_name": "Priya Patel",
            "vehicle_details": {
                "type": "two_wheeler",
                "model": "Honda Activa",
                "registration": "3002",
                "year": 2021
            },
            "coverage": {
                "type": "third_party",
                "amount": 150000,
                "start_date": "2023-05-20",
                "end_date": "2024-05-19",
                "add_ons": []
            },
            "premium": 2200,
            "status": "active"
        },
        "2004": {
            "policy_number": "2004",
            "customer_id": "1003",
            "customer_name": "Amit Singh",
            "vehicle_details": {
                "type": "commercial",
                "model": "Tata Ace",
                "registration": "3003",
                "year": 2019
            },
            "coverage": {
                "type": "comprehensive",
                "amount": 800000,
                "start_date": "2023-03-10",
                "end_date": "2024-03-09",
                "add_ons": ["Passenger Cover", "Goods in Transit"]
            },
            "premium": 15000,
            "status": "active"
        }
    }
    
    # Return a default policy if the policy_id doesn't exist in our dummy data
    if policy_id in policies:
        return policies[policy_id]
    else:
        # Instead of raising an error, return a default policy with the requested ID
        return {
            "policy_number": policy_id,
            "customer_name": "Default Customer",
            "vehicle_details": {
                "type": "four_wheeler",
                "model": "Default Model",
                "registration": "XX00XX0000",
                "year": 2023
            },
            "coverage": {
                "type": "comprehensive",
                "amount": 500000,
                "start_date": "2024-01-01",
                "end_date": "2025-01-01",
                "add_ons": ["Zero Depreciation"]
            },
            "premium": 10000,
            "status": "active"
        }


@function_tool()
async def calculate_premium(
    context: RunContext,
    vehicle_type: str,
    vehicle_value: int,
    vehicle_age: int,
    coverage_type: str,
    add_ons: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Calculate the premium for a vehicle insurance policy.
    
    Args:
        vehicle_type: Type of vehicle (two_wheeler, four_wheeler, commercial)
        vehicle_value: Current market value of the vehicle in INR
        vehicle_age: Age of the vehicle in years
        coverage_type: Type of coverage (third_party, comprehensive, zero_dep)
        add_ons: Optional list of add-on coverages
    
    Returns:
        A dictionary containing premium details and breakdown
    """
    if add_ons is None:
        add_ons = []
    
    # Base premium calculation (dummy logic)
    base_rates = {
        "two_wheeler": 0.02,  # 2% of vehicle value
        "four_wheeler": 0.025,  # 2.5% of vehicle value
        "commercial": 0.035   # 3.5% of vehicle value
    }
    
    coverage_multipliers = {
        "third_party": 0.6,
        "comprehensive": 1.0,
        "zero_dep": 1.3
    }
    
    age_factors = {
        0: 0.9,  # New vehicle discount
        1: 0.95,
        2: 1.0,
        3: 1.05,
        4: 1.1,
        5: 1.15,
        6: 1.2,
        7: 1.25,
        8: 1.3,
        9: 1.35,
        10: 1.4
    }
    
    # Cap vehicle age at 10 years for calculation
    calc_age = min(vehicle_age, 10)
    
    # Calculate base premium
    base_premium = vehicle_value * base_rates.get(vehicle_type, 0.03)
    
    # Apply coverage type multiplier
    adjusted_premium = base_premium * coverage_multipliers.get(coverage_type, 1.0)
    
    # Apply age factor
    adjusted_premium = adjusted_premium * age_factors.get(calc_age, 1.5)
    
    # Calculate add-on costs
    add_on_costs = {}
    total_add_on_cost = 0
    
    add_on_rates = {
        "Zero Depreciation": 0.15 * base_premium,
        "Engine Protection": 0.1 * base_premium,
        "Roadside Assistance": 0.05 * base_premium,
        "Return to Invoice": 0.12 * base_premium,
        "Key Replacement": 0.03 * base_premium,
        "Passenger Cover": 0.08 * base_premium,
        "Driver Cover": 0.07 * base_premium,
        "Goods in Transit": 0.2 * base_premium,
        "Personal Accident Cover": 0.06 * base_premium,
        "Consumables Cover": 0.04 * base_premium
    }
    
    for add_on in add_ons:
        if add_on in add_on_rates:
            cost = add_on_rates[add_on]
            add_on_costs[add_on] = cost
            total_add_on_cost += cost
    
    # Calculate total premium
    total_premium = adjusted_premium + total_add_on_cost
    
    # Apply GST (18%)
    gst = total_premium * 0.18
    final_premium = total_premium + gst
    
    return {
        "base_premium": round(base_premium, 2),
        "adjusted_premium": round(adjusted_premium, 2),
        "add_on_costs": {k: round(v, 2) for k, v in add_on_costs.items()},
        "total_add_on_cost": round(total_add_on_cost, 2),
        "pre_tax_premium": round(total_premium, 2),
        "gst": round(gst, 2),
        "final_premium": round(final_premium, 2)
    }


@function_tool()
async def check_claim_status(
    context: RunContext,
    claim_id: str
) -> Dict[str, Any]:
    """
    Check the status of an insurance claim.
    
    Args:
        claim_id: The unique identifier for the claim
    
    Returns:
        A dictionary containing claim status and details
    """
    # Dummy claim data with 4-digit numeric IDs
    claims = {
        "4001": {
            "claim_id": "4001",
            "policy_id": "2001",
            "customer_id": "1001",
            "customer_name": "Rahul Sharma",
            "vehicle_details": {
                "model": "Maruti Swift",
                "registration": "3001"
            },
            "incident_date": "2023-08-15",
            "claim_amount": 25000,
            "status": "approved",
            "settlement_amount": 22500,
            "processing_time": "5 days",
            "notes": "Claim approved with 10% depreciation"
        },
        "4002": {
            "claim_id": "4002",
            "policy_id": "2003",
            "customer_id": "1002",
            "customer_name": "Priya Patel",
            "vehicle_details": {
                "model": "Honda Activa",
                "registration": "3002"
            },
            "incident_date": "2023-09-20",
            "claim_amount": 8000,
            "status": "processing",
            "processing_time": "2 days so far",
            "notes": "Documents verification in progress"
        },
        "4003": {
            "claim_id": "4003",
            "policy_id": "2004",
            "customer_id": "1003",
            "customer_name": "Amit Singh",
            "vehicle_details": {
                "model": "Tata Ace",
                "registration": "3003"
            },
            "incident_date": "2023-07-05",
            "claim_amount": 45000,
            "status": "rejected",
            "processing_time": "10 days",
            "notes": "Claim rejected due to policy exclusions"
        }
    }
    
    # Return a default claim if the claim_id doesn't exist in our dummy data
    if claim_id in claims:
        return claims[claim_id]
    else:
        # Instead of raising an error, return a default claim with the requested ID
        return {
            "claim_id": claim_id,
            "policy_id": "POL-DEFAULT",
            "customer_name": "Default Customer",
            "vehicle_details": {
                "model": "Default Model",
                "registration": "XX00XX0000"
            },
            "incident_date": "2025-01-01",
            "claim_amount": 15000,
            "status": "processing",
            "processing_time": "3 days so far",
            "notes": "Claim is being processed. Documents verification in progress."
        }


@function_tool()
async def get_agent_commission(
    context: RunContext,
    policy_type: str,
    premium_amount: float,
    is_new_policy: bool,
    insurance_company: str
) -> Dict[str, Any]:
    """
    Calculate the commission an agent will receive for selling an insurance policy.
    
    Args:
        policy_type: Type of policy (two_wheeler, four_wheeler, commercial)
        premium_amount: The premium amount of the policy
        is_new_policy: Whether this is a new policy or a renewal
        insurance_company: The insurance company providing the policy
    
    Returns:
        A dictionary containing commission details
    """
    # Base commission rates by policy type
    base_commission_rates = {
        "two_wheeler": 0.15,  # 15% for two-wheeler policies
        "four_wheeler": 0.175,  # 17.5% for four-wheeler policies
        "commercial": 0.20    # 20% for commercial vehicle policies
    }
    
    # Company-specific adjustments
    company_multipliers = {
        "Bajaj Allianz": 1.05,
        "ICICI Lombard": 1.0,
        "HDFC ERGO": 1.1,
        "Tata AIG": 1.15,
        "Reliance General": 0.95,
        "Kotak General Insurance": 1.0,
        "New India Assurance": 0.9,
        "Oriental Insurance": 0.85,
        "United India Insurance": 0.8,
        # Default for other companies
        "default": 1.0
    }
    
    # Get base commission rate
    base_rate = base_commission_rates.get(policy_type, 0.15)
    
    # Apply new policy vs renewal adjustment
    if not is_new_policy:
        base_rate = base_rate * 0.7  # 30% lower commission for renewals
    
    # Apply company-specific multiplier
    company_multiplier = company_multipliers.get(insurance_company, company_multipliers["default"])
    
    # Calculate commission
    commission_rate = base_rate * company_multiplier
    commission_amount = premium_amount * commission_rate
    
    # Calculate incentives
    incentives = 0
    incentive_details = []
    
    # Monthly target incentive (dummy logic)
    if premium_amount > 10000:
        target_incentive = premium_amount * 0.02
        incentives += target_incentive
        incentive_details.append({
            "type": "Monthly Target Bonus",
            "amount": round(target_incentive, 2)
        })
    
    # Special campaign incentive (dummy logic)
    if insurance_company in ["Bajaj Allianz", "HDFC ERGO", "Tata AIG"] and is_new_policy:
        campaign_incentive = premium_amount * 0.03
        incentives += campaign_incentive
        incentive_details.append({
            "type": "Special Campaign Bonus",
            "amount": round(campaign_incentive, 2)
        })
    
    # Total earnings
    total_earnings = commission_amount + incentives
    
    return {
        "base_commission_rate": f"{base_rate * 100:.2f}%",
        "adjusted_commission_rate": f"{commission_rate * 100:.2f}%",
        "commission_amount": round(commission_amount, 2),
        "incentives": round(incentives, 2),
        "incentive_details": incentive_details,
        "total_earnings": round(total_earnings, 2),
        "payment_timeline": "15th of next month"
    }
