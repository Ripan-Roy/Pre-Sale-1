from pydantic import BaseModel, EmailStr
from typing import Optional


class SellerModel(BaseModel):
    # Basic Information
    seller_name: str
    email: EmailStr
    phone_number: str
    business_type: str

    # Business Details
    business_name: str
    business_registration_number: str
    business_license_number: Optional[str]
    gst_vat_number: str
    pan_tin: str

    # Address Information
    registered_address: str
    warehouse_address: Optional[str]
    return_address: Optional[str]

    # Banking Information
    bank_account_holder_name: str
    bank_account_number: str
    bank_name: str
    branch_name: str
    ifsc_swift_code: str

    # Product Information
    product_categories: str
    brand_name: str
    product_types: str

    # Legal Documents
    id_proof: str
    address_proof: str
    business_license_document: str
    tax_documents: str

    # Logistics & Shipping
    preferred_courier_partners: Optional[str]
    shipping_zones: Optional[str]
    return_policy: Optional[str]

    # Customer Support
    support_contact_email: Optional[EmailStr]
    support_contact_phone: Optional[str]
    customer_service_hours: Optional[str]

    # Compliance & Agreements
    terms_of_service_agreement: bool = False
    privacy_policy_agreement: bool = False
    kyc_compliance: bool = False

    # Miscellaneous
    seller_profile_description: Optional[str]
    logo_or_brand_image: Optional[str]
    store_url: Optional[str]

    class Config:
        orm_mode = True


