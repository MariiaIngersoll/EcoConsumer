import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { setCompanies} from "../redux_store/CompaniesSlice";
import { useNavigate } from "react-router-dom";


function AllCompanies() {
  const dispatch = useDispatch();
  const companies = useSelector((state) => state.companies.companies);
  const navigate = useNavigate();

  useEffect(() => {
    fetch("/api/manufacturers")
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
      <p className="paragraphForAllCompanies">Discover a collection of eco-conscious companies driven by their commitment to sustainability on our platform. Each partner we feature holds a core value in aligning their business practices with a focus on the environment. From pioneering renewable energy providers to innovative sustainable product manufacturers, these companies stand as pillars in the realm of eco-consciousness. Through their contributions, they redefine success, proving that thriving businesses and environmental care can go hand in hand. Join us in supporting these trailblazers, taking steps towards a greener future.</p>
      {companies.map((company) => (
        <div
          className="single-company"
          key={company.id}
          onClick={() => handleCompanyClick(company.id)}
        >
        <img src={company.image} alt={`Product: ${company.name}`} />
        <h1>{company.name}</h1>
        </div>
      ))}
    </div>
  );
  }
  
  export default AllCompanies;