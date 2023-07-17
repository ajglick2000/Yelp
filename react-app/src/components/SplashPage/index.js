import React, { useEffect, useState } from "react";

function SplashPage() {
    const [title] = useState("Home");

    useEffect(() => {
        document.title = title;
    }, [title]);

    useEffect(() => {
        document.body.style.overflow = "hidden";
        return () => {
            document.body.style.overflow = "visible";
        };
    }, []);
    return (
        <>
            <div className="info">
                <h1>Welcome to Yelp</h1>
            </div>

            <div className="info2">
                <h2>Login or Sign Up to access the Full site</h2>
            </div>
        </>
    );
}

export default SplashPage;
