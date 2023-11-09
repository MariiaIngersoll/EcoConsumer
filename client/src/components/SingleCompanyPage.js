import React from "react";

function SingleCompanyPage( {company} ) {

    return (
        <div className="single-company">
            <img src={company.image} alt={company.name} />
            <h1>{company.name}</h1>
        </div>
    )
}

export default SingleCompanyPage