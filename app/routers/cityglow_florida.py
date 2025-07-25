from fastapi import APIRouter, HTTPException
from typing import Dict, Any
from app.services.cityglow_service import cityglow_service

router = APIRouter()



@router.get("/service_categories", summary="Get Service Categories")
async def get_service_categories() -> Dict[str, Any]:
    """Get all available service categories"""
    try:
        return cityglow_service.get_service_categories()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading service categories: {str(e)}")


@router.get("/services/{service_category}", summary="Get Services by Category")
async def get_services(service_category: str) -> Dict[str, Any]:
    """Get all services within a specific category"""
    try:
        return cityglow_service.get_services_by_category(service_category)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading services: {str(e)}")


@router.get("/addons/{service_name}", summary="Get Service Add-ons")
async def get_addons(service_name: str) -> Dict[str, Any]:
    """Get available add-ons for a specific service"""
    try:
        return cityglow_service.get_addons_by_service(service_name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading add-ons: {str(e)}")


@router.get("/staff/{service_name}", summary="Get Service Staff")
async def get_staff(service_name: str) -> Dict[str, Any]:
    """Get available staff for a specific service"""
    try:
        return cityglow_service.get_staff_by_service(service_name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading staff: {str(e)}")


@router.get("/get_all", summary="Get All Data")
async def get_all() -> Dict[str, Any]:
    """Get all data in a structured format:

    ```
    {
        "total_categories": <number>,
        "categories": [
            {
                "id": <category_id>,
                "name": "<category_name>",
                "services": [
                    {
                    "id": <service_id>,
                    "name": "<service_name>",
                    "price": <default_price>,
                    "duration": <default_duration_minutes>,
                    "description": "<service_description>",
                    "staff": [
                        {
                            "id": <staff_id>,
                            "name": "<full_name>"
                        }
                    ],
                    "addons": [
                        {
                            "group_id": <addon_group_id>,
                            "group_name": "<addon_group_name>",
                            "options": [
                                {
                                    "id": <option_id>,
                                    "name": "<option_name>",
                                    "price": <option_price>
                                }
                            ]
                        }
                ]
            }
        ]
    }
    ```
    
    """
    try:
        return cityglow_service.get_all_data()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading all data: {str(e)}")


@router.get("/refresh_data", summary="Refresh Services Data")
async def refresh_data() -> Dict[str, Any]:
    """Refresh services data by fetching latest from mangomint API"""
    try:
        # Use the service's reload method which handles the API call
        cityglow_service.reload_data()
        
        # Get some stats from the reloaded data
        categories_count = len(cityglow_service.startup_data.get('servicesInfo', {}).get('serviceCategories', []))
        services_count = len(cityglow_service.startup_data.get('servicesInfo', {}).get('servicesById', {}))
        
        return {
            "success": True,
            "message": "Services data refreshed successfully",
            "categories_count": categories_count,
            "services_count": services_count
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error refreshing services data: {str(e)}"
        ) 