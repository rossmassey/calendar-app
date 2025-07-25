import json
import os
from typing import Dict, List, Optional, Any
from pathlib import Path

class CityGlowService:
    """Service class for handling City Glow Florida booking data"""
    
    def __init__(self):
        self.startup_data: Optional[Dict[str, Any]] = None
        self._load_services_data()
    
    def _load_services_data(self):
        """Load services data from JSON file"""
        try:
            # Look for services.json in the project root
            json_path = Path(__file__).parent.parent.parent / "services.json"
            
            if not json_path.exists():
                raise FileNotFoundError(f"services.json not found at {json_path}")
            
            with open(json_path, 'r') as f:
                content = f.read()
                # The file contains a string representation of a dict, so we need to eval it
                self.startup_data = eval(content)
                
        except Exception as e:
            raise Exception(f"Failed to load services.json: {e}")
    
    def get_service_categories(self) -> Dict[str, Any]:
        """Get all available service categories"""
        if not self.startup_data:
            raise Exception("Services data not loaded")
        
        categories = self.startup_data['servicesInfo']['serviceCategories']
        
        return {
            "total": len(categories),
            "categories": [
                {
                    "id": category['id'],
                    "name": category['name']
                }
                for category in categories
            ]
        }
    
    def get_services_by_category(self, service_category: str) -> Dict[str, Any]:
        """Get all services within a specific category"""
        if not self.startup_data:
            raise Exception("Services data not loaded")
        
        categories = self.startup_data['servicesInfo']['serviceCategories']
        services = self.startup_data['servicesInfo']['servicesById']
        
        # Find category ID
        category_id = None
        for category in categories:
            if category['name'].lower() == service_category.lower():
                category_id = category['id']
                break
        
        if not category_id:
            raise ValueError(f"Service category '{service_category}' not found")
        
        # Filter services by category
        filtered_services = {}
        for sid, sinfo in services.items():
            if sinfo['serviceCategoryId'] == category_id:
                filtered_services[sid] = sinfo
        
        return {
            "category": service_category,
            "category_id": category_id,
            "total": len(filtered_services),
            "services": [
                {
                    "id": int(service_id),
                    "name": service_info['name'],
                    "price": service_info['defaultPrice'],
                    "duration": service_info['defaultDuration'],
                    "description": service_info.get('description')
                }
                for service_id, service_info in filtered_services.items()
            ]
        }
    
    def get_addons_by_service(self, service_name: str) -> Dict[str, Any]:
        """Get available add-ons for a specific service"""
        if not self.startup_data:
            raise Exception("Services data not loaded")
        
        services = self.startup_data['servicesInfo']['servicesById']
        
        # Find service ID by name
        selected_service_id = None
        for service_id, service_info in services.items():
            if service_info['name'].lower() == service_name.lower():
                selected_service_id = service_id
                break
        
        if not selected_service_id:
            raise ValueError(f"Service '{service_name}' not found")
        
        # Get option group IDs for this service
        option_group_ids = self.startup_data['servicesInfo'].get(
            'serviceOptionGroupIdsByServiceId', {}
        ).get(selected_service_id, [])
        
        if not option_group_ids:
            return {
                "service": service_name,
                "service_id": int(selected_service_id),
                "total_groups": 0,
                "addon_groups": []
            }
        
        option_groups = self.startup_data['servicesInfo']['serviceOptionGroupsById']
        service_options = self.startup_data['servicesInfo']['serviceOptionsById']
        
        addon_groups = []
        for group_id in option_group_ids:
            group = option_groups[str(group_id)]
            
            # Find options in this group
            group_options = []
            for opt_id, option in service_options.items():
                if option['serviceOptionGroupId'] == group_id:
                    group_options.append({
                        "id": int(opt_id),
                        "name": option['name'],
                        "price": option['price']
                    })
            
            addon_groups.append({
                "group_id": group_id,
                "group_name": group['name'],
                "prompt": group['prompt'],
                "options": group_options
            })
        
        return {
            "service": service_name,
            "service_id": int(selected_service_id),
            "total_groups": len(option_group_ids),
            "addon_groups": addon_groups
        }
    
    def get_staff_by_service(self, service_name: str) -> Dict[str, Any]:
        """Get available staff for a specific service"""
        if not self.startup_data:
            raise Exception("Services data not loaded")
        
        services = self.startup_data['servicesInfo']['servicesById']
        staff_by_id = self.startup_data['staffInfo']['staffById']
        staff_ids_by_service = self.startup_data['staffInfo']['staffIdsByServiceId']
        
        # Find service ID by name
        selected_service_id = None
        for service_id, service_info in services.items():
            if service_info['name'].lower() == service_name.lower():
                selected_service_id = service_id
                break
        
        if not selected_service_id:
            raise ValueError(f"Service '{service_name}' not found")
        
        # Get available staff for this service
        if selected_service_id not in staff_ids_by_service:
            return {
                "service": service_name,
                "service_id": int(selected_service_id),
                "total": 0,
                "staff": []
            }
        
        available_staff_ids = staff_ids_by_service[selected_service_id]
        
        staff_list = []
        for staff_id in available_staff_ids:
            staff = staff_by_id[str(staff_id)]
            full_name = staff['firstName']
            if staff.get('lastName'):
                full_name += f" {staff['lastName']}"
            
            staff_list.append({
                "id": staff_id,
                "name": full_name,
                "first_name": staff['firstName'],
                "last_name": staff.get('lastName')
            })
        
        return {
            "service": service_name,
            "service_id": int(selected_service_id),
            "total": len(available_staff_ids),
            "staff": staff_list
        }
    
    def get_all_data(self) -> Dict[str, Any]:
        """Get all data in a structured format: categories -> services -> (staff + addons)"""
        if not self.startup_data:
            raise Exception("Services data not loaded")
        
        categories = self.startup_data['servicesInfo']['serviceCategories']
        services = self.startup_data['servicesInfo']['servicesById']
        staff_by_id = self.startup_data['staffInfo']['staffById']
        staff_ids_by_service = self.startup_data['staffInfo']['staffIdsByServiceId']
        option_groups = self.startup_data['servicesInfo'].get('serviceOptionGroupsById', {})
        service_options = self.startup_data['servicesInfo'].get('serviceOptionsById', {})
        service_option_groups = self.startup_data['servicesInfo'].get('serviceOptionGroupIdsByServiceId', {})
        
        result_categories = []
        
        for category in categories:
            category_data = {
                "id": category['id'],
                "name": category['name'],
                "services": []
            }
            
            # Get all services for this category
            for service_id, service_info in services.items():
                if service_info['serviceCategoryId'] == category['id']:
                    
                    # Get staff for this service
                    service_staff = []
                    if service_id in staff_ids_by_service:
                        for staff_id in staff_ids_by_service[service_id]:
                            staff = staff_by_id[str(staff_id)]
                            full_name = staff['firstName']
                            if staff.get('lastName'):
                                full_name += f" {staff['lastName']}"
                            service_staff.append({
                                "id": staff_id,
                                "name": full_name
                            })
                    
                    # Get addons for this service
                    service_addons = []
                    if service_id in service_option_groups:
                        for group_id in service_option_groups[service_id]:
                            group = option_groups.get(str(group_id), {})
                            group_options = []
                            
                            for opt_id, option in service_options.items():
                                if option.get('serviceOptionGroupId') == group_id:
                                    group_options.append({
                                        "id": int(opt_id),
                                        "name": option['name'],
                                        "price": option['price']
                                    })
                            
                            if group:
                                service_addons.append({
                                    "group_id": group_id,
                                    "group_name": group.get('name', ''),
                                    "options": group_options
                                })
                    
                    category_data["services"].append({
                        "id": int(service_id),
                        "name": service_info['name'],
                        "price": service_info['defaultPrice'],
                        "duration": service_info['defaultDuration'],
                        "description": service_info.get('description'),
                        "staff": service_staff,
                        "addons": service_addons
                    })
            
            result_categories.append(category_data)
        
        return {
            "total_categories": len(categories),
            "categories": result_categories
        }

# Global instance
cityglow_service = CityGlowService() 