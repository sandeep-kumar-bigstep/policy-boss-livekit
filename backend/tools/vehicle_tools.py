"""
Vehicle Tools for Vehicle Insurance Agent

This module contains tools related to vehicle information and validation.
"""

from livekit.agents import function_tool, RunContext, ToolError
from typing import Dict, Any, Optional


@function_tool()
async def get_vehicle_details(
    context: RunContext,
    registration_number: str
) -> Dict[str, Any]:
    """
    Get detailed information about a vehicle based on its registration number.
    
    Args:
        registration_number: The vehicle registration number (e.g., "MH01AB1234")
    
    Returns:
        A dictionary containing vehicle details
    """
    # Dummy vehicle database with 4-digit numeric IDs in sequential order
    vehicles = {
        "3001": {
            "registration": "3001",
            "customer_id": "1001",
            "make": "Maruti Suzuki",
            "model": "Swift",
            "variant": "VXI",
            "fuel_type": "Petrol",
            "year": 2020,
            "engine_number": "K12MN1234567",
            "chassis_number": "MA3EJKD1S00123456",
            "seating_capacity": 5,
            "cubic_capacity": 1197,
            "registration_date": "2020-03-15",
            "insurance_history": [
                {
                    "policy_number": "2001",
                    "insurer": "Bajaj Allianz",
                    "period": "2022-03-15 to 2023-03-14"
                },
                {
                    "policy_number": "2001",
                    "insurer": "Bajaj Allianz",
                    "period": "2023-03-15 to 2024-03-14"
                }
            ],
            "owner_name": "Rahul Sharma",
            "rto": "Mumbai Central RTO",
            "hypothecation": None
        },
        "3002": {
            "registration": "3002",
            "customer_id": "1002",
            "make": "Honda",
            "model": "Activa 6G",
            "variant": "Standard",
            "fuel_type": "Petrol",
            "year": 2021,
            "engine_number": "JF16ET1234567",
            "chassis_number": "ME4JF165LT1234567",
            "seating_capacity": 2,
            "cubic_capacity": 109,
            "registration_date": "2021-06-10",
            "insurance_history": [
                {
                    "policy_number": "2003",
                    "insurer": "ICICI Lombard",
                    "period": "2021-06-10 to 2022-06-09"
                },
                {
                    "policy_number": "2003",
                    "insurer": "ICICI Lombard",
                    "period": "2022-06-10 to 2023-06-09"
                },
                {
                    "policy_number": "2003",
                    "insurer": "ICICI Lombard",
                    "period": "2023-06-10 to 2024-06-09"
                }
            ],
            "owner_name": "Priya Patel",
            "rto": "Delhi South RTO",
            "hypothecation": None
        },
        "3003": {
            "registration": "3003",
            "customer_id": "1003",
            "make": "Tata",
            "model": "Ace",
            "variant": "HT",
            "fuel_type": "Diesel",
            "year": 2019,
            "engine_number": "275IDT1234567",
            "chassis_number": "MAT445075L1234567",
            "seating_capacity": 2,
            "cubic_capacity": 702,
            "registration_date": "2019-08-22",
            "insurance_history": [
                {
                    "policy_number": "2004",
                    "insurer": "New India Assurance",
                    "period": "2022-08-22 to 2023-08-21"
                },
                {
                    "policy_number": "2004",
                    "insurer": "New India Assurance",
                    "period": "2023-08-22 to 2024-08-21"
                }
            ],
            "owner_name": "Amit Singh",
            "rto": "Bangalore Central RTO",
            "hypothecation": "HDFC Bank"
        }
    }
    
    # Return a default vehicle if the registration_number doesn't exist in our dummy data
    if registration_number in vehicles:
        return vehicles[registration_number]
    else:
        # Instead of raising an error, return a default vehicle with the requested registration number
        return {
            "registration": registration_number,
            "make": "Default Manufacturer",
            "model": "Default Model",
            "variant": "Standard",
            "fuel_type": "Petrol",
            "year": 2023,
            "engine_number": "DEFAULT123456",
            "chassis_number": "DEFAULT123456789",
            "seating_capacity": 5,
            "cubic_capacity": 1200,
            "registration_date": "2023-01-01",
            "insurance_history": [
                {
                    "policy_number": f"POL-{registration_number}-001",
                    "insurer": "Default Insurance",
                    "period": "2023-01-01 to 2024-01-01"
                },
                {
                    "policy_number": f"POL-{registration_number}-002",
                    "insurer": "Default Insurance",
                    "period": "2024-01-01 to 2025-01-01"
                }
            ],
            "owner_name": "Default Owner",
            "rto": "Default RTO",
            "hypothecation": None
        }


@function_tool()
async def validate_vehicle_registration(
    context: RunContext,
    registration_number: str
) -> Dict[str, Any]:
    """
    Validate a vehicle registration number and check if it follows the correct format.
    
    Args:
        registration_number: The vehicle registration number to validate
    
    Returns:
        A dictionary containing validation results
    """
    import re
    
    # Basic validation for Indian vehicle registration format
    # Format: [State Code (2)] [District Code (2)] [Series (1-3)] [Number (4)]
    # Example: MH01AB1234, KA02EF9012
    
    pattern = r'^[A-Z]{2}[0-9]{2}[A-Z]{1,3}[0-9]{4}$'
    
    is_valid = bool(re.match(pattern, registration_number))
    
    if not is_valid:
        return {
            "is_valid": False,
            "message": "Invalid registration number format. Expected format: [State Code (2)][District Code (2)][Series (1-3)][Number (4)]",
            "examples": ["MH01AB1234", "KA02EF9012", "DL05CD5678"]
        }
    
    # Extract state code for additional information
    state_code = registration_number[:2]
    
    # Dummy state code mapping
    state_codes = {
        "MH": "Maharashtra",
        "DL": "Delhi",
        "KA": "Karnataka",
        "TN": "Tamil Nadu",
        "GJ": "Gujarat",
        "UP": "Uttar Pradesh",
        "HR": "Haryana",
        "AP": "Andhra Pradesh",
        "TS": "Telangana",
        "KL": "Kerala",
        "MP": "Madhya Pradesh",
        "PB": "Punjab",
        "RJ": "Rajasthan",
        "WB": "West Bengal",
        "BR": "Bihar"
    }
    
    state_name = state_codes.get(state_code, "Unknown State")
    
    # Extract district code
    district_code = registration_number[2:4]
    
    return {
        "is_valid": True,
        "registration_number": registration_number,
        "state_code": state_code,
        "state_name": state_name,
        "district_code": district_code,
        "series": registration_number[4:-4],
        "number": registration_number[-4:],
        "message": "Valid registration number format"
    }
