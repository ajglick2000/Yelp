const SET_CONVERSATIONS = "conversations/getConversations";

const setConversations = (conversations) => {
    return {
        type: SET_CONVERSATIONS,
        payload: conversations,
    };
};

export const getConversations = () => async (dispatch) => {
    const res = await fetch(`/api/conversations/`, {});
    if (res.ok) {
        const conversations = await res.json();
        dispatch(setConversations(conversations));
    }
};

const initialState = {};
const conversationsReducer = (state = initialState, action) => {
    let newState = Object.assign({}, state);
    switch (action.type) {
        case SET_CONVERSATIONS:
            newState = action.payload;
            return newState;
        default:
            return state;
    }
};

export default conversationsReducer;
