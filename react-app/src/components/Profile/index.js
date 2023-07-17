import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import * as listingActions from "../../store/listing";
import ListingCard from "../ListingCard";

function Profile() {
    const dispatch = useDispatch();
    const history = useHistory();
    const sessionUser = useSelector((state) => state.session.user);
    const listingsObj = useSelector((state) => state.listings);
    const listings = Object.values(listingsObj);
    const filteredListings = listings.filter(
        (listing) => listing.userId === sessionUser.id
    );
    const [title] = useState(`${sessionUser.username}`);

    useEffect(() => {
        document.title = title;
    }, [title]);

    useEffect(() => {
        if (!sessionUser) history.push("/");
        if (sessionUser) dispatch(listingActions.loadAllListings());
    }, [sessionUser, dispatch, history]);

    return (
        <div className="page-container">
            <h1 id="all-listings">{sessionUser.username}'s Listings</h1>
            <div className="listing-gallery">
                {filteredListings &&
                    filteredListings
                        .slice(0)
                        .reverse()
                        .map((listing) => (
                            <ListingCard key={listing.id} listing={listing} />
                        ))}
            </div>
            <h2 id="listing-title">End of your listings</h2>
        </div>
    );
}
export default Profile;
