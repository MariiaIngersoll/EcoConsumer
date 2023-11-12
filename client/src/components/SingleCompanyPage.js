import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { setSingleCompany } from "../redux_store/CompaniesSlice";
import { useParams } from "react-router-dom";

function SingleCompanyPage( ) {
  const { companyId } = useParams();
  const dispatch = useDispatch();

  useEffect(() => {
    fetch(`http://127.0.0.1:5555/api/manufacturers/${companyId}`)
      .then((r) => r.json())
      .then((data) => {
        dispatch(setSingleCompany(data)); 
      });
  }, [dispatch, companyId]);

  const singleCompany = useSelector((state) => state.companies.singleCompany);
  
  if (!singleCompany) {
    return <div>Loading...</div>;
  }

  return (
    <div className="single-company-page">
      <h1>{singleCompany.name}</h1>
      <img src={singleCompany.image} alt={singleCompany.name} />
      <p>{singleCompany.description}</p>
      <h2>Products:</h2>
      <ul className="company-products-div">
        {singleCompany.products.map((product) => (
          <li key={product.id}>
            {product.name}
            <img src={product.image} alt={product.name} />
          </li>
        ))}
      </ul>
    </div>
  );

}

export default SingleCompanyPage