from fastapi import APIRouter, Body
from models.company import Company


from database import CompanyModel
company_route = APIRouter()

@company_route.get("/companies")
def get_all_companies():
    companies = list(CompanyModel.select().dicts())
    return companies

@company_route.get("/companies/{company_id}")
def get_company(company_id: int):
    try:
        company = CompanyModel.get(CompanyModel.id == company_id)
        return company
    except Exception as e:
        print(e)
        return {"error": str(e)}
    
@company_route.post("/companies")
def create_company(company: Company = Body(...)):
    new_company = CompanyModel.create(
        name=company.name,
        address=company.address,
        city=company.city,
        state=company.state,
        phone_number=company.phone_number,
        email=company.email,
        website=company.website
    )
    return new_company

@company_route.put("/companies/{company_id}")
def update_company(company_id: int, company_data: Company = Body(...)):
    try:
        company = CompanyModel.get(CompanyModel.id == company_id)
        company.name = company_data.name
        company.address = company_data.address
        company.city = company_data.city
        company.state = company_data.state
        company.phone_number = company_data.phone_number
        company.email = company_data.email
        company.website = company_data.website
        company.save()
        return company
    except Exception as e:
        print(e)
        return {"error": str(e)}
    

@company_route.delete("/companies/{company_id}")
def delete_company(company_id: int):
    try:
        company = CompanyModel.get(CompanyModel.id == company_id)
        company.delete_instance()
        return {"message": "Company deleted successfully"}
    except Exception as e:
        print(e)
        return {"error": str(e)}