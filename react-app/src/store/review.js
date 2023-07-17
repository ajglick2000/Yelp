const LOAD_ALL_REVIEWS = "listing/loadAllReviews";
const LOAD_SINGLE_REVIEW = "listing/loadSingleReview";
const DELETE_REVIEW = "listing/removeReview";
const CLEAR_REVIEWS = "review/clearReviews";

const addReview = (review) => {
    return {
        type: LOAD_SINGLE_REVIEW,
        payload: review,
    };
};

const loadReviews = (reviews) => {
    return {
        type: LOAD_ALL_REVIEWS,
        payload: reviews,
    };
};

const deleteReview = (id) => {
    return {
        type: DELETE_REVIEW,
        payload: id,
    };
};

const clearReviews = () => {
    return {
        type: CLEAR_REVIEWS,
    };
};

export const newReview = (newReview) => async (dispatch) => {
    const { userId, listingId, title, text, rating } = newReview;
    const response = await fetch("/api/reviews/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            userId,
            listingId,
            title,
            text,
            rating,
        }),
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(addReview(data));
    }
};

export const loadAllReviews = (listingId) => async (dispatch) => {
    const res = await fetch(`/api/listings/${listingId}/reviews`);
    if (res.ok) {
        const reviews = await res.json();
        dispatch(loadReviews(reviews));
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
        dispatch(addReview(review));
    }
};

export const removeReview = (idString) => async (dispatch) => {
    const id = parseInt(idString, 10);
    const res = await fetch(`/api/reviews/${id}`, {
        method: "DELETE",
    });

    if (res.ok) {
        dispatch(deleteReview(id));
    }
};

export const clearStore = () => async (dispatch) => {
    dispatch(clearReviews());
};

const initialState = {};
const reviewsReducer = (state = initialState, action) => {
    let newState = Object.assign({}, state);
    switch (action.type) {
        case LOAD_SINGLE_REVIEW:
            newState[action.payload.id] = action.payload;
            return newState;
        case LOAD_ALL_REVIEWS:
            newState = action.payload;
            return newState;
        case DELETE_REVIEW:
            delete newState[action.payload];
            return newState;
        case CLEAR_REVIEWS:
            return initialState;
        default:
            return state;
    }
};

export default reviewsReducer;
