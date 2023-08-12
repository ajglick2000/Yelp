import React, { useState, useEffect } from "react";
import { Modal } from "../../context/Modal";
import { useDispatch, useSelector } from "react-redux";
import * as conversationActions from "../../store/conversation";
import ConversationCard from "./ConversationCard";

function ConversationsModal({ listingId }) {
    const [showModal, setShowModal] = useState(false);
    const dispatch = useDispatch();
    const sessionUser = useSelector((state) => state.session.user);

    const conversationsObj = useSelector((state) => state.conversations);
    const conversations = Object.values(conversationsObj);

    useEffect(() => {
        dispatch(conversationActions.getConversations());

        // return () => {
        //     dispatch(reviewActions.clearStore());
        // };
    }, []);

    const [userId, setUserId] = useState(sessionUser?.id);
    const [text, setText] = useState("");
    const [errors, setErrors] = useState([]);
    const [hasSubmitted, setHasSubmitted] = useState(false);
    const [disable, setDisable] = useState(false);

    const handleSubmit = () => {
        setHasSubmitted(true);
        setDisable(true);

        if (errors.length > 0) return;

        const newMessageData = {};
        setUserId(sessionUser.id);
        newMessageData.userId = userId;
        newMessageData.listingId = listingId;
        newMessageData.text = text;

        // dispatch(messageActions.sendAsUser(newMessageData))
        //     .then(() => {
        //         setText("");
        //         setErrors([]);
        //         setHasSubmitted(false);
        //         setShowModal(false);
        //         window.location.reload();
        //     })
        //     .catch(async (res) => {
        //         const data = await res.json();
        //         if (data && data.errors) setErrors(data.errors);
        //     });
    };

    return (
        <>
            <button onClick={() => setShowModal(true)}>Inbox</button>
            {showModal && (
                <Modal onClose={() => setShowModal(false)}>
                    <div className="review-gallery">
                        {conversations &&
                            conversations
                                .slice(0)
                                .reverse()
                                .map((conversation) => (
                                    <ConversationCard
                                        key={
                                            conversation.id
                                                ? conversation.id
                                                : 0
                                        }
                                        conversation={conversation}
                                    />
                                ))}
                    </div>
                </Modal>
            )}
        </>
    );
}

export default ConversationsModal;
