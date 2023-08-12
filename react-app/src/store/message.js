const GET_AS_USER = "messages/getAsUser";
const SEND_AS_USER = "messages/sendAsUser";
const GET_AS_LISTING = "messages/getAsListing";
const SEND_AS_LISTING = "messages/sendAsListing";

export const sendAsUser = (newMessageData) => async (dispatch) => {
    const { text, listingId } = newMessageData;
    const res = await fetch(`/api/listings/${listingId}/messages`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            text,
        }),
    });
    if (res.ok) {
        const message = await res.json();
        // dispatch(loadListings(listings));
    }
};

const initialState = {};
const messagesReducer = (state = initialState, action) => {
    let newState = Object.assign({}, state);
    switch (action.type) {
        default:
            return state;
    }
};

export default messagesReducer;
