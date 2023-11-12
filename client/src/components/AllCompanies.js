import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { setCompanies} from "../redux_store/CompaniesSlice";
import { useNavigate } from "react-router-dom";


function AllCompanies() {
  const dispatch = useDispatch();
  const companies = useSelector((state) => state.companies.companies);
  const navigate = useNavigate();

  useEffect(() => {
    fetch("http://127.0.0.1:5555/api/manufacturers")
      .then((r) => r.json())
      .then((data) => {
        dispatch(setCompanies(data));
      });
  }, [dispatch]);

  const handleCompanyClick = (companyId) => {
    navigate(`/companies/${companyId}`);
  };

  return (
    <div className="companies-container">
      {companies.map((company) => (
        <div
          className="single-company"
          key={company.id}
          onClick={() => handleCompanyClick(company.id)}
        >
        <img src={company.image}></img>
        <h1>{company.name}</h1>
        </div>
      ))}
    </div>
  );
  }
  
  export default AllCompanies;