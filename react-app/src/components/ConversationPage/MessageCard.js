import React, { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { Modal } from "../../context/Modal";

function MessageCard({ review }) {
    const history = useHistory();
    const sessionUser = useSelector((state) => state.session.user);

    const [showEditModal, setShowEditModal] = useState(false);
    const [showDeleteModal, setShowDeleteModal] = useState(false);
    const [reviewUser, setReviewUser] = useState({});
    const userId = review.userId;

    useEffect(() => {
        if (!sessionUser) history.push("/");
    }, [sessionUser, history]);

    useEffect(() => {
        let isMounted = true;
        if (!userId) {
            return;
        }
        (async () => {
            const response = await fetch(`/api/users/${userId}`);
            const reviewUser = await response.json();
            if (isMounted) {
                setReviewUser(reviewUser);
            }
        })();

        return () => {
            isMounted = false;
        };
    }, [userId]);

    return (
        <div className="listing-container">
            <div className="review-details">
                <h2 id="listing-title">{review?.username}</h2>

                <h3 id="listing-rating">{review?.text}</h3>
            </div>
            <div className="review-actions">
                <h4 id="listing-rating">
                    {review.rating ? `Review by: ${reviewUser.username}` : ""}
                </h4>
            </div>
        </div>
    );
}

export default MessageCard;
