import React, { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { NavLink } from "react-router-dom/cjs/react-router-dom.min";

function ConversationCard({ conversation }) {
    const history = useHistory();
    const sessionUser = useSelector((state) => state.session.user);
    const userId =
        conversation.members[0].id === sessionUser.id
            ? conversation.members[1]
            : conversation.members[0];

    useEffect(() => {
        if (!sessionUser) history.push("/");
    }, [sessionUser, history]);

    return (
        <div className="listing-container">
            <div className="review-details">
                <NavLink to={`/conversations/${conversation.id}`} exact={true}>
                    <h2 id="listing-title">{`Conversation with: ${userId.username}`}</h2>
                    <h3 id="listing-rating">{conversation?.text}</h3>
                </NavLink>
            </div>
        </div>
    );
}

export default ConversationCard;
