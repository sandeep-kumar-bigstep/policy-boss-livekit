"""
Customer Tools for Vehicle Insurance Agent

This module contains tools related to customer profiles and policy management.
"""

from livekit.agents import function_tool, RunContext, ToolError
from typing import Dict, List, Any, Optional


@function_tool()
async def get_customer_profile(
    context: RunContext,
    customer_id: str
) -> Dict[str, Any]:
    """
    Get detailed profile information for a customer.
    
    Args:
        customer_id: The unique identifier for the customer
    
    Returns:
        A dictionary containing customer profile details
    """
    # Dummy customer profiles with 4-digit numeric IDs in sequential order
    customers = {
        "1001": {
            "customer_id": "1001",
            "name": "Rahul Sharma",
            "age": 35,
            "gender": "Male",
            "contact": {
                "phone": "+91 9876543210",
                "email": "rahul.sharma@example.com",
                "address": "123 Park Street, Mumbai, Maharashtra"
            },
            "occupation": "Software Engineer",
            "driving_experience": 12,
            "claim_history": {
                "total_claims": 1,
                "last_claim_date": "2022-05-10"
            },
            "customer_since": "2018-03-15"
        },
        "1002": {
            "customer_id": "1002",
            "name": "Priya Patel",
            "age": 28,
            "gender": "Female",
            "contact": {
                "phone": "+91 8765432109",
                "email": "priya.patel@example.com",
                "address": "456 Lake View, Delhi"
            },
            "occupation": "Doctor",
            "driving_experience": 8,
            "claim_history": {
                "total_claims": 0,
                "last_claim_date": None
            },
            "customer_since": "2020-07-22"
        },
        "1003": {
            "customer_id": "1003",
            "name": "Amit Singh",
            "age": 42,
            "gender": "Male",
            "contact": {
                "phone": "+91 7654321098",
                "email": "amit.singh@example.com",
                "address": "789 Business Park, Bangalore, Karnataka"
            },
            "occupation": "Business Owner",
            "driving_experience": 20,
            "claim_history": {
                "total_claims": 2,
                "last_claim_date": "2023-01-18"
            },
            "customer_since": "2015-11-30"
        }
    }
    
    # Return a default customer if the customer_id doesn't exist in our dummy data
    if customer_id in customers:
        return customers[customer_id]
    else:
        # Instead of raising an error, return a default customer with the requested ID
        return {
            "customer_id": customer_id,
            "name": "Default Customer",
            "age": 30,
            "gender": "Not Specified",
            "contact": {
                "phone": "+91 9999999999",
                "email": "default.customer@example.com",
                "address": "Default Address, Default City, Default State"
            },
            "occupation": "Not Specified",
            "driving_experience": 5,
            "claim_history": {
                "total_claims": 0,
                "last_claim_date": None
            },
            "customer_since": "2024-01-01"
        }


@function_tool()
async def update_customer_details(
    context: RunContext,
    customer_id: str,
    field: str,
    value: str
) -> Dict[str, Any]:
    """
    Update a specific field in a customer's profile.
    
    Args:
        customer_id: The unique identifier for the customer
        field: The field to update (e.g., "phone", "email", "address")
        value: The new value for the field
    
    Returns:
        A dictionary containing the update status and updated field
    """
    # Dummy function to simulate updating customer details
    valid_fields = [
        "phone", "email", "address", "occupation", 
        "driving_experience", "age"
    ]
    
    # Always proceed with the update, even if the field is invalid or customer doesn't exist
    valid_field = field if field in valid_fields else "address"
    
    # Check if the customer exists in our dummy data
    customers = {
        "1001": "Rahul Sharma",
        "1002": "Priya Patel",
        "1003": "Amit Singh"
    }
    
    # Use the customer name if it exists, otherwise use a default name
    customer_name = customers.get(customer_id, "Default Customer")
        
    # In a real implementation, this would update a database
    return {
        "success": True,
        "customer_id": customer_id,
        "customer_name": customer_name,
        "updated_field": valid_field,
        "old_value": "Previous value would be fetched from database",
        "new_value": value,
        "timestamp": "2025-05-14T17:10:50+05:30"
    }


@function_tool()
async def get_customer_policies(
    context: RunContext,
    customer_id: str,
    policy_status: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get all insurance policies for a specific customer.
    
    Args:
        customer_id: The unique identifier for the customer
        policy_status: Optional filter for policy status (active, expired, pending)
    
    Returns:
        A dictionary containing the customer's policies
    """
    # Dummy customer policies with 4-digit numeric customer IDs
    customer_policies = {
        "1001": [
            {
                "policy_id": "2001",
                "type": "four_wheeler",
                "vehicle": "Maruti Swift",
                "coverage": 500000,
                "premium": 8500,
                "start_date": "2023-01-15",
                "end_date": "2024-01-14",
                "status": "active"
            },
            {
                "policy_id": "2002",
                "type": "two_wheeler",
                "vehicle": "Honda CB Shine",
                "coverage": 150000,
                "premium": 2300,
                "start_date": "2022-05-10",
                "end_date": "2023-05-09",
                "status": "expired"
            }
        ],
        "1002": [
            {
                "policy_id": "2003",
                "type": "two_wheeler",
                "vehicle": "Honda Activa",
                "coverage": 150000,
                "premium": 2200,
                "start_date": "2023-05-20",
                "end_date": "2024-05-19",
                "status": "active"
            }
        ],
        "1003": [
            {
                "policy_id": "2004",
                "type": "commercial",
                "vehicle": "Tata Ace",
                "coverage": 800000,
                "premium": 15000,
                "start_date": "2023-03-10",
                "end_date": "2024-03-09",
                "status": "active"
            },
            {
                "policy_id": "2005",
                "type": "four_wheeler",
                "vehicle": "Toyota Innova",
                "coverage": 650000,
                "premium": 12000,
                "start_date": "2023-08-15",
                "end_date": "2024-08-14",
                "status": "active"
            },
            {
                "policy_id": "2006",
                "type": "four_wheeler",
                "vehicle": "Hyundai i20",
                "coverage": 450000,
                "premium": 7500,
                "start_date": "2022-12-01",
                "end_date": "2023-11-30",
                "status": "pending_renewal"
            }
        ]
    }
    
    if customer_id not in customer_policies:
        # Instead of raising an error, return a default policy list
        policies = [
            {
                "policy_id": f"POL-{customer_id}-001",
                "type": "four_wheeler",
                "vehicle": "Default Vehicle",
                "coverage": 500000,
                "premium": 10000,
                "start_date": "2024-01-01",
                "end_date": "2025-01-01",
                "status": "active"
            }
        ]
        return {
            "customer_id": customer_id,
            "policy_count": 1,
            "policies": policies
        }
    
    policies = customer_policies[customer_id]
    
    # Filter by status if provided
    if policy_status:
        policies = [p for p in policies if p["status"] == policy_status]
    
    return {
        "customer_id": customer_id,
        "policy_count": len(policies),
        "policies": policies
    }
