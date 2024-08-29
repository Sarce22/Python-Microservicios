from fastapi import APIRouter, Body
from ..models.company import Company

company_route = APIRouter()

@company_route.get("/")
async def get_all_companies():
    try: 
        return {"message": f"All company data"}
    except Exception as e:
        print(e)
        return {"error":str(e)}

@company_route.get("/{company_id}")
async def get_company(company_id: int):
    try: 
        return {"message": f"COmpany book for ID {company_id}"}
    except Exception as e:
        print(e)
        return {"error":str(e)}

@company_route.post("/")
async def create_company(company: Company = Body(...)):
    try: 
        return {"message": "Company created", "comapny": company}
    except Exception as e:
        print(e)
        return {"error":str(e)}

@company_route.put("/{company_id}")
async def update_company(company_id: int, company: Company = Body(...)):
    try: 
        return {"message": f"Company with ID {company_id} updated", "company": company}
    except Exception as e:
        print(e)
        return {"error":str(e)}

@company_route.delete("/{company_id}")
async def delete_company(company_id: int):
    try: 
        return {"message": f"Company with ID {company_id} deleted"}
    except Exception as e:
        print(e)
        return {"error":str(e)}