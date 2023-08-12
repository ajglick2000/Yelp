import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import * as listingActions from "./../store/listing";
import ListingCard from "./ListingCard";

function Favorites() {
    const dispatch = useDispatch();
    const history = useHistory();
    const sessionUser = useSelector((state) => state.session.user);
    const listingsObj = useSelector((state) => state.listings);
    const listings = Object.values(listingsObj);
    const [title] = useState("Favorites");

    useEffect(() => {
        document.title = title;
    }, [title]);

    useEffect(() => {
        if (!sessionUser) history.push("/");
        if (sessionUser) dispatch(listingActions.loadFavorites());
    }, [sessionUser, dispatch, history]);

    return (
        <div className="page-container">
            <h1 id="all-listings">
                {sessionUser.username}'s Favorite Listings
            </h1>
            <div className="listing-gallery">
                {listings &&
                    listings
                        .slice(0)
                        .reverse()
                        .map((listing) => (
                            <ListingCard key={listing.id} listing={listing} />
                        ))}
            </div>
            <h2 id="listing-title">End of your favorites</h2>
        </div>
    );
}
export default Favorites;
