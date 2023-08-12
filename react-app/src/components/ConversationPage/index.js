import React, { useState, useEffect } from "react";
import { useHistory, useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import * as conversationActions from "../../store/conversation";
import ReviewCard from "../ReviewCard";
import MessageCard from "./MessageCard";
import ContactListingModal from "../ContactListingModal";

function ConversationPage() {
    const dispatch = useDispatch();
    const history = useHistory();
    const { conversationId } = useParams();

    const conversation = useSelector(
        (state) => state.conversations[conversationId]
    );
    console.log(conversation);
    let messages;
    const sessionUser = useSelector((state) => state.session.user);
    const messagesObj = conversation?.messages;
    const listingId = conversation?.listingId;
    if (messagesObj) {
        messages = Object.values(messagesObj);
    }
    // const [title] = useState(
    //     `${
    //         conversation.members[0].id === sessionUser.id
    //             ? conversation.members[1].username
    //             : conversation.members[0].username
    //     }`
    // );

    // const userId =
    //     conversation.members[0].id === sessionUser.id
    //         ? conversation.members[1]
    //         : conversation.members[0];

    // useEffect(() => {
    //     document.title = title;
    // }, [title]);

    useEffect(() => {
        if (!sessionUser) history.push("/");
    }, [sessionUser, history]);

    useEffect(() => {
        if (conversationId) {
            dispatch(conversationActions.getConversations());
            // dispatch(reviewActions.loadAllReviews(conversationId));
        }
        // return () => {
        //     dispatch(reviewActions.clearStore());
        // };
    }, [conversationId, dispatch]);

    return (
        <>
            {conversation && (
                <div className="page-container">
                    <div className="review-gallery">
                        <ContactListingModal listingId={listingId} />
                        <h1 id="all-listings">
                            Conversation with{" "}
                            {conversation.members[0].id === sessionUser.id
                                ? conversation.members[1].username
                                : conversation.members[0].username}
                        </h1>
                        {messages &&
                            messages
                                .slice(0)
                                .map((review, idx) => (
                                    <MessageCard
                                        key={review.id ? review.id : 0}
                                        review={review}
                                    />
                                ))}
                    </div>
                </div>
            )}
        </>
    );
}

export default ConversationPage;
