const LOAD_ALL_LISTINGS = "listing/loadAllListings";
const LOAD_SINGLE_LISTING = "listing/loadSingleListing";
const DELETE_LISTING = "listing/removeListing";
const TOGGLE_FAVORITE = "listing/toggleFavorite";

const addListing = (listing) => {
    return {
        type: LOAD_SINGLE_LISTING,
        payload: listing,
    };
};

const loadListings = (listings) => {
    return {
        type: LOAD_ALL_LISTINGS,
        payload: listings,
    };
};

const deleteListing = (id) => {
    return {
        type: DELETE_LISTING,
        payload: id,
    };
};

const toggleFavorite = (id) => {
    return {
        type: TOGGLE_FAVORITE,
        payload: id,
    };
};

export const newListing = (newListing) => async (dispatch) => {
    const { title, location, category, description, image_url } = newListing;

    const formData = new FormData();

    formData.append("title", title);
    formData.append("location", location);
    formData.append("category", category);
    formData.append("description", description);
    formData.append("image_url", image_url);

    console.log(formData);
    const response = await fetch("/api/listings/", {
        method: "POST",
        body: formData,
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(addListing(data));
    }
};

export const loadAllListings = () => async (dispatch) => {
    const res = await fetch(`/api/listings/`);
    if (res.ok) {
        const listings = await res.json();
        dispatch(loadListings(listings));
    }
};

export const loadFavorites = () => async (dispatch) => {
    const res = await fetch(`/api/listings/favorites`);
    if (res.ok) {
        const listings = await res.json();
        dispatch(loadListings(listings));
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
        dispatch(addListing(listing));
    }
};

export const removeListing = (idString) => async (dispatch) => {
    const id = parseInt(idString, 10);
    const res = await fetch(`/api/listings/${id}`, {
        method: "DELETE",
    });

    if (res.ok) {
        dispatch(deleteListing(id));
    }
};

export const loadSingleListing = (id) => async (dispatch) => {
    const res = await fetch(`/api/listings/${id}`);
    if (res.ok) {
        const data = await res.json();
        if (data.errors) return data.errors;
        dispatch(addListing(data));
    }
};

export const addFavoriteListing = (id) => async (dispatch) => {
    console.log("adding favorite in store");
    const res = await fetch(`/api/listings/${id}/favorite`, {
        method: "POST",
    });
    if (res.ok) {
        const data = await res.json();
        if (data.errors) return data.errors;
        dispatch(toggleFavorite(id));
    }
};

export const removeFavoriteListing = (id) => async (dispatch) => {
    const res = await fetch(`/api/listings/${id}/favorite`, {
        method: "DELETE",
    });
    if (res.ok) {
        const data = await res.json();
        if (data.errors) return data.errors;
        dispatch(toggleFavorite(id));
    }
};

const initialState = {};
const listingsReducer = (state = initialState, action) => {
    let newState = Object.assign({}, state);
    switch (action.type) {
        case LOAD_SINGLE_LISTING:
            newState[action.payload.id] = action.payload;
            return newState;
        case LOAD_ALL_LISTINGS:
            newState = action.payload;
            return newState;
        case DELETE_LISTING:
            delete newState[action.payload];
            return newState;
        case TOGGLE_FAVORITE:
            let currListing = state[action.payload];
            currListing.isFavorite = !currListing.isFavorite;
            newState = state;
            return newState;
        default:
            return state;
    }
};

export default listingsReducer;
