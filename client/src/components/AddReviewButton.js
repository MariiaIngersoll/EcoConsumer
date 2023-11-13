import React, { useEffect, useState } from "react";

function AddReviewButton() {

    const [showForm, setShowForm] = useState(false)
    const [content, setContent] = useState("")
    const [reviews, setReviews] = useState([])
    const [rating, setRating] = useState(0);

    useEffect(()=> {
        fetch("http://127.0.0.1:5555/api/reviews")
        .then((r) => r.json())
        .then((data) => setReviews(data))
    }, [])

    const onClickButton = () => {
        setShowForm(true)
    }

    const handleInputChange = (e) => {
        setContent(e.target.value);
    };

    const handleRatingChange = (e) => {
        setRating(e.target.value);
    };

    const handleAddReview = (e) => {
        e.preventDefault();
        const reviewData = {
            content: content,
            rating: rating,
        };
        fetch("http://127.0.0.1:5555/api/reviews", {
            method: "POST",
            headers: {
            "Content-Type": "application/json",
            },
            body: JSON.stringify(reviewData),
        })
            .then((r) => r.json())
            .then((newItem) => {
            console.log(newItem)
            setReviews(newItem)});
            
            
    }

    return (
        <div>
            <button onClick={onClickButton}>Add Review</button>
            {showForm && (
                <form >
                    <input
                        type="number"
                        value={rating}
                        onChange={handleRatingChange}
                        placeholder="Rating (1-5)"
                    ></input>
                    <textarea className="review"
                        value={content}
                        onChange={handleInputChange}
                        
                        placeholder="Type your review here..."
                    ></textarea>
                    <button onClick={handleAddReview}>Submit Review</button>
                </form>
            )}
        </div>
    )
}

export default AddReviewButton