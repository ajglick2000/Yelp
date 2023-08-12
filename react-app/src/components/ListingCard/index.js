import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, NavLink } from "react-router-dom";
import { Modal } from "../../context/Modal";
import EditListingModal from "./EditListingModal";
import DeleteListingModal from "./DeleteListingModal";
import ReactStars from "react-rating-stars-component";
import { addFavoriteListing, removeFavoriteListing } from "../../store/listing";

function ListingCard({ listing }) {
    const history = useHistory();
    const sessionUser = useSelector((state) => state.session.user);
    const dispatch = useDispatch();

    const [showEditModal, setShowEditModal] = useState(false);
    const [showDeleteModal, setShowDeleteModal] = useState(false);
    const [isFavorite, setIsFavorite] = useState(false);

    useEffect(() => {
        if (!sessionUser) history.push("/");
        if (listing.isFavorite) {
            setIsFavorite(true);
        } else {
            setIsFavorite(false);
        }
    }, [sessionUser, history]);

    let handleFavoriteButton = async () => {
        console.log(isFavorite);
        if (isFavorite) {
            await dispatch(removeFavoriteListing(listing.id));
            setIsFavorite(false);
        } else {
            await dispatch(addFavoriteListing(listing.id));
            setIsFavorite(true);
        }
    };

    let sessionLinks;
    if (sessionUser.id === listing.userId) {
        sessionLinks = (
            <div className="listing-buttons">
                <button
                    id="edit-button"
                    onClick={(e) => setShowEditModal(!showEditModal)}
                >
                    <i className="fa-regular fa-pen-to-square"></i>
                </button>
                {showEditModal && (
                    <Modal onClose={() => setShowEditModal(false)}>
                        <EditListingModal
                            hideModal={() => setShowEditModal(false)}
                            listing={listing}
                        />
                    </Modal>
                )}
                <button
                    id="card-delete"
                    onClick={(e) => setShowDeleteModal(true)}
                >
                    <i className="fa-regular fa-trash-can"></i>
                </button>
                {showDeleteModal && (
                    <Modal onClose={() => setShowDeleteModal(false)}>
                        <DeleteListingModal
                            hideModal={() => setShowDeleteModal(false)}
                            listing={listing}
                        />
                    </Modal>
                )}
            </div>
        );
    } else {
        sessionLinks = (
            <div className="listing-buttons">
                <button
                    className={`favorite-button add-review-button`}
                    onClick={handleFavoriteButton}
                >
                    <i
                        className={`${
                            isFavorite ? "fa-solid" : "fa-regular"
                        } fa-heart`}
                    ></i>
                </button>
            </div>
        );
    }

    const ratingStars = {
        size: 25,
        count: 5,
        isHalf: true,
        value: listing?.rating,
        color: "gray",
        edit: false,
        activeColor: "cyan",
    };

    let category;
    switch (listing?.category) {
        case 1:
            category = "Restaurant";
            break;
        case 2:
            category = "Bar";
            break;
        case 3:
            category = "Shopping";
            break;
        case 4:
            category = "Grocery";
            break;
        case 5:
            category = "Medical";
            break;
        case 6:
            category = "Misc.";
            break;
        default:
            category = "None";
            break;
    }

    return (
        <div className="listing-container">
            <div className="listing-image">
                <NavLink to={`/listings/${listing?.id}`}>
                    <img
                        id="listing-image"
                        src={listing?.imageUrl}
                        alt={`${listing?.title} alt`}
                        onError={({ currentTarget }) => {
                            currentTarget.onerror = null;
                            currentTarget.src =
                                "https://styles.redditmedia.com/t5_3gvs7p/styles/communityIcon_q2rzyba8wg161.png";
                        }}
                    />
                </NavLink>
            </div>
            <div className="listing-details">
                <div className="title-bar">
                    <h2 id="listing-title">{listing?.title}</h2>
                    <p id="listing-category">{category}</p>
                </div>
                <h3 id="listing-location">{listing?.location}</h3>
                <ReactStars {...ratingStars} />
                <p id="listing-description">{listing?.description}</p>
            </div>
            {sessionLinks}
        </div>
    );
}

export default ListingCard;
