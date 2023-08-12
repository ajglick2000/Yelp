import React, { useState, useEffect } from "react";
import { Modal } from "../../context/Modal";
import { useDispatch, useSelector } from "react-redux";
import * as messageActions from "../../store/message";

function ContactListingModal({ listingId }) {
    const [showModal, setShowModal] = useState(false);
    const dispatch = useDispatch();
    const sessionUser = useSelector((state) => state.session.user);

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

        dispatch(messageActions.sendAsUser(newMessageData))
            .then(() => {
                setText("");
                setErrors([]);
                setHasSubmitted(false);
                setShowModal(false);
                window.location.reload();
            })
            .catch(async (res) => {
                const data = await res.json();
                if (data && data.errors) setErrors(data.errors);
            });
    };

    return (
        <>
            <button
                className="add-review-button"
                onClick={() => setShowModal(true)}
            >
                <i className="fa-regular fa-envelope"></i> Send Message
            </button>
            {showModal && (
                <Modal onClose={() => setShowModal(false)}>
                    <div className="listing-form-container">
                        <h2>New Message Details</h2>
                        <form
                            className="listing-form"
                            onSubmit={(e) => {
                                e.preventDefault();
                                handleSubmit();
                            }}
                        >
                            <ul className="listing-form-errors">
                                {hasSubmitted &&
                                    errors.map((error, idx) => (
                                        <li key={idx}>{error}</li>
                                    ))}
                            </ul>
                            <label className="listing-label">Message *</label>
                            <textarea
                                onChange={(e) => setText(e.target.value)}
                                className="listing-input-textarea"
                                placeholder="Message Text..."
                                value={text}
                                rows={5}
                            />
                            <button
                                id="listing-submit"
                                type="submit"
                                disabled={disable}
                            >
                                Send Message
                            </button>
                        </form>
                    </div>
                </Modal>
            )}
        </>
    );
}

export default ContactListingModal;
