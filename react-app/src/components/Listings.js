import React, { useContext, useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import * as listingActions from "../store/listing";
import ListingCard from "./ListingCard";
import { SearchContext } from "../context/Search";
import "./Listings.css";

function Listings() {
    const dispatch = useDispatch();
    const history = useHistory();
    const sessionUser = useSelector((state) => state.session.user);
    const listingsObj = useSelector((state) => state.listings);
    const { setCurrentSearch } = useContext(SearchContext);
    const listings = Object.values(listingsObj);
    const [title] = useState("Listings");
    const initialState = [true, false, false, false, false, false, false];
    const [checkList, setCheckList] = useState(initialState);

    const handleCheckbox = (checkBoxId) => {
        setCheckList((prevState) => {
            if (checkBoxId === 0) {
                return initialState;
            }
            let checker = true;
            let checkBoxIdState = true;
            for (let i = 1; i < checkList.length; i++) {
                if (checkBoxId === i) {
                    checkBoxIdState = !checkList[i];
                } else if (checkList[i]) {
                    checker = false;
                }
            }
            if (!checkBoxIdState && checker) {
                return initialState;
            }
            return [
                false,
                ...prevState.slice(1, checkBoxId),
                !prevState[checkBoxId],
                ...prevState.slice(checkBoxId + 1),
            ];
        });
    };

    const filteredListings = listings.filter((list) => {
        if (checkList[0]) return listings;
        return checkList[list.category];
    });

    useEffect(() => {
        document.title = title;
    }, [title]);

    useEffect(() => {
        if (!sessionUser) history.push("/");
        if (sessionUser) dispatch(listingActions.loadAllListings());
    }, [sessionUser, dispatch, history]);

    const onSearch = async (e) => {
        e.preventDefault();
        history.push("/results");
    };

    return (
        <div className="page-container">
            <h1 id="all-listings">Listings</h1>
            <form className="search-bar" onSubmit={onSearch}>
                <input
                    onChange={(e) => setCurrentSearch(e.target.value)}
                    type="text"
                    className="search-input"
                    placeholder="Search Listings by Title..."
                />
                <button className="search-submit" type="submit">
                    <i className="fa-solid fa-magnifying-glass"></i>
                </button>
            </form>
            <div className="listing-gallery">
                {filteredListings &&
                    filteredListings
                        .slice(0)
                        .reverse()
                        .map((listing) => (
                            <ListingCard key={listing.id} listing={listing} />
                        ))}
            </div>
            <h2 id="listing-title">End of Listings</h2>
        </div>
    );
}
export default Listings;
