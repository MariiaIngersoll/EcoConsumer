import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { setCompanies} from "../redux_store/CompaniesSlice";
import SingleCompanyPage from "./SingleCompanyPage";


function AllCompanies() {
  const dispatch = useDispatch();
  const companies = useSelector((state) => state.companies.companies);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/api/manufacturers")
      .then((r) => r.json())
      .then((data) => {
        dispatch(setCompanies(data));
      });
  }, [dispatch]);

  const companiesArray = companies.map((company) => (
    <SingleCompanyPage company={company} key={company.id} />
  ));

  console.log(companiesArray)

  return (
    <>
      <div className="companies-container">
        {companiesArray}
      </div>
    </>
  );
}

export default AllCompanies;