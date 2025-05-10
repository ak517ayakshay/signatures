from fastapi import APIRouter, Query, Depends, Security
from pydantic import BaseModel
from typing import Optional, Dict, List, Any
import datetime

from alyf_pyutils.alyf_provider_utility import ProviderConfigItem

router = APIRouter()

# -----------------------------
# Dependencies this is just for sample 
# -----------------------------

async def token_auth(api_key: str = Security(...)) -> str:
    """
    Dependency function to authenticate token.
    Replace the logic below with actual token validation.
    """
    return " "


# -----------------------------
# Models
# -----------------------------

class MessageHistory(BaseModel):
    message_id: str
    timestamp: datetime.datetime
    message_text: str
    ai_generated: str


class MemberResponse(BaseModel):
    """Response model for member data"""
    member_id: str
    provider_id: str
    active: bool
    first_name: str
    last_name: str
    create_time: datetime.datetime
    update_time: datetime.datetime
    tryv_userid: str
    address: str
    fallback_time_zone: str
    email: str
    synth: bool
    phone_number: str
    height: str
    gender: str
    date_of_birth: datetime.datetime
    databroker_info: Dict[str, Any] = {}
    consent: List[Any] = []
    provider_details: Dict[str, Any] = {}


class DashboardRequest(BaseModel):
    member_id: str
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    vitals: Optional[List[str]] = None


# -----------------------------
# Routes 
# -----------------------------

@router.post("/v1/apc/provider/config_update", status_code=200)
async def provider_config_update(
    config_updates: Dict[ProviderConfigItem, Any],  # This clearly shows key is ProviderConfigItem and value can be any type
    pid: str = Depends(token_auth)
):
    """
    Updates provider configuration settings.
    """
    return None


@router.post("/member_dashboards")
async def get_dashboard(
    dashboard_request: DashboardRequest,
    provider_id: str = Depends(token_auth)
) -> Dict[str, str]:
    """
    Get dashboard data for a member.
    
    Returns:
        Dict[str, str]: A dictionary where:
            - Keys are panel names (e.g., "Heart", "Body", "Mind")
            - Values are iframe HTML strings
     Example:
            {
                "Heart": "<iframe src='https://panels.alyf.health/d/heart_pg/Heart?var-m_id=123&...' />",
                "Body": "<iframe src='https://panels.alyf.health/d/body_pg/Body?var-m_id=123&...' />",
                "Mind": "<iframe src='https://panels.alyf.health/d/mind_pg/Mind?var-m_id=123&...' />"
            }
    """
    return None


@router.delete("/v1/apc/ask_alyf/clear_message_history")
async def clear_message_history(
    provider_id: str = Depends(token_auth),
    member_id: Optional[str] = Query(None, description="Member ID"),
    thread_id: Optional[str] = Query(None, description="Thread ID")
):
    """
    Clear message history for a provider.
    
    Args:
        provider_id: Extracted from the authorization token
        member_id: Optional member ID
        thread_id: Optional thread ID
    """
    return None


@router.get("/v1/member/get", response_model=MemberResponse)
async def get_member_data(
    id: str = Query(None, description="Member ID"),
    email: Optional[str] = Query(None, description="Member email"),
    phone_number: Optional[str] = Query(None, description="Member phone number"),
    provider_id: Optional[str] = Query(None, description="Provider ID to get provider name")
):
    """
    Unified endpoint to get either member data or provider name.
    
    - To get member data: Provide either id, email, or phone_number
    - To get provider name: Provide provider_id
    
    Returns either MemberResponse or ProviderNameResponse based on the provided parameters.
    """
    return None


@router.get("/ask_alyf/get_message_history", response_model=List[MessageHistory])
async def get_message_history(
    provider_id: str = Depends(token_auth),
    member_id: Optional[str] = None,
    thread_id: Optional[str] = None
) -> List[MessageHistory]:
    """
    Get message history for a provider or provider+member combination.
    
    Args:
        provider_id: The provider's ID (authenticated via token)
        member_id: Optional member ID to filter messages
        thread_id: Optional thread ID to filter messages
        
    Returns:
        List of message history entries
    """
    return None
