const SET_LISTINGS = "listing/setListings";
const SET_INDIVIDUAL_LISTING = "listing/setIndividualListing";
const REMOVE_LISTING = "listing/removeListing";

const setListings = (listings) => {
    return {
        type: SET_LISTINGS,
        payload: listings,
    };
};

const setIndividualListing = (listing) => {
    return {
        type: SET_INDIVIDUAL_LISTING,
        payload: listing,
    };
};

const removeListing = (id) => {
    return {
        type: REMOVE_LISTING,
        payload: id,
    };
};

export const createListing = (newListing) => async (dispatch) => {
    const { title, location, category, description, image_url } = newListing;

    const formData = new FormData();

    formData.append("title", title);
    formData.append("location", location);
    formData.append("category", category);
    formData.append("description", description);
    formData.append("image_url", image_url);

    const res = await fetch("/api/listings/", {
        method: "POST",
        body: formData,
    });

    if (res.ok) {
        const data = await res.json();
        dispatch(setIndividualListing(data));
    }
};

export const getListings = () => async (dispatch) => {
    const res = await fetch(`/api/listings/`);
    if (res.ok) {
        const listings = await res.json();
        dispatch(setListings(listings));
    }
};

export const getIndividualListing = (id) => async (dispatch) => {
    const res = await fetch(`/api/listings/${id}`);
    if (res.ok) {
        const data = await res.json();
        if (data.errors) return data.errors;
        dispatch(setIndividualListing(data));
    }
};

export const editListing = (editedListing) => async (dispatch) => {
    const { id, title, location, category, description, image_url } =
        editedListing;

    const formData = new FormData();

    formData.append("title", title);
    formData.append("location", location);
    formData.append("category", category);
    formData.append("description", description);
    formData.append("image_url", image_url);

    const res = await fetch(`/api/listings/${id}`, {
        method: "PUT",
        body: formData,
    });

    if (res.ok) {
        const listing = await res.json();
        dispatch(setIndividualListing(listing));
    }
};

export const deleteListing = (idString) => async (dispatch) => {
    const id = parseInt(idString, 10);
    const res = await fetch(`/api/listings/${id}`, {
        method: "DELETE",
    });

    if (res.ok) {
        dispatch(removeListing(id));
    }
};

const initialState = {};
const listingsReducer = (state = initialState, action) => {
    let newState = Object.assign({}, state);
    switch (action.type) {
        case SET_LISTINGS:
            newState = action.payload;
            return newState;
        case SET_INDIVIDUAL_LISTING:
            newState[action.payload.id] = action.payload;
            return newState;
        case REMOVE_LISTING:
            delete newState[action.payload];
            return newState;
        default:
            return state;
    }
};

export default listingsReducer;
