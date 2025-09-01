import json
from api_request import send_api_request, get_family
from auth_helper import AuthInstance
from ui import pause

PACKAGE_FAMILY_CODE = "5d63dddd-4f90-4f4c-8438-2f005c20151f"

def get_package_edu():
    api_key = AuthInstance.api_key
    tokens = AuthInstance.get_active_tokens()
    if not tokens:
        print("No active user tokens found.")
        pause()
        return []

    # Ambil data family dari API
    data = get_family(api_key, tokens, PACKAGE_FAMILY_CODE)
    if not data or "package_variants" not in data:
        print("Failed to fetch package data.")
        pause()
        return []

    packages = []
    start_number = 1

    # Iterasi tiap variant dan option
    for variant in data.get("package_variants", []):
        for option in variant.get("package_options", []):
            friendly_name = option.get("name", "Unnamed Package")
            price = option.get("price", "Unknown")
            code = option.get("package_option_code", "")

            packages.append({
                "number": start_number,
                "name": friendly_name,
                "price": price,
                "code": code
            })

            start_number += 1

    return packages
