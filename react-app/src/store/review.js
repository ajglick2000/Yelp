const SET_REVIEWS = "review/setReviews";
const SET_INDIVIDUAL_REVIEW = "review/setIndividualReview";
const REMOVE_REVIEW = "review/removeReview";
const CLEAR_REVIEWS = "review/clearReviews";

const setReviews = (reviews) => {
    return {
        type: SET_REVIEWS,
        payload: reviews,
    };
};

const setIndividualReview = (review) => {
    return {
        type: SET_INDIVIDUAL_REVIEW,
        payload: review,
    };
};

const removeReview = (id) => {
    return {
        type: REMOVE_REVIEW,
        payload: id,
    };
};

const clearReviews = () => {
    return {
        type: CLEAR_REVIEWS,
    };
};

export const createReview = (newReview) => async (dispatch) => {
    const { listingId, title, text, rating } = newReview;
    const res = await fetch("/api/reviews/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            listingId,
            title,
            text,
            rating,
        }),
    });

    if (res.ok) {
        const data = await res.json();
        dispatch(setIndividualReview(data));
    }
};

export const getReviews = (listingId) => async (dispatch) => {
    const res = await fetch(`/api/listings/${listingId}/reviews`);
    if (res.ok) {
        const reviews = await res.json();
        dispatch(setReviews(reviews));
    }
};

export const editReview = (editedReview) => async (dispatch) => {
    const id = parseInt(editedReview.id, 10);
    const res = await fetch(`/api/reviews/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(editedReview),
    });

    if (res.ok) {
        const review = await res.json();
        dispatch(setIndividualReview(review));
    }
};

export const deleteReview = (idString) => async (dispatch) => {
    const id = parseInt(idString, 10);
    const res = await fetch(`/api/reviews/${id}`, {
        method: "DELETE",
    });

    if (res.ok) {
        dispatch(removeReview(id));
    }
};

const initialState = {};
const reviewsReducer = (state = initialState, action) => {
    let newState = Object.assign({}, state);
    switch (action.type) {
        case SET_REVIEWS:
            newState = action.payload;
            return newState;
        case SET_INDIVIDUAL_REVIEW:
            newState[action.payload.id] = action.payload;
            return newState;
        case REMOVE_REVIEW:
            delete newState[action.payload];
            return newState;
        case CLEAR_REVIEWS:
            return initialState;
        default:
            return state;
    }
};

export default reviewsReducer;
