import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { useDispatch } from "react-redux";
import { authenticate } from "./store/session";
import NavBar from "./components/Navigation/NavBar";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import Listings from "./components/Listings";
import SplashPage from "./components/SplashPage";
import SingleListing from "./components/SingleListing";
import SearchResults from "./components/SearchResults";
import Profile from "./components/Profile";
import Favorites from "./components/Favorites";
import ConversationPage from "./components/ConversationPage";

function App() {
    const [loaded, setLoaded] = useState(false);
    const dispatch = useDispatch();

    useEffect(() => {
        (async () => {
            await dispatch(authenticate());
            setLoaded(true);
        })();
    }, [dispatch]);

    if (!loaded) {
        return null;
    }

    return (
        <BrowserRouter>
            <NavBar />
            <Switch>
                <ProtectedRoute path="/listings" exact={true}>
                    <Listings />
                </ProtectedRoute>
                <ProtectedRoute
                    path="/conversations/:conversationId"
                    exact={true}
                >
                    <ConversationPage />
                </ProtectedRoute>
                <ProtectedRoute path="/favorites" exact={true}>
                    <Favorites />
                </ProtectedRoute>
                <ProtectedRoute path="/results" exact={true}>
                    <SearchResults />
                </ProtectedRoute>
                <ProtectedRoute path="/profile" exact={true}>
                    <Profile />
                </ProtectedRoute>
                <ProtectedRoute path="/listings/:listingId">
                    <SingleListing />
                </ProtectedRoute>
                <Route path="/">
                    <SplashPage />
                </Route>
            </Switch>
        </BrowserRouter>
    );
}

export default App;
